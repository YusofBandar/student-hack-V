import urllib2
import json
from twilio.rest import TwilioRestClient
smsbody = "fake"
result = urllib2.urlopen("http://b23ce867.ngrok.io/?sentence=" + smsbody).read()
data = json.loads(result)
print data

# Find these values at https://twilio.com/user/account
account_sid = "AC6b866e9d0bca45aecdf3accdf5895794"
auth_token = "f62e6c4add0380e34797044708c66f43"
client = TwilioRestClient(account_sid, auth_token)

result = parseInt(result)
url = ''

if result == 1:
    url = "http://b23ce867.ngrok.io/static/xml/dt1.xml"
elif result == 2 or result == 3:
    url = "http://b23ce867.ngrok.io/static/xml/dt2.xml" 
elif result == 4 or result == 5:
    url = "http://b23ce867.ngrok.io/static/xml/dt3.xml" 
elif result == 6 or result == 7:
    url = "http://b23ce867.ngrok.io/static/xml/dt4.xml" 
elif result == 8 or result == 9 or result == 10:
    url = "http://b23ce867.ngrok.io/static/xml/dt5.xml" 


call = client.calls.create(url=url,
    to="+447432752417",
    from_=" +441618504875")
