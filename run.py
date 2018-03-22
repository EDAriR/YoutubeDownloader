from flask import Flask, render_template, request
from modles import item
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("base.html")


@app.route("/results")
def result_page():
    page = request.args.get('sp')
    if page == None :
        search = request.args.get('search')
        soup = item.find_search_content(search)
        all_item = item.every_video(soup)
        all_page = item.page_bar(soup)
        return render_template("result.html", search=search, all_item=all_item,all_page=all_page)
    elif page != None :
        search = request.args.get('q')
        page = request.args.get('sp')
        current_page = request.args.get('current_page')
        value = "q={}".format(search) + "&" + "sp={}".format(page)
        soup = item.find_page_content(value)
        all_item = item.every_video(soup)
        all_page = item.page_bar(soup)
        return render_template("result.html",  search=search, all_item=all_item,all_page=all_page,
                               current_page=current_page, int=int)


@app.route("/download")
def download():
    value = request.args.get('value')
    download_type, url = value.split("&")
    if download_type == "MP3":
        item.download_mp3(url)
        return render_template("download.html")
    elif download_type == "MP4":
        print('value' + value)
        item.download_mp4(url)
        return render_template("download.html")


if __name__ == "__main__":
    app.run(port=80, debug=True)
