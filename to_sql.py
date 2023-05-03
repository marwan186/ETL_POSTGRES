import pandas as pd
from sqlalchemy import create_engine

def main():
    # Set up database connection
    engine = create_engine('postgresql://etl:123456@localhost:5433/dataset88')

    # Read data from CSV file into a DataFrame
    df = pd.read_csv('data/input/DimTruck.csv')

    # Drop duplicates based on a specific column
    #df = df.drop_duplicates(subset=['column_name'], keep='last')

    # Insert remaining rows into database using upsert logic
    df.to_sql(name='DimTruck', con=engine, if_exists='replace', index=False)

if __name__ == '__main__':
    main()