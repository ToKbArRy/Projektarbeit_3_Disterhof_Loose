#import sklearn
 #%%

import pandas as pd
import os

parent_dir = "E:/Game Data/data/"


class read_data:
    def test1(parent_dir):
        data = pd.DataFrame()

        for subdir, dirs, files in os.walk(parent_dir):
            for file in files:
                if "A1" in file:
                    df = pd.read_csv(os.path.join(subdir, file), sep=",",usecols = ["logid","time"])
                    df["player"] = file[0:-7]
                    data = pd.concat([data, df])
                    print(file)

        return data        




 #%%
data = read_data.test1(parent_dir)
 #%%
# nur EnterWorld und ExitWorld
played_amount = data[data["logid"].isin([1003,1004])]
played_amount_group_player = played_amount.groupby(["player"])
for player_name,player_df in played_amount_group_player:
    print(player_name)
    print(player_df.sort_values(by="time"))

    for row in player_df.iterrows():
        row["logid"]

player_df.logid.shift()


#played_amount = played_amount.groupby(["player"]).count()
print(played_amount)
#played_amount
#%%


#%%

"""
for subdir, dirs, files in os.walk(parent_dir):
    for file in files:
        y = pd.read_csv(os.path.join(subdir, file),sep=",",usecols = ["logid","actor_zone_id"])
        y = y[(y["logid"] == 1005) 




    def __init__(self,parent_dir):
        for subdir, dirs, files in os.walk(parent_dir):
            for file in files:
                #data = pd.read_csv(os.path.join(subdir, file), sep=",")
                return file

"""
# %%
