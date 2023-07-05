import plotly.express as pl

def interactive_plot(df):
    fig=pl.line()
    for i in df.columns[1:]:
        fig.add_scatter(x=df["Date"],y=df[i],name = i)
    fig.update_layout(
    autosize=True,
    width=1420,
    height=500,
    margin=dict(
        l=50,
        r=50,
        pad=4
    ))
    return fig