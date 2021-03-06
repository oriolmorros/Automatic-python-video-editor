from moviepy.editor import *
import moviepy
#we ask for input
partes=input("How many videos do you want?")
musics=input("How many songs (1 to 5)?")
blanegre=input("Black & White?")
resum=input("Shortened?")

#music import
musiclips={}
musiclips[1] = AudioFileClip("music1.mp3")
if int(musics) > 1:
    musiclips[2] = AudioFileClip("music2.mp3")
if int(musics) > 2:
    musiclips[3] = AudioFileClip("music3.mp3")
if int(musics) > 3:
    musiclips[4] = AudioFileClip("music4.mp3")
if int(musics) > 4:
    musiclips[5] = AudioFileClip("music5.mp3")


#video import
clip = (VideoFileClip("1.mp4", audio=False))
if blanegre == "yes":
    clip=moviepy.video.fx.all.blackwhite(clip, RGB=None, preserve_luminosity=True)



for parte in range(int(partes)):
    clip1=clip.subclip((parte*clip.duration)/float(partes),((parte+1)*clip.duration)/float(partes))
    length=clip1.duration
    ite=parte+1
    if resum == "si":
        clip1=clip1.subclip((length*0.25),(length*0.75))



    if int(ite)>int(musics):
        ite=1
    clip1a = clip1.set_audio(musiclips[ite])
    clip1a = clip1a.set_end(clip1.duration)


    if clip1a.duration > musiclips[ite].duration:
        clip1a = clip1a.set_end(float(musiclips[ite].duration))
        print("clip mas largo que la musica, cortamos, ahora dura "+str(clip1a.duration))


    clip1a.write_videofile("clip"+str(parte)+".mp4")
