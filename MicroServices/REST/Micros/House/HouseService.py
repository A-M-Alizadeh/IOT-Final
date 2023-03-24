import cherrypy
import os
import sys
import json
# from config import catalogPath

import sys
sys.path.insert(1, '/Users/graybook/Documents/Polito/Projects/IOT/Final/MicroServices/REST')
# from Catalog.CatalogManager import CatalogManager
# from Catalog.CatalogMaker import CatalogMaker


class HouseService(object):
    exposed = True

    def GET(self, *uri, **params):
        with open('../../../../Catalog/data.json') as user_file:
            file_contents = user_file.read()
        content = json.loads(file_contents)
        return json.dumps(content["houses"])
    
    def POST(self, *uri, **params):
        return "POST house!"
    
    def PUT(self, *uri, **params):
        return "PUT house!"
    
    def DELETE(self, *uri, **params):
        return "DELET house!"
    

if __name__ == '__main__':
    data = json.loads(open('../../config.json').read())
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