""" This module consults the latest news from the Hacker News API
    The parameter i defines the position in which the top stories start to be scrolled, 
    the parameter n defines the amount of top stories that will be displayed
"""
import json
from urllib.request import urlopen


def get_headlines(i, n):
    """ gets the titles of top stories """
    top_story_ids = urlopen("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty").read()

    ids = json.loads(top_story_ids)
    headlines = []

    for story_id in ids[i:]:
        if ids.index(story_id) <= n+1:
            story_url = "https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty".format(story_id)
            story = urlopen(story_url).read()
            story_items = json.loads(story) 
            headlines.append(story_items)
    return headlines
    