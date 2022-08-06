from typing import Optional
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd



def scatterplot(df: pd.DataFrame, plot_config: dict) -> go.Figure:
    # removing NaNs
    x = plot_config["x"]
    y = plot_config["y"]
    color_col: Optional[str] = plot_config.get("color_col")
    mark_col: Optional[str] = plot_config.get("mark_col")
    df = df.dropna(subset=[x, y])
    fig = px.scatter(df, x, y, color=color_col, symbol=mark_col)
    return fig
