import youtube_dl
import time
from datetime import datetime

from youtube_dl import DownloadError
import sys
import traceback

# https://stackoverflow.com/questions/64825310/downloading-data-directly-into-a-temporary-file-with-python-youtube-dl
ydl_opts = {
    'outtmpl': './%(uploader)s/%(title)s_%(release_date)s.%(ext)s',
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'merge_output_format': 'mp4',
    'writethumbnail': True,
    'writedescription': True,
    'nocheckcertificate': True,
    "nopart": True
}

mp3_opts = {
    'format': 'bestaudio/best',
    'writethumbnail': True,
    'writedescription': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'nocheckcertificate': True
}


def dl_main(opts, url):
    opts.update({'cookiefile': 'youtube.com_cookies.txt'})
    with youtube_dl.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url)
        print(info)


def count_down(num, t_name='分鐘', wait_sec=60):
    t_num = int(num)

    if t_name == 'hours':
        t_num = t_num * 60

    print('wait ' + str(num) + ' ' + t_name)

    print('Start count down :' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    for i in range(t_num):
        print('need ' + str(t_num - i) + ' ' + t_name)
        time.sleep(wait_sec)

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('End count down :' + now)


def main(argv):
    # if 'https://youtu.be/' in argv[1]:
    print('Get url :' + argv[1])
    # elif 'h' == argv[1] or 'help' == argv[1]:
    #     print('please enter url like https://youtu.be/your_video_path')
    #     print('for example python3 ')
    # else:
    #     print('need url like: https://youtu.be/your_video_path')
    #
    # if len(argv) >= 3:
    #     print('Get folder path :' + argv[2])
    #     ydl_opts['outtmpl'] = argv[2] + '/%(title)s.%(ext)s'
    # if len(argv) >= 4:
    #     print('Get download type :' + argv[3])
    #     if 'mp3' == argv[3]:
    #         print('Use mp3 mode')
    #         ydl_opts = mp3_opts
    #     else:
    #         print('Use default mp4 mode')

    # if 'https://youtu.be' in argv[1]:
    url = argv[1]
    wait_dl(ydl_opts, url)
    # else:
    #     print('need url like: https://youtu.be/{your_video_path}')


def wait_dl(ydl_opts, yt_url):
    try:
        dl_main(ydl_opts, yt_url)
        i = 'done'

    except DownloadError as e:

        i = str(e.exc_info[1])

        print('--------')
        for x in e.exc_info:
            print(x)

        print('--------')
        i_arr = i.split(' ')
        print(i_arr)

        if 'event will begin' in i or '將於' in i:

            if 'few' in i or '幾分鐘' in i:
                count_down(1, wait_sec=10)
            else:
                if '這個現場直播將於' in i:
                    t = i_arr[1]
                    t_str = i_arr[2]
                elif 'ERROR' in i:
                    t_str = i_arr[8]
                    t = i_arr[7]
                else:
                    t = i_arr[6]
                    t_str = i_arr[7]

                count_down(t, t_str)

        elif 'Premieres' in i or '將在' in i:

            t = i_arr[1]
            t_str = i_arr[2]

            if len(i_arr) > 3:
                t = i_arr[2]
                t_str = i_arr[3]

            count_down(t, t_str)

        print('line 128')
        print(isinstance(youtube_dl.utils.ExtractorError, type(e)))

    except BaseError as e:
        traceback.print_exc(e)

    print('=========')

    if 'will begin' in i or '幾分鐘' in i:
        wait_dl(ydl_opts, yt_url)
    else:
        print('line 140')
        print(i)


if __name__ == "__main__":
    main(sys.argv)
