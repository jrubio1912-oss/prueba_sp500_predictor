import pandas as pd


def preprocess_data(df):

    df = df.copy()

    # Aplanar MultiIndex
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.droplevel(1)

    # Convertir fecha
    df["Date"] = pd.to_datetime(df["Date"])

    # Ordenar temporalmente
    df.sort_values("Date", inplace=True)

    # Resetear índices
    df.reset_index(drop=True, inplace=True)

    # Eliminar duplicados
    df.drop_duplicates(inplace=True)

    # Eliminar valores nulos
    df.dropna(inplace=True)

    return df