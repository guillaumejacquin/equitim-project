from cgitb import text
import plotly.graph_objects as go
import kaleido 

#si  coupon == coupon_autocall == True, 2 blocs, (soit SANS barrière coupon) 
#si coupon == coupon_Phoenix == True, 3 blocs (soit avec barrière coupon)

def bloc3(Class):
    niveau_autocall = 90
    last_autocall = 70
    niveau_capital = 50
    degressivite_finale = 71

    niveau_median = last_autocall - niveau_capital

    labels = [5, 17, 39]
    widths = [10,20,10]

    
    fig = go.Figure()

    data = {
        "x1": [last_autocall,last_autocall,niveau_capital],
        "x2": [last_autocall,0,niveau_median],
        "x3": [0,last_autocall,last_autocall],
    }
    color = {
        "x1": '#E5EBF7',
        "x2":  '#D9CD9F',
        "x3":  '#F7F4E9',
    }

    for key in data:
       for key in data:
        fig.add_trace(
            go.Bar(
            name=key,
            y=data[key],
            x= labels,

            width=widths,
            offset=0,
            # customdata=np.transpose([labels, widths*data[key]]),
            
            marker_color = color[key],
            textfont_color="white",
            textposition="inside",
            textangle=0,
            showlegend= False,
            hoverinfo ='none'

        ))

#axe des abcisses

    fig.add_annotation(
    x=4.5,
    y=140,  # arrows' head
    ax=4.5,  # arrows' tail
    ay=0,  # arrows' tail
    xref='x',
    yref='y',
    axref='x',
    ayref='y',
    text='',  # if you want only the arrow
    showarrow=True,
    arrowhead=3,
    arrowwidth=2,
    arrowcolor='black'
    )
    
    fig.add_annotation(
    x=50,
    y=0,  # arrows' head
    ax=4.5,  # arrows' tail
    ay=0,  # arrows' tail
    xref='x',
    yref='y',
    axref='x',
    ayref='y',
    text='',  # if you want only the arrow
    showarrow=True,
    arrowhead=3,
    arrowwidth=2,
    arrowcolor='black'
    )
    
    fig.add_shape( # add a lignes premier block line
        type="line", line_color="black", line_width=3, opacity=1, line_dash="dot",
        x0=5, x1=15, y0=last_autocall, y1=last_autocall
    )

    fig.add_shape( # add la ligne horizontale deuxieme block line
        type="line", line_color="black", line_width=3, opacity=1, line_dash="dot",
        x0=17, x1=37, y0=last_autocall, y1=last_autocall
    )


    fig.add_shape( # add la ligne horizontale deuxieme block line degressive
        type="line", line_color="green", line_width=3, opacity=1, line_dash="dot",
        x0=17, x1=37, y0=niveau_autocall, y1=degressivite_finale
    )

    fig.add_trace(go.Scatter(x=[17,37,37,17],
                            y=[niveau_autocall,degressivite_finale,last_autocall,last_autocall],
                            fill='toself',
                            fillcolor='#D9CD9F',
                            line=dict(width=0),
                            showlegend=False,
                            mode='lines'))


    fig.add_shape( # add la ligne horizontale troisieme block line
        type="line", line_color="black", line_width=3, opacity=1, line_dash="dot",
        x0=39, x1=49, y0=last_autocall, y1=last_autocall
    )

    fig.add_shape( # add la ligne horizontale deuxieme block line degressive
        type="line", line_color="#C00000", line_width=3, opacity=1, line_dash="dash",
        x0=39, x1=49, y0=niveau_capital, y1=niveau_capital
    )

    #ici on remplace les valeurs x (ecrites abcisses(ne plus avoir 10 20 30 40 mais trimestre1 etc)) (hard codées)
    fig.update_xaxes(tickangle=0,
                    tickmode = 'array',
                    tickvals = [10, 27, 44],
                    ticktext= ["Trimestre 1 à 3", "Trimestre 4 a 39", "Trimestre 40"])


    fig.update_yaxes(tickangle=0,
                    tickmode = 'array',
                    tickvals = [0, niveau_capital, last_autocall, niveau_autocall],
                    ticktext= ["","", "", ""],
                    ),
                    
    fig.update_layout(barmode="stack",uniformtext=dict(mode="hide", minsize=10),
    )

    #ajout des petites lignes nulles
    x0 = 4
    x1 = x0+0.5
    fig.add_shape(type="line",
    x0=x0, y0=niveau_autocall, x1=x1, y1=niveau_autocall,
    line=dict(color="green",width=3))

    fig.add_shape(type="line",
    x0=x0, y0=last_autocall, x1=x1, y1=last_autocall,
    line=dict(color="black",width=3))
    
    fig.add_shape(type="line",
    x0=x0, y0=niveau_capital, x1=x1, y1=niveau_capital,
    line=dict(color="#C00000",width=3))
    

    #les valeurs qu on va mettre
    fig.add_annotation(x=2.5, y=niveau_autocall - 2,text= ("Niveau de<br> Référence<br> (" + str(niveau_autocall) + "%)"), showarrow=False,
                    font=dict( family="Proxima Nova", size=14, color="Green" ),
                    )

    fig.add_annotation(x=3.25, y=last_autocall,text= str(last_autocall) +"%", showarrow=False,
                    font=dict( family="Proxima Nova", size=14, color="Black" ),
                    )
    fig.add_annotation(x=3.25, y=niveau_capital,text= str(niveau_capital) +"%", showarrow=False,
                    font=dict( family="Proxima Nova", size=14, color="Red" ),
                    ) 
    fig.add_annotation(x=4, y=1,text= str("0%"), showarrow=False,
                    font=dict( family="Proxima Nova", size=14, color="Black" ),
                    )                                            

    #le premier parametre de range x, permet de mettre ou non un blanc entre le 0 et le premier bloc
    fig.update_xaxes(range=[0,55])
    fig.update_yaxes(range=[0,130])

    #enlever le fond blanc
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        })
    # fig.show()
    # fig.write_image("file_name222.png", format="png", scale=1, engine='kaleido')

    return(fig)
    
    #NIVEAU de reference seulement si 100 % sinon creer bloc 90%(classique) et au dessu sniveau de reference100% (en noir)