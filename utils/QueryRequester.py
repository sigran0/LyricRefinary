
from utils.Requester import Requester


class QueryRequester:

    def __init__(self):
        self.base_url = 'http://localhost:3000/api/songs?start={}&limit={}'
        self.query = ''
        self.query_depth = 0

        self.end_date = False
        self.start_date = False
        self.requester = None
        self.limit = 50
        self.start_index = 0

    def begin_query(self):
        if self.requester is not None:
            raise RuntimeWarning('Request was already started, you can not edit url queries')

        self.query += '&'
        self.query_depth += 1

    def get_query(self):
        return self.query

    def get_url(self):
        return self.base_url + self.query

    def by_artist_id(self, *artist_ids):
        for artist_id in artist_ids:
            self.begin_query()
            self.query += 'artist_id={}'.format(artist_id)

        return self

    def by_artist(self, *artists):
        for artist in artists:
            self.begin_query()
            self.query += 'artist={}'.format(artist)

        return self

    def by_song_id(self, *song_ids):
        for song_id in song_ids:
            self.begin_query()
            self.query += 'song_id={}'.format(song_id)

        return self

    def by_title(self, *titles):
        for title in titles:
            self.begin_query()
            self.query += 'title={}'.format(title)

        return self

    def by_genre(self, *genres):
        for genre in genres:
            self.begin_query()
            self.query += 'genre={}'.format(genre)

        return self

    def by_title_in(self, *title_ins):
        for title_in in title_ins:
            self.begin_query()
            self.query += 'title_in={}'.format(title_in)

        return self

    def by_lyric_in(self, *lyric_ins):
        for lyric_in in lyric_ins:
            self.begin_query()
            self.query += 'title_in={}'.format(lyric_in)

        return self

    def by_start_date(self, start_date):

        if self.start_date is True:
            raise ValueError('start_date is already input to this module')

        self.begin_query()
        self.query += 'start_date={}'.format(start_date)
        self.start_date = True

        return self

    def by_end_date(self, end_date):

        if self.end_date is True:
            raise ValueError('end_date is already input to this module')

        self.begin_query()
        self.query += 'end_date={}'.format(end_date)
        self.end_date = True

        return self

    def set_limit(self, limit):
        if limit <= 0:
            raise ValueError('limit must be greater than 0')

        self.limit = limit
        return self

    def set_start_index(self, start_index):
        if start_index <= 0:
            raise ValueError('start_index must be greater than 0')

        self.start_index = start_index
        return self

    def reset(self, start=0, limit=50):
        self.query = ''
        self.start_index = start
        self.limit = limit
        self.requester = None

    def next(self):
        if self.requester is None:
            self.requester = Requester(url=self.get_url(), start=self.start_index, limit=self.limit)

        return self.requester.next()