from flask import Flask, request, redirect, render_template, url_for


import time
from threading import Thread
import MySQLdb
app = Flask(__name__)




@app.route('/C_details.html')
def c_details():
    return render_template('C_details.html')

@app.route('/java.html')
def java():
    return render_template('java.html')

@app.route('/resume.html')
def resume():
    return render_template('resume.html')
    

@app.route('/apply_2.html', methods= ['GET','POST'])
def apply_2():
    if request.method == 'POST':
        r1=request.form['f_name']
        r2=request.form['l_name']
        r3=request.form['email']
        r4=(request.form['ph_no'])
        r5=request.form['address']
        r6=request.form['p_sum']
        r7=request.form['skills']
        r8=request.form['w_hist']
        r9=request.form['edu']
        
        conn = MySQLdb.connect("127.0.0.1","root","","minor-2")
        c = conn.cursor()
        c.execute("TRUNCATE TABLE resumetable")
        c.execute("insert into resumetable (first_name, last_name, email, phone_no, address, professional_summary, skills, work_history, education) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (r1,r2,r3,r4,r5,r6,r7,r8,r9))
        conn.commit()
        return redirect(url_for('signin'))
    
##            conn = MySQLdb.connect("127.0.0.1","root","","database")
##            c = conn.cursor()
##            c.execute("select * from table1 where username1 = %s & password1 = %s", (a,b))
            

##            return render_template('index1.html', error=error)
##    return render_template('asaaf.html', error=error)
    return render_template('apply_2.html')
    
	
	
	


@app.route('/signup.html',methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        a1=request.form['username']
        c1=request.form['email']
        b1=request.form['password']
        d1=request.form['confirmpassword']
        if b1 == d1:
            conn = MySQLdb.connect("127.0.0.1","root","","minor")
            c = conn.cursor()
            c.execute("insert into USER (USERNAME, PASSWORD, EMAIL) values(%s,%s,%s)", (a1,b1,c1))
            conn.commit()
            return redirect(url_for('signin'))
        else:
            error = 'Password does not match. Please try again.'
    return render_template('signup.html', error=error)


@app.route('/signin.html', methods= ['GET','POST'])
def signin():
    error = None
    if request.method == 'POST':
        a2=request.form['username']
        b2=request.form['password']
        conn = MySQLdb.connect("127.0.0.1","root","","minor")
        c = conn.cursor()
        c.execute("select count(username) from user where username = %s and password = %s", (a2, b2))
        data = c.fetchall()
        conn.commit()
        a3 = str(data[0])[1]
        if a3 == '1':
            return redirect(url_for('index'))
        else:
            error = "Invalid login details. Please try again"
    return render_template('signin.html', error=error)



@app.route('/index.html')
def index():
    return render_template('index.html')
    

score = 0
Ques_no = 1

@app.route('/C.html', methods= ['GET','POST'])
def C():
    global Ques_no
    try:
        conn = MySQLdb.connect("127.0.0.1","root","","minor-2")
        c = conn.cursor()
        global score
        i= 0
        c.execute("SELECT Question FROM c_arrays	 where Ques_No = %s",str(Ques_no))
        Ques_no = Ques_no + 1
        data = c.fetchall()
        a = str(data[0][0])
    except:
        Ques_no = 1
        return redirect(url_for('function'))
    
    ss1=[]
    ss2=[]
    ss3=[]
    ss4=[]
    ss5=[]
    ss6=[]
    ss7=[]
    ss8=[]
    ss9=[]
    ss10=[]
    ss11=[]
    ss12=[]
    ss13=[]
    ss14=[]
    ss15=[]
    conn.commit()
    i=1
    a = a.replace("\n",".")
    j=0
    i=0
    count1=0
    count2=0
    loop=1
    temp1=0
    try:
        while count1<len(a):
            while temp1==1 or count1<len(a):
                
                if a[count1]=='.':
                    temp=0
                    count1=count1+1
                    if loop == 1:
                        ss1=a[count2:count1]
                        if len(ss1) < 5:
                            ss1 = None
                        
                    elif loop == 2:
                        ss2=a[count2:count1]
                        if len(ss2) < 5:
                            ss2 = None
                        
                    elif loop == 3:
                        ss3=a[count2:count1]
                        if len(ss3) < 5:
                            ss3 = None
                        
                    elif loop == 4:
                        ss4=a[count2:count1]
                        if len(ss4) < 5:
                            ss4 = None
                        
                    elif loop == 5:
                        ss5=a[count2:count1]
                        if len(ss5) < 5:
                            ss5 = None
                        
                    elif loop == 6:
                        ss6=a[count2:count1]
                        if len(ss6) < 5:
                            ss6 = None
                        
                    elif loop == 7:
                        ss7=a[count2:count1]
                        if len(ss7) < 5:
                            ss7 = None
                        
                    elif loop == 8:
                        ss8=a[count2:count1]
                        if len(ss8) < 5:
                            ss8 = None
                        
                    elif loop == 9:
                        ss9=a[count2:count1]
                        if len(ss9) < 5:
                            ss9 = None
                        
                    elif loop == 10:
                        ss10=a[count2:count1]
                        if len(ss10) < 5:
                            ss10 = None
                    elif loop == 11:
                        ss11=a[count2:count1]
                        if len(ss11) < 5:
                            ss11 = None
                    elif loop == 12:
                        ss12=a[count2:count1]
                        if len(ss12) < 5:
                            ss12 = None
                    elif loop == 13:
                        ss13=a[count2:count1]
                        if len(ss13) < 5:
                            ss13 = None
                    elif loop == 14:
                        ss14=a[count2:count1]
                        if len(ss14) < 5:
                            ss14 = None
                    elif loop == 15:
                        ss15=a[count2:count1]
                        if len(ss15) < 5:
                            ss15 = None
                    count2= count1
                    loop = loop+1
                count1=count1+1
    except:
        print "Done"
    #time.sleep(5)
    print 'pre post'
    if request.method == "POST":
        print 'in'
        a2=request.form['answer']
        conn = MySQLdb.connect("127.0.0.1","root","","minor-2")
        print "a2=   "+a2
        c = conn.cursor()
        c.execute("SELECT Answer FROM c_arrays	 where Ques_No = %s",str(Ques_no-2))
        data = c.fetchall()
            
        a1 = str(data[0][0])
        if a1 == a2:
            score = score + 1
        elif a2 == '':
            score = score
        elif (a1 != a2 and a2 != ''):
            score = score - 1
        conn.commit()
        print score
        return render_template('C.html',q1=ss1,q2=ss2,q3=ss3,q4=ss4,q5=ss5,q6=ss6,q7=ss7,q8=ss8,q9=ss9,q10=ss10,q11=ss11,q12=ss12,q13=ss13,q14=ss14,q15=ss15,score=score)

    return render_template('C.html',q1=ss1,q2=ss2,q3=ss3,q4=ss4,q5=ss5,q6=ss6,q7=ss7,q8=ss8,q9=ss9,q10=ss10,q11=ss11,q12=ss12,q13=ss13,q14=ss14,q15=ss15,score=score)




@app.route('/function.html', methods= ['GET','POST'])
def function():
    global Ques_no
    try:
        conn = MySQLdb.connect("127.0.0.1","root","","minor-2")
        c = conn.cursor()
        global score
        i= 0
        c.execute("SELECT Question FROM c_functions where Ques_No = %s",str(Ques_no))
        Ques_no = Ques_no + 1
        data = c.fetchall()
        a = str(data[0][0])
    except:
        Ques_no = 1
        return redirect(url_for('index'))
    ss1=[]
    ss2=[]
    ss3=[]
    ss4=[]
    ss5=[]
    ss6=[]
    ss7=[]
    ss8=[]
    ss9=[]
    ss10=[]
    ss11=[]
    ss12=[]
    ss13=[]
    ss14=[]
    ss15=[]
    conn.commit()
    i=1
    a = a.replace("\n",".")
    j=0
    i=0
    count1=0
    count2=0
    loop=1
    temp1=0
    try:
        while count1<len(a):
            while temp1==1 or count1<len(a):
                
                if a[count1]=='.':
                    temp=0
                    count1=count1+1
                    if loop == 1:
                        ss1=a[count2:count1]
                        if len(ss1) < 5:
                            ss1 = None
                        
                    elif loop == 2:
                        ss2=a[count2:count1]
                        if len(ss2) < 5:
                            ss2 = None
                        
                    elif loop == 3:
                        ss3=a[count2:count1]
                        if len(ss3) < 5:
                            ss3 = None
                        
                    elif loop == 4:
                        ss4=a[count2:count1]
                        if len(ss4) < 5:
                            ss4 = None
                        
                    elif loop == 5:
                        ss5=a[count2:count1]
                        if len(ss5) < 5:
                            ss5 = None
                        
                    elif loop == 6:
                        ss6=a[count2:count1]
                        if len(ss6) < 5:
                            ss6 = None
                        
                    elif loop == 7:
                        ss7=a[count2:count1]
                        if len(ss7) < 5:
                            ss7 = None
                        
                    elif loop == 8:
                        ss8=a[count2:count1]
                        if len(ss8) < 5:
                            ss8 = None
                        
                    elif loop == 9:
                        ss9=a[count2:count1]
                        if len(ss9) < 5:
                            ss9 = None
                        
                    elif loop == 10:
                        ss10=a[count2:count1]
                        if len(ss10) < 5:
                            ss10 = None
                    elif loop == 11:
                        ss11=a[count2:count1]
                        if len(ss11) < 5:
                            ss11 = None
                    elif loop == 12:
                        ss12=a[count2:count1]
                        if len(ss12) < 5:
                            ss12 = None
                    elif loop == 13:
                        ss13=a[count2:count1]
                        if len(ss13) < 5:
                            ss13 = None
                    elif loop == 14:
                        ss14=a[count2:count1]
                        if len(ss14) < 5:
                            ss14 = None
                    elif loop == 15:
                        ss15=a[count2:count1]
                        if len(ss15) < 5:
                            ss15 = None
                    count2= count1
                    loop = loop+1
                count1=count1+1
    except:
        print "Done"
    #time.sleep(5)
    print 'pre post'
    if request.method == "POST":
        print 'in'
        a2=request.form['answer']
        conn = MySQLdb.connect("127.0.0.1","root","","minor-2")
        print "a2=   "+a2
        c = conn.cursor()
        c.execute("SELECT Answer FROM c_functions where Ques_No = %s",str(Ques_no-2))
        data = c.fetchall()
            
        a1 = str(data[0][0])
        if a1 == a2:
            score = score + 1
        elif a2 == '':
            score = score
        elif (a1 != a2 and a2 != ''):
            score = score - 1
        conn.commit()
        print score
        return render_template('C.html',q1=ss1,q2=ss2,q3=ss3,q4=ss4,q5=ss5,q6=ss6,q7=ss7,q8=ss8,q9=ss9,q10=ss10,q11=ss11,q12=ss12,q13=ss13,q14=ss14,q15=ss15,score=score)

    return render_template('C.html',q1=ss1,q2=ss2,q3=ss3,q4=ss4,q5=ss5,q6=ss6,q7=ss7,q8=ss8,q9=ss9,q10=ss10,q11=ss11,q12=ss12,q13=ss13,q14=ss14,q15=ss15,score=score)
	

@app.route('/C1.html', methods= ['GET','POST'])
def c1():
    global Ques_no
    try:
        conn = MySQLdb.connect("127.0.0.1","root","","minor-2")
        c = conn.cursor()
        global score
        i= 0
        c.execute("SELECT Question FROM c_basics where Ques_No = %s",str(Ques_no))
        Ques_no = Ques_no + 1
        data = c.fetchall()
        a = str(data[0][0])
    except:
        Ques_no = 1
        return redirect(url_for('question'))
    
    ss1=[]
    ss2=[]
    ss3=[]
    ss4=[]
    ss5=[]
    ss6=[]
    ss7=[]
    ss8=[]
    ss9=[]
    ss10=[]
    ss11=[]
    ss12=[]
    ss13=[]
    ss14=[]
    ss15=[]
    conn.commit()
    i=1
    a = a.replace("\n",".")
    j=0
    i=0
    count1=0
    count2=0
    loop=1
    temp1=0
    try:
        while count1<len(a):
            while temp1==1 or count1<len(a):
                
                if a[count1]=='.':
                    temp=0
                    count1=count1+1
                    if loop == 1:
                        ss1=a[count2:count1]
                        if len(ss1) < 5:
                            ss1 = None
                        
                    elif loop == 2:
                        ss2=a[count2:count1]
                        if len(ss2) < 5:
                            ss2 = None
                        
                    elif loop == 3:
                        ss3=a[count2:count1]
                        if len(ss3) < 5:
                            ss3 = None
                        
                    elif loop == 4:
                        ss4=a[count2:count1]
                        if len(ss4) < 5:
                            ss4 = None
                        
                    elif loop == 5:
                        ss5=a[count2:count1]
                        if len(ss5) < 5:
                            ss5 = None
                        
                    elif loop == 6:
                        ss6=a[count2:count1]
                        if len(ss6) < 5:
                            ss6 = None
                        
                    elif loop == 7:
                        ss7=a[count2:count1]
                        if len(ss7) < 5:
                            ss7 = None
                        
                    elif loop == 8:
                        ss8=a[count2:count1]
                        if len(ss8) < 5:
                            ss8 = None
                        
                    elif loop == 9:
                        ss9=a[count2:count1]
                        if len(ss9) < 5:
                            ss9 = None
                        
                    elif loop == 10:
                        ss10=a[count2:count1]
                        if len(ss10) < 5:
                            ss10 = None
                    elif loop == 11:
                        ss11=a[count2:count1]
                        if len(ss11) < 5:
                            ss11 = None
                    elif loop == 12:
                        ss12=a[count2:count1]
                        if len(ss12) < 5:
                            ss12 = None
                    elif loop == 13:
                        ss13=a[count2:count1]
                        if len(ss13) < 5:
                            ss13 = None
                    elif loop == 14:
                        ss14=a[count2:count1]
                        if len(ss14) < 5:
                            ss14 = None
                    elif loop == 15:
                        ss15=a[count2:count1]
                        if len(ss15) < 5:
                            ss15 = None
                    count2= count1
                    loop = loop+1
                count1=count1+1
    except:
        print "Done"
    #time.sleep(5)
    print 'pre post'
    if request.method == "POST":
        print 'in'
        a2=request.form['answer']
        conn = MySQLdb.connect("127.0.0.1","root","","minor-2")
        print "a2=   "+a2
        c = conn.cursor()
        c.execute("SELECT Answer FROM c_basics	 where Ques_No = %s",str(Ques_no-2))
        data = c.fetchall()
        
            
        a1 = str(data[0][0])
        if a1 == a2:
            score = score + 1
        elif a2 == '':
            score = score
        elif (a1 != a2 and a2 != ''):
            score = score - 1
        conn.commit()
        print score
        return render_template('C1.html',q1=ss1,q2=ss2,q3=ss3,q4=ss4,q5=ss5,q6=ss6,q7=ss7,q8=ss8,q9=ss9,q10=ss10,q11=ss11,q12=ss12,q13=ss13,q14=ss14,q15=ss15,score=score)

    return render_template('C1.html',q1=ss1,q2=ss2,q3=ss3,q4=ss4,q5=ss5,q6=ss6,q7=ss7,q8=ss8,q9=ss9,q10=ss10,q11=ss11,q12=ss12,q13=ss13,q14=ss14,q15=ss15,score=score)

	
if __name__ == '__main__':

    app.debug = True
    app.run(host="192.168.43.169")

