import cherrypy
import os
import sys
import json

"""
    -------------------------------------------- Notice --------------------------------------------
    # path to parent folder
    # there is a difference between os.getcwd() in Mac Terminal and VSCode
    # VSCode returns the path to project root folder, while Mac Terminal returns the path to the current folder
"""
currentPath = os.getcwd()[:os.getcwd().find('/Final')+len('/Final')]+os.path.sep
sys.path.insert(1, currentPath)


class Server(object):
    exposed = True

    def GET(self, *uri, **params):
        return open(currentPath+'Microservices/REST/public/html/index.html')

    def POST(self, *uri, **params):
        return "POST  Server !"

    def PUT(self, *uri, **params):
        return "PUT  Server !"

    def DELETE(self, *uri, **params):
        return "DELET  Server !"


# -------------------------------------------- Main --------------------------------------------
if __name__ == '__main__':
    data = json.loads(
        open(currentPath+'Microservices/REST/config.json').read())
    ip = data["resourceCatalog"]["host"]
    port = data["resourceCatalog"]["port"]
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Access-Control-Allow-Origin', '*')],
            'tools.sessions.on': True,
            'tools.staticdir.root': currentPath+'Microservices/REST/'
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'public'
        },
        '/css': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'public/css/'
        },
    }
    cherrypy.config.update(conf)
    cherrypy.tree.mount(Server(), '/', conf)
    cherrypy.config.update({'web.socket_ip': ip, 'server.socket_port': port})

    cherrypy.engine.start()
    cherrypy.engine.block()
