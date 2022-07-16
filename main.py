import activate_code_server

server = activate_code_server.app_server(
    debug=False
)
from flask import Blueprint


simple_page = Blueprint('simple_page', __name__, template_folder='templates')

@simple_page.route('/')
def show():
    return 'Hello World!'

if __name__ == "__main__":
    server.setup_blueprint(simple_page)
    server.setup_server()
    server.run()