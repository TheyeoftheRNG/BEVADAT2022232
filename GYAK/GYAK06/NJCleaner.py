import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


class NJCleaner():

    def __init__(self,route = "2018_03.csv") -> None:
        col_name=["date","train_id","stop_sequence","from","from_id","to","to_id","scheduled_time","actual_time","delay_minutes","status","line","type"]
        self.data = pd.read_csv(route,skiprows=1, header=None, names=col_name)

    def order_by_scheduled_time(self) -> pd.DataFrame:
        self.data = self.data.sort_values(by='scheduled_time',ascending=True)
        return self.data
    
    def drop_columns_and_nan(self)->pd.DataFrame:
        self.data=self.data.drop(["from","to"], axis=1)
        self.data = self.data.dropna()
        return self.data
    
    def convert_date_to_day(self):
        df = self.data
        df['day'] = pd.to_datetime(df['date']).dt.day_name()
        df.drop('date', axis=1, inplace=True)
        self.data = df
        return self.data

    def convert_scheduled_time_to_part_of_the_day(self):
        df = self.data
        part_of_day = []
        hour_of_day = [[row[11] + row[12]] for row in df["scheduled_time"]]
        for hour in hour_of_day:
            hour = int(hour[0])
            if hour >= 4 and hour < 8:
                part_of_day.append('early_morning')
            elif hour >= 8 and hour < 12:
                part_of_day.append('morning')
            elif hour >= 12 and hour < 16:
                part_of_day.append('afternoon')
            elif hour >= 16 and hour < 20:
                part_of_day.append('evening')
            elif hour >= 20 or hour < 4:
                part_of_day.append('night')
        df['part_of_the_day'] = part_of_day
        df = df.drop(["scheduled_time"], axis=1)
        self.data=df
        return df



    
    def convert_delay(self):
        df = self.data
        df["delay"] = [1 if x>= 5 else 0 for x in df["delay_minutes"]]
        self.data = df
        return df
    
    def drop_unnecessary_columns(self):
        df =self.data
        df = df.drop(["train_id", "actual_time", "delay_minutes"], axis=1)
        self.data=df
        return df
    
    def save_first_60k(self, path):
        df =self.data
        df.head(60000).to_csv(path, index=False)
    

    def prep_df(self,path='data/NJ.csv'):
        df = self.data
        df = self.order_by_scheduled_time()

        df = self.drop_columns_and_nan()

        df = self.convert_scheduled_time_to_part_of_the_day()

        df = self.convert_delay()

        df = self.drop_unnecessary_columns()

        self.save_first_60k(path)

        return df


