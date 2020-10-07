#YOUTUBE DOWNLOADER BY 
# PRINCE PILLE.

#pip install pafy.
import pafy

#copy your video url here:
url ="https://www.youtube.com/watch?v=hvie9ywaYnE"
video = pafy.new(url)


streams = video.streams

#list of stream for a video:
for i in streams:
    print(i)

#get best resolution regardless of file format:
best = video.getbest()

#count the number of views:
count = video.viewcount 



#can be use the to print the best resolution and best extension:
#print(best.resolution, best.extensiom)

#print the view counts.
print("View Count : " + str(count))

#where you want to store the downloaded videos and with what name should be writen in the end of the path.
filename = best.download(filepath=r"C:\Users\princ\PycharmProjects\amazing projects\youtube download\YT videos\youtube." + best.extension)
print("video downloaded successfully")
