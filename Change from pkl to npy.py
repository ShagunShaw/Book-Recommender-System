import pickle
import numpy as np

print("Start")
with open("similarity.pkl", 'rb') as f:
    data= pickle.load(f)
    np.save('sim.npy', data)

print("Done")