import pypyodbc as odbc 
import pandas as pd
import pyarrow
from credential import  username, password
import random

#Creates a connection to the Azure Database.
server = 'mysqlserver16.database.windows.net'
database = 'OPTCG'
connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};Server='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+password
conn = odbc.connect(connection_string)

#A query that selects all the information in the database and saves it within the dataset variable.
sql = '''
SELECT * FROM [dbo].[Cards]; 
'''
cursor = conn.cursor()
cursor.execute(sql)
dataset = cursor.fetchall()

#Chooses a random "card" within the dataset.
random_card = random.choice(dataset)

#Assigns all of the variables with the card information from the randomly selected card.
card_number, name, cost, power, tag, effect, counter, card_type, is_blocker, is_rush, card_architype, _ = random_card

#Displays the card information in a user friendly way. 
print("Random Card:\n")
print("Card Number:", card_number)
print("Name:", name)
print("Cost:", cost)
print("Power:", power)
print("Tag:", tag)
print("Effect:", effect)
print("Counter:", counter)
print("Type:", card_type)
print("Is Blocker:", is_blocker)
print("Is Rush:", is_rush)
print("Architype:", card_architype)