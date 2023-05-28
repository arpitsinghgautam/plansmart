import csv
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pandas as pd

# Set up API credentials and OAuth 2.0 flow
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
CLIENT_SECRETS_FILE = "credentials.json"

def authenticate():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    flow.redirect_uri = 'http://localhost:8501/'
    credentials = flow.run_local_server(port=8501)
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

def get_video_list(api_service, query):
    request = api_service.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=50
    )
    response = request.execute()
    return response.get("items", [])

def save_videos_to_df(video_list):
    data = []
    for video in video_list:
        title = video["snippet"]["title"]
        url = f"https://www.youtube.com/watch?v={video['id']['videoId']}"
        data.append({"Title": title, "URL": url})
    
    df = pd.DataFrame(data)
    return df

