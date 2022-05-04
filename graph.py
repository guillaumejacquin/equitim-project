
import plotly.express as px


def params(fig):
    fig.update_xaxes(range=[0.5,88])
    fig.update_yaxes(range=[17,150])
    # fig.update_yaxes(ticks="outside", tickwidth=1, tickcolor='crimson', ticklen=10, col=1)

    fig.update_yaxes(tickangle=0,
                    tickmode = 'array',
                    tickvals = [0],
                    ticktext= ["","", "", ""],
                    ),

    fig.update_yaxes(tickangle=0,
                    tickmode = 'array',
                    tickvals = [20, 30,40, 50, 60,70,80,90,100,110,120,130],
                    ticktext= [20, 30,40, 50, 60,70,80,90,100,110,120,130],
                    ),
    fig.update_xaxes(tickangle=0,
                    tickmode = 'array',
                    tickvals = [0.5],
                    ticktext= ["Lancement"],
                    ),
    fig.update_layout(
        legend=dict(
            itemclick="toggleothers",
            itemdoubleclick="toggle"),
            autosize=True,

            plot_bgcolor='rgb(255,255,255)',
            margin=dict(
                l=50,
                r=0,
                b=20,
                t=50,
                pad=0),
            paper_bgcolor='white')
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        }) 
    return(fig)


def axes_ordonees(fig):
    fig.add_annotation( x=1, y=140, ax=1, ay=18, xref='x', yref='y', axref='x', ayref='y',
     text='', showarrow=True, arrowhead=3, arrowwidth=2, arrowcolor='black')


    fig.add_annotation(x=82, y=18, ax=1, ay=18, xref='x', yref='y', axref='x', ayref='y', text='',
    showarrow=True, arrowhead=3, arrowwidth=2, arrowcolor='black')

    return(fig)

def traces(fig):
    niveau_de_référence = 100
    avant_dernier_niveau_de_reference = 88
    derniere_observation = 75
    perte_capital = 50
    niveau_de_scénario_déf = 32

    x_vertical_line = 81 #le x de la ligne verticale pour aligner les elements

    #la ligne verticale a droite noire
    fig.add_shape(type="line",
    x0=x_vertical_line, y0=140, x1=x_vertical_line, y1=18,
    line=dict(color="black", width=2),  line_dash="dot")

    #la ligne horizontale = niveau de référence verte

    fig.add_shape(type="line",
    x0=20, y0=niveau_de_référence, x1=70, y1=avant_dernier_niveau_de_reference,
    line=dict(color="green", width=3),  line_dash="dash")


    fig.add_annotation(x=x_vertical_line +1.75, y=niveau_de_référence  +0.5,text= (str(niveau_de_référence) + "%" ), showarrow=False,
                    font=dict(family="Proxima Nova", size=15, color="black" ), align="left")
    
    fig.add_annotation(x=x_vertical_line +1.75, y=derniere_observation + 0.5,text= (str(derniere_observation) + "%" ), showarrow=False,
                    font=dict(family="Proxima Nova", size=15, color="green" ), align="left")
    
    fig.add_shape(type="line",
    x0=x_vertical_line, y0=derniere_observation, x1= x_vertical_line - 4, y1=derniere_observation,
    line=dict(color="green", width=6),  line_dash="dash")

    fig.add_annotation(x=x_vertical_line +1.75, y=perte_capital + 0.5,text= (str(perte_capital) + "%" ), showarrow=False,
                    font=dict(family="Proxima Nova", size=15, color="red" ), align="left")
    fig.add_shape(type="line",
    x0=x_vertical_line, y0=perte_capital, x1= x_vertical_line - 3.5, y1=perte_capital,
    line=dict(color="red", width=6))
   
    fig.add_annotation(x=x_vertical_line +1.75, y=niveau_de_scénario_déf + 0.5,text= (str(niveau_de_scénario_déf) + "%" ), showarrow=False,
                    font=dict(family="Proxima Nova", size=15, color="blue" ), align="left")
    fig.add_shape(type="line",
    
    x0=x_vertical_line, y0=niveau_de_scénario_déf, x1= x_vertical_line - 3.5, y1=niveau_de_scénario_déf,
    line=dict(color="blue", width=6))

def graph():
    fig = px.line()
    params(fig)
    axes_ordonees(fig)
    traces(fig)
    fig.show()

graph()