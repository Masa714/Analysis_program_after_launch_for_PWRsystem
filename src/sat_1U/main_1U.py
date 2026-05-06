"""
create date: 2026/04/23
author: ikuta
content: main_1U
"""

#------------------------------------------------------
# import  
import src.settings_init.HK_valiables as HK_able
import src.common.Data_processing.extract_process_from_Input_csv as input
import src.common.Data_processing.output_process as output
import src.common.utils.organizing_datalist as org
import src.common.calc.PWR.Power_Generation_calc as PG
import src.common.calc.PWR.battery_calc as bc
import src.common.calc.PWR.Power_budget_calc as bud
#------------------------------------------------------
# main

def analysis_1U(file_path):
    
    #------------------------------------------------------------------------------
    # HKデータ解析

    # 1. inputのcsvファイルから必要なデータを抽出し, データ取得時のUTC時刻も加えたリストを作成
    extracted_list = input.process_csv(file_path,  # input_csvファイルパス
                                       HK_able.columns_ext, # 抽出するデータのヘッダー名
                                       HK_able.non_float_header,  # float変換しないデータ
                                       HK_able.OBC_time_sample_1U, # obc timeの例
                                       HK_able.UTC_time_sample_1U  # utc timeの例
                                       )

    # 2. 抽出したデータから計算・各種データ処理

    # PWR系
    # 〇 SAPでの発電量計算 & 計算結果をリストに格納
    extracted_list = PG.SAP_calc_result(extracted_list)
    # 〇 バッテリーでの発電量計算 & 計算結果をリストに格納
    extracted_list = bc.BAT_calc_result(extracted_list)
    # 〇 電力収支計算 & 計算結果をリストに格納 (これは発電・バッテリー計算結果を格納した後に持ってくること！)
    extracted_list = bud.Budget_result(extracted_list)

    # 3. csvファイルに出力
    
    # PWR系
    # 発電関係のcsvファイル出力
    output.csv_output(HK_able.Gene_name_1U,HK_able.columns_gene, extracted_list)
    # バッテリー関係のcsvファイル出力
    output.csv_output(HK_able.BAT_name_1U, HK_able.columns_BAT, extracted_list)
    # 電力収支関係のcsvファイル出力
    output.csv_output(HK_able.budget_name_1U, HK_able.columns_budget, extracted_list)
    #----------------------------------------------------------------------------
    # AOCS