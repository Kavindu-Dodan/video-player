import cherrypy
from src.app import VideoServer

if __name__ == '__main__':
    cherrypy.log("Server starting...")
    cherrypy.config.update({'server.socket_host': '0.0.0.0',
                            'server.socket_port': 8080})

    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.encode.on': True,
            'tools.encode.encoding': 'utf-8'
        }
    }

    cherrypy.tree.mount(VideoServer(), '/server', conf)

    cherrypy.engine.start()
    cherrypy.engine.block()
