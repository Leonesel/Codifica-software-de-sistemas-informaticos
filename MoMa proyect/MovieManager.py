#Ya no quiero estudiar
from moviepy.editor import VideoFileClip

class MovieManager:
    def get_audio(self, mp4_file, mp3_file):
        vc = VideoFileClip(mp4_file)
        ac = vc.audio
        ac.write_audiofile(mp3_file)
        ac.close()
        vc.close()

        #Quitarle el audio a el video
    def remove_audio(self, mp4_file, output_mp4):
        video = VideoFileClip(mp4_file)
        video_wa=video.without_audio()
        video_wa.write_videofile(output_mp4)
        video_wa.close()
        video.close

#Mozila Firefox DownlandHelper

mm=MovieManager()
mm.get_audio("video.mp4","audio.mp3") #sacar el audio
mm.remove_audio("video.mp4","videosinaudio.mp4") #Sacarle el audio al video