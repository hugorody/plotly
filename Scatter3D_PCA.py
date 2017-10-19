#!/usr/bin/python3

import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import *

import numpy as np

IDE, LIN, ORI = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],[1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5],[1, 1, 4, 4, 1, 1, 2, 3, 2, 3, 3, 2]

PC1, PC2, PC3 = [45, 44, 35, 32, 24, 20, 17, 12, 9, -14, -16, -20],[34, 36, 27, 20, -29, -25, -17, -14, -7, 2, 3, 4],[4, 3, 2, 1, 22, 19, -35, -30, -1, 1, 1, 2]
tracemarkers = go.Scatter3d(
    x=PC1,
    y=PC2,
    z=PC3,
    mode='markers',
    marker=dict(
        color=LIN,
        colorscale='Jet', #'Blackbody','Bluered','Blues','Earth','Electric','Greens','Greys','Hot','Jet','Picnic','Portland','Rainbow','RdBu','Reds','Viridis','YlGnBu','YlOrRd'
        size=12,
        symbol='circle',
        line=dict(
            color='rgb(204, 204, 204)',
            width=1
        ),
        opacity=0.9
    )
)

#list of objects Scatter3d
coordinates = []
coordinates.append(tracemarkers)

#create segments
count = -1
for i in PC1:
    count +=1
    x = [i,i]
    y = [PC2[count],PC2[count]]
    z = [PC3[count],min(PC3)]
    coordinates.append(go.Scatter3d(x=x, y=y, z=z, mode='lines', line = dict(color = 'black', width = 4)))

data = Data(coordinates)
layout = go.Layout(
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0
    )
)
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='simple-3d-scatter')
