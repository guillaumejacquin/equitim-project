from cgitb import text
from flask import Flask
import plotly.graph_objects as go
import kaleido

#legende en haut a droite
def legende(Class, fig, green, black, blue, red, niveau_coupon):
    fig.add_shape(type="line",
    x0=75.5, y0=116, x1=83, y1=116,
    line=dict(color=green,width=3),  line_dash="dot")
    fig.add_annotation(x=80.5, y=102.5,text= ("Seuil d'activation du <br> mécanisme de <br> remboursement anticipé <br> automatique à partir de la fin du <br>" + Class.F0 +" " + str(int(Class.PR1)) + " jusqu'à la fin du " + str(Class.F0) +"<br> " + str(int(Class.DPRR)-1) ), showarrow=False,
                    font=dict(family="Proxima Nova", size=12, color=black ), align="left"
                    )
    fig.add_shape(type="line",
    x0=75, y0=77, x1=83, y1=77,
    line=dict(color=blue,width=3),  line_dash="dot")
    fig.add_annotation(x=80.5, y=71.5,text= ("Seuil de détachement des coupons"), showarrow=False,
                    font=dict(family="Proxima Nova", size=12, color=black ), align="left"
                    )
    fig.add_shape(type="line",
    x0=75, y0=50, x1=83, y1=50,
    line=dict(color=red,width=3), line_dash="dash")

    fig.add_annotation(x=79, y=45,text= ("Seuil de perte en capital <br> à l'échéance"), showarrow=False,
                    font=dict(family="Proxima Nova", size=12, color=black ), align="left",
                    )


    return fig

#Laxe abcisse ordonnée, parametrage visuel
def abcisse_ordonnee(Class, fig):
    fig.add_annotation( x=4.5, y=140, ax=4.5, ay=0, xref='x', yref='y', axref='x', ayref='y',
     text='', showarrow=True, arrowhead=3, arrowwidth=2, arrowcolor='black')

    fig.add_annotation(x=75, y=0, ax=4.5, ay=0, xref='x', yref='y', axref='x', ayref='y', text='',
    showarrow=True, arrowhead=3, arrowwidth=2, arrowcolor='black')
    
    # Periode + le nombre (exempla trimestre 1 a 3)
    firstvaluexabciss = Class.F0 + Class.F0s + " 1 à " +  str(int(Class.PR1) - 1)
    firstvaluexabciss = firstvaluexabciss.capitalize()

    secondvaluexabciss = Class.F0 + Class.F0s + " " +  str(int(Class.PR1))  + " à " + str(int(Class.DPRR) - 1)
    secondvaluexabciss = secondvaluexabciss.capitalize()
  
    thirdvaluexabciss = Class.F0  +" " + str(Class.DPRR)
    thirdvaluexabciss = thirdvaluexabciss.capitalize()

    fig.update_xaxes(tickangle=0,
                    tickmode = 'array',
                    tickvals = [10, 30, 47, 68],
                    ticktext= [firstvaluexabciss, secondvaluexabciss, thirdvaluexabciss, thirdvaluexabciss])

    fig.update_yaxes(tickangle=0,
                    tickmode = 'array',
                    tickvals = [0],
                    ticktext= ["","", "", ""],
                    ),
    
    #le premier parametre de range x, permet de mettre ou non un blanc entre le 0 et le premier bloc
    fig.update_xaxes(range=[0,88])
    fig.update_yaxes(range=[-3,130])
    return(fig)


#le bloc le plus a gauche
def first_bloc(Class, fig, blue, niveau_coupon):                     
    fig.add_shape( # add la ligne horizontale deuxieme block line
        type="line", line_color=blue, line_width=3, opacity=1, line_dash="dot",
        x0=5, x1=20,  y0=niveau_coupon[0], y1=niveau_coupon[1]
    )
    return(fig)


def second_block(Class, fig):
    fig.add_trace(go.Scatter(x=[22,37,37,22],
                            y=[float(Class.BAC),float(Class.BCPN),float(Class.BCPN),float(Class.BCPN)],
                            fill='toself',
                            fillcolor='#D9CD9F',
                            line=dict(width=0),
                            showlegend=False,
                            mode='lines',  
                            hoverinfo ='none',
    ))
    return(fig)


def third_block(Class, fig):
    fig.add_trace(go.Scatter(x=[39,54,54,39],
                            y=[ float(Class.ABDAC),  float(Class.DBAC), 0, 0],
                            fill='toself',
                            fillcolor='#E5EBF7',
                            line=dict(width=0),
                            showlegend=False,
                            mode='lines',  
                            hoverinfo ='none',
    ))

