#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Print top 10 hot posts for a subreddit or None if invalid"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "python:top.ten:v1.0 (by /u/yourusername)"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        posts = response.json().get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    except Exception:
        print(None)

