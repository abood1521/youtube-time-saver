import os

dir_path = os.path.dirname(os.path.realpath(__file__))
ids_of_playlists = []

def getting_the_youtube_playlists_id_from_the_file(file, listt):
    with open(dir_path + f'\{file}', 'r', encoding='utf-8') as f:
        for line in f:
            start = line.find(': ')
            end = line.find('\n')
            expected_string = line[start+2:end].strip()
            #print(expected_string)
            expected_string = list(expected_string)
            expected_string[1] = "U"
            expected_string = "".join(expected_string)
            #print(expected_string)
            listt.append(expected_string)
    return listt
x = getting_the_youtube_playlists_id_from_the_file('wanted_channels.txt', ids_of_playlists)
#print(x)
