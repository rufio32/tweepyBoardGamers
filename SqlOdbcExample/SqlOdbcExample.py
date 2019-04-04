import pyodbc


server = '13.66.153.161'
database = 'russreed'
username = 'michaeldickson1'
password = 'SharingMyPassword2019*'


connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database
connection_string = connection_string + ';UID=' + username + ';PWD=' + password

openConnection = pyodbc.connect(connection_string, timeout=60)
openCursor = openConnection.cursor() ##This is our way of passing stuff to and from the database.

sqlString = 'SELECT PersonId, FullName from Application.People WHERE isEmployee = 1'
openCursor.execute(sqlString)
myDataset = openCursor.fetchall()

for row in myDataset:
    print(row.FullName)

Tweet = 'I like turtles'
UserName = 'ZombieKid'

sqlString = 'INSERT Tweets (Tweet, UserName) VALUES (?, ?)'
args = Tweet, UserName

openConnection.execute(sqlString, args)
openConnection.commit()

openCursor.close()
openConnection.close()

