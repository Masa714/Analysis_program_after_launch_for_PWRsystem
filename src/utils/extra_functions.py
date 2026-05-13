"""
date:2026/05/12
author:ikuta 
this file for extra functions
"""

#-------------------------------------------
# import
import src.settings_init.common_valiables as com_val
import src.utils.csv_processor.extract_process_from_Input_csv as input
#------------------------------------------
# functions
# おまけ機能

# 1. 任意のutc時刻をobc_time(秒)に変換する
def given_utc_to_obc():
    if com_val.wanna_convert_enable == 1:
            obc_1U = input.convert_given_utc_to_obc(
                com_val.wanna_convert_obc_time_1U,
                com_val.OBC_time_sample_1U,
                com_val.UTC_time_sample_1U
            )
            print(f"1U_obctime  {obc_1U}")

            obc_2U =input.convert_given_utc_to_obc(
                com_val.wanna_convert_obc_time_2U,
                com_val.OBC_time_sample_2U,
                com_val.UTC_time_sample_2U
            )
            print(f"2U_obctime  {obc_2U}")

#-------------------------------------------------------------
# main 

# おまけ機能を一度に実行する関数
def extra_functions():
      # 1.の実行
      given_utc_to_obc()
