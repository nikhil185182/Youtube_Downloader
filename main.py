from pytube import YouTube

savePath = './newdoc'

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(savePath)
    except:
        print("An error has occurred")
    print("Download is completed successfully")



# Using readlines()
file1 = open('urls.txt', 'r')
Lines = file1.readlines()
  
count = 0
for line in Lines:
    count += 1
    Download(line.strip())