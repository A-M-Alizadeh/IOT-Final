import cherrypy
import os
import sys
import json

#path to current folder
currentPath = os.path.dirname(os.path.abspath(__file__)) + os.path.sep

"""
    -------------------------------------------- Notice --------------------------------------------
    path to parent folder
    if you want to use the parent folder, uncomment the following lines
    you need to change the path used for other path used in the code
"""
# currentPath = os.getcwd()[:os.getcwd().find('/Final')+len('/Final')]+os.path.sep
# sys.path.insert(1, currentPath)


class Server(object):
    exposed = True

    def GET(self, *uri, **params):
        return open(currentPath+'public/html/index.html')

    def POST(self, *uri, **params):
        return "POST  Server !"

    def PUT(self, *uri, **params):
        return "PUT  Server !"

    def DELETE(self, *uri, **params):
        return "DELET  Server !"



# -------------------------------------------- Main --------------------------------------------
if __name__ == '__main__':
    data = json.loads(open(currentPath+'config.json').read())
    ip = data["resourceCatalog"]["host"]
    port = data["resourceCatalog"]["port"]

    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.staticdir.root': currentPath
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'Microservices/REST/public'
        },
    }
    cherrypy.config.update(conf)
    cherrypy.tree.mount(Server(), '/', conf)
    cherrypy.config.update({'web.socket_ip': ip, 'server.socket_port': port})

    cherrypy.engine.start()
    cherrypy.engine.block()
