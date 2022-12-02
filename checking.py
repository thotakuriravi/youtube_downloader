import os
import count_video

destination_folder = r'E:\venky\Navodaya\\'



def checking_files():
    list1 = []

    try:
        for x in os.listdir(destination_folder):

            if x.startswith('video'):

                # list1.append(x)
                #list1.append(int(video_id))
                #source = folder + x

                # Adding the count to the new file name and extension
                #destination = folder + "video " + str(id) + ' ' + x

                # Renaming the file
                #os.rename(source, destination)

                video = str(x).split(sep=' ')
                # print(video[1])
                list1.append(video[1])
    except:
        print('error')

    return list1

def not_downloded():
    downloaded_list = checking_files()
    down_index = count_video.downloaded_index()

    #print( len(downloaded_list), len(down_index))

    downloaded = []
    not_downloaded = []
    for i in down_index:
        if i in downloaded_list:
            downloaded.append(i)
        else:
            not_downloaded.append(i)
            
    return not_downloaded





    # index_data = []
    # for names in list1:
    #     spilting = names.split(sep=' ')
    #     # index_id = int(spilting[1])
    #     # index_data.append(index_id)
    #     #index.append(spilting[1])
    #     print(spilting[1])
    #     index_data= spilting[1]



