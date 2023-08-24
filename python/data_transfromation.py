import random
import requests
user_response=requests.get("https://jsonplaceholder.typicode.com/users")
post_response=requests.get("https://jsonplaceholder.typicode.com/posts")

users=user_response.json()
posts=post_response.json()

# def find_user_by_id(id):
#     return list(filter(lambda post:post.get("userId") == id))

# for post in find_user_by_id(2):
#     print(post.get("userId"), post.get("title"))
    
def find_title():
   return list(filter(lambda post:post.get("title"),posts))

word="ipsa"
list_posts = find_title()

def findIpsa():
   return list(filter(lambda post:post.get("title").split(" ").count(word)>=1 ,posts))
print(findIpsa())
