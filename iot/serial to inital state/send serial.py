import requests

# initialstate access key
access_key = "ist_WNCOhg0VQNzA4AQT9NqLLQ-UXPTwe5pF"

# initialstate bucket key
bucket_key = "697WU5WM5EYX"

# full url getting general url add varible access key and bucket key
url = "https://groker.init.st/api/events?accessKey=" + access_key + "&bucketKey=" + bucket_key

# do *this* 50 times
for x in range(50):
    # the vairalble name that shows up on initialstate
    post_name = "humidity"

    # the numer to post
    variable = x + 1000

    # formatting the url - compiles the url, postname and variable into one line , & is for string = for int
    post_url = "{}&{}={}".format(url, post_name, variable)

    # printing the url and sending post request
    print(post_url)   # print to console
    requests.post(post_url) # request is the name of a repository and post is the commmand to post it to the website