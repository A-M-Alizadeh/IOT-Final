import cherrypy
import os
import sys
import json

"""
    -------------------------------------------- Notice --------------------------------------------
    #path to parent folder
    # there is a difference between os.getcwd() in Mac Terminal and VSCode
    # VSCode returns the path to project root folder, while Mac Terminal returns the path to the current folder
"""
currentPath = os.getcwd()[:os.getcwd().find('/Final')+len('/Final')]+os.path.sep
sys.path.insert(1, currentPath)
from Catalog.CatalogManager import CatalogManager


cm = CatalogManager(currentPath+'/Catalog/Catalogue.json')

class DeviceService(object):
    exposed = True

    def GET(self, *uri, **params):
        if "deviceId" in params:
            return json.dumps(cm.findDevice(params.get("deviceId")))
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


# -------------------------------------------- Main --------------------------------------------

if __name__ == '__main__':
    # data = json.loads(open('./Microservices/REST/config.json').read())
    data = json.loads(open(currentPath + '/Microservices/REST/config.json').read())
    ip = data["deviceServer"]["host"]
    port = data["deviceServer"]["port"]
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Access-Control-Allow-Origin', '*')],
            'tools.sessions.on': True,
            'tools.encode.on': True, 
            'tools.encode.encoding': 'utf-8',
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
