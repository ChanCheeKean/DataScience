import plotly.express as px
import pandas as pd
import numpy as np

def create_line_rating(df):
    fig = px.line(df, x="date", y="value", color='category')
    fig.update_layout(
        title='Employee Rating',
        title_font_family="Arial Black",
        title_font_size=20,
        xaxis=dict(
            title='Date',
            title_font_family="Savana",
            showline=False,
            showgrid=False),
        yaxis=dict(
            title='Rating',
            title_font_family="Savana",
            showgrid=True,
            gridcolor='black',
            zeroline=True,
            showline=True),
        margin=dict(
            autoexpand=False,
            l=80,
            b=100,
            r=20,
            t=80),
        showlegend=True,
        legend=dict(
            orientation="h", 
            x=0, 
            y=-0.2),
        plot_bgcolor='#f8f9fa',
        paper_bgcolor='#f8f9fa'
        )
    return fig

def create_pie_rating(df):
    df.rename(columns={'overall_rating' : 'Overall Rating'}, inplace=True)
    fig = px.sunburst(
        df, 
        path=['job_status', 'years_at_company'], values='count',
        color='Overall Rating', 
        color_continuous_scale='RdBu',
        color_continuous_midpoint=np.average(df['Overall Rating'], weights=df['count']))

    fig.update_layout(
        title='Employee Rating by Group',
        title_font_family="Arial Black",
        title_font_size=20,
        margin=dict(
            autoexpand=False,
            l=10,
            b=50,
            r=120,
            t=80),
        plot_bgcolor='#f8f9fa',
        paper_bgcolor='#f8f9fa'
        )
    return fig

    