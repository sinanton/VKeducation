from typing import List


class Twitter:

    def __init__(self):
        self.user_tweets = {}
        self.user_following = {}
        self.timestamp = 0

    def post_tweet(self, user_id, tweet_id):
        if user_id not in self.user_tweets:
            self.user_tweets[user_id] = []
        self.user_tweets[user_id].append((tweet_id, self.timestamp))
        self.timestamp += 1

    def get_news_feed(self, user_id) -> List[int]:
        tweets = []
        if user_id in self.user_following:
            for followee_id in self.user_following[user_id]:
                if followee_id in self.user_tweets:
                    tweets.extend(self.user_tweets[followee_id])
        if user_id in self.user_tweets:
            tweets.extend(self.user_tweets[user_id])
        tweets.sort(key=lambda x: x[1], reverse=True)
        return [tweet_id for tweet_id, _ in tweets[:10]]

    def follow(self, follower_id, followee_id):
        if follower_id not in self.user_following:
            self.user_following[follower_id] = set()
        self.user_following[follower_id].add(followee_id)

    def unfollow(self, follower_id, followee_id):
        if follower_id in self.user_following and followee_id in self.user_following[follower_id]:
            self.user_following[follower_id].remove(followee_id)

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)