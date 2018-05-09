import pickle
from konlpy.tag import Twitter
from utils.Requester import Requester

target_list = {}

twitter = Twitter()

with open('pickles/over1000.pkl', 'rb') as f:
    top_morphs = pickle.load(f)

for count, data in enumerate(top_morphs):
    target_list[data] = count

artist = '좋아서하는밴드'
# url = 'http://localhost:3000/api/songs?artist={}'.format(artist)
url = 'http://localhost:3000/api/songs?start={}&limit={}'

success_song_id = []

count = 0
success = 0
fail = 0

requester = Requester(url, limit=1000)

res = requester.next()

while res is not None:

    print('[{}] success : {}, fail: {}'.format(count, success, fail))

    for data in res:
        count += 1
        stop = False

        song_info = data['song_info']
        song_id = data['song_id']
        title = song_info['title']
        lyric = song_info['lyric']
        morphs = twitter.morphs(lyric)

        result = []

        for morph in morphs:
            if morph in target_list:
                result.append((target_list[morph], morph))
            else:
                stop = True
                break

        if stop is True:
            fail += 1
            continue

        success_song_id.append(song_id)
        success += 1
    res = requester.next()

print(' > success : {}, fail : {}'.format(success, fail))

with open('success_song_ids.pkl', 'wb') as f:
    pickle.dump(success_song_id, f)