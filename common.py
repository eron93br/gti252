import time
from utils import _LOREM_IPSUM, DATASET_URL
import pandas as pd
import numpy as np
import plotly.express as px

def stream_data():
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.05)

    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )

    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.05)

def load_tips_dataset() -> pd.DataFrame:
    return pd.read_csv(DATASET_URL)

def make_visualization1(df, value1=0, value2=10):
    #TODO: REALIZAR A PERSONALIZAÇÃO DESTA VISUALIZAÇÃO!!! customização com legendas/títulos
    dfi = df[(df["tip"] >= value1) & (df["tip"] <= value2)]
    return px.histogram(dfi, x="tip")

def make_vis_tb(df):
    return px.histogram(df, x="total_bill")

def make_piechart(df):
    return px.pie(df, names='sex', title='Proporção do gênero dos clientes')  