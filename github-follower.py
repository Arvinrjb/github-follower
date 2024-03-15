from github import Github
from time import sleep
import requests


username = input("Enter the username:")
access_token = "Enter the GitHub account token"

def follow_user(username, access_token, user_to_follow):
    headers = {
        "Authorization": f"token {access_token}"
    }

    url = f"https://api.github.com/user/following/{user_to_follow}"
    
    response = requests.put(url, headers=headers)

    if response.status_code == 204:
        print(f"Successfully followed {user_to_follow}")
    else:
        print(f"Error following {user_to_follow}: {response.text}")


def followers(username, access_token):
    github = Github(access_token)

    user = github.get_user(username)
    followers = user.get_followers()
    for follower in followers:
        user_to_follow = follower.login
        try:
            follow_user(username, access_token, user_to_follow)
            print(f"Following {follower.login}")
            sleep(1)

        except :
            print("Error following")


followers(username, access_token)
