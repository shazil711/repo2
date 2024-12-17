from flask import Flask

app = Flask(__name__)


@app.route('/')


def password_controller(password):
    if len(password) > 8:
        return True
    else:
        return False

print(password_controller("123255553"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    
