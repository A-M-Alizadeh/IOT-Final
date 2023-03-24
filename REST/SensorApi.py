import cherrypy
import os
import sys
import json
import sys

class SensorApi:
    exposed = True

    def GET(self, *uri, **params):
        return "GET Sensor Hello World!"
    
    def POST(self, *uri, **params):
        return "POST Hello World!"
    
    def PUT(self, *uri, **params):
        return "PUT Hello World!"
    
    def DELETE(self, *uri, **params):
        return "DELET Hello World!"