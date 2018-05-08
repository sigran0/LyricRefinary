
import requests
import csv

with open('user.csv', 'r', encoding='utf-8') as f:

    URL = 'http://147.46.15.48:3000/register'

    #   csv에서 워커 아이디를 가져오는 부분
    rdr = list(csv.reader(f))
    worker_ids = list(map(lambda line: line[0], rdr[1:]))

    for worker_id in worker_ids:
        body = {
            'email': worker_id,
            'password': worker_id,
            'passwordConf': worker_id
        }

        res = requests.post(URL, data=body)
        print(res.text)