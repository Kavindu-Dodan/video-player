import json
import os

import cherrypy
from yaml import load


@cherrypy.expose
class VideoServer(object):

    def __init__(self):
        self.video_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'videos')) + '/'

        # We only have one video yet
        with open(self.video_path + 'video-list.yml', 'r') \
                as fileStream:
            self.video_list = load(fileStream)['videos']

        cherrypy.log("Video list loaded")

    def _cp_dispatch(self, vpath):
        cherrypy.request.params["path"] = []

        while len(vpath) > 0:
            cherrypy.request.params["path"].append(vpath.pop(0))

        return self

    def GET(self, path=None, **params):
        cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'

        # Call for video list
        if path is None:
            cherrypy.response.headers['Content-Type'] = "application/json"
            return json.dumps({"videos": self.video_list}).encode('utf8')
        elif path[0] == 'video':
            # Check for params
            cherrypy.response.headers['Content-Type'] = "video/mp4"
            return self.load_video(params['id'])

    def load_video(self, video_id):
        with open(self.video_path + video_id, 'rb') as video_stream:
            return video_stream.read()

