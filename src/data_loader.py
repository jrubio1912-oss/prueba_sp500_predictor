import yfinance as yf
import pandas as pd


def load_sp500_data(ticker="^GSPC", period="5y", interval="1d"):
    """
    Descarga datos históricos del S&P500 desde Yahoo Finance.
    """

    df = yf.download(
        ticker,
        period=period,
        interval=interval
    )

    df.reset_index(inplace=True)

    return df


def save_data(df, path="data/sp500.csv"):
    """
    Guarda dataset en formato CSV.
    """

    df.to_csv(path, index=False)


if __name__ == "__main__":

    data = load_sp500_data()

    save_data(data)

    print(data.head())