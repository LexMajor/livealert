# -*- coding: utf-8 -*-
import socket
import os, os.path
import time
from flask import Flask, url_for
app = Flask(__name__)


if os.path.exists( "/tmp/socket_interface" ):
  client = socket.socket( socket.AF_UNIX, socket.SOCK_DGRAM )
  client.connect( "/tmp/socket_interface" )
  print "Ouvert"
else:
  print "Couldn't Connect!"


@app.route('/api/v1.0/')
def api_root():
    x = "Welcome"
    client.send( x )
    print "Envoyé\n"
    return 'Envoyé\n'

@app.route('/api/v1.0/couleurs/<couleur>')
def api_couleur(couleur):
    client.send( couleur )
    print "Couleur: "+ couleur + "\n"
    return couleur

@app.route('/api/v1.0/action/<station>/<action>')
def api_action(station,action):
    client.send( station,action )
    print "Station: "+ station +", "
    print "Action: "+ action + "\n"
    return station,action

@app.route('/api/v1.0/articles')
def api_articles():
    return 'List of ' + url_for('api_articles') + '\n'

@app.route('/api/v1.0/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid + '\n'

if __name__ == '__main__':
#    app.run(debug=True)
    app.run(host='0.0.0.0')

