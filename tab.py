import pandas as pd

df = pd.DataFrame()
m1 = pd.DataFrame()
m2 = pd.DataFrame()

def party(df: pd.DataFrame, i: int, district: dict):
    if df.loc[i, 'party'] == 'REPUBLICAN':
            district['REPUBLICAN'] = max(district.get('REPUBLICAN', 0), df.loc[i, 'Pct'])
    elif df.loc[i, 'party'] in ['DEMOCRAT', 'DEMOCRATIC-FARMER-LABOR', 'DEMOCRATIC-NONPARTISAN LEAGUE']:
        district['DEMOCRAT'] = max(district.get('DEMOCRAT', 0), df.loc[i, 'Pct'])
    else:
        district['OTHER'] = max(district.get('OTHER', 0), df.loc[i, 'Pct'])

def setCD(df_: pd.DataFrame):
    index = df_.index
    for i in index:
        if df_.loc[i, 'district'] == 0:
            df_.loc[i, 'CD'] = df_.loc[i, 'state_po'] + '-AL'
        elif df_.loc[i, 'district'] < 10:
            df_.loc[i, 'CD'] = df_.loc[i, 'state_po'] + '-0' + str(df_.loc[i, 'district'])
        else:
            df_.loc[i, 'CD'] = df_.loc[i, 'state_po'] + '-' + str(df_.loc[i, 'district'])
    return df_

def toForm(tag: str, floor: float):
    data, district = {}, {}
    dfB = df[(df['Pct'] > floor) & (df['state_po'] != 'NY')]
    index = dfB.index
    prev = dfB.loc[index[0], 'CD']
    for i in index:
        if dfB.loc[i, 'CD'] != prev:
            if district.get('REPUBLICAN', 0) == 0:
                district['REPUBLICAN'] = 0
            if district.get('DEMOCRAT', 0) == 0:
                district['DEMOCRAT'] = 0
            data[prev] = district
            prev = dfB.loc[i, 'CD']
            district = {}
            # if dfB.loc[i, 'party'] == 'REPUBLICAN':
            #     district['REPUBLICAN'] = max(district.get('REPUBLICAN', 0), dfB.loc[i, 'Pct'])
            # elif dfB.loc[i, 'party'] in ['DEMOCRAT', 'DEMOCRATIC-FARMER-LABOR', 'DEMOCRATIC-NONPARTISAN LEAGUE']:
            #     district['DEMOCRAT'] = max(district.get('DEMOCRAT', 0), dfB.loc[i, 'Pct'])
            # else:
            #     district['OTHER'] = max(district.get('OTHER', 0), dfB.loc[i, 'Pct'])
            party(dfB, i, district)
        else:
            party(dfB, i, district)
    data[prev] = district

    dataDF = pd.DataFrame(data)
    dataDF.transpose().to_csv(f'{tag}.csv')

def toFormB(tag: str):
    ny = df[df['state_po'] == 'NY']
    data, district = {}, {}
    index = ny.index
    prev = ny.loc[index[0], 'CD']
    for i in index:
        if ny.loc[i, 'CD'] != prev:
            data[prev] = district
            prev = ny.loc[i, 'CD']
            district = {}
            district[ny.loc[i, 'candidate']] = ny.loc[i, 'Pct']
        else:
            district[ny.loc[i, 'candidate']] = ny.loc[i, 'Pct'] + district.get(ny.loc[i, 'candidate'], 0)
    data[prev] = district

    dataDF = pd.DataFrame(data)
    dataDF.to_csv(f'{tag}_NY.csv')

def setUp(df_: pd.DataFrame, year: int):
    df_ = df_[(df_['year'] == year) & (df_['state_po'] != 'DC')]
    df_ = setCD(df_)
    df_['Pct'] = (df_['candidatevotes'] / abs(df_['totalvotes'])) * 100
    df_ = df_[['state_po', 'CD', 'candidate', 'party', 'Pct']]
    df_ = df_.dropna()
    return df_

def merge():
    merged = m1.merge(m2, on='id', how='outer')
    merged.to_csv('merged.csv')