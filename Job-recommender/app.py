
import email
from pyexpat import model
from tkinter import S
from flask import Flask , render_template , request , redirect , url_for
from flask import Flask, render_template, request, redirect, session
import sqlite3 as sql



app = Flask(__name__)
app.secret_key = 'fasdgfdgdfg'

@app.route('/')
def home():
    return render_template('home.html')



"""@app.route('/index')

def index():
    return render_template('index.html')"""

@app.route('/index')
def index():
   con = sql.connect("job_database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from jobs")
   
   jobs = cur.fetchall()
   return render_template("index.html", jobs = jobs)




@app.route('/login1')
def login1():
    return render_template('login1.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

"""@app.route('/search1')
def search1():
    return render_template('search1.html')"""

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/companies')
def companies():
    return render_template('companies.html')

@app.route('/postjob')
def postjob():
    return render_template('postjob.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         keywords = request.form['keywords']
         jobrole = request.form['jobrole']
         company = request.form['company']
         location = request.form['location']
         experience = request.form['experience']
         ctc = request.form['ctc']
         
         with sql.connect("job_database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO jobs (keywords,jobrole,company,location,experience,ctc) VALUES (?,?,?,?,?,?)",(keywords,jobrole,company,location,experience,ctc) )

            con.commit()
            msg = "Record successfully added!"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/search1')
def search1():
   con = sql.connect("job_database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from jobs")
   
   jobs = cur.fetchall()
   return render_template("search1.html", jobs = jobs)



if __name__ == "__main__":
    app.run(debug=True)

