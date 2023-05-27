import csv
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

# Set up API credentials and OAuth 2.0 flow
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
CLIENT_SECRETS_FILE = "credentials.json"

def authenticate():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    flow.redirect_uri = 'http://localhost:8080/oauth2callback'
    credentials = flow.run_local_server(port=8080)
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

def save_videos_to_csv(video_list, csv_file):
    with open(csv_file, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "URL"])
        for video in video_list:
            title = video["snippet"]["title"]
            url = f"https://www.youtube.com/watch?v={video['id']['videoId']}"
            writer.writerow([title, url])

# Authenticate and create the YouTube API service
youtube = authenticate()

# Query for the videos you want to search for
search_query = "Velocity class 9"

# Get the video list
videos = get_video_list(youtube, search_query)

# Save the video list to a CSV file
csv_filename = "youtube_videos.csv"
save_videos_to_csv(videos, csv_filename)

print(f"Video list saved to {os.path.abspath(csv_filename)}")
