import pytube as pt
import os

def begin_app():
    print("Youtube video downloader application")
    print("1: Full Video (MP4)")
    print("2: Audio Only (MP3)")
    print("3: Video only (MP4)")
    choice = input("Please enter your choice (1-3): ")
    choice_int = int(choice)
    if(choice_int == 1):
        download_vid_audio()
    elif(choice_int == 2):
        download_audio()
    elif(choice_int == 3):
        download_vid()
    else:
        print("Invalid choice")
        begin_app()

def download_vid_audio():
    video_url = input("Please enter the url of the video: ")
    try:
        video = pt.YouTube(video_url)
    except:
        print("Invalid video url")
        begin_app()
    download = video.streams.first()
    download.download()
    print("Video successfully downloaded")
    begin_app()

def download_audio():
    video_url = input("Please enter the url of the video: ")
    try:
        video = pt.YouTube(video_url)
    except:
        print("Invalid video url")
        begin_app()
    download = video.streams.filter(only_audio = True)
    out_path = download[0].download()
    base, ext = os.path.splitext(out_path)
    new_path = base + ".mp3"
    os.rename(out_path, new_path)
    print("Audio successfully downloaded")
    begin_app()

def download_vid():
    video_url = input("Please enter the url of the video: ")
    try:
        video = pt.YouTube(video_url)
    except:
        print("Invalid video url")
        begin_app()
    download = video.streams.filter(only_video = True)
    download[0].download()
    print("Video successfully downloaded")
    begin_app()

begin_app()