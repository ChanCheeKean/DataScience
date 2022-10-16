'''Plotly Helper'''

# import sys
# sys.path.append('/Users/chancheekean/Google Drive/CS/Data Science/-- lib/')
# import importlib
# import plot_helper
# importlib.reload(plot_helper)
# from plot_helper import *

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.graph_objs as go
import plotly.figure_factory as ff
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def get_histrogram(df_x, xtitle=None, ytitle=None, title='title', bins=None):
    '''Histrogram Plot'''
    traces = [
        go.Histogram(
            x=df_x,
            nbinsx=bins, 
            marker_line_width=1,
            marker_color='rgb(158,202,225)',
            marker_line_color='rgb(8,48,107)',)
    ]

    layout = go.Layout(
        title=title,
        titlefont=dict(size=15, color='#0e4886'), 
        title_x=0.5,
        font=dict(size=10), 
        xaxis = dict(title = xtitle, titlefont = dict(color = '#0e4886')),
        yaxis = dict(title = ytitle, titlefont = dict(color = '#0e4886'), tickformat = '.2f'), 
        width=900, 
        height=300,
        margin=dict(l=100, r=10, t=40, b=10))

    return go.Figure (data=traces, layout=layout)

def get_histrogram_bi(df_x, cat, values, mode='overlay', xtitle=None, ytitle=None, title='title', bins=None):
    '''Bi-Variate, overlay Histrogram'''

    colors = ['#f58225', 'blue', 'orange', 'yellow']

    traces = [
        go.Histogram(
            x=df_x[df_x[cat] == name][values],
            nbinsx=bins, 
            name=str(name),
            marker_color=colors[count],
            opacity=0.75,
            marker_line_width=1) for count, name in enumerate(df_x[cat].unique())
    ]

    layout = go.Layout(
        barmode=mode,
        title=title,
        titlefont=dict(size=15, color='#0e4886'), 
        title_x=0.5,
        font=dict(size=10), 
        xaxis = dict(title = xtitle, titlefont = dict(color = '#0e4886')),
        yaxis = dict(title = ytitle, titlefont = dict(color = '#0e4886'), tickformat = '.2f'), 
        width=900, 
        height=300,
        margin=dict(l=100, r=10, t=40, b=10))

    return go.Figure (data=traces, layout=layout)

def get_bar(df_x, df_y, xtitle=None, ytitle=None, title='title'):
    '''Bar Chart'''
    traces = [
        go.Bar(
        x=df_x,
        y=df_y,
        marker_line_width=1,
        marker_color='#f58225',
        marker_line_color='#fa0400',
        opacity=0.8,)
    ]

    layout = go.Layout(
        title=title,
        titlefont=dict(size=15, color='#0e4886'), 
        title_x=0.5,
        font=dict(size=10), 
        xaxis = dict(title = xtitle, titlefont = dict(color = '#0e4886')),
        yaxis = dict(title = ytitle, titlefont = dict(color = '#0e4886'), tickformat = '.2f'), 
        width=900, 
        height=400,
        margin=dict(l=50, r=10, t=40, b=0))

    return go.Figure (data=traces, layout=layout)

def get_boxplot_cat(df_y, cat, values, xtitle=None, ytitle=None, title='title'):
    '''
    Box Plot with category
    cat: Targetted Columns to category
    values: Targetted Columns for values
    '''

    traces = [
        go.Box(
                y = df_y[df_y[cat] == name][values], 
                name = name,
                boxpoints = 'outliers', 
                jitter = 0, 
                marker = dict(size =2),
                ) 
        for name in df_y[cat].unique()
        ]

    layout = go.Layout(
        title=title,
        titlefont=dict(size=15, color='#0e4886'), 
        legend = dict(x=1, y=0.95, 
        font=dict(size=10)),
        title_x=0.5,
        font=dict(size=10), 
        xaxis = dict(title = xtitle, titlefont = dict(color = '#0e4886')),
        yaxis = dict(title = ytitle, titlefont = dict(color = '#0e4886'), tickformat = '.2f'), 
        width=900, 
        height=300,
        margin=dict(l=50, r=10, t=40, b=0))

    return go.Figure (data=traces, layout=layout)

def get_joint_plot(df_x, df_y, x_name=None, y_name=None):
    '''2D joint plot'''
    data = [
        go.Scatter(
            x=df_x, 
            y=df_y, 
            mode='markers', 
            name='points',
            marker=dict(color='rgb(102,0,0)', size=2, opacity=0.4)), 
        
        go.Histogram2dContour(
            x=df_x, 
            y=df_y, 
            name='density', 
            ncontours=20,
            colorscale='Hot', reversescale=True, showscale=False),
        
        go.Histogram(
            x=df_x, 
            name=x_name,
            marker=dict(color='rgb(102,0,0)'),
            yaxis='y2'),
        
        go.Histogram(
            y=df_y, 
            name=x_name, 
            marker=dict(color='rgb(102,0,0)'),
            xaxis='x2')
    ]
    
    layout = go.Layout(
        showlegend=False,
        autosize=False,
        xaxis=dict(domain=[0, 0.85], showgrid=False, zeroline=False),
        yaxis=dict(domain=[0, 0.85], showgrid=False, zeroline=False),
        hovermode='closest',
        bargap=0,
        xaxis2=dict(domain=[0.85, 1], showgrid=False, zeroline=False),
        yaxis2=dict(domain=[0.85, 1], showgrid=False, zeroline=False),
        width=900, 
        height=400,
        margin=dict(l=100, r=10, t=40, b=10)
    )

    return go.Figure(data=data, layout=layout)

