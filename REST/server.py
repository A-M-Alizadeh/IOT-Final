import cherrypy
import os
import sys


# cherrypy.tools.json_in() post method
# cherrypy.tools.json_out() get method

class Home:
    exposed = True

    def GET(self, *uri, **params):
        # print(os.path.abspath(os.getcwd()))
        # file = open('index.html', 'r')
        # print(file.read())
        try:
            return open(os.path.abspath(os.getcwd())+'/REST/public/html/index.html')
            # return open('index.html')
        except:
            cherrypy.response.status = 500
            return os.path.dirname(os.path.abspath(__file__)) + os.path.sep
            # return "500 file not found !!!"

class Server:
    exposed = True
    # cm = CatalogManager()

    def GET(self, *uri, **params):
        return "GET Hello World!"
    def POST(self, *uri, **params):
        return "POST Hello World!"
    
    def PUT(self, *uri, **params):
        return "PUT Hello World!"
    
    def DELETE(self, *uri, **params):
        return "DELET Hello World!"
    

if __name__ == '__main__':
    conf={
        '/':{
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
    cherrypy.tree.mount(Home(), '/home', conf)
    cherrypy.tree.mount(Server(), '/server', conf)

    cherrypy.engine.start()
    cherrypy.engine.block()