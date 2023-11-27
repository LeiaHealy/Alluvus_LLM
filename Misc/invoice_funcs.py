import pandas as pd

def load_extract_invoice(inv_path):
    complete_df = pd.read_excel(inv_path)
    df = complete_df[['Date','Notes']].copy()
    # Convert from YYYY-MM-DD to MM-DD format
    df['Date'] = df['Date'].str[5:]

    # Concatenate 'Dates' and 'Notes'
    df['Concatenated'] = df['Date'] + " " + df['Notes']

    # Extract concatenated column as string
    concat_str = "\n".join(df['Concatenated'])

    return df, concat_str