#1

'''Create a menu driven program to perform following operations into a stack (BOOK).
The structure of stack BOOK is [BOOKID,BOOKNAME]
1. Push
2. Pop
3. Display
4. Exit'''

'''stack = []

def push():
    bookid = int(input('Enter book id: '))
    bookname = input('Enter book name: ')
    l = [bookid,bookname]
    stack.append(l)
    
def pop():
    if len(stack) != 0:
        print(stack.pop())
    else:
        print('Underflow')

def display():
    if len(stack) != 0:
        for i in range(len(stack)-1,-1,-1):
            print(stack[i])
    else:
        print('Underflow')
        
while True:
    print('MENU')
    print('1. Push')
    print('2. Pop')
    print('3. Display')
    print('4. Exit')
    o = int(input('Enter your choice: '))
    if o == 1:
        push()
    elif o == 2:
        pop()
    elif o == 3:
        display()
    elif o == 4:
        break
    else:
        print('Invalid Option')
'''

#2.

'''Create a menu driven database connectivity program to do the following transaction on a
MySQL table EMPLOYEE:-
Structure of EMLOYEE table is [EMPNO,ENAME,JOB,SALARY,DOB,ADDRESS,DEPTNO].
1.Create
2.Insert
3.Display
4.Exit'''

import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',passwd='2005',db='tests')
mycursor = mydb.cursor()

def create():
    try:
        mycursor.execute('CREATE TABLE EMPLOYEE(EMPNO INT, ENAME VARCHAR(20), JOB VARCHAR(20), SALARY INT, DOB DATE, ADDRESS VARCHAR(40), DEPTNO INT)')
        mydb.commit()
        print('Table created')
    except Exception as e:
        print(e)
        
def insert():
    try:
        empno = int(input('Enter Employee No: '))
        ename = input('Enter Employee Name: ')
        job = input('Enter job: ')
        salary = int(input('Enter salary: '))
        dob = input('Enter DOB (YYYY-MM-DD): ')
        address = input('Enter address: ')
        deptno = int(input('Enter department no: '))
        mycursor.execute('INSERT INTO EMPLOYEE VALUES({},"{}","{}",{},"{}","{}",{})'.format(empno,ename,job,salary,dob,address,deptno))
        mydb.commit()
        print('Record Inserted')
    except Exception as e:
        print(e)

def display():
    mycursor.execute('SELECT * FROM EMPLOYEE')
    x = mycursor.fetchall()
    for i in x:
        print(i)
        
while True:
    print('MENU')
    print('1. Create')
    print('2. Insert')
    print('3. Display')
    print('4. Exit')
    o = int(input('Enter your choice: '))
    if o == 1:
        create()
    elif o == 2:
        insert()
    elif o == 3:
        display()
    elif o == 4:
        break
    else:
        print('Invalid Option')

#3.

'''
Create a menu driven database connectivity program to do the following transaction on a MySQL
table TEACHER , the structure of Teacher table is
[TID,TNAME,DESIGNATION,SALARY,DATEOFJOINING,PHONENUMBER,ADDRESS].

1.Create
2.Insert
3.Delete
4.Exit'''

'''import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',passwd='Emsitchaf1',db='practicalexam')
mycursor = mydb.cursor()

def create():
    try:
        mycursor.execute('CREATE TABLE TEACHER(TID INT, TNAME VARCHAR(20), DESIGNATION VARCHAR(20), SALARY INT, DATEOFJOINING DATE, PHONENUMBER INT,ADDRESS VARCHAR(40))')
        mydb.commit()
        print('Table created')
    except Exception as e:
        print(e)
        
def insert():
    try:
        tid = int(input('Enter Teacher ID: '))
        tname = input('Enter Teacher Name: ')
        designation = input('Enter designation: ')
        salary = int(input('Enter salary: '))
        doj = input('Enter date of joining (YYYY-MM-DD): ')
        phone = int(input('Enter phone no: '))
        address = input('Enter address: ')
        mycursor.execute('INSERT INTO EMPLOYEE VALUES({},"{}","{}",{},"{}",{},"{}")'.format(tid,tname,designation,salary,doj,phone,address))
        mydb.commit()
        print('Record Inserted')
    except Exception as e:
        print(e)
        
def delete():
    try:
        tid = int(input('Enter Teacher ID to be deleted: '))
        mycursor.execute('SELECT * FROM TEACHER WHERE TID={}'.format(tid))
        x = mycursor.fetchall()
        if mycursor.rowcount == 0:
            print('Record Does Not Exist')
        else:
            mycursor.execute('DELETE FROM TEACHER WHERE TID={}'.format(tid))
            mydb.commit()
            print('Record deleted')
    except Exception as e:
        print(e)
        
while True:
    print('MENU')
    print('1. Create')
    print('2. Insert')
    print('3. Delete')
    print('4. Exit')
    o = int(input('Enter your choice: '))
    if o == 1:
        create()
    elif o == 2:
        insert()
    elif o == 3:
        delete()
    elif o == 4:
        break
    else:
        print('Invalid Option')
'''
#4.

