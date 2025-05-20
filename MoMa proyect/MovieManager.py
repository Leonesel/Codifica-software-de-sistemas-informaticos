#Hola
import speech_recognition as sr
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
from deep_translator import GoogleTranslator
from gtts import gTTS

class MovieManager:
        #Obtiene el audio del video
    def get_audio(self, mp4_file, mp3_file):
        vc = VideoFileClip(mp4_file)
        ac = vc.audio
        ac.write_audiofile(mp3_file)
        ac.close()
        vc.close()

        #Quitarle el audio a el video
    def remove_audio(self, mp4_file, output_mp4):
        video = VideoFileClip(mp4_file)
        video_wa = video.without_audio()
        video_wa.write_videofile(output_mp4)
        video_wa.close()
        video.close

        #Saca el audio en .wav
    def get_wav_audio(self, mp4_file, wav_file):
        vc = VideoFileClip(mp4_file)
        ac = vc.audio
        ac.write_audiofile(wav_file, codec="pcm_s16le")
        ac.close()
        vc.close()

        #Transcrive el audio .wav
    def audio_to_text(self, audio_file):
        r = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            return "unknow"
        
        #Traduce
    def text_to_speech(self, to_translate, to_lang):
        translated = GoogleTranslator(source = 'auto', target = to_lang).translate(to_translate)
        print(translated)
        myobj = gTTS(text=translated, lang = to_lang, slow = False)
        myobj.save("welcome.mp3")

    def add_audio_to_video(self, mp4_file, mp3_file, out_file):
        videoclip = VideoFileClip(mp4_file)
        audioclip = AudioFileClip(mp3_file)

        new_audioclip = CompositeAudioClip([audioclip])
        videoclip.audio = new_audioclip
        videoclip.write_videofile(out_file)

     


#Mozila Firefox DownlandHelper para instalar videos
#pip install SpeechRecognition
#pip install moviepy==1.0.3
#pip install gTTS
#pip install deep-translator

mm = MovieManager()

print("Ya Juan de Dios")
#mm.get_audio("video.mp4","audio.mp3") #saca el audio .mp3
#mm.remove_audio("video.mp4","videosinaudio.mp4") #Saca el audio al video .mp4
#mm.get_wav_audio("video.mp4","audio.wav") #Saca otro audio en .wav
speech = mm.audio_to_text("audio.wav") #Transcribe el audio .wav
#print(speech)
mm.text_to_speech(speech,'ru') #Traduce
#mm.add_audio_to_video("videosinaudio.mp4", "welcome.mp3", "nose.mp4") #Ya juan de dios
