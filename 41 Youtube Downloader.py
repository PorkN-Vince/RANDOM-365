# needs to check the authenticity of this code. Might wanna do some upgrade for this.

import yt_dlp

playlist_url = "https://youtube.com/playlist?list=PLGjplNEQlit8-0CmoljS5yeV-GlKSUEt0"

ydl_opts = {
    "format": "best",
    "outtmpl": "%(playlist_title)s/%(title)s.%(ext)s"
    "quiet": False
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])