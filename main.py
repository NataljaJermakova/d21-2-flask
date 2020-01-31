from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def getIndex():
  return "<h1><a href='/about'>Hi!</a></h1>"

@app.route("/home")
def home():
  return render_template('home.html', active_page='home')

@app.route("/about")
def getAbout():
  return render_template('about.html')

@app.route("/contact")
def contact():
  return render_template('contact.html', phone = 897654321)


@app.route('post')
def post():
  return request.args

if __name__ == '__main__':
  app.run(host='0.0.0.0', threaded=True, port=5000, debug=True)