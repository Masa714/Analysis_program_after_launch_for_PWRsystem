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

    # 3. csvファイルに出力
    
    # PWR系
    # 発電関係のcsvファイル出力
    output.csv_output(HK_able.Gene_name_1U,HK_able.columns_gene, extracted_list)
    # バッテリー関係のcsvファイル出力
    output.csv_output(HK_able.BAT_name_1U, HK_able.columns_BAT, extracted_list)
    # 電力収支関係のcsvファイル出力
    output.csv_output(HK_able.budget_name_1U, HK_able.columns_budget, extracted_list)
    #----------------------------------------------------------------------------
