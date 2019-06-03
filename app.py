#!/usr/bin/python3
# A web site showing 
from flask import make_response
from flask import Flask, render_template
from pyquery import PyQuery as pq
import pandas as pd
import re
app = Flask(__name__)

def edit_html(csv_path):
    data = pd.read_csv(csv_path)
    html_table = data.to_html(table_id="crawl_data")

    html_string = ""

    with open("templates/logger.html", 'r') as file:
        html_string = file.read()
    html_string = re.sub('<table border="1" class="dataframe" id="crawl_data">(.|\s)*<\/table>',\
        html_table, html_string)
    with open("templates/logger.html", "w+") as file:
        file.write(html_string)

@app.route('/')
def home():
    rep = make_response(render_template("home.html"))
    rep.headers.set("Cache-Control", "no-cache, no-store")
    rep.headers.set("Pragma", "no-cache")
    return rep

@app.route('/crawl/vnexpress')
def crawl_vnexpress():
    edit_html("vnexpress.csv")
    rep = make_response(render_template("logger.html"))
    rep.headers.set("Cache-Control", "no-cache, no-store")
    rep.headers.set("Pragma", "no-cache")
    return rep

@app.route('/crawl/aliexpress')
def crawl_aliexpress():
    edit_html("aliexpress.csv")
    rep = make_response(render_template("logger.html"))
    rep.headers.set("Cache-Control", "no-cache, no-store")
    rep.headers.set("Pragma", "no-cache")
    return rep

@app.route('/crawl/vieclam24h')
def crawl_vieclam24h():
    edit_html("vieclam24h.csv")
    rep = make_response(render_template("logger.html"))
    rep.headers.set("Cache-Control", "no-cache, no-store")
    rep.headers.set("Pragma", "no-cache")
    return rep

app.run()