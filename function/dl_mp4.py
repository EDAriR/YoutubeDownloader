from __future__ import unicode_literals
import youtube_dl

ydl_opts = {'outtmpl': 'download/%(title)s.%(ext)s'}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://youtu.be/2rxU1iy5Cqc'])
