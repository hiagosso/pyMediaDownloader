from pytubefix import YouTube

class download:
    def __init__(self):
        self.youTube = None
        self.destino_audios = "audios"
        self.destino_videos = "videos"

    def audio(self,url):
        self.youTube = YouTube(url)
        audio = self.youTube.streams.filter(only_audio=True).first()
        nome = self.youTube.title + ".mp3"
        audio.download(output_path=self.destino_audios, filename=nome)

    def video(self,url):
        self.youTube = YouTube(url)
        video = self.youTube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video.download(output_path=self.destino_videos)

    def verificar(self,url):
        self.youTube = YouTube(url)
        return self.youTube.title
    

if __name__ =="main":
    download()

