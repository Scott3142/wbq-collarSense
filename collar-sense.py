from flask import Flask
from sense_hat import SenseHat
import random

app = Flask(__name__)

@app.route('/')
def index():
    
    sense = SenseHat()
    sense.clear()
    
    o = sense.get_orientation()
    pitch = o["pitch"]
    
    output_choices = ["I'm so hungry!","Take me for a walk!", "I want to sleep now.", "You're the best human ever.", "Can we get a cat?","I don't like the neighbors."]
    
    if pitch > 0:
        output = random.choice(output_choices)
    else:
        output = random.choice(output_choices)
    
    html = "<a href='#?force=refresh" + str(random.randint(0,10)) + "'>What is my dog saying?</a><p>Woof! "
    output = html + output + "</p>"
    
    return str(output)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
