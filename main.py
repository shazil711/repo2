from flask import Flask

app = Flask(__name__)


@app.route('/')



def greet(name):
    return("hello")

print(greet("name"))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    
