
import konlpy
from utils.Requester import Requester

title = '개미와 베짱이'
url = 'http://localhost:3000/api/songs?title={}'.format(title)

req = Requester(url, limit=1)
data = req.next()

lyric = data[0]['song_info']['lyric']

print(lyric)