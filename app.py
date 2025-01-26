from flask import Flask, render_template
import os

app = Flask(__name__)


app.template_folder = "plantilla"  

@app.route('/')
def home():
    my_name = os.getenv('MY_NAME', 'robot') 
    return render_template('index.html', my_name=my_name) 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True) 

