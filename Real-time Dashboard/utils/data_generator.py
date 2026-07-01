
import pandas as pd
import random
from datetime import datetime

def generate_data():
    return pd.DataFrame({
        "time": [datetime.now().strftime("%H:%M:%S")],
        "value": [random.randint(0, 100)]
    })
