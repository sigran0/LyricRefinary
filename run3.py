import pickle
from utils.Requester import Requester

target_list = []

with open('pickles/over100.pkl', 'rb') as f:
    datas = pickle.load(f)

    for count, data in enumerate(datas):
        target_list.append(data)

    title = '개미와 베짱이'
    url = 'http://localhost:3000/api/songs?title={}'.format(title)

    requester = Requester(url, limit=1)

    song_data = requester.next()
    lyric = song_data[0]['song_info']['lyric']
    print(lyric)

    print(target_list)