import pandas as pd
lines = pd.read_csv("lines.csv")
bad_words = pd.read_csv("bad_words.csv")
bad_words = [w.lower() for w in list(bad_words['Bad words'])]
lines['result'] = ['BAD' if any(w in l.lower() for w in bad_words) else 'GOOD' for l in lines['Lines']]
lines.to_csv("final.csv")