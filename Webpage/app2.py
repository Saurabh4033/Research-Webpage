
from flask import Flask,render_template,request,session,redirect,url_for,flash

app = Flask(__name__)

dict={'Date': '15012015', 'Amount': 51000000, 
'Amount in words': 'five crores ten lakhs', 
'Cheque No.': 309061, 'Signature': 'signed', 
'IFSC Code': 'UTIB0000426', 'Bank Name': 'AXIS BANK', 
'Account No.': 911010049001545, 'Beneficiary Name': 'Dinesh Kumar Venlola'}

@app.route('/')
def index(): 
    return redirect(url_for("search",dict))



# # @app.route('/search',methods=['POST','GET'])
# @app.route("/<dict>",methods=['POST','GET'])
# def search(dict):
#     stud=db.engine.execute("SELECT * FROM `Student`")
    
#         a1=dict['Account No.']

#         if (rollno!= "All") & (ptopic!="All Topic"):
#           bio=Student.query.filter_by(rollno=rollno,ptopic=ptopic).all()
#         elif (ptopic!="All Topic"):
#           bio=Student.query.filter_by(ptopic=ptopic).all()
#         elif(rollno!="All"):
#           bio=Student.query.filter_by(rollno=rollno).all()
#         else :
#           bio=Student.query.filter_by().all()
       
#         return render_template('search.html',bio=bio)
        
#     return render_template('search.html',stud=stud)


app.run(debug=True,port=8001) 