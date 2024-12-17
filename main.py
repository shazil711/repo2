from flask import Flask

app = Flask(__name__)


@app.route('/')
student_scores = [80, 60, 50, 65, 75, 55]


def sum_score(student_scores):
    sum =  0
    no_students = 0

    for score in student_scores:
        sum += score
        no_students = no_students + 1

    average_score = sum / no_students
    return average_score

print(sum_score(student_scores))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
