import json
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

def lambda_handler(event, context):
    creds = Credentials(token=event['access_token'],
                        refresh_token=event['refresh_token'],
                        client_id=event['client_id'],
                        token_uri=event['token_uri'],
                        client_secret=event['client_secret'],
                        scopes=event['scope'])
    service = build('calendar', 'v3', credentials=creds, cache_discovery=False)
    event = {
              'summary': event['calsumm'],
              'location': event['calloc'],
              'description': event['caldesc'],
              'start': {
                'dateTime': event['startdate'],
                'timeZone': event['startzone'],
              },
              'end': {
                'dateTime': event['enddate'],
                'timeZone': event['endzone'],
              },
              'recurrence': [
                'RRULE:FREQ=DAILY;COUNT=2'
              ],
              'attendees': [
                {'email': event['mail']['id1']},
                {'email': event['mail']['id2']},
              ],
              'reminders': {
                'useDefault': False,
                'overrides': [
                  {'method': 'email', 'minutes': 24 * 60},
                  {'method': 'popup', 'minutes': 10},
                ],
              },
            }
    event = service.events().insert(calendarId='primary', body=event).execute()
    newtoken=creds.token
    print(newtoken)
    return {
        'statusCode': 200,
        'body': json.dumps('Success!')
    }