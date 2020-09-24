import os
import pandas as pd
import sqlalchemy
from olistlib.db import utils


BASE_DIR = os.path.dirname( os.path.dirname ( os.path.abspath(__file__) ) ) 
DATA_DIR = os.path.join ( BASE_DIR, 'data' )


files_names = [i for i in os.listdir( DATA_DIR ) if i.endswith('.csv')]

connection = utils.connect_db('mysql', os.path.join( BASE_DIR, '.env'))

for i in files_names:
    print(i)
    df_tmp = pd.read_csv( os.path.join( DATA_DIR, i ) )
    table_name = "tb_" + i.strip(".csv").replace("olist_","").replace("_dataset","")
    df_tmp.to_sql( table_name, 
                    connection,
                    schema = 'Olist', 
                    if_exists='replace',
                    index=False
                    )