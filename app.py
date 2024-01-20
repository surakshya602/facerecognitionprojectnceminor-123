from flask import Flask, render_template, request, url_for



app = Flask(__name__)

# Static location config
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['UPLOAD_FOLDER'] = 'static'
app.secret_key = 'secret'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['UPLOAD_FOLDER'] = 'static'



# Setting up home page
@app.route('/')
def index():
    return render_template('home.html')

# Example you can delete this if you want work on it changing function names and templates
# Apply your logics
@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/log-in')
def login():
    # logic
    # Database query logic to pass details of persons on table
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)