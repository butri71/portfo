from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)

#version to pass parameters
# @app.route('/<username>/<int:post_id>')
# def hello_world(username=None, post_id=None):
#     return render_template('./index.html', name=username, post_id=post_id)

@app.route('/')
def my_home():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

#refer to doc here https://docs.python.org/3/library/csv.html on python read/write csv files
#this function is an alternative of writing into a txt file (see above)
def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        #the line below is the only difference compared to writing into a txt file
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            #write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'


# @app.route('/blog')
# def blog():
#     return 'This is the best blog in the world!'
#
# @app.route('/blog/2020/dogs')
# def blog2():
#     return 'this is my dog'