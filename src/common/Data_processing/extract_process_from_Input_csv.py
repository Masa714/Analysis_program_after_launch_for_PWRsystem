"""
date: 2026/05/04
author: ikuta
this file for extract process from input_csv
"""

#---------------------------------------------------------------------------------
# import

import csv
from datetime import datetime, timedelta
#---------------------------------------------------------------------------------
# 以下はOBC TimeをUTCに変換するための関数群

# OBC Timeをtimedelta型に変換する関数
def parse_obc(obc_str):
    try:
        # 時間, 分, 秒に分割
        h, m, s = obc_str.split(":")
        # timedelta型に変換
        return timedelta(
            hours = int(h),
            minutes = int(m),
            seconds = float(s)
        )
    except:
        return timedelta (0)
    
# OBC → UTC変換関数
def convert_obc_to_utc(obc_str, obc_time_sample, utc_time_sample):
    
    # OBC TimeとUTC(PC Time)の基準設定
    base_obc = obc_time_sample
    base_utc = utc_time_sample
    
    # 時刻の形式設定
    utc_fmt = "%Y/%m/%d %H:%M:%S.%f"
    
    # 基準変換 (timedelta型への変換)
    base_obc_td = parse_obc(base_obc)
    base_utc_dt = datetime.strptime(base_utc, utc_fmt)

    try:
        obc_td = parse_obc(obc_str)

        # 差分（timedelta）
        diff = obc_td - base_obc_td

        # UTCに適用
        utc_dt = base_utc_dt + diff

        return utc_dt.strftime("%H:%M")

    except:
        return "00:00"

#----------------------------------------------------------------------------------------------------------------
# main

# データの抽出とOBC Timeの加工を行う
def process_csv(file_path, columns, non_float_header, obc_time_sample, utc_time_sample):
    with open(file_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)

        extracted_data = {col: [] for col in columns}

        # データの格納
        for row in reader:
            for col in columns:
                v = (row.get(col) or "").strip()

                if col in non_float_header:
                    extracted_data[col].append(v)
                else:
                    try:
                        extracted_data[col].append(float(v))
                    except:
                        extracted_data[col].append(0)

        # UTC時刻の格納
        utc_list = []
        for t in extracted_data["OBC Time"]:
            utc_list.append(convert_obc_to_utc(t, obc_time_sample, utc_time_sample))

        extracted_data["UTC Time"] = utc_list

        return extracted_data
