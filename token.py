import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

credentials = None
__G_DRIVE_TOKEN_FILE = "token.json"
__OAUTH_SCOPE = ["https://www.googleapis.com/auth/drive"]

if os.path.exists(__G_DRIVE_TOKEN_FILE):
    with open(__G_DRIVE_TOKEN_FILE, 'r') as f:
        credentials_info = json.load(f)
        credentials = Credentials.from_authorized_user_info(credentials_info)
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
else:
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', __OAUTH_SCOPE)
    credentials = flow.run_local_server(port=0, open_browser=False)

# Save the credentials for the next run
with open(__G_DRIVE_TOKEN_FILE, 'w') as token:
    token.write(credentials.to_json())
