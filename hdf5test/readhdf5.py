import h5py

def main():
    with h5py.File('BTC-ADA.hdf5', 'r') as f:
        size = f['orderbook'][:,:,0]
        print(size)

main()
