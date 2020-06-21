# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object
# import connect 
# from connect import connect
#create class

import pymysql
# import MySQLdb
conn = pymysql.connect(host='127.0.0.1',user='root',password='',db='Python')
connect = conn.cursor()
class User():
    #constructor
    def __init__(self, name,email,age):
        self.name = name
        self.email = email
        self.age = age

    def getUserInfo(self):
        # return f'His name is {self.name} and his age is {self.age}'
        # conn = pymysql.connect(host='127.0.0.1',user='root',password='',db='Python')
        # connect = conn.cursor()
        user_data = 'select * from students;'
        connect.execute(user_data)
        data = connect.fetchall()
        i=0
        for new_data in data:
            # print(f'student name is {data[i][1]} {data[i][2]} and age is {data[i][3]}')
            print(data)
            i += 1
        # return connect.fetchall()

    def IncreaseAge(self):
        self.age += 1


class Customer(User):
     #constructor
    def __init__(self, name,email,age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def getBalance(self,balance):
        self.balance = balance

    
        
#Init User object
brad = User('Kaushal Patel','kaushalpatel089@gmail.com',22)

customer = Customer('Babulal Kumawat','babubhai@gmail.com',22)
# brad.IncreaseAge()

# customer.getBalance(22)
# print(customer.getUserInfo())
# print(brad.getUserInfo())

# print(brad.getUserInfo())
# brad.getUserInfo()
brad.getUserInfo()