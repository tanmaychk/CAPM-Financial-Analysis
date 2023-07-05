#prices being normalized over initial price
def normalized(df):
    for i in df.columns[1:]:
        df[i] = df[i]/df[i][0]
    return df