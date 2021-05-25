import sqlite3
MySchool=sqlite3.connect('schooltest.db')
nm=int(input("enter marks: "))
sql="SELECT * from student WHERE marks >='"+str(nm)+"';"
curschool=MySchool.cursor()
curschool.execute(sql)
#record=curschool.fetchone()

result = curschool.fetchall()
for record in result:
    print(record)

"""if record != None:
    print(record)
    m = float(input("enter new marks: "))
    sql = "UPDATE student SET marks='" + str(m) + "' WHERE marks='" +str(nm)+ "';"
    curschool.execute(sql)
    MySchool.commit()
    print("record updated successfully")
else:
    print("Name not found")"""