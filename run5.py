
import pickle
from utils.QueryRequester import QueryRequester

with open('pickles/success_song_ids.pkl', 'rb') as f:
    success_song_ids = pickle.load(f)

for success_song_id in success_song_ids:
    requester = QueryRequester().by_song_id(success_song_id)

    res = requester.next()

    print(res)
