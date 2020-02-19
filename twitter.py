from twython import Twython

from app import (
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
)

twitter = Twython(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
)

message = "When should you decide to implement Docker? I'm trying to find when/why is a good time to use #Docker. What's your reason?"
image = open('docker.png', 'rb')

response = twitter.upload_media(media=image)
media_id = [response['media_id']]

twitter.update_status(status=message, media_ids=media_id)
print("Tweeted: " + message)