'''
Create a menu driven program to perform following operations into a stack MOV.
The structure of stack MOV is [MOVNO,TITLE,TYPE,RATING,STARS,QTY,PRICE].
1. Push
2. Pop
3. Display
4. Exit'''

'''mov = []

def push():
    movno = int(input('Enter Movie No: '))
    title = input('Enter Movie Title: ')
    typ = input('Enter Type: ')
    rating = int(input('Enter rating out of 100: '))
    stars = int(input('Enter no of stars out of 5: '))
    qty = int(input('Enter no of copies: '))
    price = float(input('Enter price of a copy: '))
    l = [movno,title,typ,rating,stars,qty,price]
    mov.append(l)
    
def pop():
    if len(mov) != 0:
        print(mov.pop())
    else:
        print('Underflow')

def display():
    if len(mov) != 0:
        for i in range(len(mov)-1,-1,-1):
            print(mov[i])
    else:
        print('Underflow')
        
while True:
    print('MENU')
    print('1. Push')
    print('2. Pop')
    print('3. Display')
    print('4. Exit')
    o = int(input('Enter your choice: '))
    if o == 1:
        push()
    elif o == 2:
        pop()
    elif o == 3:
        display()
    elif o == 4:
        break
    else:
        print('Invalid Option')'''

#5.
'''Create a menu driven program to do the following operations in a text file “Story.txt“Story.txt”
after creating the file with some information.
Display the number of blanks present in the file.

1. Display the number of lines present in the file.
2. Display the number of digits present in the file.
3. Display the number of vowels present in the file.'''


'''def lines():
    with open('Story.txt','r') as f:
        r = f.readlines()
        print('No of lines: ',len(r))

def digits():
    with open('Story.txt','r') as f:
        r = f.read()
        d = 0
        for i in r:
            if i.isdigit():
                d+=1
        print('No of digits: ',d)

def vowels():
    with open('Story.txt','r') as f:
        r = f.read()
        v = 0
        for i in r:
            if i in 'AEIOUaeoiu':
                v+=1
        print('No of vowels: ',v)

while True:
    print('MENU')
    print('1. No of lines')
    print('2. No of digits')
    print('3. No of vowels')
    print('4. Exit')
    o = int(input('Enter your choice: '))
    if o == 1:
        lines()
    elif o == 2:
        digits()
    elif o == 3:
        vowels()
    elif o == 4:
        break
    else:
        print('Invalid Option')'''

#6.

'''Create a menu driven program to do the following operations in a text file “My School.TXT” after
creating it with some information regarding your school:-

b. No of characters in the file.
c. Number of vowels present in the file.
d. Number of consonants present in the file.
e. Number of words start with “A”'''

'''def char():
    with open('My School','r') as f:
        r = f.read()
        print('No of characters:',len(r))

def vowels():
    with open('My School','r') as f:
        r = f.read()
        v = 0
        for i in r:
            if i in 'AEIOUaeiou':
                v += 1
        print('No of vowels: ',v)
        
def consonants():
    with open('My School','r') as f:
        r = f.read()
        c = 0
        for i in rL
        if i not in 'AEIOUaeiou':
            c += 1
        print('No of consonants: ',c)

def A():
    with open('My School','r') as f:
        r = f.read()
        rs = r.split()
        A = 0
        for i in rs:
            if i[0]=='A':
                A += 1
        print('Words starting with "A": ',A)
        
while True:
    print('MENU')
    print('1. No of characters')
    print('2. No of vowels')
    print('3. No of consonants')
    print('4. No of words starting with "A"')
    print('5. Exit')
    o = int(input('Enter your choice: '))
    if o == 1:
        char()
    elif o == 2:
        vowels()
    elif o == 3:
        consonants()
    elif o == 4:
        A()
    elif o == 5:
        exit
    else:
        print('Invalid Option')'''

#7.

'''Create a CSV file “books.csv” to store BOOKID, BOOKNAME, AUTHOR and PRICE  as a list:-
Write it as a menu driven program to do the following operations:-

1. ADD  
2. DISPLAY
3. SEARCH (Search a book information based on given bookid)
4. EXIT'''

'''import csv

def addrow():
    with open('books.csv','a',newline='') as f:
        rec = csv.writer(f)
        b_id = int(input('Enter the book ID: '))
        book = input('Enter name of the book: ')
        author = input('Enter name of the author: ')
        price = float(input('Enter price of the book: '))
        rec.writerow([b_id,book,author,price])
        print('Record added\n')

def readrows():
    with open('books.csv','r') as f:
        rec = csv.reader(f)
        for i in rec:
            print(i)
            
def searchbook():
    with open('books.csv','r') as f:
        rec = csv.reader(f)
        b_id = int(input('Enter book ID: '))
        for i in rec:
            if str(b_id)==i[0]:
                print('Book:',i[1])
                print('Author:',i[2])
                print('Price:',i[3])
                break
        else:
            print('Book does not exist')

while True:
    print('MENU:')
    print('1. Write a new row')
    print('2. Read all the rows')
    print('3. Search a book information')
    print('4. Exit')
    o = int(input('Enter your choice: '))
    if o == 1:
        addrow()
    elif o == 2:
        readrows()
    elif o == 3:
        searchbook()
    elif o == 4:
        break
    else:
        print('Invalid Option')'''
        
