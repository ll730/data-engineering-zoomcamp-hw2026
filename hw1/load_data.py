# Load green taxi data into PostgreSQL

import pandas as pd
from sqlalchemy import create_engine

# Read the parquet file into a DataFrame
df = pd.read_parquet('green_tripdata_2025-11.parquet')

# Create database connection
# Format: postgresql://username:password@host:port/database
engine = create_engine('postgresql://postgres:postgres@localhost:5433/green_taxi')

# Write DataFrame to PostgreSQL table
# Parameters:
#   'green_taxi_trips' - name of the table to create
#   engine - the database connection
#   if_exists='replace' - drop table if it exists and create new one
#                         other options: 'append' (add rows), 'fail' (error if exists)
#   index=False - don't include DataFrame row numbers as a column
df.to_sql('green_taxi_trips', engine, if_exists='replace', index=False)
print('Green taxi trips loaded!')

# Read the zones CSV file into a second DataFrame
df2 = pd.read_csv('taxi_zone_lookup.csv')

# Write zones to PostgreSQL table
df2.to_sql('zones', engine, if_exists='replace', index=False)
print('Zones loaded!')

print('All data loaded successfully!')