from flask import Flask, render_template,request

web=Flask(__name__)

@web.route('/')
@web.route('/register')

def home():
    return render_template('register.html')

@web.route('/confirmation',methods=['GET','POST'])
def register():
    if request.method=='POST':
        name=request.form.get('name')
        city=request.form.get('city')
        p=request.form.get('phone number')
        return render_template('confirm.html',name=name,city=city,phone_number=p)

if __name__ == '__main__':
    web.run(debug=True)

