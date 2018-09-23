import json
import os
import csv

import cherrypy
from yaml import load


@cherrypy.expose
class VideoServer(object):
    def __init__(self):
        self.VIDEO_FOLDER = os.path.abspath(os.path.join(
            os.path.dirname(__file__), '..', 'videos'))

        self.default_quality = "high"
        self.available_quality = ["high", "low"]
        self.meta_file = "meta.json"

    def _cp_dispatch(self, vpath):
        cherrypy.request.params["path"] = []

        while len(vpath) > 0:
            cherrypy.request.params["path"].append(vpath.pop(0))

        return self

    def GET(self, path=None, **params):
        cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'

        if path[0] == 'video':
            if('id' in params and "segment" not in params):
                # We consider this as a metadata request
                return self.load_meta(params['id'])
            elif('id' in params and 'segment' in params):
                if ('quality' in params):
                    # Segment request with quality
                    return self.load_video(params['id'], params['segment'], params['quality'])
                else:
                    # Segment request with default quality
                    return self.load_video(params['id'], params['segment'])
            else:
                # Invalid request
                cherrypy.HTTPError(405)
        else:
            raise cherrypy.HTTPError(404)

    def load_video(self, id, segment, quality='high'):
        cherrypy.response.headers['Content-Type'] = "video/mp4"

        video_root = self.get_video_path(id)

        video_with_quality = os.path.join(video_root, quality)

        if (os.path.exists(video_with_quality)):
            filename = "%s%s.webm" % (id, segment)

            with open(os.path.join(video_with_quality, filename), 'rb') as video_stream:
                return video_stream.read()
        else:
            raise cherrypy.HTTPError(
                404, message="No video found with id [%s], quality [%s]" % (id, quality))

    def load_meta(self, id):
        cherrypy.response.headers['Content-Type'] = "application/json"

        video_root = self.get_video_path(id)

        if (os.path.exists(video_root)):
            with open(video_root + '/' + self.meta_file, 'r') as meta_json:
                return json.dumps(json.loads(meta_json.read())).encode('UTF-8')
        else:
            raise cherrypy.HTTPError(
                404, message="No video found with id [%s]" % id)

    def get_video_path(self, id):
        return os.path.join(self.VIDEO_FOLDER, id)
