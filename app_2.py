# from flask import Flask, render_template, request, session, redirect, url_for
# import random

# app = Flask(__name__)
# app.secret_key = 'supersecretkey'

# @app.route('/')
# def form():
#     num1 = random.randint(1, 10)
#     num2 = random.randint(1, 10)
#     session['captcha'] = num1 + num2
#     return render_template('form.html', num1=num1, num2=num2)

# @app.route('/submit', methods=['POST'])
# def submit():
#     username = request.form['username']
#     password = request.form['password']
#     captcha_answer = request.form['captcha']

#     if int(captcha_answer) == session['captcha']:
#         return f'Username: {username}, Password: {password}, Captcha: Correct'
#     else:
#         return 'Captcha: Incorrect, please try again.'

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request

app = Flask(__name__)

# Generate arithmetic captcha function
def generate_captcha():
    import random
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2
    captcha = f'{num1} {operator} {num2}'
    return captcha, str(result)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user_captcha = request.form.get('captcha')
        expected_result = request.form.get('captcha_result')

        # Validate captcha
        if user_captcha == expected_result:
            return f'Welcome, {username}!'
        else:
            return 'Captcha invalid. Please try again.'

    # Generate new captcha for each GET request
    captcha, result = generate_captcha()
    return render_template('index.html', captcha=captcha, result=result)

if __name__ == '__main__':
    app.run(debug=True)
