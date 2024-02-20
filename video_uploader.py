from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time

def upload_video(file_path, title, description, category_id, keywords, privacy_status):
    body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': keywords,
            'categoryId': category_id
        },
        'status': {
            'privacyStatus': privacy_status
        }
    }

    with open(file_path, 'rb') as file:
        print(f"Uploading {file_path}...")
        response = youtube.videos().insert(
            part=",".join(body.keys()),
            body=body,
            media_body=MediaFileUpload(file_path, chunksize=-1, resumable=True)
        ).execute()

        print(f"Uploaded {file_path} with ID: {response['id']}")

    try:
        os.remove(file_path)
        print(f"Successfully deleted {file_path} after upload.")
    except Exception as e:
        print(f"Failed to delete {file_path}. Reason: {e}")


class Watcher:
    DIRECTORY_TO_WATCH = "/mnt/youtube_uploader/video"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_created(event):
        if event.is_directory:
            return None

        elif event.src_path.endswith('.mp4'):
            # Assuming the file name is descriptive enough for title and description
            file_name = os.path.basename(event.src_path)
            title = file_name.rsplit('.', 1)[0]
            description = title
            upload_video(event.src_path, title, description, '22', ['auto-upload'], 'private')


if __name__ == "__main__":
    w = Watcher()
    w.run()
