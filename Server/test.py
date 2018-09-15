import cherrypy


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello world! Got message"


if __name__ == '__main__':
    cherrypy.log("Server starting...")
    cherrypy.config.update({'server.socket_host': '0.0.0.0','server.socket_port': 8080})
    cherrypy.quickstart(HelloWorld())