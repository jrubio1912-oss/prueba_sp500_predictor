import pandas as pd


def preprocess_data(df):
    """
    Realiza limpieza y preprocesamiento básico del dataset.
    """

    # Copia para evitar modificar original
    df = df.copy()

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