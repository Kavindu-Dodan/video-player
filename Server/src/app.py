import json
import os

import cherrypy
from yaml import load


@cherrypy.expose
class VideoServer(object):

    def __init__(self):
        self.video_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'videos'))

        # We only have one video yet
        # with open(self.video_path + 'video-list.yml', 'r') \
        #         as fileStream:
        #     self.video_list = load(fileStream)['videos']

        # cherrypy.log("Video list loaded")

    def _cp_dispatch(self, vpath):
        cherrypy.request.params["path"] = []

        while len(vpath) > 0:
            cherrypy.request.params["path"].append(vpath.pop(0))

        return self

    def GET(self, path=None, **params):
        cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'
            
        if path[0] == 'video':
            cherrypy.response.headers['Content-Type'] = "video/mp4"
            return self.load_video(params['id'], params['segment'])
        else:
            raise cherrypy.HTTPError(404)

    def load_video(self, id, segment):
        video_folder = os.path.abspath(self.video_path + '/' +id )
        cherrypy.log(video_folder)
        filename = "%s%s.webm" % (id, segment)

        with open(video_folder+ '/'+filename, 'rb') as video_stream:
            return video_stream.read()

