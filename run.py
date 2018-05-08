
import re
import pickle
from utils.Requester import Requester


artist = '오늘의라디오'
limit = 10
start = 0
url = 'http://localhost:3000/api/songs?start={}&limit={}'

requester = Requester(url, limit=1000)

res = requester.next()

word_set = set()
long_word_set = set()
word_dict = dict()

count = 0

while res is not None:
    for data in res:
        song_info = data['song_info']
        # print(" > {} - {}".format(song_info['artist'], song_info['title']))
        # print(song_info['lyric'])
        # print()

        lyric = song_info['lyric']

        delimiters = " ", "\n", ".", ","
        regexPattern = '|'.join(map(re.escape, delimiters))

        split_lyric = list(filter(lambda _str: len(_str) > 0, re.split(regexPattern, lyric)))
        long_lyric = list(filter(lambda _str: len(_str) > 5, split_lyric))

        word_set.update(split_lyric)
        long_word_set.update(long_lyric)

        for _str in split_lyric:
            if _str not in word_dict:
                word_dict[_str] = 1
            else:
                word_dict[_str] += 1

        count += 1

    print('[{}] word_set : {}, long_word_set : {}'.format(count, len(word_set), len(long_word_set)))
    res = requester.next()

print(word_set)
print(long_word_set)

with open('pickles/word_set.pkl', 'wb') as f:
    pickle.dump(word_set, f)

with open('pickles/long_word_set.pkl', 'wb') as f:
    pickle.dump(long_word_set, f)

with open('pickles/word_dict.pkl', 'wb') as f:
    pickle.dump(word_dict, f)