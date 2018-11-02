
# FACEBOOK graph api
import requests

# replace your token
token = 'your-fb-token-here'

me = 'https://graph.facebook.com/v3.2/me?access_token=' + token

ret = requests.get(me)

print(ret.text)