def get_scatter(df, x, y, title='Scatter Plot', height=500, width=900, box=False, jitter_dist=None, deg=None):
    """Bivariate Scatter Plot, with best fitting line"""
    
    df = df.copy()
    df_ori = df[[x, y]].dropna().copy()
    
    if jitter_dist:
        for col in df[[x, y]].columns:
            df[col] = df[col] + np.random.randn(len(df[col])) * jitter_dist
    
    trace1 = go.Scattergl(
        x=df[x], 
        y=df[y],  
        text=df[x].index,
        mode='markers',
        name='Scatter Plot',
        marker=dict(size =2))
        
    traces = [trace1]
    
    if box:
        trace2 = go.Box(
            x=df[x], 
            text=df[x].index, 
            name=x, 
            boxpoints='outliers', 
            jitter=0, 
            marker=dict(size=2),
            yaxis='y2')
        
        trace3 = go.Box(
            y=df[y], 
            text=df[y].index, 
            name=y, 
            boxpoints='outliers', 
            jitter=0, 
            marker=dict(size =2),
            xaxis='x2')
            
        traces.extend([trace2, trace3])
    
    # only for polynomial fitting
    if deg:
        poly_features = PolynomialFeatures(degree=deg, include_bias=False)
        x_poly = poly_features.fit_transform(df_ori[[x]].values)
        poly_reg = LinearRegression()
        poly_reg.fit(x_poly, df_ori[[y]].values)
        x_unique = df_ori[x].sort_values().unique()
        
        trace4 = go.Scatter(
            name='Fitting_Lines',
            mode = 'markers+lines', 
            marker = dict(size =4, color = 'red'), 
            line = dict(width = 1.5, color = 'red'),
            x=x_unique, 
            y=poly_reg.predict(poly_features.transform(x_unique.reshape(-1, 1))).flatten())
            
        traces.append(trace4)
    
    vs_layout = go.Layout (
        hovermode='closest',
        title=title, 
        title_x=0.5,
        titlefont=dict(size=14, color='#0e4886'), 
        font=dict(size=10), 
        xaxis=dict(tickfont=dict(size=10), titlefont=dict(color='#0e4886'), title=x,  domain=[0, 0.85], showgrid=False), 
        xaxis2=dict(domain=[0.85, 1], showticklabels=False, showgrid=False), 
        yaxis=dict(tickfont=dict(size=10), title=y, titlefont=dict(color='#0e4886'), domain=[0, 0.85], showgrid=False, tickvals = df_ori[y].unique()), 
        yaxis2=dict(domain=[0.85,1], showticklabels=False, showgrid=False), 
        showlegend=False, 
        width=width, 
        height=height,
        margin=dict(l=10, r=10, t=80, b=10))
    
    fig = go.Figure (data=traces, layout=vs_layout)
    return fig
    
def get_corr_heatmap(df, title='Correlation Heatmap', height=300, width=900, grouped=False, zmax=1, zmin=0):
    '''Display Correlation Heatmap by inputting DataFrame'''
    
    df = df.corr()
    
    if grouped:
        df.index = [x[0] + ': ' + x[1] for x in df.index]
    
    fig = ff.create_annotated_heatmap(
        z=df.values.round(2), 
        x=df.columns.tolist(), 
        y=df.index.tolist(), 
        reversescale=True,
        zmin=zmin,
        zmax=zmax,
        showscale=True)
    
    fig['layout']['yaxis']['autorange'] = "reversed"
    
    fig['layout'].update(
        title=title, 
        title_x=0.5,
        titlefont=dict(size=18, color='#0e4886'), 
        font=dict(size=12), 
        width=width, 
        height=height,
        margin=dict(l=10, r=10, t=80, b=10))
    
    return fig

def get_ts_plot(df_x, title=None, yaxis_label=None, xaxis_label=None, hover_mode='x', legend_bool=True, xtick=0, drag_mode='zoom'):
    '''TIme Series Plot'''


    try:
        traces = [
            go.Scattergl(
                x=df_x.index, 
                y=df_x[name].round(2),
                mode='markers + lines',
                name=name, 
                marker=dict(size =2), 
                line=dict(width=1)) for name in df_x.columns
        ]

    except:
        traces = [
                go.Scattergl(
                    x=df_x.index, 
                    y=df_x.round(2), 
                    mode='markers + lines', 
                    name=df_x.name,
                    marker=dict(size=2, color='blue'), 
                    line=dict(width=1, color='blue'))
        ]


    layout=go.Layout (
            title=title, 
            title_x=0.5,
            titlefont=dict(size=14, color='#0e4886'), 
            font=dict(size=10),
            hovermode=hover_mode,
            dragmode=drag_mode, 
            showlegend=legend_bool,
            xaxis=dict(dtick=xtick, title=xaxis_label, titlefont=dict(color='#0e4886')),
            yaxis=dict(title=yaxis_label, titlefont=dict(color='#0e4886'), tickformat='.2f'), 
            width=900, 
            height=400,
            margin=dict(l=50, r=10, t=40, b=40)
    )

    fig = go.Figure (data=traces, layout=layout)
    return fig
