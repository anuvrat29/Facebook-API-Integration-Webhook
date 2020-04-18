"""
    This is the main file which is responsible to communicate to facebook page messenger
    and facebook page wall and able to reply back.
"""
# pylint: disable=E0611
# pylint: disable=E0001
# pylint: disable=W0702
import re
import requests
from flask import Flask, request
from pymessenger import Bot

from config import BOT_ID, PAGE_ACCESS_TOKEN, FACEBOOK_SCREEN_NAME, HEADERS

APP = Flask(__name__)
BOT = Bot(str(PAGE_ACCESS_TOKEN))

class Listener:
    """
        This class contains all the methods which is required in API Integration.
    """
    @classmethod
    def response_facebook(cls, response):
        """
            This method will respond to facebook messenger same message whatever user sent.
            If you want to send custom message then replace here with your message.
        """
        BOT.send_text_message(response["senderid"], response["requestmessage"])
        print("Message Sent Successfully to " + response["sendername"])
        return "", 200

    @staticmethod
    @APP.route('/facebook', methods=['GET'])
    def check():
        """
            This is a method which facebook will check intermittently.
        """
        return """<html><h1 align="center"> You are in Anuvrat Facebook API"""\
               + """ Integration Account </h1></html>"""

    @staticmethod
    @APP.route('/facebook/webhook', methods=['GET'])
    def verify():
        """
            This is a method which facebook will check intermittently.
        """
        if request.args.get('hub.mode') == 'subscribe' and request.args.get('hub.challenge'):
            if not request.args.get('hub.verify_token') == 'check1234':
                return 'Verification code mismatch', 403
            return request.args['hub.challenge'], 200
        return "This is working", 200

    @staticmethod
    @APP.route('/facebook/webhook', methods=['POST'])
    def webhook():
        """
            This is a important method which collects data
            from facebook and sends back to facebook.
        """
        data = {}
        try:
            if request.get_json()['entry'][0]['changes'][0]['value']['verb'] == "add":
                data = request.get_json()
            else:
                data = {}
        except:
            data = request.get_json()

        # This is the start point for facebook code redirection and processing.
        try:
            data = data['entry'][0]['messaging'][0]
            if data['sender']['id'] != str(BOT_ID):
                url = FACEBOOK_SCREEN_NAME.format(data['sender']['id'])
                querystring = {"access_token": PAGE_ACCESS_TOKEN}
                usr_json = requests.get(url, headers=HEADERS, params=querystring)
                sender_name = usr_json.json()['name']

                pattern = re.compile("["u"\U0001F600-\U0001F64F""]+", flags=re.UNICODE)
                text = pattern.sub(r"", str(data['message']['text'])).strip()
                if text == "":
                    return "", 200
                reqparam = {
                    "requestmessage": text,
                    "senderid": str(data['sender']['id']),
                    "sendername": sender_name
                }
                print("\nRequest: " + str(reqparam))
                Listener().response_facebook(reqparam)
        except:
            pass

        return "", 200

if __name__ == "__main__":
    APP.run(debug=True, port=65000)
