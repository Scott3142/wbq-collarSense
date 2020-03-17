from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
import json
import random
from gpiozero import Button
from time import time,sleep

app = Flask(__name__)

@app.route('/')
def splash():
    return render_template('splash.html')

@app.route("/holding/")
def inprogress():
    return render_template('holding.html')

@app.route("/playing/")
def game_playing():
    
    ### Put code here ###

    output_choices = ["I'm so hungry!","Take me for a walk!", "I want to sleep now.", "You're the best human ever.", "I want to get a cat!","I don't like the neighbors."]
    
    #button.wait_for_press()
    output = random.choice(output_choices)

    ### End code ###

    return jsonify(scores=output)

@app.route("/score/<scoreValue>")
def score(scoreValue):
    return render_template('final.html',scoreValue=scoreValue)

if __name__ == "__main__":
    app.run(debug=True)
