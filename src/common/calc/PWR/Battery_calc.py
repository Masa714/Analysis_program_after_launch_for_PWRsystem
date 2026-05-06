"""
date: 2026/05/04
author: ikuta
this file for battery analysis
"""

#------------------------------------------------------------------
# import
import src.common.utils.organizing_datalist as org
#------------------------------------------------------------------
# function

# 1. バッテリーの充電電力を計算する関数
def battery_charge_calc(curs_2ndbat, vols_2ndbat):
    # 充電が+, 放電は-になる
    Charging_mW_2ndbat = curs_2ndbat * vols_2ndbat
    # 辞書で返す（ヘッダー付き）
    return {
        "Battery_charge":Charging_mW_2ndbat
    }

#----------------------------------------------------------------
# main

# バッテリー関連の計算を行い, 結果を全てリストに格納する
def BAT_calc_result(extracted_list):
    
    #------------------------------------------------
    # 1.の関数
    # 値格納用のリストの作成
    charging_list = []

    # バッテリー充電電力の計算
    for curs_2ndbat, vols_2ndbat in zip(
        extracted_list["curs_2ndbat"],
        extracted_list["vols_2ndbat"]
    ):
    
        result = battery_charge_calc(
            curs_2ndbat, vols_2ndbat
        )
    
        # リストに値を格納
        charging_list.append(result["Battery_charge"])
    #----------------------------------------------------------
    
    # extracted_listに列を追加
    org.dict_append("Battery_charge", charging_list, extracted_list)
    return extracted_list
