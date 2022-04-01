from cgitb import text
import plotly.graph_objects as go
import kaleido

# 1 #si  coupon == coupon_autocall == True, 2 blocs, (soit SANS barrière coupon)

# 2 #si coupon == coupon_Phoenix == True, 3 blocs (soit avec barrière coupon)
        ## Possibilité qu'il y ait uniquement deux bloc dans le cas ou la balise (tag) de Non-Call (1PR) == 0
        ## Sinon, NC > 0, alors toujours 3 blocs et dans le premier bloc se trouveras uniquement la barrière coupon(bleu marine)

def bloc3(Class, name, whitestrap=False):
    bloc = 3
    niveau_autocall = [-50, -50, float(Class.BAC), float(Class.ABDAC), float(Class.DBAC)] #ligne verte
    niveau_coupon = [float(Class.BCPN), float(Class.BCPN), float(Class.BCPN), float(Class.BCPN), float(Class.BCPN)] #ligne noire  niveau coupon
    niveau_capital = float(Class.PDI) #Ligne rouge
    niveau_median = niveau_coupon[0] - niveau_capital
    labels = [5, 17, 39]
    widths = [10,20,10]

    fig = go.Figure()
    
    data = {
        "x1": [niveau_coupon[0],niveau_coupon[0],niveau_capital],
        "x2": [niveau_coupon[0],0,niveau_median],
        "x3": [0,niveau_coupon[0],niveau_coupon[0]],
    }

    color = {
        "x1": '#E5EBF7',
        "x2":  '#D9CD9F',
        "x3":  '#F7F4E9',
    }

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
            hoverinfo ='none',
        ))
    fig.update_layout(barmode="stack",uniformtext=dict(mode="hide", minsize=10),
    
    )
#axe des abcisses
#------------------------------------------NE BOUGE PAS----------------------------------------------------------------------------------------------
    fig.add_annotation( x=4.5, y=140, ax=4.5, ay=0, xref='x', yref='y', axref='x', ayref='y',
     text='', showarrow=True, arrowhead=3, arrowwidth=2, arrowcolor='black')

    fig.add_annotation(x=50, y=0, ax=4.5, ay=0, xref='x', yref='y', axref='x', ayref='y', text='',
    showarrow=True, arrowhead=3, arrowwidth=2, arrowcolor='black')

    fig.update_xaxes(tickangle=0,
                    tickmode = 'array',
                    tickvals = [10, 27, 44],
                    ticktext= ["Trimestre 1 à 3", "Trimestre 4 a 39", "Trimestre 40"])

    fig.update_yaxes(tickangle=0,
                    tickmode = 'array',
                    tickvals = [0],
                    ticktext= ["","", "", ""],
                    ),


    #LIGNE NOIRE

    fig.add_shape( # add a lignes premier block line
        type="line", line_color="black", line_width=3, opacity=1, line_dash="dot",
        x0=5, x1=15, y0=niveau_coupon[0], y1=niveau_coupon[1]
    )


    fig.add_shape( # add la ligne horizontale deuxieme block line
        type="line", line_color="black", line_width=3, opacity=1, line_dash="dot",
        x0=17, x1=37, y0=niveau_coupon[2], y1=niveau_coupon[3]
    )

    fig.add_shape( # add la ligne horizontale troisieme block line
        type="line", line_color="black", line_width=3, opacity=1, line_dash="dot",
        x0=39, x1=49, y0=niveau_coupon[4], y1=niveau_coupon[4]
    )
    # !LIGNE NOIRE

    #LIGNE VERTE

    fig.add_shape( # add la ligne horizontale deuxieme block line degressive
        type="line", line_color="green", line_width=3, opacity=1, line_dash="dot",
        x0=5, x1=15, y0=niveau_autocall[0], y1=niveau_autocall[1]
    )
    fig.add_shape( # add la ligne horizontale deuxieme block line degressive
        type="line", line_color="green", line_width=3, opacity=1, line_dash="dot",
        x0=17, x1=37, y0=niveau_autocall[2], y1=niveau_autocall[3]
    )

    fig.add_shape( # add la ligne horizontale deuxieme block line degressive
        type="line", line_color="green", line_width=3, opacity=1, line_dash="dot",
        x0=39, x1=49, y0=niveau_autocall[4], y1=niveau_autocall[4]
    )
    #!LIGNE VERTE

    #LIGNE ROUGE
    if (niveau_capital >= niveau_autocall[4] and niveau_autocall[4] > 0 or niveau_capital >= niveau_coupon[4] and niveau_coupon[4] > 0):
        niveau_capital = -5
    fig.add_shape( # add la ligne horizontale deuxieme block line degressive
        type="line", line_color="#C00000", line_width=3, opacity=1, line_dash="dash",
        x0=39, x1=49, y0=niveau_capital, y1=niveau_capital
    )

    #!LIGNE ROUGE
    if (niveau_autocall[3] > 0):
        fig.add_trace(go.Scatter(x=[17,37,37,17],
                            y=[niveau_autocall[2],niveau_autocall[3],niveau_coupon[3],niveau_coupon[2]],
                            fill='toself',
                            fillcolor='#D9CD9F',
                            line=dict(width=0),
                            showlegend=False,
                            mode='lines',  
                            hoverinfo ='none',
))

    #ici on remplace les valeurs x (ecrites abcisses(ne plus avoir 10 20 30 40 mais trimestre1 etc))
        # ajout des petites lignes nulles

    x0 = 4
    x1 = x0+0.5
    fig.add_shape(type="line",
    x0=x0, y0=niveau_autocall[2], x1=x1, y1=niveau_autocall[2],
    line=dict(color="green",width=3))

    fig.add_shape(type="line",
    x0=x0, y0=niveau_coupon[-1], x1=x1, y1=niveau_coupon[-1],
    line=dict(color="black",width=3))

    fig.add_shape(type="line",
    x0=x0, y0=niveau_capital, x1=x1, y1=niveau_capital,
    line=dict(color="#C00000",width=3))
