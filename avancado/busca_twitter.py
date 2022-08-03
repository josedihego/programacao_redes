# -*- coding: utf-8 -*-

#pip install ipython
#pip install twitter


import  twitter


api = twitter.Api(consumer_key='aiWCEBiWFiEnjnR2gW5fIcggi',
  consumer_secret='I9ra25juAZTVQbxOledUv0OW67dhWorol0DcYbFHszL5uQiXSs',
  access_token_key='1149066632087646208-ZpxWSHbu4yQcagbHUAfeLEQDxlowqQ',
  access_token_secret='0eqzpuFDI1E2H5Zl8pxTfWDxOFAXwoGIKn0dIdU8NL3in')


print(api.VerifyCredentials())


busca = api.GetSearch("previdência") # Replace happy with your search
for tweet in busca:
    print(tweet.id, tweet.text)
