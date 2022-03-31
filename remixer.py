from moviepy.editor import *
import moviepy
#inputs are asked
partes=input("How many cuts do you want?")
corte=input("What percentage would you like to cut?[0-90](%)")
blanegre=input("black and white?")


#import music

musiclip = AudioFileClip("music1.mp3")

corte=(float(corte)/2)/100

#import video
clip = (VideoFileClip("1.mp4", audio=False))
if blanegre == "si":
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
        clip1=clip1.crossfadein(1.0)
        final_clip = concatenate_videoclips([final_clip, clip1])
    contador=1

dura = final_clip.duration
final_clip = final_clip.set_audio(musiclip)
final_clip = final_clip.set_end(dura)
if final_clip.duration > musiclip.duration:
    final_clip = final_clip.set_end(float(musiclip.duration))
    print("video longer than music, the clip is cut, it will now last: " + str(musiclip.duration))

final_clip.write_videofile("remixed.mp4")