#------------------------------------------NE BOUGE PAS---------------------------------------------------------------------------------------------

#-------------------------------------Pas fini, doit gerer les 100% ----------------------------------------------------
    #NIVEAU de reference seulement si 100 % sinon creer bloc 90%(classique) et au dessu sniveau de reference100% (en noir)

    #les valeurs qu on va mettre
    if (niveau_autocall[2] != 100):
        fig.add_annotation(x=2.5, y=100 - 2,text= ("Niveau de Référence<br> (100%)"), showarrow=False,
                    font=dict(family="Proxima Nova", size=8, color="Green" ),
                    )
   
        fig.add_annotation(x=3.0, y=niveau_autocall[2], text= str(niveau_autocall[2]) +"%", showarrow=False,
                    font=dict(family="Proxima Nova", size=14, color="Green" ))
    else:

        fig.add_annotation(x=2.5, y=100 - 2,text= ("Niveau de<br> Référence<br> (" + str(niveau_autocall[2]) + "%)"), showarrow=False,
                    font=dict(family="Proxima Nova", size=10, color="Green" ),
                    )

    fig.add_annotation(x=3.0, y=niveau_coupon[-1], text= str(niveau_coupon[-1]) +"%", showarrow=False,
                    font=dict(family="Proxima Nova", size=14, color="Black" ),
                    )
    fig.add_annotation(x=3.0, y=niveau_capital,text= str(niveau_capital) +"%", showarrow=False,
                    font=dict(family="Proxima Nova", size=14, color="Red" ),
                    )
   