#8.

'''Write an interactive menu driven program to perform the following operations on a data file
“UAE.dat” which stores the information such as Emirates_Id, Name, and Visa Number as a list.
1. Add a record
2. Display All records
3. Search a record based on given Emirates_ID
4. Exit'''

'''import pickle

def add():
    with open('UAE.dat','ab') as f:
        try:
            eid = int(input('Enter Emirates ID: '))
            name = input('Enter name: ')
            visa = int(input('Enter visa no: '))
            l = [eid,name,visa]
            pickle.dump(l,f)
        except Exception as e:
            print(e)

def display():
    with open('UAE.dat','rb') as f:
        try:
            while True:
                r = pickle.load(f)
                print(r)
        except EOFError:
            print('EOF')

def search():
    with open('UAE.dat','rb') as f:
        eid = int(input('Enter Emirates ID to be searched for: '))
        rec = []
        f = 0
        try:
            while True:
                r = pickle.load(f)
                if r[0] == eid:
                    f = 1
                    rec = r
        except EOFError:
            if f == 0:
                print('Emirates ID not found')
            else:
                print(rec)

while True:
    print('MENU')
    print('1. Add a record')
    print('2. Display records')
    print('3. Search for an Emirates ID')
    print('4. Exit')
    o = int(input('Enter your choice: '))
    if o == 1:
        add()
    elif o == 2:
        display()
    elif o == 3:
        search()
    elif o == 4:
        break
    else:
        print('Invalid Option')'''

#9.

'''Create a menu driven program to perform following operations into a CSV file STUDENT.
The structure of the file STUDENT is [ROLLNO,NAME,GENDER ,MARKS,DOB] .
1. ADD A NEW RECORD
2. DISPLAY
3. MODIFY A RECORD(Based on given rollno)
4. Exit'''

'''import csv
import os 

def add():
    with open('student.csv','a',newline='') as f:
        rollno = int(input('Enter roll no: '))
        name = input('Enter name: ')
        gender = input('Enter gender: ')
        marks = int(input('Enter marks: '))
        dob = input('Enter date of birth (yyyy-mm-dd): ')
        l = [rollno,name,gender,marks,dob]
        rec = csv.writer(f)
        rec.writerow(l)
        print('Record Added')
        
def display():
    with open('student.csv','r') as f:
        rec = csv.reader(f)
        for i in rec:
            print(i)

def modify():
    with open('student.csv','r') as f:
        l = []
        f = 0
        rec = csv.reader(f)
        l.append(next(rec))
        rollno = int(input('Enter rollno to be updated: '))
        for i in rec:
            if int(i[0])==rec:
                i[3] = int(input('Enter new marks: '))
                l.append(i)
                f = 1 
            else:
                l.append(i)
    with open('student.csv','w',newline='') as f:
        rec = csv.writer(f)
        for i in l:
            csv.writerow(i)
    if f == 1:
        print('Record Sucessfully Modified')
    else:
        print('Record not found')

while True:
    print('MENU')
    print('1. Add a record')
    print('2. Display records')
    print('3. Modify a record')
    print('4. Exit')
    o = int(input('Enter your choice: '))
    if o == 1:
        add()
    elif o == 2:
        display()
    elif o == 3:
        modify()
    elif o == 4:
        break
    else:
        print('Invalid Option')'''
                
#10.

'''Create a menu driven program to perform following operations into a binary file ITEM.dat.
The structure of the file ITEM is [ITEMNO, INAME, QTY, PRICE]
1. ADD A NEW RECORD
2. DISPLAY
3. DELETE A RECORD(Based on given rollno)
4. Exit'''

'''import os
import pickle

def add():
    with open('ITEM.dat','wb') as f:
        itemno = int(input('Enter item no.: '))
        iname = input('Enter item name: ')
        qty = int(input('Enter quantity: '))
        price = float(input('Enter price: '))
        l = [itemno,iname,qty,price]
        pickle.dump(l,f)
        print('Record successfully added')
        
def display():
    with open('ITEM.dat','rb') as f:
        try:
            while True:
                print(pickle.load(f))
        except EOFError:
            print('End of File')
            
def delete():
    with open('ITEM.dat','rb') as f:
        with open('temp.dat','wb') as f1:
            itemno = int(input('Enter item no to be deleted: '))
            f = 0
            try:
                while True:
                    rec = pickle.load(f)
                    if rec[0] == itemno:
                        f=1
                        pass
                    else:
                        pickle.dump(rec,f1)
            except EOFError:
                if f == 0:
                    print('Record Successfully Deleted')
                else:
                    print('Record not found')
    os.remove('ITEM.dat')
    os.rename('temp.dat','ITEM.dat')
    
while True:
    print('MENU')
    print('1. Add a record')
    print('2. Display records')
    print('3. Delete a record')
    print('4. Exit')
    o = int(input('Enter your choice: '))
    if o == 1:
        add()
    elif o == 2:
        display()
    elif o == 3:
        delete()
    elif o == 4:
        break
    else:
        print('Invalid Option') '''  