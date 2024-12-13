from flask import Flask

app = Flask(__name__)


@app.route('/')
def greet():
    print("Hello")
    print("how are you dumb?")

greet()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
