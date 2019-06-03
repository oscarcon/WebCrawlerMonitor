import pandas as pd
import re

data = pd.read_csv("vnexpress.csv")
html_table = data.to_html(table_id="crawl_data")

html_string = ""

with open("static/logger.html", 'r') as file:
    html_string = file.read()
html_string = re.sub('<table border=1 class="dataframe" id="crawl_data">(.|\s)*<\/table>',\
    html_table, html_string)
with open("static/logger.html", "w+") as file:
    file.write(html_string)