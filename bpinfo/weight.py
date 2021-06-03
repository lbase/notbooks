#!/usr/bin/python3
# rfile
# from file:///home/rfile/python3/notebooks/bpinfo/weight.ipynb
import logging
import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy import select
def main(filename) :
    try:

        eng = create_engine("mysql://rfile:simple@flatboy/rfile")
        myconn = eng.connect()
        # log
        logger = logging.getLogger('dev')
        logger.setLevel(logging.INFO)
        fileHandler = logging.FileHandler('weight.log')
        fileHandler.setLevel(logging.INFO)
        logger.addHandler(fileHandler)
        formatter = logging.Formatter('%(asctime)s  %(name)s  %(levelname)s: %(message)s')
        fileHandler.setFormatter(formatter)
        # log
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
        logger.info('query ran: %s ', filename )
    except Exception as e:
        print("sorry, an error occured  " , e)
        logger.error('error: %s', filename)
if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)
