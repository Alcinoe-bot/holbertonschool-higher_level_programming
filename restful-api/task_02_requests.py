#!/usr/bin/env python3
"""
module task_02_requests.py
"""


import requests
import csv


def fetch_and_print_posts():
    """
    fetches all post from JSONPlaceholder
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")

    if (response.status_code) == 200:
        data = response.json()
        for post in data:
            print(post.get("title"))
    else:
        print("failed to retrieve post.")


def fetch_and_save_posts():
    """
    Fetch posts and save them into a CSV file.
    """
    if response.status_code == 200:
        data = response.json()
        posts = [
            {
                 "id": post["id"],
                 "title": post["title"],
                 "body": post["body"]
            }
            for post in data
          ]

        with open("posts.csv", mode="w", encoding='utf-8') as csvfile:
            fieldname = ["id", "title", "body"]
            write = csv.DictWriter(csvfile, fieldname=fieldname)
            write.writeheader()
            write.writerows(posts)

        print("Posts saved to posts.csv.")
    else:
        print("Error fetching posts.")
