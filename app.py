
from lib2to3.pgen2.token import NEWLINE
from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/<string:All_pages>')
def html_pages(All_pages):
       return render_template(All_pages)
def write_t_file(data):

   with open('database.txt', mode='a') as database:
      email = data['email']
      message = data['message']
      subject = data ['subject']
      file = database.write(f' \n{email}, {message},{subject}')

def write_to_csv(data):
   with open('database.csv', mode='a') as database2:
      email = data['email']
      message = data['message']
      subject = data ['subject']
      csv_writer = csv.writer(database2, delimiter =',', quotechar='"',  quoting=csv.QUOTE_MINIMAL)
      csv_writer.writerow([email, subject,message])
 
@app.route ('/submit_form', methods= ['POST','GET'])
def submit():
    if request.method == 'POST':
       data = request.form.to_dict()
       write_t_file(data)
       write_to_csv(data)
       print(data)
       return redirect('/thankyou.html')

    else:
        return 'Something went wrong!. Try again'