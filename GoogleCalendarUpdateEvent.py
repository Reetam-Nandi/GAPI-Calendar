import json
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

def lambda_handler(event, context):
    creds = Credentials(token=event['access_token'],
                        refresh_token=event['refresh_token'],
                        client_id=event['client_id'],
                        token_uri=event['token_uri'],
                        client_secret=event['client_secret'])
    service = build('calendar', 'v3', credentials=creds, cache_discovery=False)
    event = {
              'summary': event['calsumm'],
              'location': event['calloc'],
              'description': event['caldesc'],
              'attendees': [
                {'email': event['mail']['id1']},
                {'email': event['mail']['id2']},
              ],
            }    
    event = service.events().patch(calendarId='primary',eventId = event['caleveid'], body=event).execute()
            
    return {
        'statusCode': 200,
        'body': json.dumps('Success!')
    }        
         
