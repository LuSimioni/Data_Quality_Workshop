import pandas as pd
import pandera as pa

from pandera import Check, Column, DataFrameSchema


df = pd.DataFrame({
    "column1": [1, 4, 0],
    "column2": [-1.3, -1.4, -2.9],
    "column3": pd.to_datetime(["2012", "2024", "2031"]),
})

schema = pa.infer_schema(df)

with open("inferred_schema.py", "w") as file:
        file.write(schema.to_script())