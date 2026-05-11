"""
date: 2026/05/04
author: ikuta
this file for csv output process
"""

#-------------------------------------------------------------
# import
import csv
import pandas as pd
from pathlib import Path
from datetime import datetime
import src.settings_init.HK.header_HK as head_HK
import src.utils.organizing_datalist as org
#-------------------------------------------------------------
#function

# 格納されたデータのうち、最初の行のUTC時刻をファイル名に記録するための関数

def create_filename_with_utc(original_file_name, merged_list):

    # UTCの1行目（ヘッダー除いた最初）
    first_utc = next((t for t in merged_list.get("UTC Time", []) if t is not None), None)

    # UTCが存在しない場合（全てNoneなど）
    if first_utc is None:
        print("[WARNING] UTC Time is all None")
        return f"invalid_{original_file_name}"

    # datetimeに変換
    try:
        dt = datetime.strptime(first_utc, "%Y/%m/%d %H:%M:%S")
    except Exception as e:
        print(f"[ERROR] UTC format invalid: {first_utc}")
        return f"invalid_{original_file_name}"

    # YYMMDD_HHMMSS に変換
    time_str = dt.strftime("%y%m%d_%H%M%S")

    # 新しい名前
    new_name = f"{time_str}_{original_file_name}.csv"

    return new_name

# csvにデータを格納する関数 (ファイル名, ヘッダー設定可能, 一番古いデータの時刻が名前でわかる)
def csv_output(original_file_name, data_header, merged_list): # 引数：つけたい名前, 格納するデータのヘッダーリスト, データが格納されているリスト
    # 出力フォルダパスの指定
    output_dir = Path(__file__).resolve().parents[3] / "data"/"Output"
    # フォルダが存在しないときにエラーを出す (デバッグ用)
    if not output_dir.exists():
        raise FileNotFoundError(f"Output folder not found: {output_dir}")

    # ファイル名の指定
    file_name = create_filename_with_utc(original_file_name, merged_list)
    output_file = output_dir / file_name

    # 行数（1列目基準)
    num_rows = len(next(iter(merged_list.values())))
    # valiablesで設定したデータヘッダーのうち、リストに存在するデータのみ使用する
    new_data_header = [
        col for col in data_header
        if org.normalize(col) in [org.normalize(k) for k in merged_list.keys()]
    ]

    # 出力用ヘッダー
    output_header = [
        head_HK.header_map.get(col, col)
        for col in new_data_header
        ]

    #data_header = list(merged_list.keys()) #デバッグ用

    # 行データ作成
    rows = []
    for i in range(num_rows):
        row = {}
        for col in new_data_header:

            # 対応するkeyを探す
            match_key = next(
                (k for k in merged_list.keys() if org.normalize(k) == org.normalize(col)),
                None
            )

            new_col = head_HK.header_map.get(col, col)

            if match_key:
                row[new_col] = merged_list[match_key][i]
            else:
                row[new_col] = ""

        rows.append(row)


    # CSV出力
    with open(output_file, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=output_header, delimiter=",")

        writer.writeheader()  # ヘッダー書き込み
        writer.writerows(rows)


# 与えられた名前のファイルを出力する関数(csvに対応, 一番シンプル)
def original_name_file(name, data):

    # 名前に1Uの文字が入るとき
    if "1U" in name:
        # 出力フォルダパスの指定
        output_dir = Path(__file__).resolve().parents[3] / "data" / "Output" / "1U"
    # 名前に2Uの文字が入るとき
    elif "2U" in name:
        output_dir = Path(__file__).resolve().parents[3] / "data" / "Output" / "2U"

    # フォルダが存在しないときにエラー（または作成でもOK）
    if not output_dir.exists():
        raise FileNotFoundError(f"Output folder not found: {output_dir}")
        # ↓自動作成にするならこっち
        # output_dir.mkdir(parents=True, exist_ok=True)

    # ファイル名
    file_name = name

    output_file = output_dir / file_name

    # ======================
    # 行数
    # ======================
    num_rows = len(next(iter(data.values())))

    # ======================
    # ヘッダー
    # ======================
    headers = list(data.keys())

    # ======================
    # 行データ作成
    # ======================
    rows = []

    for i in range(num_rows):
        row = {}

        for key in headers:
            if i < len(data[key]):
                row[key] = data[key][i]
            else:
                row[key] = ""

        rows.append(row)

    # ======================
    # CSV出力
    # ======================
    with open(output_file, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

# Excelファイルで出力する関数
def output_excel(name, data):

    # ======================
    # 出力フォルダ分岐
    # ======================
    if "1U" in name:
        output_dir = Path(__file__).resolve().parents[3] / "data" / "Output" / "1U"
    elif "2U" in name:
        output_dir = Path(__file__).resolve().parents[3] / "data" / "Output" / "2U"

    # フォルダがなければ作る（おすすめ）
    output_dir.mkdir(parents=True, exist_ok=True)

    # ファイル名
    output_file = output_dir / name

    # ======================
    # dict → DataFrame
    # ======================
    df = pd.DataFrame(data)

    # ======================
    # Excel出力
    # ======================
    df.to_excel(output_file, index=False)

# 1度格納した値にUTC時刻を追加したものを、そのまま出力する関数 (csvとxlsx)
def export_all_data(all_data):
    for item in all_data:

        name = item["name"]          # ← stem
        data = item["data"]

        # ファイル名(拡張子込み)
        file_name1 = f"{name}.csv"
        file_name2 = f"{name}.xlsx"
    
        # csv出力
        original_name_file(
            name=file_name1,
            data=data
        )
        # xlsx出力
        output_excel(
            name=file_name2,
            data=data
        )





