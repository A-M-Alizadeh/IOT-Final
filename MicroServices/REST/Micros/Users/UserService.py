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


# print(cherrypy.url(qs = cherrypy.request.query_string, relative = "server"))
# cherrypy.url(qs = cherrypy.request.query_string)
class UserService(object):
    exposed = True

    def GET(self, *uri, **params):
        if "userId" in params:
            return json.dumps(cm.findUser(params.get("userId")))
        else:
            return json.dumps(cm.getUsers())
    

    def POST(self, *uri, **params):
        cl = cherrypy.request.headers['Content-Length']
        rawbody = cherrypy.request.body.read(int(cl))
        body = json.loads(rawbody)
        if "username" in body and "houseId" in body:
            try:
                userId = cm.createUser(body)
                return json.dumps({"userId": userId})
            except:
                raise cherrypy.HTTPError(500, "Could not Create User")
        else:
            raise cherrypy.HTTPError(400, "Bad Request")
    

    def PUT(self, *uri, **params):
        cl = cherrypy.request.headers['Content-Length']
        rawbody = cherrypy.request.body.read(int(cl))
        body = json.loads(rawbody)
        if "userId" in body and "newUser" in body:
            try:
                userId = cm.updateUser(body.get("userId"), body.get("newUser"))
                return json.dumps({"userId": userId})
            except:
                raise cherrypy.HTTPError(500, "Could not Update User")
        else:
            raise cherrypy.HTTPError(400, "Bad Request")
    

    def DELETE(self, *uri, **params):
        if "userId" in params:
            try:
                cm.removeUser(params.get("userId"))
                return "User Successfully Removed"
            except:
                raise cherrypy.HTTPError(500, "Could not Remove User")
        else:
            raise cherrypy.HTTPError(400, "Bad Request")
    




# -------------------------------------------- Main --------------------------------------------
if __name__ == '__main__':
    data = json.loads(open(currentPath+'/Microservices/REST/config.json').read())
    ip = data["userServer"]["host"]
    port = data["userServer"]["port"]
    # TODO: update Path if needed
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
    cherrypy.tree.mount(UserService(), '/user', conf)
    cherrypy.config.update(conf)
    cherrypy.config.update({'web.socket_ip': ip,'server.socket_port': port})

    cherrypy.engine.start()
    cherrypy.engine.block()