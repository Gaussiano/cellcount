import polars as pl
from ..block import block

@block(name="hello_world", description="Synthetic control vs treated data")
def hello(params: dict, inputs: dict) -> pl.DataFrame:
    return pl.DataFrame({
        "image_id": [1, 2, 3, 4, 5, 6],
        "condition": ["control", "control", "control", "treated", "treated", "treated"],
        "cell_count": [187, 192, 178, 94, 98, 101],
    })