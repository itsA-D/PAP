import flask

from flask import Flask, render_template_string

app = Flask(__name__)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

@app.route('/fact/<int:num>')
def factorial_series(num):
    results = {i: factorial(i) for i in range(1, num + 1)}
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Factorial Series</title>
        </head>
        <body>
            <h2>Factorial Series up to {{num}}</h2>
            <ul>
            {% for i in range(1, num + 1) %}
                <li>{{ i }}! = {{ results[i] }}</li>
            {% endfor %}
            </ul>
        </body>
        </html>
    ''', num=num, results=results)

if __name__ == '__main__':
    app.run(debug=True)
