import pandas as pd

def fill_csv() -> str:
    id = ""
    return "some"

def process_row(row):
    for col in row[::-1]:
        if pd.notnull(col) and col != '':
            words = str(col).split()
            if len(words) > 2:
                return ' '.join(words[:3])
    for col in row:
        if pd.notnull(col) and col != '':
            processed = str.replace(col, ' ', '')
            if processed != '':
                return str(col).split()[0]
    return ''

def process_bha(bha: str) -> str:
    newstr = bha.replace('\'', '')
    if newstr.endswith('S'):
        return newstr[1:-1]
    else:
        return newstr

if __name__ == '__main__':
    # Read the CSV file
    df = pd.read_csv("./data.csv")

    # Create a new column 'ProcessedName' using the process_row function
    name_columns = [f"Name{i}" for i in range(1, 10)]
    df['ProcessedName'] = df[name_columns].apply(process_row, axis=1)

    # Optionally drop the original name columns
    df = df.drop(columns=name_columns)

  

    # Read the Excel file
    xls = pd.read_csv('./datato.csv')

    # Iterate through xls['Информация по ВНА'] and update values in xls
    print(xls['Инвентарный номер ВНА'].unique())
    # Convert 'Информация по ВНА' column to a list and iterate over it
    print(xls.info())
    for index, bha in enumerate(xls['Инвентарный номер ВНА'].tolist()):
        if bha == '050000005430S':
            print("WATAFAK GABEN")
        formatted_bha = process_bha(str(bha))
        matching_row = df[df['Инвентарный'] == formatted_bha]
        
        if not matching_row.empty:
            xls.at[index, 'Серийный номер'] = matching_row['Серийный'].values[0]
            xls.at[index, 'ФИО'] = matching_row['ProcessedName'].values[0]

    # Save the updated xls DataFrame back to an Excel file
    xls.to_excel('updated_result.xlsx', index=False, engine='openpyxl')


    # Save the updated xls DataFrame back to an Excel file
    xls.to_excel('updated_result.xlsx', index=False, engine='openpyxl')
