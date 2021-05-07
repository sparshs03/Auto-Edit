from moviepy.editor import *
import pygame

#OPTIONS START ------------------------
inputFile = "baki.mpg"
outputFile = "mympg.mp4"

#time in seconds
mainSceneStart = 95
mainSceneEnd = 136

importantSceneCuts = 6

#Time settings
otherScene = 5
otherSceneJump = 6
#OPTIONS END --------------------------

clip = VideoFileClip(inputFile)
clip_list = []
seconds = int(clip.duration)

print("Video Length: " + str(seconds) + " Seconds")
print("Started")

vid_index = 0


mainLength = mainSceneEnd - mainSceneStart

importantScene = mainLength / importantSceneCuts
importSceneJump = 0.1

# What works: (5,6)

#start of video
clip_length = 9
jump_amount = 0.8

while(vid_index < (clip_length * 2) - max(jump_amount, clip_length)):
    clip_list.append( clip.subclip(vid_index, vid_index + clip_length) )
    vid_index += clip_length + jump_amount

#main fight not reached
if vid_index < mainSceneStart:
    clip_length = otherScene
    jump_amount = otherSceneJump
    while(vid_index < mainSceneStart):
        clip_list.append( clip.subclip(vid_index, vid_index + clip_length) )
        vid_index += clip_length + jump_amount

#main fight reached
else:
    clip_length = importantScene
    jump_amount = importSceneJump
    while(vid_index < mainSceneEnd):
        clip_list.append( clip.subclip(vid_index, vid_index + clip_length) )
        vid_index += clip_length + jump_amount

#finish video
clip_length = otherScene
jump_amount = otherSceneJump

#resize((1280, 720))
while(vid_index < seconds - max(jump_amount, clip_length)):
    clip_list.append( clip.subclip(vid_index, vid_index + clip_length) )
    vid_index += clip_length + jump_amount


#add remaining video
if vid_index < seconds:
    clip_list.append( clip.subclip(vid_index, seconds) )


final_clip = concatenate_videoclips(clip_list)

#final_clip.preview()

final_clip.write_videofile(outputFile, codec="libx264")

print("done")