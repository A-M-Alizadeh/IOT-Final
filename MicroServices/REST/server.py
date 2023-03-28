import cherrypy
import os
import sys
import json

# import sys
# sys.path.insert(1, '/Users/graybook/Documents/Polito/Projects/IOT/Final/MicroServices/REST')


class Server(object):
    exposed = True

    def GET(self, *uri, **params):
        return open("./Microservices/REST/public/html/index.html")

    def POST(self, *uri, **params):
        return "POST  Server !"

    def PUT(self, *uri, **params):
        return "PUT  Server !"

    def DELETE(self, *uri, **params):
        return "DELET  Server !"


if __name__ == '__main__':
    print('---------> ',os.getcwdb())
    print('---------> ',os.path.dirname(os.path.abspath(__file__)) + os.path.sep)
    data = json.loads(open('./Microservices/REST/config.json').read())
    ip = data["resourceCatalog"]["host"]
    port = data["resourceCatalog"]["port"]

    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './Microservices/REST/public'
        },
    }
    cherrypy.config.update(conf)
    cherrypy.tree.mount(Server(), '/', conf)
    cherrypy.config.update({'web.socket_ip': ip, 'server.socket_port': port})

    cherrypy.engine.start()
    cherrypy.engine.block()
