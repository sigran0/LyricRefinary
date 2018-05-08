
import pickle
from operator import itemgetter
from collections import OrderedDict

_list = OrderedDict()


with open('pickles/word_dict.pkl', 'rb') as f:
    datas = pickle.load(f)
    sorted_data = OrderedDict(sorted(datas.items(), key=itemgetter(1), reverse=True))

    for data in sorted_data:

        if sorted_data[data] > 10:
            _list[data] = sorted_data[data]

print(_list)
print(len(_list))

with open('pickles/over100.pkl', 'wb') as f:
    pickle.dump(_list, f)