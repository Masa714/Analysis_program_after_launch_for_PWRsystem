"""
create date: 2026/04/23
author: ikuta
content: main_1U
"""

#------------------------------------------------------
# import  
import src.settings_init.HK_valiables as HK_able
import src.common.Data_processing.extract_process_from_Input_csv as input

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


    #----------------------------------------------------------------------------
