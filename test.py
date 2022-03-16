import plotly.graph_objects as px
import plotly.express as pd
import numpy as np


 
x = [0, 4, 12]
widths = np.array([2,2,5])


plot = px.Figure(data=[
px.Bar(name = '1', x = x, y = [75, 75, 50], marker_color='#E5EBF7'),
px.Bar(name = '2', x = x, y = [75, 0, 50], marker_color='#D9CD9F'),
px.Bar(name = '3', x = x, y = [0, 75, 50], marker_color='#F7F4E9'),
])


plot.update_layout(barmode='stack', bargap=0.2)
plot.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',

})
plot.update_xaxes(color="black")
plot.update_xaxes(ticks="inside")


plot.add_shape( # add a horizontal "target" line
    type="line", line_color="black", line_width=3, opacity=1, line_dash="dot",
    x0=2, x1=3, y0=75, y1=75
)


plot.show()
# plot.update_traces(line=dict(color="Black", width=0.5))


