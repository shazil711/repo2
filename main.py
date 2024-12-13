from flask import Flask

app = Flask(__name__)


@app.route('/')
def area_of_square(side):
    area = int(side * side)
    print(area)
 


area_of_square(6)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
