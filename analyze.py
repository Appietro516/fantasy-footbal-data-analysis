import glob
import numpy as np
import pandas as pd
import scipy.stats as sps
import re

from sklearn import preprocessing
from sklearn import datasets, linear_model

def main():
    #build dataframe from CSVs
    path = "./yearly"
    all_csv = glob.glob(path + "/*.csv")
    #read in the csv files, append a year column for use in the regression model
    dframes = [pd.read_csv(file, index_col=None, header=0).assign(Year=re.search("\d{4}", file).group(0)) for file in all_csv]
    df = pd.concat(dframes, axis=0, ignore_index=True)
    prediction_year = 2020

    #iterate player stats
    final_scores = {}
    for player in df["Player"].unique():
        player_stats = (df.loc[df['Player'] == player])
        points = player_stats['FantasyPoints'].tolist()
        years = np.array(player_stats['Year'].tolist()).reshape(-1, 1).astype(np.float64)
        #strip bad/insufficient data
        if len(points) <= 1:
            continue
        median = np.median(points)
        stdv = np.std(points)
        if median <= 0 or stdv <= 0:
            continue
        if 2019 not in years:
            continue


        #create regression model
        regr = linear_model.LinearRegression()
        regr.fit(years, points)

        #predict score for current year
        final_scores[player] = int(regr.predict(np.array(prediction_year).reshape(-1, 1).astype(np.float64))[0])

    #print top k final scores
    top_k = 10
    sorted_scores = {k:v for k, v in sorted(final_scores.items(), key=lambda item: item[1], reverse=True)}
    for k, v in list(zip(sorted_scores.keys(), sorted_scores.values()))[:top_k]:
        print(f'{k} :{v}')

#weighted harmonic mean
def weighted_hmean(arr, weights):
    return sum(weights) / sum(np.divide(weights, arr))


main()
