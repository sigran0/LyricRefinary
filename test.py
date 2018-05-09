
from konlpy.tag import Twitter
from utils.Requester import Requester

artist = '오늘의라디오'
url = 'http://localhost:3000/api/songs?artist={}'.format(artist)

req = Requester(url, limit=100)
datas = req.next()

twitter = Twitter()

for data in datas:
    song_info = data['song_info']
    title = song_info['title']
    lyric = song_info['lyric']
    morphs = twitter.morphs(lyric)

    print(' > {}'.format(title))
    print(lyric)
    print(' > {}'.format(morphs))
    print()