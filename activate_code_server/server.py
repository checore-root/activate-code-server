from flask import Flask, jsonify
from gevent.pywsgi import WSGIServer

class app_server:
    def __init__(self, *args, **kwargs):
        self.port = kwargs.get('port', 7000)
        self.host = kwargs.get('host', 'localhost')
        self.debug = kwargs.get('debug', False)
        self.app = None
        self.server = None
        self.setup_app()
        
    def setup_app(self):
        self.app = Flask(__name__)
    
    def setup_blueprint(self, blueprint):
        self.app.register_blueprint(blueprint)
        
    def setup_server(self):
        self.app.debug = True
        self.server = WSGIServer(
            (self.host, self.port),
            self.app)

    def run(self):
        self.server.serve_forever()