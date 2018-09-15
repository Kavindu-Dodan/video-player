import json
import os

import cherrypy
from yaml import load


@cherrypy.expose
class VideoServer(object):

    def __init__(self):
        self.video_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'videos/video-list.yml'))

        with open(self.video_path, 'r') \
                as fileStream:
            self.video_list = load(fileStream)['videos']

        cherrypy.log("Video list loaded")

    def _cp_dispatch(self, vpath):
        return self

    def GET(self, **params):
        res = dict()
        res["videos"] = self.video_list

        cherrypy.response.headers['Content-Type'] = "application/json"

        return json.dumps(res).encode('utf8')
