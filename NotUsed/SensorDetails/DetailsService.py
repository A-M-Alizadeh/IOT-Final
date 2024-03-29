import cherrypy
import os
import sys
import json

currentPath = os.getcwd()[:os.getcwd().find('/Final')+len('/Final')]+os.path.sep
sys.path.insert(1, currentPath)
from Catalog.CatalogManager import CatalogManager


cm = CatalogManager(currentPath+'/Catalog/Catalogue.json')


class DetailService(object):
    exposed = True

    def GET(self, *uri, **params):
        with open('../../../../Catalog/data.json') as user_file:
            file_contents = user_file.read()
        content = json.loads(file_contents)
        return json.dumps(content["services"])
    
    def POST(self, *uri, **params):
        return "POST Detail!"
    
    def PUT(self, *uri, **params):
        return "PUT Detail!"
    
    def DELETE(self, *uri, **params):
        return "DELET Detail!"
    

if __name__ == '__main__':
    data = json.loads(open('../../config.json').read())
    ip = data["detailServer"]["host"]
    port = data["detailServer"]["port"]
    
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
    cherrypy.tree.mount(DetailService(), '/detail', conf)
    cherrypy.config.update(conf)
    cherrypy.config.update({'web.socket_ip': ip,'server.socket_port': port})

    cherrypy.engine.start()
    cherrypy.engine.block()