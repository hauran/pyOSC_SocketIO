from color import app
from gevent import monkey
from socketio.server import SocketIOServer

monkey.patch_all()

SERVER_NAME = "127.0.0.1"
SERVER_PORT = 8888

if __name__ == '__main__':
    print 'Listening on http://127.0.0.1:%s and on port 10843 (flash policy server)' % SERVER_PORT
    SocketIOServer((SERVER_NAME, SERVER_PORT), app, resource="socket.io").serve_forever()
