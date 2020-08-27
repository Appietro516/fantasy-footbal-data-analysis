import glob
import numpy as np
import pandas as pd
import scipy.stats as sps

from sklearn import preprocessing

def main():
    #build dataframe from CSVs
    path = "./yearly"
    all_csv = glob.glob(path + "/*.csv")
    dframes = [pd.read_csv(file, index_col=None, header=0) for file in all_csv]
    df = pd.concat(dframes, axis=0, ignore_index=True)

    #iterate player stats
    final_scores = {}
    for player in df["Player"].unique():
        player_stats = (df.loc[df['Player'] == player])
        points = player_stats['FantasyPoints'].tolist()
        if len(points) <= 1:
            continue

        median = np.median(points)
        stdv = np.std(points)

        if median <= 0 or stdv <= 0:
            continue

        print(f'{player}: {points}, {median}, {stdv}')

    #print top k final scores
    top_k = 10
    sorted_scores = {k:v for k, v in sorted(final_scores.items(), key=lambda item: item[1], reverse=True)}
    for k, v in list(zip(sorted_scores.keys(), sorted_scores.values()))[-top_k:]:
        print(f'{k} :{v}')

#weighted harmonic mean
def weighted_hmean(arr, weights):
    return sum(weights) / sum(np.divide(weights, arr))


main()
