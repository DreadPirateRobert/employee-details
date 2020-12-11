from flask import Flask, render_template
import mysql.connector
from flask import request
import json
app = Flask(__name__, template_folder='template')

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test123')
def test_route():
    user_details = {
        'name': 'John',
        'email': 'john@doe.com'
    }

    return render_template('test.html', user=user_details)

mydatabase = mysql.connector.connect( host = 'localhost', user = 'pratik', passwd = 'pratik@123', database = 'employee', auth_plugin='mysql_native_password')
mycursor = mydatabase.cursor()

#There you can add home page and others. It is completely depends on you

@app.route('/test')
def example():
   mycursor.execute('SELECT * FROM employee')
   data = mycursor.fetchall()
#    print(data)
   return render_template('test.html', output_data = data)

@app.route('/getemployeebyid',methods=['POST'])
def getEmployeeById():
    try:
        # if session.get('user'):
 
        #     _id = request.form['id']
        #     _user = session.get('user')
 
        #     conn = mysql.connect()
        #     cursor = conn.cursor()
        #     cursor.callproc('sp_GetWishById',(_id,_user))
        #     result = cursor.fetchall()
 
        #     wish = []
        #     wish.append({'Id':result[0][0],'Title':result[0][1],'Description':result[0][2]})
 
        #     return json.dumps(wish)
        # else:
        #     return render_template('error.html', error = 'Unauthorized Access')
        query = 'SELECT * FROM employee WHERE employeeid="' + request.form.get('id') + '"; '
        print(query)
        mycursor.execute(query)
        data = mycursor.fetchall()
        print(request.form.get('id'), data)
        return json.dumps({
            'firstname': data[0][1], 
            'middlename': data[0][2],
            'lastname': data[0][3],
            'gender': data[0][4],
            'dob': data[0][5],
            'mobnumber': data[0][6],
            'altmobnumber': data[0][7],
            'emailid': data[0][8],
            'maritialstatus': data[0][9],
            'bloodgroup': data[0][10],
            'departmentid': data[0][11],
        })
    except Exception as e:
        return render_template('error.html',error = str(e))

@app.route('/addemployee')
def addemployee():
    user_details = {
        'name': 'John',
        'email': 'john@doe.com'
    }
    return render_template('addemployee.html', user=user_details)

@app.route('/addemployeedetails',methods=['POST'])
def addemployeedetails():
    print(request.form.get('firstname'))
    query = "INSERT INTO employee (firstname, middlename, lastname, gender, dob, mobnumber, altmobnumber, emailid, maritialstatus, bloodgroup, departmentid) VALUES "
    query = query + "('{firstname}', '{middlename}', '{lastname}', '{gender}', '{dob}', '{mobnumber}', '{altmobnumber}', '{emailid}', '{gender}', '{bloodgroup}', {departmentid});".format\
        (firstname = request.form.get('firstname'), middlename = request.form.get('middlename'), lastname = request.form.get('lastname'), gender = request.form.get('gender'), dob = request.form.get('dob')\
        , mobnumber = request.form.get('mobnumber'), altmobnumber = request.form.get('altmobnumber'), emailid = request.form.get('emailid'), maritialstatus = request.form.get('maritialstatus'), bloodgroup = request.form.get('bloodgroup'),  departmentid = request.form.get('departmentid'))
    print(query)
    mycursor.execute(query)
    
    mycursor.execute('SELECT * FROM employee;')
    data = mycursor.fetchall()

    return render_template('test.html', output_data = data)

if __name__=="__main__":
    app.run(debug=True)