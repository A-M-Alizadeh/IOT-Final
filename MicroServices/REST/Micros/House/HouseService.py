import cherrypy
import os
import sys
import json

import sys
sys.path.insert(1, '/Users/graybook/Documents/Polito/Projects/IOT/Final')
from Catalog.CatalogManager import CatalogManager

cm = CatalogManager('./Catalog/Catalogue.json')


class HouseService(object):
    exposed = True

    def GET(self, *uri, **params):
        if "houseId" in params:
            return json.dumps(cm.findHouse(params.get("houseId")))
        else:
            return json.dumps(cm.getHouses())
    

    def POST(self, *uri, **params):
        cl = cherrypy.request.headers['Content-Length']
        rawbody = cherrypy.request.body.read(int(cl))
        body = json.loads(rawbody)
        if "houseName" in body and "devicesList" in body:
            try:
                userId = cm.createHouse(body)
                return json.dumps({"houseId": userId})
            except:
                raise cherrypy.HTTPError(500, "Could not Create House")
        else:
            raise cherrypy.HTTPError(400, "Bad Request")
    

    def PUT(self, *uri, **params):
        cl = cherrypy.request.headers['Content-Length']
        rawbody = cherrypy.request.body.read(int(cl))
        body = json.loads(rawbody)
        if "houseId" in body and "newHouse" in body:
            try:
                houseId = cm.updateHouse(body.get("houseId"), body.get("newHouse"))
                return json.dumps({"houseId": houseId})
            except:
                raise cherrypy.HTTPError(500, "Could not Update House")
        else:
            raise cherrypy.HTTPError(400, "Bad Request")
    

    def DELETE(self, *uri, **params):
        if "houseId" in params:
            try:
                cm.removeHouse(params.get("houseId"))
                return "House Successfully Removed"
            except:
                raise cherrypy.HTTPError(500, "Could not Remove House")
        else:
            raise cherrypy.HTTPError(400, "Bad Request")
    








    

if __name__ == '__main__':
    data = json.loads(open('./Microservices/REST/config.json').read())
    ip = data["houseServer"]["host"]
    port = data["houseServer"]["port"]
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.encode.on': True, 'tools.encode.encoding': 'utf-8',
            'tools.decode.on': True,
            'tools.trailing_slash.on': True,
            'tools.staticdir.root': os.path.abspath(os.path.dirname(__file__)),
            'web.socket_ip': ip,
            'web.socket_port': port,
        }
    }
    cherrypy.tree.mount(HouseService(), '/house', conf)
    cherrypy.config.update(conf)
    cherrypy.config.update({'web.socket_ip': ip,'server.socket_port': port})

    cherrypy.engine.start()
    cherrypy.engine.block()