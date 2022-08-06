import plotly.io as pio
import plotly.graph_objects as go



def get_image_bytes(fig_dct: dict, format: str):
    return pio.to_image(fig_dct, format=format)


def get_img_from_json(json_str: str) -> go.Figure:
    return pio.from_json(json_str)
