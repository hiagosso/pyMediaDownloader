from pytubefix import YouTube
import os
from moviepy import AudioFileClip

class download:
    def __init__(self):
        self.youTube = None
        self.destino_audios_tmp = "audios_tmp"
        self.destino_audios= "audios"
        self.destino_videos = "videos"

        os.makedirs(self.destino_audios_tmp, exist_ok=True)
        os.makedirs(self.destino_audios, exist_ok=True)
        os.makedirs(self.destino_videos, exist_ok=True)

    def audio(self,url):
        self.youTube = YouTube(url)
        audio = self.youTube.streams.filter(only_audio=True).first()
        nome = self.youTube.title.replace("/", "-").replace("\\", "-")
        caminho = audio.download(output_path=self.destino_audios_tmp, filename=nome)

        clip = AudioFileClip(caminho)
        clip.write_audiofile(f"{self.destino_audios}/{nome}.mp3")
        clip.close()
        os.remove(caminho)


    def video(self,url):
        self.youTube = YouTube(url)
        video = self.youTube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video.download(output_path=self.destino_videos)

    def verificar(self,url):
        self.youTube = YouTube(url)
        return self.youTube.title
    

if __name__ =="__main__":
    download()

