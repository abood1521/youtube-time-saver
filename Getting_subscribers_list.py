import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import re

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

# Making the necessary lists
names = []
ids = []
channels_I_want_n = []
channels_I_want_i = []

print("A link is going to appear, copy this link and paste it in your internet explorer, and login using your google account (don't worry I am not going to steal your data :skull:), and then it will start asking you to choose the channels you want to watch\n")  

# The function of the api call
def main():
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "cc.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.subscriptions().list(
        part="snippet",
        mine=True,
        order="alphabetical",
        maxResults=500,
    )
    
    # Looping through all the pages of the youtube api response
    while request is not None:
        response = request.execute()
        request = youtube.subscriptions().list_next(request, response)
        for thing in response.get('items', []):
            name_of_channel = thing['snippet']['title']
            names.append(name_of_channel)
            id_of_the_channel = thing['snippet']['resourceId']['channelId']
            ids.append(id_of_the_channel)    


# Calling the youtube api request
if __name__ == "__main__":
    main()


# Parses through the repsond of the api and add the needed data to the lists
def deciding_which_channels_I_want():
    # Ask the user if they want to edit the file
    edit_file = input("Do you want to edit the file that has all the channels that I want? ")
    if edit_file == "y":
        should_I_write_to_the_file = True
    else:
        should_I_write_to_the_file = False

    # looping through all the channels names, and ids, and appending them to the acccording list
    names_file = open("wanted_channels.txt",  encoding="utf8")
    text = names_file.read()
    saved_names = text.replace('\n', ":").split(":")
    print("To save the channel just type y and then enter, but if you don't want to watch the channel just press enter")
    for channel, dd in zip(names, ids):
        if channel not in saved_names:
                Do_I_want_to_see_it = input(f'Do you want to see this |||| {channel}\'s |||| videos? ')
                if Do_I_want_to_see_it == 'y':
                    channels_I_want_n.append(channel)
                    channels_I_want_i.append(dd)
                elif Do_I_want_to_see_it == '':
                    pass        
    return channels_I_want_n, channels_I_want_i, should_I_write_to_the_file

print("")
print("")

# Calling the function
cc, ddd, writing = deciding_which_channels_I_want()
print(cc, ddd, writing)

# Editing the file

if writing == True:
    #print("The if statement is working")
    with open("wanted_channels.txt", "a", encoding="utf-8") as file:
        for channel, idd in zip(cc, ddd):
            file.writelines(f'{str(channel)}: {str(idd)}')
            file.writelines("\n")
            print(str(channel) + " " + str(idd))
    file.close()

