import numpy as np
import pandas as pd
import io
from joblib import load
from sklearn.ensemble import RandomForestRegressor
def predict(piching_data):
        rg_model = 'finalized_model_picher.sav'
        rg = load(rg_model)
        df = pd.DataFrame(
        data= piching_data.reshape(1, -1),
        columns=['防御率', '試合', '勝利', '敗北','セーブ',
                        'ホールド', '勝率', '打者', '投球回', '被安打', 
                        '被本塁打', '与四球', '与死球', '奪三振','失点',
                        '自責点', 'WHIP', 'DIPS'])
                # resultの前にデータフレームにする
                # 形式はcolaboのtest_dataと同じ形式に
        results = rg.predict(df)
        return results