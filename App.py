from flask import Flask, render_template, request, session, flash
import sys
import mysql.connector

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aaa'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/AdminLogin')
def AdminLogin():
    return render_template('AdminLogin.html')


@app.route('/NewFaculty')
def NewFaculty():
    return render_template('NewFaculty.html')


@app.route('/FacultyLogin')
def FacultyLogin():
    return render_template('FacultyLogin.html')


@app.route('/NewCourse')
def NewCourse():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM coursetb ")
    data = cur.fetchall()

    return render_template('NewCourse.html', data=data)


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['password'] == 'admin':

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb")
            data = cur.fetchall()

            return render_template('AdminHome.html', data=data)

        else:
            return render_template('index.html', error=error)


@app.route("/AdminHome")
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb")
    data = cur.fetchall()
    return render_template('AdminHome.html', data=data)


@app.route("/AStudentInfo")
def AStudentInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM studenttb")
    data = cur.fetchall()
    return render_template('AStudentInfo.html', data=data)


@app.route("/Remove11")
def Remove11():
    id = request.args.get('id')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
    cursor = conn.cursor()
    cursor.execute("delete from  coursetb  where id='" + id + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM coursetb ")
    data = cur.fetchall()

    return render_template('NewCourse.html', data=data)


@app.route("/newCourse", methods=['GET', 'POST'])
def newCourse():
    if request.method == 'POST':
        depart = request.form['depart']
        Batch = request.form['Batch']
        year = request.form['year']
        CourseName = request.form['CourseName']

        Question1 = request.form['Question1']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
        cursor = conn.cursor()
        cursor.execute(
            "insert into coursetb values('','" + depart + "','" + Batch + "','" + year + "','" + CourseName + "','" + Question1 + "')")
        conn.commit()
        conn.close()
        flash("Record Saved!")
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM coursetb ")
    data = cur.fetchall()

    return render_template('NewCourse.html', data=data)


@app.route("/newfac", methods=['GET', 'POST'])
def newfac():
    if request.method == 'POST':
        name = request.form['uname']
        mobile = request.form['mobile']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
        cursor = conn.cursor()
        cursor.execute(
            "insert into regtb values('','" + name + "','" + mobile + "','" + email + "','" + username + "','" + password + "')")
        conn.commit()
        conn.close()
        flash("Record Saved!")
    return render_template('FacultyLogin.html')


@app.route("/facultylogin", methods=['GET', 'POST'])
def facultylogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' and password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            return render_template('index.html')
            return 'Username or Password is wrong'
        else:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where username='" + username + "' and password='" + password + "'")
            data = cur.fetchall()

            flash("you are successfully logged in")
            return render_template('FacultyHome.html', data=data)


@app.route("/FacultyHome")
def FacultyHome():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where username='" + uname + "' ")
    data = cur.fetchall()
    return render_template('FacultyHome.html', data=data)


@app.route('/NewStudent')
def NewStudent():
    return render_template('NewStudent.html')


@app.route("/newstudent", methods=['GET', 'POST'])
def newstudent():
    if request.method == 'POST':
        regno = request.form['regno']
        uname = request.form['uname']
        gender = request.form['gender']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['Address']
        depart = request.form['depart']
        Batch = request.form['Batch']
        year = request.form['year']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
        cursor = conn.cursor()
        cursor.execute(
            "insert into studenttb values('','" + regno + "','" + uname + "','" + gender + "','" + mobile + "','" + email + "','" + address + "' ,'" + depart + "','" + Batch + "','" + year + "')")
        conn.commit()
        conn.close()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM studenttb  ")
        data = cur.fetchall()

        flash("Record Saved!")
        return render_template('FStudentInfo.html', data=data)


@app.route('/FStudentInfo')
def FStudentInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM studenttb  ")
    data = cur.fetchall()
    return render_template('FStudentInfo.html', data=data)


@app.route('/NewQuestion')
def NewQuestion():
    return render_template('NewQuestion.html')


@app.route("/newsques", methods=['GET', 'POST'])
def newsques():
    if request.method == 'POST':
        depart = request.form['depart']
        Batch = request.form['Batch']
        year = request.form['year']
        Subject = request.form['Subject']

        Question1 = request.form['Question1']
        Answer1 = request.form['Answer1']
        Question2 = request.form['Question2']
        Answer2 = request.form['Answer2']
        Question3 = request.form['Question3']
        Answer3 = request.form['Answer3']
        Question4 = request.form['Question4']
        Answer4 = request.form['Answer4']
        Question5 = request.form['Question5']
        Answer5 = request.form['Answer5']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
        cursor = conn.cursor()
        cursor.execute(
            "insert into questiontb values('' ,'" + depart + "','" + Batch + "','" + year + "','" + Question1
            + "','" + Answer1 + "','" + Question2 + "','" + Answer2 + "','" + Question3 + "','" + Answer3 + "','" + Question4 + "','" + Answer4 + "','" + Question5 + "','" + Answer5 + "','" + Subject + "')")
        conn.commit()
        conn.close()
        flash("Record Saved!")
        return render_template('NewQuestion.html')


def sendmsg(targetno, message):
    import requests
    requests.post(
        "http://smsserver9.creativepoint.in/api.php?username=fantasy&password=596692&to=" + targetno + "&from=FSSMSS&message=Dear user  your msg is " + message + " Sent By FSMSG FSSMSS&PEID=1501563800000030506&templateid=1507162882948811640")


@app.route("/Remove")
def Remove():
    id = request.args.get('id')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
    cursor = conn.cursor()
    cursor.execute("delete from  studenttb  where id='" + id + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM studenttb ")
    data = cur.fetchall()

    return render_template('FStudentInfo.html', data=data)


@app.route("/QRemove")
def QRemove():
    id = request.args.get('id')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
    cursor = conn.cursor()
    cursor.execute("delete from  questiontb  where id='" + id + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM questiontb ")
    data = cur.fetchall()
    return render_template('QuestionInfo.html', data=data)


@app.route("/QuestionInfo")
def QuestionInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM questiontb ")
    data = cur.fetchall()
    return render_template('QuestionInfo.html', data=data)


@app.route("/Remove1")
def Remove1():
    id = request.args.get('id')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
    cursor = conn.cursor()
    cursor.execute("delete from  studenttb  where id='" + id + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM studenttb ")
    data = cur.fetchall()

    return render_template('AStudentInfo.html', data=data)


@app.route("/studentlogin", methods=['GET', 'POST'])
def studentlogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['regno'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from studenttb where RegisterNo='" + username + "' and name='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            return render_template('index.html')

        else:
            session['depart'] = data[7]
            session['Batch'] = data[8]
            session['year'] = data[9]

            regno = session['regno']
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM studenttb where RegisterNo='" + regno + "' ")
            data = cur.fetchall()
            return render_template('StudentHome.html', data=data)


@app.route('/StudentLogin')
def StudentLogin():
    return render_template('StudentLogin.html')


@app.route("/StudentHome")
def StudentHome():
    regno = session['regno']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM studenttb where RegisterNo='" + regno + "' ")
    data = cur.fetchall()
    return render_template('StudentHome.html', data=data)


@app.route("/Exam")
def Exam():
    de = session['depart']
    ba = session['Batch']
    ye = session['year']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM questiontb where Department='" + de + "' and Batch='" + ba + "' and year='" + ye + "'")
    data = cur.fetchall()
    return render_template('Exam.html', data=data)

user_sessions = {}
exams = {
    "exam_1": {
        "questions": [
            {"id": 1, "text": "What is 2 + 2?", "options": ["3", "4", "5"], "correct": "4"},
            {"id": 2, "text": "What is the capital of France?", "options": ["Paris", "Rome", "Berlin"], "correct": "Paris"}
        ],
        "duration": 60  # 10 minutes in seconds
    }
}
@app.route("/Start")
def Start():
    id = request.args.get('id')
    session['exid'] = id

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM questiontb where id='" + id + "'")
    data = cur.fetchall()

    from datetime import datetime, timedelta
    start_time = datetime.now()
    end_time = start_time + timedelta(seconds=60)
    user_sessions[request.remote_addr] = {"start": start_time, "end": end_time}
    return render_template('ExamAnswer.html', data=data,end_time=end_time)


@app.route("/CourseInfo")
def CourseInfo():
    de = session['depart']
    ba = session['Batch']
    ye = session['year']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM coursetb where Department='" + de + "' and Batch='" + ba + "' and year='" + ye + "'")
    data = cur.fetchall()
    return render_template('CourseInfo.html', data=data)


@app.route("/Play")
def Play():
    id = request.args.get('id')
    urll = ""

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
    cursor = conn.cursor()
    cursor.execute("SELECT * from coursetb where id ='" + str(id) + "' ")
    data = cursor.fetchone()
    if data:
        urll = data[5]

    de = session['depart']
    ba = session['Batch']
    ye = session['year']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM coursetb where Department='" + de + "' and Batch='" + ba + "' and year='" + ye + "'")
    data = cur.fetchall()
    return render_template('CourseInfo.html', data=data, urr=urll)


@app.route("/Result")
def Result():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM answertb where RegNo='" + session['regno'] + "'")
    data = cur.fetchall()
    return render_template('Result.html', data=data)


@app.route("/AdminResult")
def AdminResult():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM answertb ")
    data = cur.fetchall()
    return render_template('AdminResult.html', data=data)


def check_similarity(answer1, answer2):
    vectorizer = CountVectorizer().fit_transform([answer1, answer2])
    vectors = vectorizer.toarray()
    similarity = cosine_similarity(vectors[0].reshape(1, -1), vectors[1].reshape(1, -1))[0][0]
    return similarity


@app.route("/sanswer", methods=['GET', 'POST'])
def sanswer():
    if request.method == 'POST':
        depart = session['depart']
        Batch = session['Batch']
        year = session['year']
        id = session['exid']

        Question1 = request.form['Question1']
        Answer1 = request.form['Answer1']
        Question2 = request.form['Question2']
        Answer2 = request.form['Answer2']
        Question3 = request.form['Question3']
        Answer3 = request.form['Answer3']
        Question4 = request.form['Question4']
        Answer4 = request.form['Answer4']
        Question5 = request.form['Question5']
        Answer5 = request.form['Answer5']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from questiontb where id ='" + id + "'")
        data = cursor.fetchone()
        if data is None:
            return render_template('index.html')
            return 'Username or Password is wrong'
        else:
            sub = data[14]
            a1 = data[5]
            a2 = data[7]
            a3 = data[9]
            a4 = data[11]
            a5 = data[13]

        c1 = check_similarity(a1, Answer1)
        c2 = check_similarity(a2, Answer2)
        c3 = check_similarity(a3, Answer3)
        c4 = check_similarity(a4, Answer4)
        c5 = check_similarity(a5, Answer5)

        cs1 = check_similarity(a1, Answer1)
        cs2 = check_similarity(a2, Answer2)
        cs3 = check_similarity(a3, Answer3)
        cs4 = check_similarity(a4, Answer4)
        cs5 = check_similarity(a5, Answer5)

        print(cs1)

        if c1 <= cs1:
            m1 = c1
        else:
            m1 = cs1

        if c2 <= cs2:
            m2 = c2
        else:
            m2 = cs2

        if c3 <= cs3:
            m3 = c3
        else:
            m3 = cs3

        if c4 <= cs4:
            m4 = c4
        else:
            m4 = cs4

        if c5 <= cs5:
            m5 = c5
        else:
            m5 = cs5

        total = m1 + m2 + m3 + m4 + m5

        avg = total / 5

        if avg > 0.35:
            res = "pass"
        else:
            res = "fail"

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
        cursor = conn.cursor()
        cursor.execute(
            "insert into answertb values('' ,'" + session['regno'] + "','" + sub + "','" + str(m1) + "','" + str(
                m2) + "','" + str(m3) + "','" + str(m4) + "','" + str(m5) + "','" + str(avg) + "','" + str(res) + "')")
        conn.commit()
        conn.close()
        flash("Record Saved!")
        if avg > 0.35:
            res = "pass"
        else:
            flash("Please Improved yourSelf!")

        return render_template('Result.html')


@app.route("/Chart")
def Chart():
    import matplotlib.pyplot as plt
    import io
    import base64

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
    cursor = conn.cursor()
    cursor.execute("SELECT subject, total FROM answertb where regno='" + session['regno'] + "' ")
    students = cursor.fetchall()
    print(students)
    cursor.close()

    # Extract names and marks for the chart
    names = [student[0] for student in students]
    print(names)
    marks = [float(student[1]) for student in students]
    print(marks)

    # Create a bar chart using Matplotlib
    fig, ax = plt.subplots()
    ax.bar(names, marks, color='skyblue')
    ax.set_xlabel('Subject')
    ax.set_ylabel('Marks')
    ax.set_title('Student Marks')

    # Save the plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')

    # Render HTML template and pass the chart image
    return render_template('chart.html', chart_img=img_base64)


@app.route("/ViewMark")
def ViewMark():
    reg = request.args.get('reg')
    import matplotlib.pyplot as plt
    import io
    import base64

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1studenmarkanadb')
    cursor = conn.cursor()
    cursor.execute("SELECT subject, total FROM answertb where regno='" + str(reg) + "' ")
    students = cursor.fetchall()
    print(students)
    cursor.close()

    # Extract names and marks for the chart
    names = [student[0] for student in students]
    print(names)
    marks = [float(student[1]) for student in students]
    print(marks)

    # Create a bar chart using Matplotlib
    fig, ax = plt.subplots()
    ax.bar(names, marks, color='skyblue')
    ax.set_xlabel('Subject')
    ax.set_ylabel('Marks')
    ax.set_title('Student Marks')

    # Save the plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')

    # Render HTML template and pass the chart image
    return render_template('chart1.html', chart_img=img_base64)


import google.generativeai as genai

genai.configure(api_key='AIzaSyBvIpkSInRxoUvnyq0Bq6q3xvZeOHuT8FU')


def get_completion(out):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(out)
    print(response.text)
    return response.text


@app.route("/Chat")
def Chat():
    return render_template("Chat.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = get_completion(userText)
    # return str(bot.get_response(userText))
    return response


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
