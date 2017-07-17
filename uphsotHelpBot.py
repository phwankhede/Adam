"""
This sample demonstrates an implementation of the Lex Code Hook Interface
in order to serve a sample bot which manages orders for flowers.
Bot, Intent, and Slot models which are compatible with this sample can be found in the Lex Console
as part of the 'OrderFlowers' template.

For instructions on how to set up and test this bot, as well as additional samples,
visit the Lex Getting Started documentation http://docs.aws.amazon.com/lex/latest/dg/getting-started.html.
"""
import math
import dateutil.parser
import datetime
import time
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


""" --- Helpers to build responses which match the structure of the necessary dialog actions --- """


def get_slots(intent_request):
    return intent_request['currentIntent']['slots']


def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'ElicitSlot',
            'intentName': intent_name,
            'slots': slots,
            'slotToElicit': slot_to_elicit,
            'message': message
        }
    }


def close(session_attributes, fulfillment_state, message):
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
                
        }
    }

    return response

def close_with_card(session_attributes, fulfillment_state, message,responseCard):
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message,
            'responseCard':responseCard   
        }
    }

    return response

def close_card(session_attributes, fulfillment_state,responseCard):
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'responseCard':responseCard   
        }
    }

    return response


def delegate(session_attributes, slots):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Delegate',
            'slots': slots
        }
    }


""" --- Helper Functions --- """

""" --- upshot help fun ---"""


""" --- Intents --- -----------------------------------------------------------------------------------------------------"""
def upshot_help(intent_request):
    print intent_request
    return "in upshot help"


def Hello(intent_request):
    Hello_msg = {'contentType': 'PlainText',
                    'content': 'Hi there! I am Adam, an Upshot Helpbot. I am capable of answering your questions, explaining new terms, guiding you through steps to create almost anything and more! How can I help you?'}
                    
    return close(intent_request['sessionAttributes'], 'Fulfilled', Hello_msg) 
    
def Upshot(intent_request):
    Upshot_msg = {'contentType': 'PlainText',
                    'content': 'Upshot can do the following: Onboarding and Support, Conversion, Social, Engagement and Retention, Feedback, and Intelligence. Core of Upshot includes: Cross platform SDK to grab analytics, Segments based on usage, Actions on segments and Intelligence to your app.'}

    
    return close(intent_request['sessionAttributes'], 'Fulfilled', Upshot_msg)  
    
def Yes(intent_request):
    Yes_msg = {'contentType': 'PlainText',
                    'content': 'Great! What can I help you with?'}

    
    return close(intent_request['sessionAttributes'], 'Fulfilled', Yes_msg)  
    
def No(intent_request):
    No_msg = {'contentType': 'PlainText',
                    'content': 'Okay. Goodbye!'}

    
    return close(intent_request['sessionAttributes'], 'Fulfilled', No_msg) 
    
def End(intent_request):
    End_msg = {'contentType': 'PlainText',
                    'content': 'Awesome! Is there anything else I can help you with?'}

    
    return close(intent_request['sessionAttributes'], 'Fulfilled', End_msg)  
    
def SegmentDescription(intent_request):
    SegmentDescription_msg = {'contentType': 'PlainText',
                    'content': 'Segments will allow you to analyze how groups of your application users behave. For example, you can create a segment to send a push notification to all female users between the ages of 25 and 35 who have completed an in-app purchase (which you can track through a custom event).'}
                    
  
    
    return close(intent_request['sessionAttributes'], 'Fulfilled', SegmentDescription_msg)  
    
def Segments(intent_request):
    Segments_msg = {'contentType': 'PlainText',
                    'content': 'Hi! \n I am Upshot Help Bot :) .\n U can ask me any kind of help related to Upshot'}

    responseCard = {
      "version": 1,
      "contentType": "application/vnd.amazonaws.card.generic",
      "genericAttachments": [
          {
             "title":"Step 2: Name your segment.",
             "imageUrl":"http://upshot.ai/help/upshotimages/typesegment.png",
             "attachmentLinkUrl":"http://upshot.ai/help/upshotimages/typesegment.png",
             
           },
       ] 
     }
    return close_with_card(intent_request['sessionAttributes'], 'Fulfilled', Segments_msg, responseCard)
    
    #return close(intent_request['sessionAttributes'], 'Fulfilled', Segments_msg)    
    
