import youtube_dl
import time
from datetime import datetime

from youtube_dl import DownloadError
import sys

# https://stackoverflow.com/questions/64825310/downloading-data-directly-into-a-temporary-file-with-python-youtube-dl
ydl_opts = {
    'outtmpl': './%(title)s.%(ext)s',
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'merge_output_format': 'mp4',
    'nocheckcertificate': True
}

mp3_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'nocheckcertificate': True
}


def dl_main(opts, url):
    with youtube_dl.YoutubeDL(opts) as ydl:
        ydl.download([url])


def count_down(num, t_name):
    t_num = int(num)
    wait_sec = 60

    if t_name != 'minutes':
        print('wait ' + num + ' ' + t_name)
    if t_name == 'hours':
        print('wait ' + num + ' ' + t_name)
        t_num = t_num * 60

    print('Start count down : ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    for i in range(t_num):
        print('need ' + str(t_num - i) + ' minutes')
        time.sleep(wait_sec)

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('End count down : ' + now)


def main(argv):
    if 'https://youtu.be/' in argv[1]:
        print('Get url :' + argv[1])
    elif 'h' == argv[1] or 'help' == argv[1]:
        print('please enter url like https://youtu.be/your_video_path')
        print('for example python3 ')
    else:
        print('need url like: https://youtu.be/your_video_path')

    if len(argv) >= 3:
        print('Get folder path :' + argv[2])
        ydl_opts['outtmpl'] = argv[2] + '/%(title)s.%(ext)s'
    # if len(argv) >= 4:
    #     print('Get download type :' + argv[3])
    #     if 'mp3' == argv[3]:
    #         print('Use mp3 mode')
    #         ydl_opts = mp3_opts
    #     else:
    #         print('Use default mp4 mode')

    if 'https://youtu.be' in argv[1]:
        yt_url = argv[1]
        wait_dl(ydl_opts, yt_url)
    else:
        print('need url like: https://youtu.be/{your_video_path}')


def wait_dl(ydl_opts, yt_url):
    try:
        dl_main(ydl_opts, yt_url)
    except DownloadError as e:

        i = e.exc_info[1]

        print('--------')
        for x in e.exc_info:
            print(x)
            # print('youtube_dl.utils.ExtractorError' in str(type(x)))
            # print('youtube_dl.utils.DownloadError:' in str(type(x)))

        print('--------')

        print('i am ' + str(i))

        if 'few' in str(i):

            time.sleep(60)
            wait_dl(ydl_opts, yt_url)

        elif 'event will begin' in str(i):

            if 'in a few moments' in str(i):
                t = '1'
                t_str = 'minutes'
            elif 'ERROR' in str(i):
                t_str = str(i).split(' ')[8]
                t = str(i).split(' ')[7]
            else:
                t = str(i).split(' ')[6]
                t_str = str(i).split(' ')[7]

            count_down(t, t_str)
            wait_dl(ydl_opts, yt_url)

        else:
            print(i)


if __name__ == "__main__":
    main(sys.argv)
