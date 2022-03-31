from moviepy.editor import *
import moviepy
#preguntamos videos y musica
partes=input("how many cuts do you want?")
corte=input("what percentage would you like to cut?[0-90](%)")
blanegre=input("black and white?[yes or no]")
musi=input("do you want music?"[yes or no])

#importamos musica

if musi == "yes":
    musiclip = AudioFileClip("music1.mp3")

corte=(float(corte)/2)/100

#importamos video
if musi == "yes":
    clip = (VideoFileClip("1.mp4", audio=False))
else:
    clip = (VideoFileClip("1.mp4", audio=True))

if blanegre == "yes":
    clip=moviepy.video.fx.all.blackwhite(clip, RGB=None, preserve_luminosity=True)


contador=0
for parte in range(int(partes)):

    clip1=clip.subclip((parte*clip.duration)/float(partes),((parte+1)*clip.duration)/float(partes))
    length=clip1.duration
    ite=parte+1
    clip1=clip1.subclip((length*corte),(length*(1-corte)))
    if contador==0:
        final_clip=clip1
    else:
       
        final_clip = concatenate_videoclips([final_clip, clip1])

    contador=1

dura = final_clip.duration
if musi == "si":
    final_clip = final_clip.set_audio(musiclip)
    final_clip = final_clip.set_end(dura)
    if final_clip.duration > musiclip.duration:
        final_clip = final_clip.set_end(float(musiclip.duration))
        print("video longer than music, cut, it now lasts: " + str(musiclip.duration))

final_clip.write_videofile("remixed.mp4")
