from flask import Flask, render_template, request, jsonify, Response
from modles import item

import os
import subprocess
import sys
import logging
import shutil

# from werkzeug import secure_filename

app = Flask(__name__)

app.logger.setLevel(logging.ERROR)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['TEMP_FOLDER'] = '/tmp'
app.config['OCR_OUTPUT_FILE'] = 'ocr'


@app.route("/")
def hello():
    return render_template("base.html")


@app.errorhandler(404)
def not_found(error):
    resp = jsonify({
        u'status': 404,
        u'message': u'Resource not found'
    })
    resp.status_code = 404
    return resp


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




@app.route("/json/<key_id>", methods=['POST'])
def getJsonTest(key_id):
    json = request.get_json(force=True)
    print(json)
    # print(json['appIds'])
    print(type(json))
    # query_string = request.args.get('first_name')
    query_string = request.query_string
    print("query: " + str(query_string))
    # json['appIds'] = key_id
    # Access - Control - Allow - Origin: * Access-Control-Expose-Headers: Access-Control-Allow-Origin
    # headers = {
    #     'Access-Control-Expose-Headers': 'Access-Control-Allow-Origin',
    #     'Access - Control - Allow - Origin': '*'
    # }
    return Response(jsonify(json))


@app.route('/test', methods=['GET'])
def test():
    return render_template('upload_form.html', landing_page='process')


if __name__ == "__main__":
    app.run(port=8080, debug=True)
