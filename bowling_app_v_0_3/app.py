from flask import render_template
from myproject import app


@app.route('/')
def index():
    return render_template('home.html')



if __name__ == '__main__':
    app.run()