def CampaignDescription(intent_request):
    CampaignDescription_msg = {'contentType': 'PlainText',
                    'content': 'Campaigns module helps you push actions to segmented users. Run a campaign to link an action to a segment. Before running a campaign you should create a segment and an action (survey/poll/rating/add/push).'}

    
    return close(intent_request['sessionAttributes'], 'Fulfilled', CampaignDescription_msg) 
    
def Campaigns(intent_request):
    Campaigns_msg = {'contentType': 'PlainText',
                    'content': 'Hi! \n I am Upshot Help Bot :) .\n U can ask me any kind of help related to Upshot'}

    
    return close(intent_request['sessionAttributes'], 'Fulfilled', Campaigns_msg)    
    
    
def AdsDescription(intent_request):
    AdsDescription_msg = {'contentType': 'PlainText',
                    'content': 'Upshot ad is one of the most powerful actions to push. Choose one of the available types and use ads to inform users about anything you want. What makes an Ad so powerful is its ability to push an image that also calls an action to the user.'}

    
    return close(intent_request['sessionAttributes'], 'Fulfilled', AdsDescription_msg) 
    
def Ads(intent_request):
    Ads_msg = {'contentType': 'PlainText',
                    'content': 'Hi! \n I am Upshot Help Bot :) .\n U can ask me any kind of help related to Upshot'}

    
    return close(intent_request['sessionAttributes'], 'Fulfilled', Ads_msg)    
    
def AdType(intent_request):
    AdType_msg = {'contentType': 'PlainText',
                    'content': 'Step 1: Create an Ad -> Step 2: Create a segment -> Step 3: Create a campaign'}

    
    return close(intent_request['sessionAttributes'], 'Fulfilled', AdType_msg)  
    

    #return close_with_card(intent_request['sessionAttributes'], 'Fulfilled', msg, responseCard)
""" --- Intents  -----------------------------------------------------------------------------------------------------"""

def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    logger.debug('dispatch userId={}, intentName={}'.format(intent_request['userId'], intent_request['currentIntent']['name']))

    intent_name = intent_request['currentIntent']['name']
    #user_id = intent_request['userId']
    # Dispatch to your bot's intent handlers
    # if intent_name == 'OrderFlowers':
    #     return order_flowers(intent_request)

    # elif intent_name == 'UpshotHelp':
    #     return upshot_help(intent_request)
            
    # elif intent_name == 'Badges':
    #     return upshot_Badges(intent_request,user_id)    
      
    # elif intent_name == 'Campaigns':
    #     return upshot_Campaigns(intent_request,user_id)  
        
    # elif intent_name == 'Funnels':
    #     return upshot_Funnels(intent_request,user_id)    
        
    if intent_name == 'Hello':
        return Hello(intent_request)
        
    elif intent_name == 'Upshot':
        return Upshot(intent_request) 
        
    elif intent_name == 'Yes':
        return Yes(intent_request)  
        
    elif intent_name == 'No':
        return No(intent_request)  
        
    elif intent_name == 'End':
        return End(intent_request)   
        
    elif intent_name == 'SegmentDescription':
        return SegmentDescription(intent_request)   
        
    elif intent_name == 'Segments':
        return Segments(intent_request)     
       
    elif intent_name == 'CampaignDescription':
        return CampaignDescription(intent_request)  
        
    elif intent_name == 'Campaigns':
        return Campaigns(intent_request)     
        
    elif intent_name == 'AdsDescription':
        return AdsDescription(intent_request) 
        
    elif intent_name == 'Ads':
        return Ads(intent_request)     
        
    elif intent_name == 'AdType':
        return AdType(intent_request)     
    
        
    raise Exception('Intent with name ' + intent_name + ' not supported')


""" --- Main handler --- """


def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """
    # By default, treat the user request as coming from the America/New_York time zone.
    os.environ['TZ'] = 'America/New_York'
    time.tzset()
    logger.debug('event.bot.name={}'.format(event['bot']['name']))
    
    return dispatch(event)
