import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import datetime
from Togettheplaylistids import getting_the_youtube_playlists_id_from_the_file


scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
api_key = "" # Put Your API Key here
dir_path = os.path.dirname(os.path.realpath(__file__))
empty_list = []
date_time = str(datetime.date.today())
youtube_links = []
saved_texts = []
# The function to get the channel ids from the file
def getting_the_youtube_channels_id_from_the_file(file, listt):
    with open(dir_path + f'\{file}', 'r', encoding='utf-8') as f:
        for line in f:
            start = line.find(': ')
            end = line.find('\n')
            expected_string = line[start+2:end].strip()
            #print(expected_string)
            listt.append(expected_string)
    return listt

def saving_for_later(file_name:str, text):
    with open(file_name, "a", encoding="utf-8") as file:
        file.writelines(text)
        file.writelines("\n")
    file.close()


def main():
    # Initialzing the API
    api_service_name = "youtube"
    api_version = "v3"
    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)

    
    # Getting the playlist ids (the playlist that contains all the videos of a channel)
    ids_of_playlist_edited = getting_the_youtube_playlists_id_from_the_file('wanted_channels.txt', empty_list)
    
    # This is the for loop to get the videos from the playlist
    
    # Looping through all the channels to get their playlists
    for playlist_id in ids_of_playlist_edited:
        reqeust = youtube.playlistItems().list(
            playlistId = playlist_id,
            part='snippet',
            maxResults = 5
        )
        response = reqeust.execute()
        
        # Looping through all the items from the response
        for part in response.get('items', []):
            date_of_video = part['snippet']['publishedAt']
            video_name = part['snippet']['title']
            channel_name = part['snippet']['channelTitle']
            video_id = part['snippet']['resourceId']['videoId']
            date_of_video_sliced = date_of_video[0:-10]
            youtube_link = 'youtube.com/watch?v=' + video_id
            if date_time==date_of_video_sliced:
                print(f'{channel_name}|| {video_name}|| {youtube_link}')
                youtube_links.append(youtube_link)
                saved_texts.append(f'{channel_name} ||| {video_name} ||| {youtube_link} ||| {date_of_video_sliced}')
                print("")
            else:
                 pass
    
    print("Done")
    download = input("Do you want to download all the videos? ")
    # You'll need to downlaod youtube-dl for this to work
    if download == 'y':
        for yl in youtube_links:
            os.system(f' youtube-dl {yl}')
    get_links = input("Do you want to get the links of all the videos? ")
    if get_links == "y":
        for yl in youtube_links:
            print(yl)
   
    save_for_later = input("Do you want to save the links for a later day? ")
    
    if save_for_later == "y":
        for text in saved_texts:
            saving_for_later("saved_links.txt", text)

main()
