import os
import glob
import psycopg2
import pandas as pd
from QUERIES import *



def main():

    conn=psycopg2.connect(
    host='localhost',
    database='datatest5',
    user='etl',
    password='123456',
    port='5433'
    )

    cur=conn.cursor()
    
  

    df = pd.read_csv('data/input/DimTruck.csv')

    column_names = ['Truckid', 'TruckType']
    for index, row in df.iterrows():
        values = tuple(row[column] for column in column_names)
        query = f"INSERT INTO DimTruck ({','.join(column_names)}) VALUES {values}"
        cur.execute(query)
    conn.commit()



    

    
    df = pd.read_csv('data/input/DimStation.csv')

    column_names = ['Stationid', 'City']
    for index, row in df.iterrows():
        values = tuple(row[column] for column in column_names)
        query = f"INSERT INTO station ({','.join(column_names)}) VALUES {values}"
        cur.execute(query)
    conn.commit()




    df = pd.read_csv('data/input/FactTrips.csv')

    column_names = ['Tripid','Stationid','Truckid']
    for index, row in df.iterrows():
        values = tuple(row[column] for column in column_names)
        query = f"INSERT INTO FactTrips ({','.join(column_names)}) VALUES {values}"
        cur.execute(query)
    conn.commit()

    #cur.execute(DimTruck_table_insert, fact_data)



# def upsert_dimtruck(cur, truckid, trucktype):
#     cur.execute("SELECT COUNT(*) FROM DimTruck WHERE Truckid = %s", (truckid,))
#     count = cur.fetchone()[0]

#     if count > 0:
#         cur.execute("UPDATE DimTruck SET TruckType = %s WHERE Truckid = %s", (trucktype, truckid))
#     else:
#         cur.execute("INSERT INTO DimTruck (Truckid, TruckType) VALUES (%s, %s)", (truckid, trucktype))
# def main():


#     conn = psycopg2.connect(
#     host='localhost',
#     database='datatest5',
#     user='etl',
#     password='123456',
#     port='5433'
#     )

#     cur = conn.cursor()

#     df = pd.read_csv('data/input/dimtruck1.csv')

#     column_names = ['Truckid', 'TruckType']
#     for index, row in df.iterrows():
#         truckid = row['Truckid']
#         trucktype = row['TruckType']
#         upsert_dimtruck(cur, truckid, trucktype)
    

    # trigger_query = """
    # CREATE TRIGGER TT
    # BEFORE INSERT ON DimTruck
    # FOR EACH ROW
    # BEGIN
    #     UPDATE DimTruck SET TruckType = SS WHERE Truckid = NEW.Truckid;
    # END;
    # """
    #cur.execute(trigger_query)

    # commit the changes to the database
    conn.commit()

    # close the cursor and connection
    cur.close()
   
    #cur.execute("INSERT INTO INTO DimTruck (Truckid, TruckType) VALUES (332, SSD);""")
    conn.close()





if __name__ == "__main__":
    main()



