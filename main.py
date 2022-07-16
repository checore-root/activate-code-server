import activate_code_server

server = activate_code_server.app_server(
    host='localhost',
    port=7000,
)

if __name__ == "__main__":
    server.setup_blueprint(activate_code_server.simple_page)
    server.run()
