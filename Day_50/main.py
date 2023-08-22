from Internet_Speed import Internet_Speed
from Twitter_Bot import Twitter_Bot

DRIVER_PATH = "/Users/architchoudhary/Desktop/Programming/Drivers/chromedriver"
TWITTER_USERNAME = "Testing563751"
TWITTER_PASSWORD = ".fX8'CV%2ph}%?@"

internet = Internet_Speed(path=DRIVER_PATH)

download_speed = internet.download_speed
upload_speed = internet.upload_speed

internet.quit()

twitter = Twitter_Bot(username=TWITTER_USERNAME, password=TWITTER_PASSWORD, path=DRIVER_PATH)

tweet = f"Good Morning @Something! Download speed: {download_speed} Upload speed: {upload_speed}"

twitter.create_post(tweet)
twitter.post_tweet()

twitter.quit()

