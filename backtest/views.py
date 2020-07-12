from django.shortcuts import render

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from bokeh.plotting import figure, output_file, show, ColumnDataSource
import bokeh.layouts
from bokeh.embed import components
from bokeh.models import HoverTool
from bokeh.resources import CDN
import pandas as pd
from datetime import date
from pandas_datareader import data as pdr
from .forms import sma_search

from .btsingle import btsingle

# Create your views here.
# Backtesting SMA

def backtest(request):
    #input variables
    stock_in = 'SPY'
    start_date_in = '2016-01-01'
    end_date_in = '2019-12-25'
    pfast = 50
    pslow = 200
    #run strategy
    script, div, sharpe_ratio = btsingle(stock_in, start_date_in, end_date_in, pfast, pslow)
    return render(request,'backtest/bttest.html', {'script':script, 'div':div, 'sr':sharpe_ratio, 'ticker': stock_in, 'fsma': pfast, 'ssma': pslow, 'start':start_date_in, 'end':end_date_in})
