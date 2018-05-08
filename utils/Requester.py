

import requests
import json

class Requester:

    def __init__(self, url, start=0, limit=50):
        self.url = url
        self.start = start
        self.limit = limit

    def next(self):
        url = self.url.format(self.start, self.limit)

        res = requests.get(url)
        jobject = json.loads(res.text)
        datas = jobject['data']

        self.start += self.limit

        if len(datas) <= 0:
            return None
        return datas