from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')


@app.route('/companies.html/')
def companies():
    return render_template('companies.html')

@app.route('/companies.html/liberty.html/')
def liberty():
     return render_template('liberty.html')

@app.route('/companies.html/slalom.html/')
def slalom():
     return render_template('slalom.html')


if __name__ == '__main__':
    app.run(debug=True)