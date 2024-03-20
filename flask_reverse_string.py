from flask import Flask, render_template, redirect, url_for, request
from reverse_string import reverse_string

app = Flask(__name__)


@app.route('/reverse', methods= ['POST'])
def do_reverse() -> 'html':
    title = "Here are your results:"
    input_string = request.form['input_string']
    results = reverse_string(input_string)
    return render_template('results.html',
                            the_title = title, 
                            the_input_string = input_string, 
                            the_results = results,)

@app.route('/entrypage', methods=['GET', 'POST'])
def entry_page() -> 'html':
    return render_template('entry.html', 
                            the_title = "Welcome to the reverse string app!")

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login() -> 'html':
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('entry_page'))
    return render_template('login.html', error=error)                           


app.run(debug=True)
