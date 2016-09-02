import flask
app = flask.Flask(__name__)
#app.config.update(SERVER_NAME='http://127.0.0.1:8011')

@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin',methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin',methods=['POST'])
def signin():
    if flask.request.form['username'] == 'myw' and flask.request.form['password'] == '111':
        return '<h3>Hello, admin!</h3>'
    else:
        return 'Bad username or password.'

if __name__ == '__main__':
    app.run()