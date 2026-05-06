"""
date: 2026/05/04
author: ikuta
this file for power budget
"""

#------------------------------------------------------------------
# import
import src.common.utils.organizing_datalist as org
#------------------------------------------------------------------
# function

# 1. バスでの電力消費を計算する関数
def bus_consumption_calc(curs_bus, vols_bus):
    mW_bus = curs_bus * vols_bus
    # 辞書で返す（ヘッダー付き）
    return {
        "Bus_consumption":mW_bus
    }

# 2. 電力収支の合計を計算する関数
def budget_check(SAP_gene, battery_charge, bus_consume):
    # 理想は０　(発電量 = 充電 + バス消費) 
    budget_total = SAP_gene - battery_charge - bus_consume
    return{
           "budget_check":budget_total        
    }
#------------------------------------------------------------------------------
# main

# 電力収支関連の計算を行い, 結果を全てリストに格納する
def Budget_result(extracted_list):
    
    #------------------------------------------------
    # 1.の関数
    # 値格納用のリストの作成
    budget_list = []

    # バス消費電力の計算
    for curs_bus, vols_bus in zip(
        extracted_list["curs_bus"],
        extracted_list["vols_bus"]
    ):
    
        result = bus_consumption_calc(
            curs_bus, vols_bus
        )
    
        # リストに値を格納
        budget_list.append(result["Bus_consumption"])

    # extracted_listに列を追加 (ここでこれやっとかないと, 2.の計算ができない)
    org.dict_append("Bus_consumption", budget_list, extracted_list)
    #----------------------------------------------------------
    # 2.の関数
    # 値格納用のリストの作成
    check_list = []

    # 収支のチェック
    for SAP_generation_total, Battery_charge, Bus_consumption in zip(
        extracted_list["SAP_generation_total"],
        extracted_list["Battery_charge"],
        extracted_list["Bus_consumption"]
    ):
    
        result = budget_check(
            SAP_generation_total, Battery_charge, Bus_consumption
        )
    
        # リストに値を格納
        check_list.append(result["budget_check"])
    #-------------------------------------------------------------------
    # extracted_listに列を追加
    org.dict_append("budget_check", check_list, extracted_list)
    return extracted_list

