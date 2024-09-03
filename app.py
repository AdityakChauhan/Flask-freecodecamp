from flask import Flask, jsonify, render_template
app = Flask(__name__)

JOBS = [
    {
    'id':1,
    'title':'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 13,90,000'
    },
    {
    'id':2,
    'title':'SOftware',
    'location': 'Noida, India',
    'salary': 'Rs. 18,40,000'
    },
    {
    'id':3,
    'title':'Backend',
    'location': 'Hyderabad, India',
    'salary': 'Rs. 20,40,000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name = 'Jovian')

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS) 

if __name__=="__main__":
    app.run(port='3002', debug = True)