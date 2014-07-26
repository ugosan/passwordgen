from flask import render_template
from app import app
import xkcd
from googleimages import GoogleImagesSearch

@app.route('/')
@app.route('/index')
def index():
    
    words = xkcd.getWords()
    gi = GoogleImagesSearch()
    images1 = gi.query(words[0])
    images2 = gi.query(words[1])
    images3 = gi.query(words[2])
    
    
    return render_template("index.html",
        word1 = words[0],
        word2 = words[1],
        word3 = words[2],
        images1 = images1,
        images2 = images2,
        images3 = images3)