def bloc3_4(Class, name, whitestrap=False):
    bloc = 3
    green = "#00B050"
    blue = "#002E8A"
    red = "#C00000"
    black = "#000000"
    niveau_autocall = [-50, -50, float(Class.BAC), float(Class.ABDAC), float(Class.DBAC)] #ligne verte
    niveau_coupon = [float(Class.BCPN), float(Class.BCPN), float(Class.BCPN), float(Class.BCPN), float(Class.BCPN)] #ligne noire  niveau coupon
    niveau_capital = float(Class.PDI) #Ligne rouge
    niveau_median = niveau_coupon[0] - niveau_capital
    labels = [5, 22, 39, 58]
    widths = [15,15, 15, 15]
    myvar = niveau_capital

    fig = go.Figure()
    
    print("-------------------")
    print(niveau_coupon[0],niveau_coupon[0],niveau_capital)
    print("-------------------")
    x2=  130 - niveau_coupon[0]
    secondblock = float(Class.DBAC) - niveau_capital
    x3_3 = 130 - (niveau_capital + secondblock)
    data = {
        "x1": [niveau_coupon[0],niveau_coupon[0],niveau_capital, niveau_capital],
        "x2": [x2,0,secondblock, secondblock],
        "x3": [0,x2, x3_3, x3_3],
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
#-

    abcisse_ordonnee(Class, fig)
    
    #ici on remplace les valeurs x (ecrites abcisses(ne plus avoir 10 20 30 40 mais trimestre1 etc))
        # ajout des petites lignes nulles #LES TICK SES FDP
    x0 = 4
    x1 = x0+0.5
    fig.add_shape(type="line",
    x0=x0, y0=niveau_autocall[2], x1=x1, y1=niveau_autocall[2],
    line=dict(color=green,width=3))

    fig.add_shape(type="line",
    x0=x0, y0=niveau_coupon[-1], x1=x1, y1=niveau_coupon[-1],
    line=dict(color=blue,width=3))

    fig.add_shape(type="line",
    x0=x0, y0=niveau_capital, x1=x1, y1=niveau_capital,
    line=dict(color="#C00000",width=3))
#------------------------------------------NE BOUGE PAS---------------------------------------------------------------------------------------------

#-------------------------------------Pas fini, doit gerer les 100% ----------------------------------------------------
    #NIVEAU de reference seulement si 100 % sinon creer bloc 90%(classique) et au dessu sniveau de reference100% (en noir)

    #les valeurs qu on va mettre
    mystring = "100%"
    # if (niveau_autocall[2] != 100):
    #     fig.add_annotation(x=3, y=niveau_coupon[0],text= (niveau_coupon[0]), showarrow=False,
    #                 font=dict(family="Proxima Nova", size=14, color=green ),
    #                 )
   
    #     # fig.add_annotation(x=3.0, y=niveau_autocall[2], text= str(niveau_autocall[2]) +"%", showarrow=False,
    #     #             font=dict(family="Proxima Nova", size=14, color=green ))
    # else:
    #     mystring = str(Class.BAC) + "%"
    #     fig.add_annotation(x=3, y=str(Class.BAC),text= (mystring), showarrow=False,
    #                 font=dict(family="Proxima Nova", size=14, color=green ),
    #                 )

    # fig.add_annotation(x=3.0, y=niveau_coupon[-1], text= str(niveau_coupon[-1]) +"%", showarrow=False,
    #                 font=dict(family="Proxima Nova", size=14, color=blue ),
    #                 )
    # fig.add_annotation(x=3.0, y=niveau_capital,text= str(niveau_capital) +"%", showarrow=False,
    #                 font=dict(family="Proxima Nova", size=14, color="red" ),
    #                 )
   
#-------------------------------------!Pas fini, doit gerer les 100%! ----------------------------------------------------


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

            fig.add_trace(go.Scatter(x=[39,49,49,39], 
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

    first_bloc(Class, fig, blue, niveau_coupon)
    print("èèèèèèèèèèèèèèèèè", niveau_capital)
    if ((niveau_capital) <= -2):
        fig.add_shape( # add la ligne horizontale deuxieme block line degressive
        type="line", line_color=red, line_width=2, opacity=1, line_dash="dash",
        x0=39, x1=49, y0=float(Class.DBAC) - 1, y1=float(Class.DBAC) -1
    )



    second_block(Class, fig)



#     fig.add_trace(go.Scatter(x=[39,54,54,39],
#                             y=[float(Class.BCPN),float(Class.BCPN),float(Class.BCPN),float(Class.BCPN)],
#                             fill='toself',
#                             fillcolor='#D9CD9F',
#                             line=dict(width=0),
#                             showlegend=False,
#                             mode='lines',  
#                             hoverinfo ='none',
# ))


    fig.add_trace(go.Scatter(x=[39,54,54,39],
                            y=[ float(Class.ABDAC),  float(Class.DBAC), 0, 0],
                            fill='toself',
                            fillcolor='#E5EBF7',
                            line=dict(width=0),
                            showlegend=False,
                            mode='lines',  
                            hoverinfo ='none',
))

    fig.add_trace(go.Scatter(x=[39,54,54,39],
                            y=[ Class.BCPN,  float(Class.DBAC), float(Class.DBAC), float(Class.DBAC)],
                            fill='toself',
                            fillcolor='#E5EBF7',
                            line=dict(width=0),
                            showlegend=False,
                            mode='lines',  
                            hoverinfo ='none',
))

    legende(Class, fig, green, black, blue, red, niveau_coupon)



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

#page 2 voir de l indice espace