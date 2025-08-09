from textual.app import App
from textual.widgets import Header,Input,Button,Label
from textual.containers import VerticalGroup,HorizontalGroup
from textual import on
from downloader import download

baixador = download()

class aplicacao(App):
    TITLE =  "pyMediaDownload"
    SUB_TITLE = "baixador de videos do youtube :)"
    def compose(self):
        yield VerticalGroup(
            Header(show_clock=False),
            Input(placeholder="digite a url",id='entrada'),

            HorizontalGroup(
                Button("verificar",id="verificar"),
                Button("audio", id="audio"),
                Button("video",id="video"),
                Button("limpar",id="limpar"),
                Button("sair", id="sair"),
                id="grupo_botoes"
            ),
            Label("",id="aviso"),
            id="caixa"
        )
    
    def on_mount(self):
        caixa = self.query_one("#caixa")
        caixa.styles.border = ("heavy","yellow")
        caixa.styles.height = "100%"

        grupo_botoes = self.query_one("#grupo_botoes")
        grupo_botoes.styles.align_horizontal = "center"

    @on(Button.Pressed)
    def clicou(self, event: Button.Pressed):
        url = self.query_one("#entrada",Input)
        aviso = self.query_one("#aviso",Label)
        
        if event.button.id == "verificar":
            try:
                titulo = baixador.verificar(url.value)
                aviso.update(f"{titulo}")
            except:
                aviso.update("campo vazio")
            self.set_timer(1,lambda: aviso.update(""))

        elif event.button.id == "audio":
            try:
                baixador.audio(url.value)
            finally:
                aviso.update("audio baixado")
            self.set_timer(1,lambda: aviso.update(""))

        elif event.button.id == "video":
            try:
                baixador.video(url.value)
            finally:
                aviso.update("video baixado")
            self.set_timer(1,lambda: aviso.update(""))

        elif event.button.id == "limpar":
            url.value = ""
        elif event.button.id == "sair":
            aplicacao.exit(self)
    
if __name__ == "__main__":
    app = aplicacao()
    app.run()