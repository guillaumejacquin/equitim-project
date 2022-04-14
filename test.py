from ast import Return
from matplotlib.pyplot import ticklabel_format
from pandas_datareader import data
import pandas as pd
import plotly.express as px

def bloc4():
    tickers = ['AAPL']
    tickers = ['AAPL', 'MSFT', '^GSPC']

    if (len(tickers) == 1):
        bloc4_simple_tickers(tickers)
    
    elif (len(tickers) > 1):
        bloc4_multiple_tickers(tickers)

    else: 
        print("error")


def bloc4_simple_tickers(tickers):
    # We would like all available data from 01/01/2000 until 12/31/2016.
    start_date = '2017-01-01'
    end_date = "2022-01-01"

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
        showlegend=True,

        plot_bgcolor='white'

    )
    fig.show()
    fig.write_image("test.png", format="png", scale=4, engine='kaleido')






def bloc4_multiple_tickers(tickers):
    start_date = '2017-04-04'
    end_date = "2022-04-04"

    result = pd.DataFrame()
    name = []
    # User pandas_reader.data.DataReader to load the desired data. As simple as that.
    compteur = 0
    for datas in tickers:
        panel_data = data.DataReader(datas, 'yahoo', start_date, end_date)


        adj_close = panel_data["Adj Close"]
        lastvalue = adj_close.iloc[0]

        result[datas] = ((panel_data['Adj Close'] / lastvalue) - 1) * 100
        name.append(datas)

        # result = ((lastvalue/firstvalue) -1) * 100

        compteur += 1
    
    if len(name) == 2:
        fig = px.line(data_frame = adj_close
                ,x = adj_close.index
                ,y = [result[name[0]],result[name[1]]]
                ,color_discrete_sequence = ['#B9A049', '#002060']# #00B5E, #599295

                )
    if len(name) == 3:
        fig = px.line(data_frame = adj_close
                ,x = adj_close.index
                ,y = [result[name[0]],result[name[1]], result[name[2]]]
                ,color_discrete_sequence = ['#B9A049', '#002060', '#404040']# #00B5E, #599295
    #gold, bleu marine, gris, bleu equitim clair, vert canard gris
                )
    if len(name) == 4:
        fig = px.line(data_frame = adj_close
                ,x = adj_close.index
                ,y = [result[name[0]],result[name[1]], result[name[2]], result[name[3]]]
                ,color_discrete_sequence = ['#B9A049', '#002060', '#404040', '#00B5E'] #599295

                )


    if len(name) == 5:
        fig = px.line(data_frame = adj_close
                ,x = adj_close.index
                ,y = [result[name[0]],result[name[1]], result[name[2]], result[name[3]], result[name[4]]]
                ,color_discrete_sequence = ['#B9A049', '#002060', '#404040', '#00B5E', '#599295']

                )
    
    fig.update_layout(
        width=1000,#1400
        autosize=True,
            margin=dict(
                l=50,
                r=0,
                b=20,
                t=50,
                pad=0),
        xaxis=dict(
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor='rgb(0, 0, 0)',
            linewidth= 1,
            ticks='outside',
            tickformat='%m/%Y',
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
            autorange = True,
            ticks='outside',
            gridwidth=1,
            gridcolor='rgb(242, 242, 242)',
            linecolor='rgb(0, 0, 0)',
            linewidth= 1,
            title=None,
            ticksuffix="%",
            tickfont=dict(
                family='Proxima Nova',
                size=13,
                color='rgb(82, 82, 82)',
                )
        ),


        showlegend=True,

        plot_bgcolor='white'

    )
    
    fig.update_layout(legend=dict(
        yanchor="top",
        y=-0.065,
        xanchor="left",
        x=0.48
    ))
    for i, new_name in enumerate(name):
        fig.data[i].name = new_name

    # fig.show()

    fig.write_image("test.png", format="png", scale=4, engine='kaleido')





bloc4()