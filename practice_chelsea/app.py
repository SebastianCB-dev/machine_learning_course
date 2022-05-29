import pandas as pd

df_chelsea = pd.read_csv('Chelsea_DataSet.csv')
df_chelsea["Goals"] = df_chelsea["Goals"].fillna(0)
df_organizado = df_chelsea.sort_values("Goals", ascending=False).reset_index(drop=True)
#print(df_organizado)

Frank_Lampard = df_organizado[df_organizado["Player Name"] == 'Frank Lampard']
goals_fl = Frank_Lampard["Goals"]
print(goals_fl.to_list()[0]) # Goles

