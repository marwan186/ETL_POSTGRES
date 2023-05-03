FactTrips_table_create = (
    """CREATE TABLE FactTrips
    (Tripid int PRIMARY KEY,
    Stationid int,
    Truckid int,  
    foreign key(Stationid) references station(Stationid),
    foreign key(Truckid) references DimTruck(Truckid));"""
)

station_table_create= (
    
    """CREATE TABLE station 
    (Stationid int PRIMARY KEY,
    City varchar);"""

)
DimTruck_data_table_create= (
    
    """CREATE TABLE DimTruck
    (Truckid int PRIMARY KEY,
    TruckType varchar);"""
)

FactTrips_table_create1 = (
    """CREATE TABLE FactTrips1
    (Tripid int PRIMARY KEY,
    Stationid int,
    Truckid int,  
    foreign key(Stationid) references station(Stationid),
    foreign key(Truckid) references DimTruck(Truckid));"""
)


# trigger_query=("""
# CREATE TRIGGER Check_age BEFORE INSERT ON DimTruck 
# FOR EACH ROW
# BEGIN
# IF NEW.Truckid < 23 THEN
# SET MESSAGE_TEXT = 'ERROR: 
#     AGE MUST BE ATLEAST 25 YEARS!';
# END IF;
# END;""")
# #INSERT RECORDS 
# #FactTrips_table_insert=("""f"INSERT INTO FactTrips ({','.join(%s,%s,%s)}) VALUES {%s,%s,%s}";""")
# # DimTruck_table_insert = ("""INSERT INTO DimTruck (Truckid, TruckType) VALUES (%s, %s);""")
# # DimStation_table_insert = ("""INSERT INTO DimStation (Stationid, City) VALUES (%s, %s);""")

create_table_queries= [station_table_create, DimTruck_data_table_create,FactTrips_table_create,FactTrips_table_create1]
drop_table_queries= [station_table_create, DimTruck_data_table_create,FactTrips_table_create,FactTrips_table_create1]


