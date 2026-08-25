from flask import Flask, render_template

web=Flask(__name__)

@web.route('/')
@web.route('/register')

def home():
    return render_template('register.html')

if __name__ == '__main__':
    web.run(debug=True)

