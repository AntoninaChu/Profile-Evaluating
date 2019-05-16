from InstagramAPI import InstagramAPI
import time
from datetime import datetime

def get_comment(username, pwd, media_id):

    #stop conditions, the script will end when first of them will be true
    until_date = '2017-03-31'
    count      = 100


    API = InstagramAPI(username,pwd)
    API.login()

    max_id            = ''
    comments          = []

    _ = API.getMediaComments(media_id,max_id=max_id)
    #comments' page come from older to newer, lets preserve desc order in full list
    for c in reversed(API.LastJson['comments']):
        comments.append(c['user']['username'])

    return comments

def get_likes(username, pwd, media_id):
    #stop conditions, the script will end when first of them will be true

    API = InstagramAPI(username,pwd)
    API.login()
    likes = []

    _ = API.getMediaLikers(media_id)
    #comments' page come from older to newer, lets preserve desc order in full list
    for c in reversed(API.LastJson['users']):
        likes.append(c['username'])
    return likes
