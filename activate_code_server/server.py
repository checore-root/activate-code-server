from flask import Flask
from gevent.pywsgi import WSGIServer

class app_server:
    def __init__(self, *args, **kwargs):
        self.port = kwargs.get('port', 8000)
        self.host = kwargs.get('host', 'localhost')
        self.database_engine = kwargs.get('database_engine', 'sqlite')
        self.database_name = kwargs.get('database_name', 'activate_code_server')
        self.database_user = kwargs.get('database_user', 'root')
        self.database_password = kwargs.get('database_password', '12345678')
        self.app = None
        self.server = None
        self.setup_app()
        
    def setup_app(self):
        self.app = Flask(__name__)
    
    def setup_blueprint(self, blueprint):
        self.app.register_blueprint(blueprint)
        
    def setup_server(self):
        self.server = WSGIServer(
            (self.host, self.port),
            self.app)

    def run(self):
        self.setup_server()
        self.server.serve_forever()