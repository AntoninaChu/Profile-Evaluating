from InstagramAPI import InstagramAPI
from get_comments import get_comment

#data from user
login = 'login'
password = 'password'
image_url = 'image_url'

profile = InstagramAPI(login, password)

profile.login()

res = profile.getTotalSelfFollowers()
for follower in res:
    # prints only username of follower
    print(follower['username'])

res2 = profile.getTotalSelfFollowings()
for follower in res2:
    # prints only username of follower
    print(follower['username'])

res3 = get_comment(login, password, image_url)
print(res3)
