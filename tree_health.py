import pandas as pd
import numpy as np

df = pd.read_csv('D:\Documents\misc\python_practice\Tree_Data.csv', sep=",")

df_head = df.head()

#egyediseg tesztelese
df['tree_id'].unique().size == df.shape[0]

df["status"].unique()
df["health"].unique()
df[df["status"]=="Alive"]["health"].unique()

#aranyok
((df["status"]=="Stump").sum() + (df["status"]=="Dead").sum()) / (df["status"]=="Alive").sum()

#szuresek
df_missing = df[df["status"] == 'Alive']
df_dead = df[(df["status"] == "Stump") | (df["status"] == "Dead")]
df_filtered = df_fintered[~df_fintered["tree_id"].isin(df_dead["tree_id"])]

df_filtered[(df_filtered["tree_dbh"] > 60) | (df_filtered["tree_dbh"] == 60)]


#hianyzo adatok szurese
df_missing = df_missing[df_missing["health"] != df_missing["health"]]
df_fintered = df[~df.index.isin(df_missing.index)]


#describe
mean_by_spc = df_filtered.groupby("spc_common").mean()
mean_by_spc["tree_dbh"].hist()
mean_by_spc[mean_by_spc["tree_dbh"] > 18]


#vizualizacio
import seaborn as sns
import matplotlib.pyplot as plt

df_filt_3 = df_filtered.loc[(df_filtered['spc_common']=="London planetree") | (df_filtered['spc_common']=="eastern cottonwood") | (df_filtered['spc_common']=="silver maple")]


ax = sns.violinplot(x="spc_common", y="tree_dbh", data=df_filt_3)
ax2 = sns.boxplot(x="spc_common", y="tree_dbh", data=df_filt_3)

df_filt_3[["spc_common", "health", "tree_dbh"]].describe()

df_filt_3[ "tree_dbh"].mean()
df_filt_3[ "tree_dbh"].quantile(0.99)
df_filt_3[ "tree_dbh"].max()


#75 percentilis feletti atmeroju fak kiszurese
mask = df.groupby("spc_common")["tree_dbh"].describe()
df2 = df.merge(mask["75%"], how="left", on="spc_common")
df2.loc[df2["tree_dbh"] < df2['75%']]

ax3 = sns.lmplot(x="latitude", y="longitude", fit_reg=False, hue="health", data=df_filt_3)
ax4 = sns.heatmap(df_filt_3, annot=True, annot_kws={"size": 7})
#jarda helyzete es az egeszsegi allapot
df_health_con = df_filtered.groupby("health")["tree_dbh"].describe()


((df["status"]=="Stump").sum() + (df["status"]=="Dead").sum()) / (df["status"]=="Alive").sum()

#apply function
df_head["test_length"] = df_head["spc_common"].apply(len_calc)

def len_calc(x):
    return(len(str(x)))

df2.loc[df2["tree_id"]==180683]
