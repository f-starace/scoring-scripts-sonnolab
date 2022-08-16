
# TODO: Implement types

from pydantic import BaseModel



class PlotConfigOptions(BaseModel):
    """
    Options for configuring the plot
    """
    x: str = None
    y: str = None
    title: str = None
    xlabel: str = None
    ylabel: str = None
    xlim: tuple = None
    ylim: tuple = None
