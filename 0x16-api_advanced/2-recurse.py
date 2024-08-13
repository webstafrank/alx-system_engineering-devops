#!/usr/bin/python3
"""
Module for querying the Reddit API to recursively return a list of all
hot article titles for a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to accumulate titles during recursion.

    Returns:
        list: A list of titles if the subreddit is valid, None otherwise.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'custom_user_agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data['data']['children']
    for post in posts:
        hot_list.append(post['data']['title'])

    after = data['data'].get('after')
    if after:
        # Recursive call with the new after parameter
        return recurse(subreddit, hot_list)
    else:
        return hot_list

