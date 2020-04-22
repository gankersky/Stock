from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import StockInfo,DayData,RealTimeData,MonthData
from bokeh.plotting import figure
from bokeh.models import Range1d
from bokeh.embed import components
from bokeh.resources import CDN
from bokeh.plotting import ColumnDataSource, figure, output_file, show
from bokeh.models import HoverTool
from bokeh.models import BasicTickFormatter
import datetime
from yahoo_fin import stock_info as si
import time
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components

# Create your views here.

from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.dates import DateFormatter
import matplotlib.pyplot as plt

import random
import datetime
from django.template import loader

def json1(request):
    return render(request,'Stock/json1.html')

def json2(request):
    return JsonResponse({'h1':'hello','h2':'world'})

def ajax_demo1(request):
    return render(request, "Stock/ajax_demo1.html")


def ajax_add(request):
    i1 = int(request.GET.get("i1"))
    i2 = int(request.GET.get("i2"))
    ret = i1 + i2
    return JsonResponse(ret, safe=False)


def index3(request):
    # 1.获取模板
    template = loader.get_template('Stock/index3.html')
    # 2.定义上下文
    context = {"data1": StockInfo.objects.order_by("-st_name")[0].st_name,
               "data2": StockInfo.objects.order_by("-id")[0].id}
    # 3.渲染模板
    return JsonResponse(template.render(context, request))


# 折线图对应的的模板
def showlinediagram(request):
    return render(request, 'Stock/showlinediagram.html')

def data_fresh(request):
    context = {"data1": StockInfo.objects.order_by("-st_name")[0].st_name,
               "data2": StockInfo.objects.order_by("-id")[0].id}
    return JsonResponse(context)



def homepage(request):
    x = [1,2,3,4,5]
    y = [1,2,3,4,5]

    plot = figure(title = 'Line Graph', x_axis_label='X-Ax',y_axis_label='Y-Ax',plot_width = 400,plot_height = 400)

    plot.line(x,y,line_width = 2)
    script,div = components(plot)
    return render(request,'Stock/stockplot.html',{'script': script,'div': div})

# def index(request):
#     x= [1,3,5,7,9,11,13]
#     y= [1,2,3,4,5,6,7]
#     title = 'y = f(x)'
#
#     plot = figure(title= title ,
#         x_axis_label= 'X-Axis',
#         y_axis_label= 'Y-Axis',
#         plot_width =400,
#         plot_height =400)
#
#     plot.line(x, y, legend= 'f(x)', line_width = 2)
#     #Store components
#     script, div = components(plot)
#
#     #Feed them to the Django template.
#     return render(request,'Stock/stockplot.html',
#         {'script': script, 'div': div})

def stockList(request):
    stock_list= StockInfo.objects.all()
    context = {
        'st_list': 'Stock List',
        'stock_list':stock_list,
    }
    return render(request,'Stock/stockList.html',context)

def dashBoard(request,stock_id):
    stockinfo = StockInfo.objects.get(id = stock_id) #这里得是外键的名
    day_st_name = StockInfo.objects.get(id = stock_id)
    stock_day_price = stockinfo.daydata_set.all()  #这里的一对多是数据库类
    context = {
        'stock_day_price' : stock_day_price,
        'Stock_Name:': day_st_name,
    }
    return render(request,'Stock/stdayprice.html',context)
def dashBoard_m(request,stock_id):
    stockinfo = StockInfo.objects.get(id = stock_id) #这里得是外键的名
    #mon_st_name = StockInfo.objects.get(id = stockinfo_id)
    stock_mon_price = stockinfo.monthdata_set.all()  #这里的一对多是数据库类
    context = {
        'stock':stockinfo,
        'stock_mon_price' : stock_mon_price,
        'Stock_Name': 'Stock Name',
        'time':'Monthtime',
        'price':'Price',
        'vol':'Volume',
    }
    return render(request,'Stock/stmonprice.html',context)

