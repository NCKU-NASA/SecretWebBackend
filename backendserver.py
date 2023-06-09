#!/usr/bin/env python3

from flask import Flask,request,redirect,Response


app = Flask(__name__)

@app.route('/',methods=['GET'])
def getip():
    if "a" in request.args and "b" in request.args:
        return str(int(request.args['a']) + int(request.args['b']))
    else:
        if 'X-Forwarded-For' in request.headers:
            return request.headers['X-Forwarded-For']
        return request.remote_addr

if __name__ == "__main__":
    app.run(port=8000)
