import re
import unicodedata
from socketio import socketio_manage
from socketio.namespace import BaseNamespace
from gevent import monkey
from flask import Flask, Response, request, render_template, url_for, redirect

monkey.patch_all()

app = Flask(__name__)
app.debug = True
_self = None

@app.route('/')
def root():
    return render_template('index.html')

def update(path, arg):
    print ("update", path, arg, _self)
    # cns = ColorNamespace()
    # cns.change(path) 

class ColorNamespace(BaseNamespace):
    def initialize(self):
        _self = self
        self.logger = app.logger
        self.log("Socketio session started")

    def log(self, message):
        self.logger.info("[{0}] {1}".format(self.socket.sessid, message))
    
    def change(self, val):
        # _self = self(BaseNamespace())
        print("Socketio change", self, val)
        # _self.emit('gotem1',{'gotem1':'gotem'})
        return True

    def on_test(self, val):
        self.emit('gotem',{'gotem':'gotem'})
        return True


@app.route('/socket.io/<path:remaining>')
def socketio(remaining):
    try:
        socketio_manage(request.environ, {'/color': ColorNamespace}, request)
    except:
        app.logger.error("Exception while handling socketio connection",exc_info=True)
    return Response()


if __name__ == '__main__':
    app.run()
