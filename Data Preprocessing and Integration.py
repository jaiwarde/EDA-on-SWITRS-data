
# importing the required libraries 
import pandas as pd # data processing
import sqlite3 # connecting to SQLite database 


# Create a SQL connection to our SQLite database
con=sqlite3.connect('C:/Users/jaiwa/Desktop/DCU lectures/CA682 Data Management & Visualization/Assignment/switrs.sqlite')


# Writing a query to import all the data from collision post 2015 and creating 'collisions' pandas dataframe
collision_query='''
        SELECT * FROM Collisions
        WHERE SUBSTR(CAST(Collision_Date AS STRING),1,4)  >= '2016'
'''

# Parsing the collision date feature
collisions = pd.read_sql_query(collision_query,con,parse_dates=["collision_date"])


# Wrting the query to INTEGRATE the different sources for the data 

# Integrating the data from party SQLite table by refining the query for only case_ids post 2015
parties_query='''
        SELECT * FROM Parties
        WHERE case_id in (SELECT case_id FROM Collisions
                          WHERE SUBSTR(CAST(Collision_Date AS STRING),1,4)  >= '2016')
'''

parties = pd.read_sql_query(parties_query,con,parse_dates=["collision_date"])

# Integrating the data from victims SQLite table by refining the query for only case_ids post 2015
victims_query='''
        SELECT * FROM Victims
        WHERE case_id in (SELECT case_id FROM Collisions
                          WHERE SUBSTR(CAST(Collision_Date AS STRING),1,4)  >= '2016')
'''

victims = pd.read_sql_query(victims_query,con,parse_dates=["collision_date"])

# Generating the CSVs in the targetted folder to use further for data visualization
collisions.to_csv('C:/Users/jaiwa/Desktop/DCU lectures/CA682 Data Management & Visualization/Assignment/collisions.csv',index = False)

parties.to_csv('C:/Users/jaiwa/Desktop/DCU lectures/CA682 Data Management & Visualization/Assignment/parties.csv',index = False)

victims.to_csv('C:/Users/jaiwa/Desktop/DCU lectures/CA682 Data Management & Visualization/Assignment/victims.csv',index = False)
