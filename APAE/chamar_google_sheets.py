from __future__ import print_function

import os.path
import pandas as pd

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class Chamar:

    def __init__(self, ID, RANGE):
        # If modifying these scopes, delete the file tooken.json.
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

        # The ID and range of a sample spreadsheet.
        self.SAMPLE_SPREADSHEET_ID = ID
        self.SAMPLE_RANGE_NAME = RANGE


    def main(self):

        creds = None

        if os.path.exists('creds/token.json'):
            creds = Credentials.from_authorized_user_file('creds/token.json', self.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'creds/User-APAE.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('creds/token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            service = build('sheets', 'v4', credentials=creds)

            # ler the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
                                        range=self.SAMPLE_RANGE_NAME).execute()

            return pd.DataFrame(result['values'], columns=['USER', 'PASSWORD', 'ID', 'EMAIL', 'KEY'])

        except HttpError as err:
            print(err)

