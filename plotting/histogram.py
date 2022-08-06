import pandas as pd
from typing import Literal, Optional
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd



def histogram(df: pd.DataFrame, plot_config: dict) -> go.Figure:
    x: str = plot_config["x"]
    bargap: Optional[float] = plot_config.get("bargap")
    color: Optional[str] = plot_config.get("color_col")
    marginal: Optional[Literal["box", "violin", "rug"]] = plot_config.get(
        "marginal", "box"
    )

    fig = px.histogram(
        df,
        x=x,
        marginal=marginal,  # or violin, rug
        hover_data=df.columns,
        color=color,
    )
    if bargap:
        fig.update_layout(bargap=bargap)
    return fig
