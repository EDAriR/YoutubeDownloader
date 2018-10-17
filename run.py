from flask import Flask, render_template, request, jsonify, Response
from modles import item

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("base.html")


@app.route("/results")
def result_page():
    page = request.args.get('sp')
    if page == None:
        search = request.args.get('search')
        soup = item.find_search_content(search)
        all_item = item.every_video(soup)
        all_page = item.page_bar(soup)
        return render_template("result.html", search=search, all_item=all_item, all_page=all_page)
    elif page != None:
        search = request.args.get('q')
        page = request.args.get('sp')
        current_page = request.args.get('current_page')
        value = "q={}".format(search) + "&" + "sp={}".format(page)
        soup = item.find_page_content(value)
        all_item = item.every_video(soup)
        all_page = item.page_bar(soup)
        return render_template("result.html", search=search, all_item=all_item, all_page=all_page,
                               current_page=current_page, int=int)


@app.route("/download")
def download():
    value = request.args.get('value')
    download_type, url = value.split("&")
    if download_type == "MP3":
        title = item.download_mp3(url)
        import os
        arr = os.listdir('.')
        for filename in arr:
            if title in filename:
                def generate():
                    with open(filename, "rb") as fogg:
                        data = fogg.read(1024)
                        while data:
                            yield data
                            data = fogg.read(1024)

                from flask import Response
                return Response(generate(), mimetype="audio/ogg")
        return render_template("download.html")


@app.route("/json/<key_id>", methods=['POST'])
def getJsonTest(key_id):
    json = request.get_json(force=True)
    print(json)
    print(json['appIds'])
    print(type(json))
    query_string = request.query_string
    print("query: " + query_string)
    json['appIds'] = key_id
    # Access - Control - Allow - Origin: *
    return Response(jsonify(json), header='Access - Control - Allow - Origin: *')


if __name__ == "__main__":
    app.run(port=8080, debug=True)
