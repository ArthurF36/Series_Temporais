import pandas as pd

def limpar_Texto(df: pd.DataFrame) -> pd.DataFrame:
    for coluna in df.columns:
        if pd.api.types.is_string_dtype(df[coluna]) or pd.api.types.is_object_dtype(df[coluna]):
            df[coluna] = (df[coluna].astype(str)
                          .str.replace(r"^[^0-9A-Za-zÀ-ÿ]+", "", regex=True)  
                          .str.replace(r"[\n\r\t\xa0]", " ", regex=True)      
                          .str.replace(r"\s+", " ", regex=True)               
                          .str.strip()                          
            )

    return df

def converter_tipo_coluna(df):
    data_formatada = df.columns[0]

    # Converter data corretamente
    df[data_formatada] = pd.to_datetime(df[data_formatada], format='%m/%d/%Y')

    # Ordenar
    df = df.sort_values(data_formatada)

    # Definir como índice (ideal para séries temporais)
    df = df.set_index(data_formatada)

    # Converter resto para float
    for coluna in df.columns:
        df[coluna] = pd.to_numeric(df[coluna], errors='coerce')

    return df