#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string>')
def print_string(string):
    print (string)
    return f'{string}'

@app.route('/count/<int:integer>')
def count(integer):
    return "\n".join(str(i) for i in range(integer)) +"\n"

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return 'Error: Both parameters must be numbers', 400

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2 if num2 != 0 else 'Error: Division by zero'
        if isinstance(result, float):
            result = round(result, 1)  # Round to 1 decimal place
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Error: Unsupported operation', 400

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
