import pandas as pd
import numpy as np
import re


def read_data() -> pd.DataFrame:
    df = pd.read_csv('./data/fieldwork.csv', delimiter=';')
    return df


def filter_characters(sentence: str) -> str:
    return re.sub('[^a-zA-Z]+', '', sentence)


def format_coordinate(df: pd.DataFrame, name: str) -> pd.DataFrame:
    df[name] = df[name].str.replace(',', '.').astype(float)
    return df


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    # Select columns
    df = df.rename(columns={'vegetatiestructuur': 'class'})
    df = df[['lat', 'lon', 'class']]

    # Normalise class names
    df['class'] = df['class'].apply(filter_characters)

    # Lat and lot formatting
    df = format_coordinate(df, 'lat')
    df = format_coordinate(df, 'lon')
    return df


def add_class_index(df: pd.DataFrame) -> pd.DataFrame:
    classes = df['class'].unique()
    class_df = pd.DataFrame(np.sort(classes), columns=['class']).reset_index()
    df = pd.merge(df, class_df, on='class', how='left')
    return df


def main():
    df = read_data()
    df = preprocess_data(df)
    df = add_class_index(df)
    print(df.head())
    print(df.dtypes)


if __name__ == '__main__':
    main()