import requests
import json
from flask import Flask, request
from twilio import twiml
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC6b866e9d0bca45aecdf3accdf5895794"
auth_token = "f62e6c4add0380e34797044708c66f43"
client = TwilioRestClient(account_sid, auth_token)

app = Flask(__name__)
 
@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']

    message_body = '%20'.join([y.strip() for y in message_body.split(' ')])

    result = requests.get("http://b23ce867.ngrok.io/?sentence=" + message_body).json()

    result = int(result['result'])
    url = ''

    print(result)

    # if result == 1:
    #     url = "http://b23ce867.ngrok.io/static/xml/dt1.xml"
    # elif result == 2 or result == 3:
    #     url = "http://b23ce867.ngrok.io/static/xml/dt2.xml" 
    # elif result == 4 or result == 5:
    #     url = "http://b23ce867.ngrok.io/static/xml/dt3.xml" 
    # elif result == 6 or result == 7:
    #     url = "http://b23ce867.ngrok.io/static/xml/dt4.xml" 
    # elif result == 8 or result == 9 or result == 10:
    #     url = "http://b23ce867.ngrok.io/static/xml/dt5.xml" 

    # print(url)


    # call = client.calls.create(url=url,
    #     to="+447432752417",
    #     from_=" +441618504875")

    resp = twiml.Response()
    resp.message("Your message is being scored by the official Trump O'Meter with {} out of 10".format(result))
    return str(resp)
 
if __name__ == '__main__':
    app.run()
