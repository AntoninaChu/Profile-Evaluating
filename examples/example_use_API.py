from InstagramAPI import InstagramAPI
from get_comments_likes import get_comment, get_likes

#data from user
login = 'login'
password = 'password'
image_url = 'media_url'

profile = InstagramAPI(login, password)

profile.login()
media_id = profile.get_media_id(image_url)

res = profile.getTotalSelfFollowers()
for follower in res:
    # prints only username of follower
    print(follower['username'])

res2 = profile.getTotalSelfFollowings()
for follower in res2:
    # prints only username of follower
    print(follower['username'])

res3 = get_comment(login, password, media_id)
print(res3)

res4 = get_likes(login, password, media_id)
print(res4)
