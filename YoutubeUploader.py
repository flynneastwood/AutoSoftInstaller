
# 2. This example makes a simple upload request. We recommend that you consider
#    using resumable uploads instead, particularly if you are transferring large
#    files or there's a high likelihood of a network interruption or other
#    transmission failure. To learn more about resumable uploads, see:
#    https://developers.google.com/api-client-library/python/guide/media_upload

import os
import json

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from googleapiclient.http import MediaFileUpload


scopes = ["https://www.googleapis.com/auth/youtube.upload"]

videoMedia = './testVidUpload.mp4'
thumbnail = './16_Forest.jpg'

with open('postContent.json', 'r') as json_file:     #get post content
    content = json.load(json_file)

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "./code_secret_client_340838595868-52kvrrdcuqh2n88tdjr1g3rnpigdumfk.apps.googleusercontent.com.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
          "snippet": {
            "categoryId": "1",
            "description":(content['Youtube']['body']),
            "tags": (content['Youtube']['tags']),
            "title":(content['GENERAL']['title'])
            #"thumbnails": thumbnail
          },
          "status": {
            "privacyStatus": "private",
            "madeForKids": False,
            "selfDeclaredMadeForKids": False
          }
        },
        
        media_body=MediaFileUpload(videoMedia)  #Path to the video to upload.
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()