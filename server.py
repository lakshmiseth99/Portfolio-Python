#creating a server

from flask import Flask,render_template, url_for,request,redirect
import csv
#use the flask class to instantiate app

app=Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')

# dynamically accepts different urls
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email=data['email']
        subject=data['subject']
        message=data['message']
        
        file = database.write(f'{email},{subject},{message}')

# def write_to_csv(data):
#     with open('database.csv',newline='',mode='a') as database2:
#         email=data["email"]
#         subject=email["subject"]
#         message=data["message"]
#         csv_writer=csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
#         csv_writer.writerow([email,subject,message])


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]  # Assuming "subject" is a key directly in data
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
#get means browser wamts us to send information
@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
    if request.method=='POST':
        #try:
        #To acces values like message,email whci turns form  data to dictionary
        #It converts the form data into a dictionary
        data=request.form.to_dict()
        write_to_csv(data)
        #print(data)
        return redirect('./thankyou.html')
        # except:
        #     return 'Oh no!!!! Its incorrect, data not loaded to db'
    else:
       
        return 'Something went wrong'










# PRACTICE PURPOSE
# #Any time when we hits the / I wamt to define a function hello world
# # @app.route('/<username>')
# # def hello_world(username=None):
# #     return render_template('index.html',name=username)
# #render template is used to access the html files, for that we need to store it in a folder named templates

# @app.route('/blog')
# def blog():
#     return ' These is the BLOG page'

# @app.route('/about')
# def about():
#     return render_template('about.html')

# # @app.route('/favicon')
# # def fav():
# #     return render_template('index.html')


# # if __name__ == "__main__":
# #     app.run(debug=True)