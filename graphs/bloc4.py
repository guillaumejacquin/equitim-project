from ast import Return
from pandas_datareader import data
import pandas as pd
import plotly.express as px

def bloc4(Class, Name):
    tickers = ['ALO.PA'] #Exemple de test
    #recuper les tickers de la base de donnée
    tickers = ['WFC', 'RNO.PA', '^GSPC'] #exemple de test
    ###ici####
    tickers = Class.Yahoo #vraie
    print("--------------")
    print(tickers)
    if (len(tickers) == 1):
        bloc4_simple_tickers(tickers, Class, Name)
    
    elif (len(tickers) > 1):
        bloc4_multiple_tickers(tickers, Class, Name)

    else: 
        print("error")

from pandas.tseries.offsets import Day, BDay
from datetime import date
import datetime


def bloc4_simple_tickers(tickers, Class, Name):
    end_date = Class.DPCI
    bdays=BDay()
    start = Class.PDC1
    end_date = Class.DPCI

    start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
    is_business_day = bdays.is_on_offset(start_date)

    while is_business_day != True:
        start_date = start_date - datetime.timedelta(days=1)
        print(start_date)
        is_business_day = bdays.is_on_offset(start_date)
    
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    is_business_day = bdays.is_on_offset(end_date)

    while is_business_day != True:
        end_date = end_date + datetime.timedelta(days=1)
        print(end_date)
        is_business_day = bdays.is_on_offset(end_date)
        print("is_business", is_business_day)
    
    # User pandas_reader.data.DataReader to load the desired data. As simple as that.
    panel_data = data.DataReader(tickers[0], 'yahoo', start_date, end_date)
    panel_data.head(9)
    panel_data.tail(10)
    #ADj close,

    adj_close = panel_data["Adj Close"]
    lastvalue = adj_close.iloc[-1]
    firstvalue = adj_close.iloc[0]

    result = ((lastvalue/firstvalue) -1) * 100  
    fig = px.line(adj_close.index, x=adj_close.index, y=adj_close)

    fig.data[0].line.color = 'rgb(197, 175, 92)'
    fig.data[0].line.width = 1


    fig.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor='rgb(0, 0, 0)',
            linewidth= 1,
            ticks='outside',
            title=None,
            tickfont=dict(
                family='Proxima Nova',
                size=12,
                color='rgb(82, 82, 82)',   
            ),
        ),
        yaxis=dict(
            showgrid=True,
            zeroline=False,
            showline=True,
            showticklabels=True,
            ticks='outside',
            gridwidth=1,
            gridcolor='rgb(242, 242, 242)',
            linecolor='rgb(0, 0, 0)',
            linewidth= 1,
            title=None,
            tickfont=dict(
                family='Proxima Nova',
                size=13,
                color='rgb(82, 82, 82)',
                )
        ),
        showlegend=False,

        plot_bgcolor='white'
    )
    
    #fig.show()
    fig.write_image(Name, format="png", scale=4, engine='kaleido')


def bloc4_multiple_tickers(tickers, Class, Name):
    end_date = Class.DPCI
    bdays=BDay()
    start = Class.PDC1
    end_date = Class.DPCI

    start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
    is_business_day = bdays.is_on_offset(start_date)

    while is_business_day != True:
        start_date = start_date - datetime.timedelta(days=1)
        print(start_date)
        is_business_day = bdays.is_on_offset(start_date)
    
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    is_business_day = bdays.is_on_offset(end_date)

    while is_business_day != True:
        end_date = end_date + datetime.timedelta(days=1)
        print(end_date)
        is_business_day = bdays.is_on_offset(end_date)
    

    result = pd.DataFrame()
    name = []
    # User pandas_reader.data.DataReader to load the desired data. As simple as that.
    for datas in tickers:
        panel_data = data.DataReader(datas, 'yahoo', start_date, end_date)

        adj_close = panel_data["Adj Close"]
        lastvalue = adj_close.iloc[0]
        
        panel_data[datas] = (panel_data['Adj Close'] / lastvalue) * 100
        result[datas] = (panel_data['Adj Close'] / lastvalue) * 100
        name.append(datas)

        # result = ((lastvalue/firstvalue) -1) * 100

    print("bloc4 names", name)
    
    if len(name) == 2:
        fig = px.line(data_frame = adj_close
                ,x = adj_close.index
                ,y = [result[name[0]],result[name[1]]]
                )
   
    if len(name) == 3:
        fig = px.line(data_frame = adj_close
                ,x = adj_close.index
                ,y = [result[name[0]],result[name[1]], result[name[2]]]
                )
    if len(name) == 4:
        fig = px.line(data_frame = adj_close
                ,x = adj_close.index
                ,y = [result[name[0]],result[name[1]], result[name[2]], result[name[3]]]
                )


    if len(name) == 5:
        fig = px.line(data_frame = adj_close
                ,x = adj_close.index
                ,y = [result[name[0]],result[name[1]], result[name[2]], result[name[3]], result[name[4]]]
                )

    fig.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor='rgb(0, 0, 0)',
            linewidth= 1,
            ticks='outside',
            title=None,
            tickfont=dict(
                family='Proxima Nova',
                size=12,
                color='rgb(82, 82, 82)',   
            ),
        ),
        yaxis=dict(
            showgrid=True,
            zeroline=False,
            showline=True,
            showticklabels=True,
            ticks='outside',
            gridwidth=1,
            gridcolor='rgb(242, 242, 242)',
            linecolor='rgb(0, 0, 0)',
            linewidth= 1,
            title=None,
            tickfont=dict(
                family='Proxima Nova',
                size=13,
                color='rgb(82, 82, 82)',
                )
        ),
        showlegend=False,
        plot_bgcolor='white'
    )
    # fig.show()
    fig.write_image(Name, format="png", scale=2, engine='kaleido')

