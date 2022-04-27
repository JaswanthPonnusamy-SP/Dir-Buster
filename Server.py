import os
import threading
import base64
import requests
import sqlite3

from flask import request, Response, Flask, render_template, logging, make_response, jsonify, send_from_directory
from werkzeug.utils import redirect, secure_filename

from click_jacking import click_jacking
from cors_Domain import cors_domain
from decodeurl import decode_url
from encodeurl import encode_url
from ip_add import ip
from last_urlid import last_url
from signup import sign_up
from logincheck import loginclass
from xss_protection import xss_Protection
from DemoProject import demoapp

from passgen import passwdgen

app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def alphabets(alpha,url1):
    alphab = list("abcdefghijklmnopqrstuvwxyz")
    for j in range(26):
        url2 = url1 +"/"+alpha+alphab[j]
        r = requests.get(url2)
        if(r.status_code%100!=4):
            print(r.status_code,r.url)



@app.route('/bustURL')
def bustURL1():

    url1=""


    url1=request.args.get("url")
    alpha=list("abcdefghijklmnopqrstuvwxyz")
    list2=[]
    for i in range(26):
        t1 = threading.Thread(target=alphabets, args=(alpha[i],url1))
        t1.start()
        t1.join()

    return url1


@app.route('/dirBuster')
def dirbuster():
    return render_template("dirBuster.html")


if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8010,debug=True)
