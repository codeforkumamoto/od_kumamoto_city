import pandas as pd
import sys
import os

def convert_first_sheet_to_csv(excel_file_path):
    # Excelファイルのディレクトリとファイル名を取得
    directory, file_name = os.path.split(excel_file_path)
    # 拡張子を除いたファイル名を取得
    base_name = os.path.splitext(file_name)[0]
    # CSVファイルパスを設定
    csv_file_path = os.path.join(directory, f"{base_name}.csv")

    # 全シート名を取得
    sheet_names = pd.ExcelFile(excel_file_path).sheet_names
    
    # Excelの最初のシートを読み込む(見出し含む)
    df = pd.read_excel(excel_file_path, sheet_name=sheet_names[0])
    # 残りのシート
    for sheet in sheet_names[1:]:
        temp_df = pd.read_excel(excel_file_path, sheet_name=sheet, skiprows=1)
        # 列名をリセットし、最初の列名を統一
        temp_df.columns = df.columns[:temp_df.shape[1]]
        df = pd.concat([df, temp_df], ignore_index=True, axis=0)

    # DataFrameをCSVファイルとして保存
    df.to_csv(csv_file_path, index=False)
    print(f"Saved CSV at {csv_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python xls2csv.py path_to_excel_file.xlsx")
    else:
        convert_first_sheet_to_csv(sys.argv[1])
