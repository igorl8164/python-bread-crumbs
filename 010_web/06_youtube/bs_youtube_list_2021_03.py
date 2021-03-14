from pytube import YouTube  # python3 -m pip install pytube
from bs4 import BeautifulSoup as BS  # python3 -m pip install beautifulsoup4
from pprint import pprint
import time
import pyperclip  # on Linux  $ sudo apt-get install xsel   $ sudo apt-get install xclip  $ python3 -m pip install pyperclip


# teg_html = input('inspect element playlist youtube copy paste -> \n')
if pyperclip.is_available():
    print('error ')
    exit(0)

teg_html = pyperclip.paste()
print('\nlen teg_html', len(teg_html))
# print(teg_html)

# save to files
t = time.localtime()
t_name =  '_'.join([str(x) for x in [t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec]])

# with open(f'element_html_{t_name}.html', 'w', encoding = pyperclip.ENCODING) as f:
#     f.write(teg_html)

path_html = r'tmp_shotcut.htm'
path_html = r'tmp_inkscape.htm'
# path_html = r'tmp_gimp.htm'

with open(path_html, 'r', encoding='utf-8') as f:
    w = f.read()

# ------------------------------------------ #
print('read', len(w))
str_bs = BS(w, features="html.parser")  # 'lxml'

#p = str_bs.prettify()
#print(p)

r = str_bs.findAll('h3', class_="style-scope ytd-playlist-video-renderer")  #('ytd-playlist-panel-video-renderer')  # , class_="style-scope ytd-app")#  {'id': "video-title", 'class': "style-scope ytd-playlist-video-renderer"})  # {'id': "contents"} , 'class': "style-scope ytd-playlist-video-list-renderer"
# print(str_bs.element_classes)
# print(r)
print('find class ', len(r))

#  ---------------------------------------------------------------------------------- #
if r == 0:
    exit(0)

title_href = list()
for item in r:
    t = item.find('a', class_= 'yt-simple-endpoint style-scope ytd-playlist-video-renderer')#'yt-simple-endpoint style-scope ytd-playlist-panel-video-renderer')
    h = 'https://www.youtube.com' + t.get('href')
    print(h)
#   span  class_="style-scope ytd-playlist-panel-video-renderer"
    tt = item.find('a', class_='yt-simple-endpoint style-scope ytd-playlist-video-renderer', id="video-title")
    t = tt.get('title')

# .
    t = t.replace('Inkscape. ', '')
    t = t.replace('Gimp. ', '')
    t = t.replace('Шаг за шагом. ', '')
    t = t.replace('  ', ' ')
    t = t.replace('  ', ' ')

    print(t)  # t.get('title')  get_text()
    title_href.append((t, h))
    print('-'*40)

for p, u in title_href:
    print(f'[{p}]({u})')
    print()
# ---------------------------------------------------------------------------------- #

path = r'/media/user01/Data1/linux/soft/shotcut'
path = r'/media/user01/Data1/linux/soft/inkscape'
# path = r'/media/user01/Data1/linux/soft/gimp'

video_urls = title_href

def download_youtube(ur_list, p):
    for i, ut in enumerate(ur_list):
        t, u = ut
        print('title:', t)
        print('url:', u)
        yt = YouTube(u)
        print(i)
        print('title:', yt.title)
        # print(yt.thumbnail_url)
        print('captions:', yt.captions)
        # print('description:', yt.description)
        r = yt.streams.get_highest_resolution()
        print('get_highest_resolution:', r)
        print('default_filename:', r.default_filename)
        fp = '%03d_' % (i + 1)
        print('filename_prefix:', fp)

        dn = False
        count_dn = 0
        rez = ''
        while not dn:
            try:
                time.sleep(1)
                count_dn += 1
                if count_dn > 4:  # количество попыток
                    dn = True
                    continue
                # download the highest resolution video
                print(i)
                rez = r.download(output_path=p, filename_prefix=fp)

            except Exception as e:
                print('error download count n:', count_dn)
            else:
                dn = True

        print(rez)
        print('-'*40)

download_youtube(video_urls, path)

print('exit')

# ---------------------------------------------------------------------------------- #
