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

    # Excelの最初のシートを読み込む
    df = pd.read_excel(excel_file_path)
    print(df.head())

    # DataFrameをCSVファイルとして保存
    df.to_csv(csv_file_path, mode='w', index=False)
    print(f"Saved CSV at {csv_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python xls2csv.py path_to_excel_file.xlsx")
    else:
        convert_first_sheet_to_csv(sys.argv[1])
