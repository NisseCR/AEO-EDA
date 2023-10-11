import pandas as pd


def read() -> pd.DataFrame:
    df = pd.read_csv('test.csv')
    return df


def cross_match_utm_difference(df: pd.DataFrame) -> pd.DataFrame:
    _df = df.copy()
    _df = pd.merge(_df, _df, how='cross')
    _df = _df[(_df['x1'] != _df['x2']) & (_df['y1'] != _df['y2'])]
    _df['delta_x'] = abs(_df['x1'] - _df['x2'])
    _df['delta_y'] = abs(_df['y1'] - _df['y2'])
    _df['delta_xy'] = _df['delta_x'] + _df['delta_y']
    _df = _df.sort_values(by='delta_xy', ascennding=True)
    return _df


def main():
    df = read()
    cross_df = cross_match_utm_difference(df)
    print(cross_df.head())


if __name__ == '__main__':
    main()
