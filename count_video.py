
def video_id():
    with open('info.txt') as f:
        lines = f.readlines()
        last_line = lines[len(lines)-1]
        spilting = last_line.split(sep=' ')
        video_id = int(spilting[0])
    
    return video_id



def downloaded_index():

    downloaded_index = []
    with open('info.txt') as f:
        lines = f.readlines()
        for line in lines:
            downloaded_index.append(line.split(sep=' ')[0])

    return downloaded_index
