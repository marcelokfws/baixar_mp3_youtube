from pytube import YouTube
import moviepy.editor as mp
import re
import os
from PyQt5 import uic, QtWidgets

def funcao_principal():

    try:
        link = tela.lineEdit.text()
        yt = YouTube(link)
        ys = yt.streams.filter(only_audio=True).first().download()

        for file in os.listdir():
            if re.search('mp4', file):
                mp4_path = os.path.join( file)
                mp3_path = os.path.join( os.path.splitext(file)[0]+'.mp3')
                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path)
    except Exception:

        tela.erro.setText(str('Você digitou ou colou o link de forma errada'))

app = QtWidgets.QApplication([])
tela = uic.loadUi("tela.ui")
tela.pushButton.clicked.connect(funcao_principal)

tela.show()
app.exec()