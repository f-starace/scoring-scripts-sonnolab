from typing import Literal, Optional
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from .types import PlotConfigOptions


def boxplot(df: pd.DataFrame, plot_config: PlotConfigOptions) -> go.Figure:
    x = plot_config["x"]
    y = plot_config["y"]
    color_col: Optional[str] = plot_config.get("color_col")
    points: Optional[Literal["all"]] = plot_config.get("points")
    # removing NaNs
    df = df.dropna(subset=[x, y])
    fig = px.box(
        df,
        x,
        y,
        points=points,
        color=color_col,
    )
    return fig
