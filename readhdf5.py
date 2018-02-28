import h5py

def main():
    with h5py.File('BTC-ADA.hdf5', 'r') as f:
        # extract one table
        data = f['orderbook'][:,:,0]
        print(data)

if __name__ == "__main__":
    main()
