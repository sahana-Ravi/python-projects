import mysql.connector
import mysql

movies = [
    {"id": 1, "name": "sahana", "year": 2001},
    {"id": 2, "name": "preethi", "year": 2002},
    {"id": 3, "name": "gowtham", "year": 2000},
    {"id": 4, "name": "karun", "year": 1999}

]


# database user connection
mydb = mysql.connector.connect(host="localhost", username="root",
                               password="password123", database="employee")  # USE EXISTING DATABASE
print(mydb)

# create a cursor
mycursor = mydb.cursor()


# SHOW ALL DATABASES
# mycursor.execute("SHOW DATABASES")


# CRATE DATABASE
# mycursor.execute("CREATE DATABASE MOVIES")

# create table command(dosent work if it is already there)
# mycursor.execute("CREATE TABLE MOIVES (Id INT, Name VARCHAR(100), Year INT)")


# insert data to database table
# for movie in movies:
#     mycursor.execute("INSERT INTO MOIVES (Id, Name, Year) VALUES (%s, %s, %s)",
#                      (movie["id"], movie["name"], movie["year"]))
#     mydb.commit()


# # select data from database
# mycursor.execute("SELECT * FROM MOIVES")
# myresult = mycursor.fetchall()
# # print(myresult)


# # where clause
# mycursor.execute("SELECT * FROM MOIVES WHERE name='gowtham'")
# result = mycursor.fetchall()
# # print(result)



# #drop talbe
# mycursor.execute("DROP TABLE MOIVES")

# mycursor.execute("CREATE TABLE MOIVES (Id INT, Name VARCHAR(100), Year INT)")

mydb = mysql.connector.connect(host="localhost", username="root",
                               password="password123", database="employee")  # USE EXISTING DATABASE
print(mydb)

# create a cursor
mycursor = mydb.cursor()

#create a table
mycursor.execute("CREATE TABLE MOVIES (Id INT, Name VARCHAR(100), Year INT)")


# insert data to database table
for movie in movies:
    mycursor.execute("INSERT INTO MOVIES (Id, Name, Year) VALUES (%s, %s, %s)",
                     (movie["id"], movie["name"], movie["year"]))
    mydb.commit()

# delete clause
mycursor.execute("DELETE FROM MOVIES WHERE name ='gowtham'")
result = mycursor.fetchall()
mydb.commit()
print(result)

# # select data from database
mycursor.execute("SELECT * FROM MOVIES")
myresult = mycursor.fetchall()
print(myresult)

# where clause
mycursor.execute("SELECT * FROM MOVIES WHERE name='sahana'")
result = mycursor.fetchall()
print(result)
