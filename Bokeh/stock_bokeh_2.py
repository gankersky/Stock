import requests 
from lxml import etree
import json
import numpy as np
from flask import Flask, jsonify, make_response, request
import threading as thd
import time
import datetime

from bokeh.models.formatters import DatetimeTickFormatter
from bokeh.models import AjaxDataSource, CustomJS
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

# Bokeh related code

adapter = CustomJS(code="""
    const result = {x: [], y: []}
    const pts = cb_data.response.points
    for (let i=0; i<pts.length; i++) {
        result.x.push(pts[i][0])
        result.y.push(pts[i][1])
    }
    return result
""")

source = AjaxDataSource(data_url='http://localhost:5050/data',
                        polling_interval=100, adapter=adapter)
# hover=HoverTool(
#     tooltips=[  #这里把需要的数据都列出来
#     	("Day", "$index"),
#         ( 'Time',    '@x{%F}'            ),
#         ( 'Price',   '@%s€'%y_name ), # use @{ } for field names with spaces
#         ( 'NetChg',  '@descy%' ),
#     ],

#     formatters={   #这里注意格式
#         '@x'    : 'datetime', # use 'datetime' formatter for '@date' field
#         '@desc' : 'printf',   # use 'printf' formatter for '@{adj close}' field
#                                      # use default 'numeral' formatter for other fields
#     },

#     # display a tooltip whenever the cursor is vertically in line with a glyph
#     mode='vline'
# )


# Flask related code

app = Flask(__name__)

def stock_price():
	headers = {
	        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.933.400 QQBrowser/9.4.8699.400',
	    }

	r= requests.get('https://finance.yahoo.com/quote/ZAL.DE?p=ZAL.DE',headers=headers)
	r.encoding = "utf-8"
	#构造一个xpath解析对象
	selector = etree.HTML(r.text)
	p_money = selector.xpath('//div[@class="My(6px) Pos(r) smartphone_Mt(6px)"]//span[@data-reactid="32"]/text()')
	p_NetChg = selector.xpath('//div[@class="My(6px) Pos(r) smartphone_Mt(6px)"]//span[@data-reactid="33"]/text()')
	p_time = selector.xpath('//div[@class="My(6px) Pos(r) smartphone_Mt(6px)"]//span[@data-reactid="35"]/text()')
	return p_money[0],p_NetChg[0],p_time[0]

#跨站点HTTP 
def crossdomain(f):
    def wrapped_function(*args, **kwargs):
        resp = make_response(f(*args, **kwargs))
        h = resp.headers
        h['Access-Control-Allow-Origin'] = '*'
        h['Access-Control-Allow-Methods'] = "GET, OPTIONS, POST"
        h['Access-Control-Max-Age'] = str(21600)
        requested_headers = request.headers.get('Access-Control-Request-Headers')
        if requested_headers:
            h['Access-Control-Allow-Headers'] = requested_headers
        return resp
    return wrapped_function
li_a = []
li_b = []
def fn():
    a,b,c=stock_price()

    li_a.append(a)
    #print(time.time(),li_a)
    #li_b.append(datetime.datetime.now())
    #li_b.append(time.strftime('%X',time.localtime(time.time())))
    li_b.append(time.strftime('%M%S',time.localtime(time.time())))
    #li_b.append(c)
    thd.Timer(2,fn).start()
    return li_b,li_a
    

#x = list(np.arange(0, 6, 0.1))
x,y = fn()
#y = list(np.sin(x) + np.random.random(len(x)))

@app.route('/data', methods=['GET', 'OPTIONS', 'POST'])
@crossdomain
def data():
    x.append(x[-1])
    y.append(y[-1])
    time.sleep(2)
    return jsonify(points=list(zip(x,y)))

p = figure(plot_height=300, plot_width=800, background_fill_color="lightgrey",x_axis_type='datetime',
            x_axis_label='Date',
            y_axis_label='Price',title="Streaming Stock via Ajax")
#p.xaxis.formatter = DatetimeTickFormatter(hours="%H:%M", seconds="%S")
p.circle('x', 'y', source=source)
#p.line('x', 'y', source=source,line_width=2,color='navy',alpha=1)

p.x_range.follow = "end"
p.x_range.follow_interval = 100

# show and run

show(p)
app.run(port=5050)


