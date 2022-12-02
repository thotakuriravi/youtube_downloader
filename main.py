import os
from urllib.error import HTTPError
from pytube import YouTube, Playlist
import count_video
folder = r'E:\code\'Youtube Downloder'\\'
destination_folder = r'E:\venky\\'
pl_url = "https://www.youtube.com/playlist?list=PLZ67c1-XfKx44ts2ogMbst4vsnguaRzRr"
pl = Playlist(pl_url)
print(len(pl))
#print(f'\n Playlist Title: {pl.title}')
LastDownloadedVideoId = count_video.video_id()
print(LastDownloadedVideoId)


def append_new_line(file_name, text_to_append):
    """Append given text as a new line at the end of file"""
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

while True:

    try:
        id = 1

        for yt_video_url in pl.video_urls:           
            print(id)
            
            if id > LastDownloadedVideoId:

                ytv = YouTube(yt_video_url)
                #print(f'\n Video Title: {ytv.title}')
                #print(f' Video URL: {yt_video_url}')
                #file_name = f' video {id} {ytv.title}'

                if ytv.streams.get_by_resolution("720p") != None:
                    ytv_streams = ytv.streams.get_by_resolution("720p")
                    ytv_streams.download()

                    #YouTube(yt_video_url)
                    # Append one line to a file that does not exist
                    append_new_line('info.txt', f'{id} 720p Video URL: {yt_video_url}')
                    
                    
                    # info.append( f'\n 720p Video URL: {yt_video_url}')

                    # with open('readme.txt', 'w') as f:
                    #     f.write('/n' .join(f' 720p Video URL: {yt_video_url}'))
                else :
                    if ytv.streams.get_by_resolution("480p") != None:
                        ytv_streams = ytv.streams.get_by_resolution("480p")
                        ytv_streams.download()
                        append_new_line('info.txt', f'{id} 480p Video URL: {yt_video_url}')
                        # info.append( f'\n 480p Video URL: {yt_video_url}')

                        # with open('readme.txt', 'w') as f:
                        #     f.write('/n' .join(f' 480p Video URL: {yt_video_url}'))

                    else: 
                        ytv_streams = ytv.streams.get_by_resolution("360p")
                        ytv_streams.download()
                        append_new_line('info.txt', f'{id} 360p Video URL: {yt_video_url}')
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
        id = id + 1
    except:
        time.sleep(2)
        print('error')

    



    #     f.write('/n' .join(f' 360p Video URL: {yt_video_url}'))

        #print(f'\n Download Completed...:\n {ytv.title} \n {ytv_streams[strm_no]}')



'''

#ytv_streams_li = list((enumerate(ytv_streams)))

        # print("\n Stream lists:")
        # for stream in ytv_streams_li:

        # 	print(stream)
            
        # print()

        # strm_no = int(input("Enter stream no: "))

        # print(f' Downloading...:\n {ytv_streams}')
        # 
        '''