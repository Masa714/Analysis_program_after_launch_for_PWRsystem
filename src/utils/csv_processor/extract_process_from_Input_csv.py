"""
date: 2026/05/04
author: ikuta
this file for extract process from input_csv
"""
#---------------------------------------------------------------------------------
# import

import csv
from datetime import datetime, timedelta
import src.utils.organizing_datalist as org
#---------------------------------------------------------------------------------
# 以下はOBC TimeをUTCに変換するための関数群

# 時刻表記の文字列をdatatime型にパースする関数
def parse_base_time(time_str):
    for fmt in ("%Y/%m/%d %H:%M:%S.%f", "%Y/%m/%d %H:%M:%S"):
        try:
            return datetime.strptime(time_str, fmt)
        except:
            continue
    return None

# ---------------------------
# CSVのOBC時刻の文字列 → float型の累積秒に変換
# ---------------------------

def obc_to_seconds(obc_str):
    # 空文字やNoneの場合は処理せず終了
    if not obc_str:
        return None

    # 前後の空白を削除（" 11:46 " → "11:46"）
    obc_str = obc_str.strip()

    try:
        # ":"で分割（例："11:46:30" → ["11", "46", "30"]）
        parts = obc_str.split(":")

        # ------------------------------
        # パターン1：時・分・秒あり（hh:mm:ss）
        # ------------------------------
        if len(parts) == 3:
            h, m, s = parts

        # ------------------------------
        # パターン2：時・分のみ（hh:mm）
        # → 秒が無いので0として扱う
        # ------------------------------
        elif len(parts) == 2:
            h, m = parts
            s = 0   # 秒を0秒として補完

        # ------------------------------
        # 想定外フォーマット（例："11" など）
        # ------------------------------
        else:
            return None

        # ------------------------------
        # 時間 → 秒に変換
        # h：時間 → 秒に変換（×3600）
        # m：分 → 秒に変換（×60）
        # s：秒
        # ------------------------------
        return float(h) * 3600 + float(m) * 60 + float(s)

    except Exception as e:
        # 数値変換などでエラーが出た場合
        print("[OBC ERROR]", obc_str, e)
        return None


# OBC → UTC変換関数
def convert_obc_to_utc(obc_str, obc_time_sample, utc_time_sample):

    base_utc_dt = parse_base_time(utc_time_sample)
    if base_utc_dt is None:
        return None

    try:
        # CSV → 累積秒
        obc_sec = obc_to_seconds(obc_str)

        # sample（累積秒）
        base_obc_sec = obc_to_seconds(obc_time_sample)

        # Noneが入っていたら計算できないため, 結果をNoneで出力する 
        if obc_sec is None or base_obc_sec is None:
            return None
        
        #デバッグ
        #print("obc_str:", obc_str)
        #print("obc_sec:", obc_sec)
        #print("base_obc_sec:", base_obc_sec)

        # 差分
        diff_sec = obc_sec - base_obc_sec

        # UTC反映
        utc_dt = base_utc_dt + timedelta(seconds=diff_sec)

        return utc_dt.strftime("%Y/%m/%d %H:%M:%S")

    except:
        return None
#----------------------------------------------------------------------------------------------------------------
# main

# データの抽出とOBC Timeの加工を行う
def process_csv(file_path, non_float_header, obc_time_sample, utc_time_sample):
    #print("=== ENTER process_csv ===") #デバッグ
    with open(file_path, encoding="utf-8") as f:
        reader = list(csv.reader(f)) # 一旦すべて読み込み

        # --------------------------------------------------
        # ヘッダーとデータを分離
        header = reader[0]
        data_rows = reader[1:]

        columns = header
        
        # 列名 → index の辞書を作成
        col_index = {
            org.normalize(col): i for i, col in enumerate(header)
        }
        
        # OBC Timeが小さい順にソート
        def get_obc(row):
            idx = col_index.get(org.normalize("OBC Time"))

            if idx is not None and idx < len(row):
                raw_obc = row[idx]
            else:
                raw_obc = None

            converted = obc_to_seconds((raw_obc or "").strip())

            #print("RAW:", raw_obc, "→", converted)

            return converted

        data_rows.sort(key=lambda row: get_obc(row) or float("inf"))

        extracted_data = {} # データ抽出後の格納用リストの初期化
        seen_obc = set() # 同じOBC Timeのデータを一つのみ使用するための工夫

        for row in data_rows:
            # OBC Timeが重複するものを削除 (秒単位で判断)
            obc_value = get_obc(row)

            # 不正データのスキップ
            if obc_value is None:
                continue
            # 重複削除
            if obc_value in seen_obc:
                continue
            seen_obc.add(obc_value)

            # 抽出してデータを格納
            for col in columns:

                idx = col_index.get(org.normalize(col))

                # 値取得（列ズレ対策あり）
                if idx is None or idx >= len(row):
                    v = ""
                else:
                    v = (row[idx] or "").strip()

                # キーを初期化
                if col not in extracted_data:
                    extracted_data[col] = []

                if col in non_float_header:
                    extracted_data[col].append(v)
                else:
                    try:
                        extracted_data[col].append(float(v))
                    except:
                        extracted_data[col].append(0)

        #print("=== BEFORE UTC BLOCK ===") #デバッグ
        #print("OBC Time count:", len(extracted_data.get("OBC Time", []))) #デバッグ

        # UTC変換
        utc_list = []

        # デバッグ用
        #print("utc_time_sample:", utc_time_sample)
        #print("parsed UTC:", parse_base_time(utc_time_sample))
        #print("obc_time_sample:", obc_time_sample)
        #print("converted:", obc_to_seconds(obc_time_sample))

        for t in extracted_data.get("OBC Time", []):
            utc_list.append(
                convert_obc_to_utc(t, obc_time_sample, utc_time_sample)
            )

        org.dict_append("UTC Time", utc_list, extracted_data)
   
    # デバッグ
    #print("=== merged_list keys ===")
    #for k in extracted_data.keys():
        #print(k)

    return extracted_data
