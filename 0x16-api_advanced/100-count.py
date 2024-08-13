#!/usr/bin/python3
"""
Module for querying the Reddit API to recursively count keyword occurrences
in hot article titles for a given subreddit.
"""

import re
import requests
from collections import defaultdict

def count_words(subreddit, word_list):
    """
    Recursively queries the Reddit API and prints a sorted count of given
    keywords in hot article titles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.

    Returns:
        None: Prints the count of keywords or nothing if subreddit is invalid.
    """
    def count_titles(subreddit, after='', hot_dict=defaultdict(int)):
        """
        Recursive helper function to query the Reddit API and count keyword
        occurrences in titles.

        Args:
            subreddit (str): The name of the subreddit.
            after (str): Pagination parameter.
            hot_dict (dict): Dictionary to accumulate keyword counts.

        Returns:
            dict: Updated dictionary with keyword counts.
        """
        url = f'https://www.reddit.com/r/{subreddit}/hot.json'
        headers = {'User-Agent': 'custom_user_agent'}
        params = {'after': after} if after else {}
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        if response.status_code != 200:
            return hot_dict

        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                pattern = re.compile(r'\b' + re.escape(word.lower()) + r'\b')
                hot_dict[word.lower()] += len(pattern.findall(title))

        after = data['data'].get('after')
        if after:
            return count_titles(subreddit, after, hot_dict)
        return hot_dict

    hot_dict = count_titles(subreddit)
    
    if not hot_dict:
        return

    sorted_words = sorted(hot_dict.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_words:
        if count > 0:
            print(f"{word}: {count}")

