from flask import Flask

app = Flask(__name__)


@app.route('/')
import random



result = random.randint(0,1)

if result == 0:
    print("tails")
else:
    print("Heads")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
