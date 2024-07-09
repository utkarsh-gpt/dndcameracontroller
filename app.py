from flask import Flask, jsonify, render_template, request
from database import collection

app = Flask(__name__)

@app.route('/api-get', methods = ['GET'])
def get_latest():
    data = collection.find_one(sort=[('_id', -1)])
    collection.delete_one(sort=[('_id', -1)])
    return data

@app.route('/', methods = ['GET','POST'])
def send():
    command = ""
    
    if 'left_button' in request.form:
        command = "left"
    # elif 'stop_button' in request.form:
    #     command = "stop"
    elif 'right_button' in request.form:
        command = "right"
    
    print(command)
    collection.insert_one({"command":command})
    
    return render_template('home.html', command = command)

if __name__ == '__main__':
    app.run(debug=True)