#from flask import Flask, render_template, request
import flask
from price import price_finder, compare
from objectdetection_finalversion import run_detectorF
#compare(noOfS, item_name, store):
#price_finder(address, no, item_name)
dp1 = 'web.html'
dp2 = 'web2.html'
dp3 = 'web3.html'
dp = [dp1, dp2, dp3]

app = flask.Flask(__name__)

@app.route('/web')
def web():
    return flask.send_file('web.html')

@app.route('/web2')
def web2():
    return flask.send_file('web2.html')

@app.route('/web3')
def web3():
    return flask.send_file('web3.html')

@app.route('/')
def index():
    return flask.send_file('index.html')
@app.route('/main')
def main():
    return flask.send_file('main.html')
@app.route('/program1', methods=['GET', 'POST'])
def program1():
    if flask.request.method == 'POST':
        tpath = flask.request.form.get('address')
        if tpath == ('1'):
            address = dp1
        else:
            if tpath == ('2'):
                address = dp2
            else:
                if tpath == ('3'):
                    address = dp3
                else:
                    address = tpath
        no = flask.request.form.get('no')
        item_name = flask.request.form.get('item_name')

        # Use the form data in your price_finder function
        result = price_finder(address, no, item_name)

        # Return the result to a separate HTML page
        return flask.render_template_string('<h1>Result for price finding</h1><p>{{ result }}</p>', result=result)
    else:
        return flask.send_file('program1.html')
@app.route('/program2')
def program2():
    #noOfS, item_name, store
    if flask.request.method == 'POST':
        tpath = flask.request.form.get('store')
        if tpath == '1':
            store = dp1
        else:
            if tpath == '2':
                store = dp2
            else:
                if tpath == '3':
                    store = dp3
                else:
                    store = tpath
        noOfS = flask.request.form.get('noOfS')
        item_name = flask.request.form.get('item_name')

        # Use the form data in your price_finder function
        result = compare(noOfS, item_name, store)

        # Return the result to a separate HTML page
        return flask.render_template_string('<h1>Result for price compare</h1><p>{{ result }}</p>', result=result)
    else:
        return flask.send_file('program2.html')
@app.route('/receive_photo')
def receive_photo():
    #if 'photo' in request.files:
    #    photo = request.files['photo']
    #    photo.save('uploads/photo.jpg')  # Save the photo locally
    #    return flask.send_file('reveive_photo.html')
    #else:
        return flask.send_file('receive_photo.html')
@app.route('/', methods=['POST'])
def result():
    print(request.form['foo']) # should display 'bar'
    return 'Received !' # response to your request.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')