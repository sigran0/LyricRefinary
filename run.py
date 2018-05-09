
import re
import pickle
from konlpy.tag import Twitter
from utils.Requester import Requester

twitter = Twitter()

artist = '오늘의라디오'
limit = 10
start = 0
url = 'http://localhost:3000/api/songs?start={}&limit={}'

word_set = set()
word_dict = dict()

count = 0

requester = Requester(url, limit=1000)
res = requester.next()

while res is not None:
    for data in res:
        song_info = data['song_info']

        lyric = song_info['lyric']

        split_lyric = twitter.morphs(lyric)

        word_set.update(split_lyric)

        for _str in split_lyric:
            if _str not in word_dict:
                word_dict[_str] = 1
            else:
                word_dict[_str] += 1
        count += 1

    print('[{}] word_set : {}'.format(count, len(word_set)))
    res = requester.next()

print(word_set)

with open('pickles/word_set.pkl', 'wb') as f:
    pickle.dump(word_set, f)

with open('pickles/word_dict.pkl', 'wb') as f:
    pickle.dump(word_dict, f)