from flask import Flask, flash, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
# Watch video page
@app.route("/")
def index():
    return render_template('intro.html')

@app.route("/watch")
def watch():
    return render_template("watch.html")

# Form page

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # You can process form data here if needed
        name = request.form.get('name')
        sdo = request.form.get('sdo')
        position = request.form.get('position')
        contact = request.form.get('contact')
        email = request.form.get('email')

        # Optionally validate/save data here

        # Redirect to success page after submission
        return redirect(url_for('success'))

    # For GET, just render the form
    return render_template('form.html')
# Success page

@app.route("/success")
def success():
    return render_template("success.html")

@app.route('/flash')
def flash_page():
    return render_template('flash.html')

# Landing page
@app.route("/landing")
def landing():
    return render_template("landing.html")

if __name__ == '__main__':
    app.run()
