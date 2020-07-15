import os
import csv
from flask import Flask, render_template, send_from_directory, request, redirect
app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               './assets/favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_data_to_txt(data):
    with open("./web_server/database.txt", "a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"{email}, {subject}, {message}\n")

def write_data_to_csv(data):
    with open("./web_server/database.csv",newline = '', mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter = ',')
        csv_writer.writerow([email,subject,message])

@app.route('/send_email', methods=['POST', 'GET'])
def send_email():
    error = None
    if request.method == 'POST':
        data = request.form.to_dict()
        write_data_to_csv(data)
        return redirect("./thankyou.html")
    else:
        return "Something wrong, try again!!!"