#-------------------------------------!Pas fini, doit gerer les 100%! ----------------------------------------------------

    #le premier parametre de range x, permet de mettre ou non un blanc entre le 0 et le premier bloc
    fig.update_xaxes(range=[0,61])
    fig.update_yaxes(range=[0,130])

    #enlever le fond blanc
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        })
    if (whitestrap == True):
            fig.add_trace(go.Scatter(x=[5,15,15,5], 
                                    y=[niveau_autocall[0] +1 ,niveau_autocall[1] + 1, niveau_autocall[1] -1, niveau_autocall[0] -1],
                                    fill='toself',
                                    fillcolor='white',
                                    line=dict(width=0),
                                    showlegend=False,
                                    mode='lines',  
                                    hoverinfo ='none',))

            fig.add_trace(go.Scatter(x=[17,37,37,17], 
                                    y=[niveau_autocall[2] +1 ,niveau_autocall[3] + 1, niveau_autocall[3] -1, niveau_autocall[2] -1],
                                    fill='toself',
                                    fillcolor='white',
                                    line=dict(width=0),
                                    showlegend=False,
                                    mode='lines',  
                                    hoverinfo ='none',))

            fig.add_trace(go.Scatter(x=[17,37,37,17], 
                                    y=[niveau_autocall[4] +1 ,niveau_autocall[4] + 1, niveau_autocall[4] -1, niveau_autocall[4] -1],
                                    fill='toself',
                                    fillcolor='white',
                                    line=dict(width=0),
                                    showlegend=False,
                                    mode='lines',  
                                    hoverinfo ='none',))
                            
            fig.add_trace(go.Scatter(x=[39,49,49,39], 
                                    y=[niveau_capital +1 ,niveau_capital + 1, niveau_capital -1, niveau_capital -1],
                                    fill='toself',
                                    fillcolor='white',
                                    line=dict(width=0),
                                    showlegend=False,
                                    mode='lines',  
                                    hoverinfo ='none',))

            fig.add_trace(go.Scatter(x=[5,15,15,5], 
                                    y=[niveau_coupon[0] +1 ,niveau_coupon[1] + 1, niveau_coupon[1] -1, niveau_coupon[0] -1],
                                    fill='toself',
                                    fillcolor='white',
                                    line=dict(width=0),
                                    showlegend=False,
                                    mode='lines',  
                                    hoverinfo ='none',))

            fig.add_trace(go.Scatter(x=[17,37,37,17], 
                                    y=[niveau_coupon[2] +1 ,niveau_coupon[3] + 1, niveau_coupon[3] -1, niveau_coupon[2] -1],
                                    fill='toself',
                                    fillcolor='white',
                                    line=dict(width=0),
                                    showlegend=False,
                                    mode='lines',  
                                    hoverinfo ='none',))
            
            fig.add_trace(go.Scatter(x=[39,49,49,39], 
                                    y=[niveau_coupon[4] +1 ,niveau_coupon[4] + 1, niveau_coupon[4] -1, niveau_coupon[4] -1],
                                    fill='toself',
                                    fillcolor='white',
                                    line=dict(width=0),
                                    showlegend=False,
                                    mode='lines',  
                                    hoverinfo ='none',))


    fig.add_shape(type="line",
    x0=51, y0=116, x1=60, y1=116,
    line=dict(color="green",width=1),  line_dash="dot")
    
    
    fig.add_annotation(x=55, y=96,text= ("Seuil d'activation du <br> mécanisme de <br> remboursement anticipé <br> automatique à partir de la fin du <br> trimestre 4 jusqu'à la fin du trimestre <br> 20 et de versement des gains à <br> l'échéance"), showarrow=False,
                    font=dict(family="Proxima Nova", size=12, color="Black" ), align="left"
                    )

    fig.add_shape(type="line",
    x0=51, y0=60, x1=60, y1=60,
    line=dict(color="red",width=1),  line_dash="dot")
    
    
    fig.add_annotation(x=54, y=52,text= ("Seuil de perte en capital <br> à l'échéance"), showarrow=False,
                    font=dict(family="Proxima Nova", size=12, color="Black" ), align="left",
                    )
    
    fig.update_layout(
                            legend=dict(
                                itemclick="toggleothers",
                                itemdoubleclick="toggle"),
                            autosize=True,
                            width=1400,#1400
                            height=675,#800
                            plot_bgcolor='rgb(255,255,255)',
                            margin=dict(
                                l=50,
                                r=0,
                                b=20,
                                t=50,
                                pad=0),
                            paper_bgcolor='white')
    fig.write_image(name, format="png", scale=2, engine='kaleido')
    # fig.show()


    return(fig)

    #REGARDER SI POSSIBLE DE FAIRE  ALIGNER DISTRIBUER VERTICALEMENT