import youtube_dl

ydl_opts = {'outtmpl': '/video/%(title)s.%(ext)s'}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=kN5cqf63kb8'])