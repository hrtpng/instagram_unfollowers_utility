from instagrapi import Client
cl = Client()
cl.login('login', 'password.')
user_id = cl.user_id_from_username('username')
following = cl.user_following(user_id)
following = [f.username for f in following.values()]
followers = cl.user_followers_gql(user_id)
followers = [f.username for f in followers]

following_list = list(following.keys())
followers_list = list(followers.keys())

def get_unfollowers():
    unfollowers_list = []
    unfollowing_list = []

    who_not_subscribed_you = list(set(following_list).difference(set(followers_list)))
    for id in who_not_subscribed_you:
        unfollowers_list.append(following[id].username)
    print('People who are not subscribed to you: ', unfollowers_list)

    you_are_not_subscribed = list(set(followers_list).difference(set(following_list)))
    for id in you_are_not_subscribed:
        unfollowing_list.append(followers[id].username)
    print('People you are not subscribed to: ', unfollowing_list)


if __name__ == '__main__':
    get_unfollowers()
