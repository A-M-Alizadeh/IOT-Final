import cherrypy
import os
import sys
import json
# from config import catalogPath

import sys
sys.path.insert(1, '/Users/graybook/Documents/Polito/Projects/IOT/Final') #/MicroServices/REST/Micros
# from Catalog.CatalogManager import CatalogManager
# from Catalog.CatalogMaker import CatalogMaker


class UserService(object):
    exposed = True

    def GET(self, *uri, **params):
        with open('../../../../Catalog/data.json') as user_file:
            file_contents = user_file.read()
        content = json.loads(file_contents)
        return json.dumps(content["users"])
    
    def POST(self, *uri, **params):
        return "POST user!"
    
    def PUT(self, *uri, **params):
        return "PUT user!"
    
    def DELETE(self, *uri, **params):
        return "DELET user!"
    

if __name__ == '__main__':
    data = json.loads(open('./Microservices/REST/config.json').read())
    ip = data["userServer"]["host"]
    port = data["userServer"]["port"]
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
    cherrypy.tree.mount(UserService(), '/user', conf)
    cherrypy.config.update(conf)
    cherrypy.config.update({'web.socket_ip': ip,'server.socket_port': port})

    cherrypy.engine.start()
    cherrypy.engine.block()