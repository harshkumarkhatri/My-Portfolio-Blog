from flask import Flask, render_template,url_for
application = app=Flask(__name__)\

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html',title='ABOUT PAGE')


if __name__=='__main__':
    app.run(debug=True)
