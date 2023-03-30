"""
Find the hashtag in the following twit
"""

tweet = "Join The Legend of #Zelda series producer, Eiji Aonuma, for roughly 10 minutes of gameplay from The Legend of Zelda: #TearsOfTheKingdom on 3/28 at 7:00 a.m. PT on our YouTube channel."

pos1 = tweet.index("#")
subtweet = tweet[pos1 : ]
pos2 = subtweet.index(" ")
hashtag = subtweet[: pos2]

print(hashtag)