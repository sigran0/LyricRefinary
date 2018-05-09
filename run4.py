
import pickle

with open('pickles/30663137.pkl', 'rb') as f:
    datas = pickle.load(f)

    for data in datas:
        print(data)
