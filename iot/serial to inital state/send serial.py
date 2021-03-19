import requests

# initialstate access key
access_key = "ist_WNCOhg0VQNzA4AQT9NqLLQ-UXPTwe5pF"

# initialstate bucket key
bucket_key = "697WU5WM5EYX"

# full url
url = "https://groker.init.st/api/events?accessKey=" + access_key + "&bucketKey=" + bucket_key

# do *this* 50 times
for x in range(50):
    # the vairalble name that shows up on initialstate
    post_name = "humidity"

    # the numer to post
    variable = x + 1000

    # formatting the url
    post_url = "{}&{}={}".format(url, post_name, variable)

    # printing the url and sending post request
    print(post_url)
    requests.post(post_url)