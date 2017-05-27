from flask import Flask
from flask import request
from flask import render_template

from silver_robot.lib.silverRobot import run
from decimal import Decimal



app = Flask(__name__)


@app.route("/")
def index():
    #do whatevr here...
    return "Hello Heruko"

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'



@app.route('/hello2/')
@app.route('/hello2/<name>')
def hello2(name=None):
    return render_template('hello2.html', name=name)



def do_the_login():
	return 'firstname: ' + request.form['firstname'] + '<br/>lastname: ' + request.form['lastname']
def show_the_login_form():
	return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form)
        return do_the_login()
    else:
        return show_the_login_form()




def guloso_post():
    qtd_classes = int(request.form['qtd_classes'])

    f = request.files['the_file']
    f_bytes = f.read()
    f_str = f_bytes.decode()
    f_str = f_str.replace('\n', '')

    nums = []
    for n in f_str.split(";"):
        if n.isnumeric():
            nums.append(Decimal(n))

    return run(nums, qtd_classes)


@app.route('/guloso', methods=['GET', 'POST'])
def guloso():
    if request.method == 'POST':
        return guloso_post()
    else:
        return render_template('upload.html', action='guloso')







#
# ==================================================
# ==================================================
#
if __name__ == "__main__":
    app.run(debug=True)
