import os
import h5py
import numpy as np
import csv
import pandas as pd
from datetime import datetime

def get_epoch_time(filename):
    """
    Takes in String date 2018-02-27 00:39:00
    returns epoch time (int)
    """
    datetime_obj = datetime.strptime(filename[-23:-4], "%Y-%m-%d %H:%M:%S")
    return datetime_obj.timestamp()


def main():
    PATH = os.path.join("Bittrex","BTC-ADA","Orderbook2")

    dataset_file = h5py.File("BTC-ADA.hdf5", "w")

    for subdir, dirs, files in os.walk(PATH):
        # sort the directory so we can preserve order
        files.sort()

        # meta data should this even be needed
        #dataset_file.create_dataset("meta", data=len(files), dtype='i')

        data = dataset_file.create_dataset("orderbook", (100,4,len(files)), dtype='f')

        for x in range(len(files)):
            # get epoch time
            # this might be a bad idea as it will be hard to retrieve
            # get_time = get_epoch_time(files[x])

            # open csv file in to panda dataframe
            df = pd.read_csv(os.path.join(PATH, files[x]))

            # create dataset with dataframe values
            # TITLE: number of file in the folder
            # HEADERS:
            # BuyRate BuyQuantity SellRate SellQuantity
            data[:,:,x] = df.values
            #dataset_file.create_dataset(str(x), data = df.values, dtype='f')

    # close dataset_file
    dataset_file.close()



if __name__ == "__main__":
    main()
