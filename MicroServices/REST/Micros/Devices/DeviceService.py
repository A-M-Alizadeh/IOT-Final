# from Catalog.CatalogManager import CatalogManager
# import cherrypy
# import os
# import sys
# import json

# import sys
# # /MicroServices/REST/Micros
# sys.path.insert(1, '/Users/graybook/Documents/Polito/Projects/IOT/Final')

# cm = CatalogManager('./Catalog/Catalogue.json')

import cherrypy
import os
import sys
import json

import sys
sys.path.insert(1, '/Users/graybook/Documents/Polito/Projects/IOT/Final') #/MicroServices/REST/Micros
from Catalog.CatalogManager import CatalogManager

cm = CatalogManager('./Catalog/Catalogue.json')


class DeviceService(object):
    exposed = True

    def GET(self, *uri, **params):
        if "userId" in params:
            return json.dumps(cm.findDeviceByUser(params.get("userId")))
        elif "houseId" in params:
            return json.dumps(cm.findDeviceByHouse(params.get("houseId")))
        else:
            return json.dumps(cm.getAllDevices())


    def POST(self, *uri, **params):
        cl = cherrypy.request.headers['Content-Length']
        rawbody = cherrypy.request.body.read(int(cl))
        body = json.loads(rawbody)
        if "userId" in body and "houseId" in body and "newDevice" in body:
            try:
                deviceId = cm.createOrUpdateDevice(body.get("newDevice"),body.get("userId"), body.get("houseId"))
                return json.dumps({"deviceId": deviceId})
            except:
                raise cherrypy.HTTPError(500, "Could not Create Device")
        else:
            raise cherrypy.HTTPError(400, "Bad Request")


    def PUT(self, *uri, **params):
        cl = cherrypy.request.headers['Content-Length']
        rawbody = cherrypy.request.body.read(int(cl))
        body = json.loads(rawbody)
        if "userId" in body and "houseId" in body and "newDevice" in body:
            try:
                deviceId = cm.createOrUpdateDevice(body.get("newDevice"),body.get("userId"), body.get("houseId"))
                return json.dumps({"deviceId": deviceId})
            except:
                raise cherrypy.HTTPError(500, "Could not Update Device")
        else:
            raise cherrypy.HTTPError(400, "Bad Request")


    def DELETE(self, *uri, **params):
        if "deviceId" in params:
            try:
                cm.removeDevice(params.get("deviceId"), params.get("houseId"))
                return "Device Successfully Removed"
            except:
                raise cherrypy.HTTPError(500, "Could not Remove User")
        else:
            raise cherrypy.HTTPError(400, "Bad Request")











if __name__ == '__main__':
    # data = json.loads(open('./Microservices/REST/config.json').read())
    data = json.loads(open('./Microservices/REST/config.json').read())
    ip = data["deviceServer"]["host"]
    port = data["deviceServer"]["port"]
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
    cherrypy.tree.mount(DeviceService(), '/device', conf)
    cherrypy.config.update(conf)
    cherrypy.config.update({'web.socket_ip': ip, 'server.socket_port': port})

    cherrypy.engine.start()
    cherrypy.engine.block()
