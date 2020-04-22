from django.contrib import admin
from Stock.models import StockInfo, DayData, RealTimeData, MonthData


# Register your models here.

class DayDataAdmin(admin.ModelAdmin):
    list_display = ['id','stockinfo','Data','Open','High', 'Low','Close','AdjClose','Volume']
class MonthDataAdmin(admin.ModelAdmin):
    list_display = ['id','stockinfo','Data','Open','High', 'Low','Close','AdjClose','Volume']

class StockInfoAdmin(admin.ModelAdmin):
    list_display = ['id','st_name']

admin.site.register(StockInfo,StockInfoAdmin)
admin.site.register(DayData,DayDataAdmin)
admin.site.register(RealTimeData)
admin.site.register(MonthData,MonthDataAdmin)
