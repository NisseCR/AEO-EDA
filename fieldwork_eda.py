import pandas as pd


def read() -> pd.DataFrame:
    df = pd.read_csv('./data/fieldwork.csv', delimiter=';')
    df['lat'] = df['lat'].replace(',', '.').replace("'", '').astype(float)
    df['lon'] = df['lon'].replace(',', '.').replace("'", '').astype(float)
    return df


def cross_match_utm_difference(df: pd.DataFrame) -> pd.DataFrame:
    _df = df.copy()
    _df = pd.merge(_df, _df, how='cross')
    _df = _df[(_df['lat_x'] != _df['lat_y']) & (_df['lon_x'] != _df['lon_y'])]
    _df['delta_lat'] = abs(_df['lat_x'] - _df['lat_y'])
    _df['delta_lon'] = abs(_df['lon_x'] - _df['lon_y'])
    _df['delta_xy'] = _df['delta_lat'] + _df['delta_lon']
    _df = _df.sort_values(by='delta_xy', ascennding=True)
    return _df


def main():
    df = read()
    df = cross_match_utm_difference(df)
    print(df.columns)
    print(df)


if __name__ == '__main__':
    main()
