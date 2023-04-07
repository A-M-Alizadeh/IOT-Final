import cherrypy
import os
import sys
import json

currentPath = os.getcwd()[:os.getcwd().find('/Final')+len('/Final')]+os.path.sep
sys.path.insert(1, currentPath)

class AwarenessService(object):
    exposed = True

    def GET(self, *uri, **params):
        pass
    

    def POST(self, *uri, **params):
        pass
    

    def PUT(self, *uri, **params):
        pass
    

    def DELETE(self, *uri, **params):
        pass
    

# -------------------------------------------- Main --------------------------------------------

if __name__ == '__main__':
    data = json.loads(open(currentPath+'/Microservices/REST/config.json').read())
    ip = data["AwarenessService"]["host"]
    port = data["AwarenessService"]["port"]
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
    cherrypy.tree.mount(AwarenessService(), '/aware', conf)
    cherrypy.config.update(conf)
    cherrypy.config.update({'web.socket_ip': ip,'server.socket_port': port})

    cherrypy.engine.start()
    cherrypy.engine.block()