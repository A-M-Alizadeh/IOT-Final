import cherrypy
import os
import sys
import json
import sys

class Server:
    exposed = True

    def GET(self, *uri, **params):
        # cm = CatalogManager("./DAO/Catalogue.json")
        # return json.dumps(cm.getCatalog())
        with open('./DAO/data.json') as user_file:
            file_contents = user_file.read()
        return json.dumps(json.loads(file_contents))
    
    def POST(self, *uri, **params):
        return "POST Hello World!"
    
    def PUT(self, *uri, **params):
        return "PUT Hello World!"
    
    def DELETE(self, *uri, **params):
        return "DELET Hello World!"