import pandas as pd

stims = pd.read_csv('lppFR_annot.csv')

x = stims[["word", "onset",  "offset"]]
x["duration"] = x.offset - x.onset

x.to_csv("lpp.csv")
