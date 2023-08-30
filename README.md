# youtube--time-saver
A tool that get's you all the video you ACTUALLY want from the channels you ACTUALLY watch
## What does it do?
It gives you the videos from the channels you are subscribed (and chose) to, and were uploaded today, so that you wouldn't waste a lot of time watching things that you wouldn't benefit from, but watch the things you actually care about.

## Setting It Up:
1. Install required packages bu running ```pip install -r requirements.txt```
2. Add your api codes in the code in the ```Getting_all_the_videos_of_the_channels.py``` specifically in the ```api_key``` variable
3. Go to the Credentials panel from the Google API console. Create a client ID , and copy the text and add it in the ```cc.json``` file, or download it to the same directory as the Python script you're running and change the code in the ```Getting_subscriber_list.py``` specifically the ```client_secret_file```.

## Using It:
1. Run the ```Getting_subscribers_list.py``` and follow the instruction show in the terminal
2. Run the ```videos.py``` if you are using ```windows``` because the paths are different in ```linux``` for that you could run ```Getting_all_the_videos_of_the_channels.py```(would be happy to get help in this)
