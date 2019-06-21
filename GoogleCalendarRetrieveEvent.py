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
    page_token = None
    while True:
      events = service.events().list(calendarId='primary', pageToken=page_token).execute()
      for event in events['items']:
        print(event['summary'])
        print(event['id'])
      page_token = events.get('nextPageToken')
      if not page_token:
        break
            
    return {
        'statusCode': 200,
        'body': json.dumps('Success!')
    }        
         
