"""
create date: 2026/04/23
author: ikuta
content: main_2U
"""

#------------------------------------------------------
# import  
import src.settings_init.HK.header_HK as head_HK
import src.settings_init.HK.output_file_name_HK as out_HK
import src.settings_init.common_valiables as com_val
import src.utils.csv_processor.extract_process_from_Input_csv as input
import src.utils.csv_processor.output_process as output
import src.data_process.HK.calc.PWR.Battery_calc as bc
import src.data_process.HK.calc.PWR.Power_budget_calc as bud
import src.data_process.HK.calc.PWR.Power_Generation_calc as PG
import src.data_process.HK.plot.SAP_data_plot as SP
#------------------------------------------------------
# main

def analysis_2U(file_path):
    
    #-----------------------------------------------------------------------------------
    # HKデータ解析
    if com_val.HK_analysis_enable == 1 and "HK" in file_path.name:
        # 1. inputのcsvファイルから必要なデータを抽出し, データ取得時のUTC時刻も加えたリストを作成
        extracted_list = input.process_csv(file_path,  # input_csvファイル名
                                        head_HK.non_float_header,  # float変換しないデータ
                                        com_val.OBC_time_sample_2U, # obc timeの例
                                        com_val.UTC_time_sample_2U  # utc timeの例
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
        # HKのcsv出力 (UTC_TIMEなどを追加)
        output.reorder_and_insert_utc_then_export(out_HK.HKname_2U, extracted_list)
        # SAP関係のcsvファイル出力
        output.csv_output(out_HK.Gene_name_2U, head_HK.columns_gene, extracted_list)
        # バッテリー関係のcsvファイル出力
        output.csv_output(out_HK.BAT_name_2U, head_HK.columns_BAT, extracted_list)
        # 電力収支関係のcsvファイル出力
        output.csv_output(out_HK.budget_name_2U, head_HK.columns_budget, extracted_list)

        # 4. plot
        # PWR系
        SP.sap_plot(extracted_list)
    
    #-----------------------------------------------------------------------------------
    # AOCSデータ解析
    if com_val.AOCS_analysis_enable == 1:
    # 1. inputのcsvファイルから必要なデータを抽出し, データ取得時のUTC時刻も加えたリストを作成
        extracted_list = input.process_csv(file_path,  # input_csvファイル名
                                        head_HK.non_float_header,  # float変換しないデータ
                                        com_val.OBC_time_sample_2U, # obc timeの例
                                        com_val.UTC_time_sample_2U  # utc timeの例
                                        )



