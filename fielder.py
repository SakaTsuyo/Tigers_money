import numpy as np
import pandas as pd
import io
from joblib import load
from sklearn.ensemble import RandomForestRegressor

def predict(fielding_data):
    rg_model = 'finalized_model_fielder.sav'
    rg = load(rg_model)
    df = pd.DataFrame(
    data= fielding_data.reshape(1, -1),
    columns=['打率','試合', '打席数', '打数', '安打','本塁打',
                '打点', '盗塁','四球', '死球','三振',
                '犠打','併殺打', '出塁率','長打率','OPS'])
            # resultの前にデータフレームにする
            # 形式はcolaboのtest_dataと同じ形式に
    results = rg.predict(df)
    return results