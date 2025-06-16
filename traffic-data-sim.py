import pandas as pd
import numpy as np

time_of_day = ['morning', 'afternoon', 'evening']
weather = ['clear', 'rain', 'foggy', 'cloudy']
road_type = ['main road', 'secondary road', 'residential']
event = [0, 1]  # 0 = no event, 1 = special event nearby

data = pd.DataFrame({
    'time_of_day': np.random.choice(time_of_day, 1000),
    'weather': np.random.choice(weather, 1000),
    'road_type': np.random.choice(road_type, 1000),
    'event': np.random.choice(event, 1000)
})

def simulate_congestion(row):
    if row['weather'] == 'rain' or row['event'] == 1:
        if row['road_type'] == 'main road':
            return 'High'
        elif row['road_type'] == 'secondary road':
            return 'Moderate'
        else:
            return np.random.choice(['Low', 'Moderate'])
    elif row['time_of_day'] == 'evening':
        return np.random.choice(['Moderate', 'High'])
    else:
        return 'Low'

data['congestion_level'] = data.apply(simulate_congestion, axis=1)

data.to_csv("kigali_traffic_dataset.csv", index=False)
