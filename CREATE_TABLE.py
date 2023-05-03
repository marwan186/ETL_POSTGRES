import psycopg2
from QUERIES import create_table_queries, drop_table_queries
def create_database():

    conn= psycopg2.connect(
    host= "localhost",
    database= "def",
    user="etl",
    password="123456",
    port="5433"

)
    conn.set_session(autocommit=True)
    cur= conn.cursor()
    cur.execute("DROP DATABASE IF EXISTS dataset88;")
    cur.execute( "CREATE DATABASE mr WITH ENCODING 'utf8' TEMPLATE template0;")
    conn.close()


    conn= psycopg2.connect(
    host= "localhost",
    database="mr",
    user="etl",
    password= "123456",
    port= "5433"
    )
    cur= conn.cursor()
    return cur, conn


def drop_tables(cur, conn):

    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()



def creat_tables(cur,conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()



def main():
    cur,conn=create_database()
    drop_tables(cur,conn)
    creat_tables(cur,conn)
    conn.close()


if __name__ == "__main__":
    main()