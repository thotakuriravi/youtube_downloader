
from typing import Optional
from pytube import YouTube, Playlist

folder = r'E:\code\Youtube1\\'
destination_folder = r'E:\code\Youtube1\download\\'

pl_url = "https://www.youtube.com/playlist?list=PLZ67c1-XfKx44ts2ogMbst4vsnguaRzRr"
playlist = Playlist(pl_url)
id = 1

def append_new_line(file_name, text_to_append):
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)

for video in playlist.video_urls:
    ytv = YouTube(video)
    
    file_name = f' video {id} {ytv.title}'
    print(file_name)
    
    # Creating the engine
   
    if ytv.streams.get_by_resolution("720p") != None:
        ytv_streams = ytv.streams.get_by_resolution("720p")
        ytv_streams.download()
        # YouTube(video)
        # Append one line to a file that does not exist
        append_new_line('info.txt', f'720p Video URL: {video}')

        # info.append( f'\n 720p Video URL: {yt_video_url}')

        # with open('readme.txt', 'w') as f:
        #     f.write('/n' .join(f' 720p Video URL: {yt_video_url}'))
    else:
        if ytv.streams.get_by_resolution("480p") != None:
            ytv_streams = ytv.streams.get_by_resolution("480p")
            ytv_streams.download()
            append_new_line('info.txt', f'480p Video URL: {video}')
            # info.append( f'\n 480p Video URL: {yt_video_url}')

            # with open('readme.txt', 'w') as f:
            #     f.write('/n' .join(f' 480p Video URL: {yt_video_url}'))

        else:
            ytv_streams = ytv.streams.get_by_resolution("360p")
            ytv_streams.download()
            append_new_line('info.txt', f'360p Video URL: {video}')
            # info.append( f'\n 360p Video URL: {yt_video_url}')

            # with open('readme.txt', 'w') as f:

            #     f.write('/n' .join(f' 360p Video URL: {yt_video_url}'))

        # ytv_streams.download()

    for x in os.listdir(folder):

                    if x.startswith(ytv.title[:4]):
                        print(ytv.title[:4])
                    # Prints only text file present in My Folder
                        print(x)
                        source = folder + x

                        # Adding the count to the new file name and extension
                        destination = folder + "video " + str(id)+ ' '+ x

                        # Renaming the file
                        os.rename(source, destination)
    for x in os.listdir(folder):

        if x.startswith('video'):
            print(ytv.title[:4])
        # Prints only text file present in My Folder
            print(x)
            source = folder + x

            # Adding the count to the new file name and extension
            destination = destination_folder + x

            # Renaming the file
            os.rename(source, destination)
                        
    id += 1
