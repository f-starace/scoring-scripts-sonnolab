from typing import Optional
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from .types import PlotConfigOptions



def scatterplot(df: pd.DataFrame, plot_config: PlotConfigOptions) -> go.Figure:
    x = plot_config.x
    y = plot_config.y
    color_col: Optional[str] = plot_config.get("color_col")
    mark_col: Optional[str] = plot_config.get("mark_col")
    df = df.dropna(subset=[x, y])
    fig = px.scatter(df, x, y, color=color_col, symbol=mark_col)
    return fig
