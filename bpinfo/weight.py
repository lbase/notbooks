# rfile
# from file:///home/rfile/python3/notebooks/bpinfo/weight.ipynb
import os
import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy import select
def main(filename) :
    try:

        eng = create_engine("mysql://rfile:simple@flatboy/rfile")
        myconn = eng.connect()
        # read file
        wtdata = pd.read_csv(filename)
        # ALTER TABLE fatty AUTO_INCREMENT = 0
        #wtdata = pd.read_csv('wt5-31-2021.csv')
        wtdata.columns = wtdata.columns.str.replace(' ', '_')
        wtdata.columns = wtdata.columns.str.replace('-', '_')
        # this one working
        # store time data in var to put it back after replace statement below - easier than iterate through the columns
        # which had to be done to get the float data
        listtime = wtdata.Time = pd.to_datetime(wtdata.Time)
        wtdata = wtdata.replace(to_replace="\s\D*",  value='', regex=True)
        wtdata.Time = listtime # time back in proper format for sql import
        wtdata[["Weight","Body_Fat","Fat_Free_Body_Weight","Subcutaneous_Fat","Body_Water","Muscle_Mass","Skeletal_Muscles","Bone_Mass","Protein","BMR"]] = \
        wtdata[["Weight","Body_Fat","Fat_Free_Body_Weight","Subcutaneous_Fat","Body_Water","Muscle_Mass","Skeletal_Muscles","Bone_Mass","Protein","BMR"]].apply(pd.to_numeric)
        wtdata = wtdata.sort_values('Time')
        wtdata.to_sql('fatty', myconn, if_exists='append', index=False)
    except :
        print("sorry, an error occured" )
if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)
