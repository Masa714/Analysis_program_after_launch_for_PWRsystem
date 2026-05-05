"""
date: 2026/05/04
author: ikuta
this file for csv output process
"""

#-------------------------------------------------------------
# import
import csv
from pathlib import Path
import extract_process_from_Input_csv as input
import src.settings.valiables as able
import Power_Generation.Power_Generation_calc as PG
#-------------------------------------------------------------
# main

# 出力フォルダパスの指定
output_dir = Path(__file__).resolve().parent.parent.parent / "data"/"Output_csv"

#------------------------------------------------------------
# 1. 発電量関係

# 出力ファイルの名前設定
file_name_1U = able.Gene_name_1U
file_name_2U = able.Gene_name_2U
output_file_1U = output_dir/f"{file_name_1U}.csv"
output_file_2U = output_dir/f"{file_name_2U}.csv"

# 格納するデータのヘッダー指定
columns = able.columns_gene

# 行数（1列目基準） ここから先のextractはinputからではなく、
num_rows_1U = len(next(iter(input.extract_1U())))
num_rows_2U = len(next(iter(input.extract_2U())))

# 行データ作成(1U)
rows_1U = []
for i in range(num_rows_1U):
    row = {col: input.extract_1U[col][i] for col in columns}
    rows_1U.append(row)

# CSV出力
with open(output_file_1U, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=columns)

    writer.writeheader()  # ヘッダー書き込み
    writer.writerows(rows_1U)

# 行データ作成(2U)
rows_2U = []
for i in range(num_rows_2U):
    row = {col: input.extract_2U[col][i] for col in columns}
    rows_2U.append(row)

# CSV出力
with open(output_file_2U, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=columns)

    writer.writeheader()  # ヘッダー書き込み
    writer.writerows(rows_2U)

#----------------------------------------------------------------------
# 2. 2次電池関係
# 出力ファイルの名前設定
file_name = "Battery_condition"
output_file = output_dir/f"{file_name}.csv"

columns = list(input.extract.keys())

# 行数（1列目基準）
num_rows = len(next(iter(input.extract.values())))

# 行データ作成
rows = []
for i in range(num_rows):
    row = {col: input.extract[col][i] for col in columns}
    rows.append(row)

# CSV出力
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=columns)

    writer.writeheader()  # ヘッダー書き込み
    writer.writerows(rows)


#----------------------------------------------------------------------
# 3. 電力収支関係
# 出力ファイルの名前設定
file_name = "Power_budget"
output_file = output_dir/f"{file_name}.csv"

# 抽出するデータのヘッダー
columns = []

# 行数（1列目基準）
num_rows = len(next(iter(input.extract.values())))

# 行データ作成
rows = []
for i in range(num_rows):
    row = {col: input.extract[col][i] for col in columns}
    rows.append(row)

# CSV出力
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=columns)

    writer.writeheader()  # ヘッダー書き込み
    writer.writerows(rows)



