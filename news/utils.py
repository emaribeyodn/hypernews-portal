import itertools
import json
import os
from datetime import datetime
from typing import List

from django.conf import settings


def get_data_news():
    with open(os.path.join(settings.BASE_DIR, settings.NEWS_JSON_PATH), 'r') as f:
        news = json.load(f)
    return news
    

def get_sorted_news(news: List[dict]) -> List[dict]:
    return sorted(news, reverse=True, key=lambda x: datetime.strptime(x['created'], '%Y-%m-%d %H:%M:%S'))


def group_news_by_date(news: List[dict]) -> List[dict]:
    grouped_news = itertools.groupby(news, lambda y: y['created'].split(' ')[0])
    return {key: [x for x in value] for key, value in grouped_news}


def add_news(data, news):
    with open(os.path.join(settings.BASE_DIR, settings.NEWS_JSON_PATH), 'w') as f:
        data.append(news)
        json.dump(data, f)