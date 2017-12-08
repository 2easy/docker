import os
from flask import Flask
app = Flask(__name__)

@app.route('/<int:foo>')
def hello_world(foo):
    return "Third VERSION!! Host number %s %d" % (os.getenv('HOST_NUM'), foo)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