# def scatter(request):
#     # create some data
#     x1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     y1 = [0, 8, 2, 4, 6, 9, 5, 6, 25, 28, 4, 7]
#     x2 = [2, 5, 7, 15, 18, 19, 25, 28, 9, 10, 4]
#     y2 = [2, 4, 6, 9, 15, 18, 0, 8, 2, 25, 28]
#     x3 = [0, 1, 0, 8, 2, 4, 6, 9, 7, 8, 9]
#     y3 = [0, 8, 4, 6, 9, 15, 18, 19, 19, 25, 28]
#
#     # select the tools we want
#     TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
#
#     # the red and blue graphs will share this data range
#     xr1 = Range1d(start=0, end=30)
#     yr1 = Range1d(start=0, end=30)
#
#     # only the green will use this data range
#     xr2 = Range1d(start=0, end=30)
#     yr2 = Range1d(start=0, end=30)
#
#     # build our figures
#     p1 = figure(x_range=xr1, y_range=yr1, tools=TOOLS, plot_width=300, plot_height=300)
#     p1.scatter(x1, y1, size=12, color="red", alpha=0.5)
#
#     p2 = figure(x_range=xr1, y_range=yr1, tools=TOOLS, plot_width=300, plot_height=300)
#     p2.scatter(x2, y2, size=12, color="blue", alpha=0.5)
#
#     p3 = figure(x_range=xr2, y_range=yr2, tools=TOOLS, plot_width=300, plot_height=300)
#     p3.scatter(x3, y3, size=12, color="green", alpha=0.5)
#
#     # plots can be a single Bokeh Model, a list/tuple, or even a dictionary
#     plots = {'Red': p1, 'Blue': p2, 'Green': p3}
#
#     script, div = components(plots,CDN)
#     context = {
#         'script': script,
#         'div': div
#     }
#     return render(request, 'Stock/stockList.html', context)

# def stockPlot(request):
#
#
#     ak_li = ["MTX.DU", "TKA.DE", "ZAL.DE", 'DAI.DE', 'C001.DE']
#
#     def Ak_Bok(akname):
#         val_li = []
#         for i in range(90):
#             value_all = si.get_data(akname, start_date=(datetime.datetime.now() + datetime.timedelta(days=-(i + 1))))
#             value_each = value_all['close'][0]
#             val_li.append(value_each)
#         # print(val_li)
#         return val_li
#
#     end = datetime.date.today() + datetime.timedelta(-1)
#     datetime_list = list(datetime.datetime.now() + datetime.timedelta(days=-(i + 1)) for i in range(90))
#     date_list = list(dt.strftime('%Y-%m-%d') for dt in datetime_list)
#     value_list = []
#     value_list = Ak_Bok(ak_li[2])
#     netChg_list = []
#
#     for i in range(91):
#         if i == 0:
#             continue
#         elif i < 90:
#             netc = 100 * (value_list[i - 1] - value_list[i]) / value_list[i]
#             # netc_f = str(float('%.5f' % netc))
#             netChg_list.append(netc)
#         else:
#             netChg_list.append(0)
#     datetime_list = datetime_list[::-1]
#     value_list = value_list[::-1]
#     netChg_list = netChg_list[::-1]
#
#     source = ColumnDataSource(data=dict(
#         x=datetime_list,
#         y=value_list,
#         descy=netChg_list,
#     ))
#
#     y_name = 'y'
#     # desc = 'desc'+y_name
#     # print(desc)
#     hover = HoverTool(
#         tooltips=[  # 这里把需要的数据都列出来
#             ("Day", "$index"),
#             ('Time', '@x{%F}'),
#             ('Price', '@%s€' % y_name),  # use @{ } for field names with spaces
#             ('NetChg', '@descy%'),
#         ],
#
#         formatters={  # 这里注意格式
#             '@x': 'datetime',  # use 'datetime' formatter for '@date' field
#             '@desc': 'printf',  # use 'printf' formatter for '@{adj close}' field
#             # use default 'numeral' formatter for other fields
#         },
#
#         # display a tooltip whenever the cursor is vertically in line with a glyph
#         mode='vline'
#     )
#     TOOLS = "hover,crosshair,pan,wheel_zoom,box_zoom,reset,save,box_select"
#     p = figure(plot_width=800, plot_height=400, x_axis_type='datetime',
#                x_axis_label='Date',
#                y_axis_label='Price', tools=[hover],
#                y_range=(0, max(value_list) * (1.5)), title="The Stock Info")
#     p.line('x', '%s' % y_name, legend="ZAL.DE", source=source, color='navy', alpha=1)
#     # p.circle('x', 'y', size=2, source=source)#之前不显示，是source的问题
#     script, div = components(p,CDN)
#     context = {
#         'script': script,
#         'div': div
#     }
#     return render(request, 'Stock/stockplot.html', context)
