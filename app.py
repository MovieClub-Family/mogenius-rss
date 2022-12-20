import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

#Ex https://Itz-zaid:ghp_147bkkabcdefgh@github.com/Itz-zaid/anything
os.system("git clone https://github.com/DML-Org/NodeRSSBot ok && cd ok && npm run build && npm prune --production && npm i -g pm2 && pm2 start npm --name node_rssbot -- start &")
