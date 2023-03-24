# from Catalog.CatalogMaker import CatalogMaker
# from Catalog.CatalogManager import CatalogManager
import cherrypy
import os
import sys
import json

import sys
sys.path.insert(1, '/Users/graybook/Documents/Polito/Projects/IOT/Final')


class Server(object):
    exposed = True

    def GET(self, *uri, **params):
        return "GET  Server !"

    def POST(self, *uri, **params):
        return "POST  Server !"

    def PUT(self, *uri, **params):
        return "PUT  Server !"

    def DELETE(self, *uri, **params):
        return "DELET  Server !"


if __name__ == '__main__':
    data = json.loads(open('./config.json').read())
    ip = data["resourceCatalog"]["host"]
    port = data["resourceCatalog"]["port"]

    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.dirname(os.path.abspath(__file__)) + os.path.sep
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        },
        '/css': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './css'
        },
        '/js': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './js'
        },
    }
    cherrypy.config.update(conf)
    cherrypy.tree.mount(Server(), '/main', conf)
    cherrypy.config.update({'web.socket_ip': ip, 'server.socket_port': port})
    # cherrypy.tree.mount(HouseApi.HouseApi(), '/house', conf)
    # cherrypy.tree.mount(UserApi.UserApi(), '/user', conf)
    # cherrypy.tree.mount(SensorApi.SensorApi(), '/sensor', conf)
    # cherrypy.tree.mount(Server(), '/server', conf)

    cherrypy.engine.start()
    cherrypy.engine.block()
