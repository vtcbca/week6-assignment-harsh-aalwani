'''
Peform Following task using PYTHON Script. If any problem communicate with other student using discussion board of "Week 6 Assignment".
1. Create a result table which contain student id, student name and 5 subject marks. 
2. Enter 10 studnet details with its marks.
3. Dump table into csv file "result.csv".
4. Read result.csv file and Print Total Marks and Grade of each student. Also Append Total Marks and Grade column into result.csv file.
5. List out Top 3 Student id and name with its percentage.
'''
# Creating Table Result
def createTable():
    cur.execute("CREATE TABLE result (id text, sname text, sub1 int, sub2 int, sub3 int, sub4 int, sub5 int);")
    conn.commit()
# Inserting Records into Table
def insertRecords():
    print("Enter 10 Records: ")
    L=[]
    i=0
    for i in range(10):
        i=i+1
        print("_______________________________________________________________________________________")
        print("Record {}".format(i))
        sid=input("ID: ")
        sname=input("Name: ")
        sub1=int(input("Statistics: "))
        sub2=int(input("SE: "))
        sub3=int(input("OOP: "))
        sub4=int(input("PY & SQLite3: "))
        sub5=int(input("Web Designing: "))
        records=(sid,sname,sub1,sub2,sub3,sub4,sub5)
        L.append(records)
    query="INSERT INTO result VALUES(?,?,?,?,?,?,?);"   #Inserting 10 Records
    cur.executemany(query,L)
    conn.commit()
# Dumping all records from table to result.csv file
def dumpRecords():
    cur.execute("SELECT *FROM result")
    rows=cur.fetchall()
    header=['sid','sname','sub1','sub2','sub3','sub4','sub5']
    with open("D:\\pythonnote\\result.csv","w",newline="") as fetch_data:
        records=csv.writer(fetch_data)
        records.writerow(header)
        records.writerows(rows)
# Adding Total Marks, Percentage and Grade into result.csv
def addField():
    with open("D:\\pythonnote\\result.csv","r") as file_obj:
        filereader=csv.reader(file_obj)
        new_row=[]
        i=0
        headers=next(filereader)
        for records in filereader:
            i=i+1
            print("_______________________________________________________________________________________")
            print("Record {}:- ".format(i))
            print("ID:           {}".format(records[0]))
            print("Name:         {}".format(records[1]))
            print("Statstics:    {}".format(records[2]))
            print("SE:           {}".format(records[3]))
            print("OOP:          {}".format(records[4]))
            print("PY & SQLite3: {}".format(records[5]))
            print("Web Designing:{}".format(records[6]))
            #Total Marks of All Subjects
            records.append(int(records[2])+int(records[3])+int(records[4])+int(records[5])+int(records[6]))
            records.append(records[7]/5)    #Total Marks divided by Number of subjects=5
            print("Total Marks:  {}".format(records[7]))
            print("Percentage:   {}".format(records[8]))
            if records[8]>80 and records[8]<=100:    #Based on condition grade is assigned
                records.append('Distinction')
            elif records[8]>65 and records[8]<=80:
                records.append('First Class')
            elif records[8]>50 and records[8]<=65:
                records.append('Second Class')
            elif records[8]>35 and records[8]<=50:
                records.append('Pass')
            else:
                records.append('Fail')
            print("Grade:        {}".format(records[9]))
            new_row.append(records)
    with open("D:\\pythonnote\\result.csv","w",newline="") as writer_obj:
        filewriter=csv.writer(writer_obj)
        headers.extend(('total','per','grade'))   #Added New Headers
        filewriter.writerow(headers)
        filewriter.writerows(new_row)
# Records of Top 3 students based on Percentage
def topper():
    with open("D:\\pythonnote\\result.csv","r") as read_obj:
        i=0
        filereader=csv.reader(read_obj)
        data_content=list(filereader)     #Converting into a list
        L=[]
        for data in data_content:
            L.append(data[8])    #New list for percentage
        L.pop(0)                 #Header removed
        L.sort(reverse=True)     #Sorted List in Descending Order
        for per in L[:3]:        #First 3 Records are taken
            for list_stud in data_content:
                if per in list_stud:       #If percentage is in record, it prints data
                    i=i+1
                    print("_______________________________________________________________________________________")
                    print("Top {}:-".format(i))
                    print("ID:         {}".format(list_stud[0]))
                    print("Name:       {}".format(list_stud[1]))
                    print("Percentage: {}\n".format(list_stud[8]))
def operation():
    createTable()     #1- Create Table Result
    insertRecords()   #2- Insert 10 Records in Result
    dumpRecords()     #3- Dump table into csv file
    addField()        #4- Calculatin Total marks, Percentage and adding Grades, all data appends into result.csv file
    topper()          #5- Result of top 3 students with highest percentage
import sqlite3 as sq
import csv
conn=sq.connect("D:\\database\\week6.db")
cur=conn.cursor()
conn.commit()
operation()         #All operations are inside this function
