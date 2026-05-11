"""
create date: 2026/04/23
author: ikuta
content: main (このファイルを実行する)
"""
#------------------------------------------------------------------------------------
#import
from pathlib import Path
import src.sat_1U.main_1U as main_1U
import src.sat_2U.main_2U as main_2U
import src.utils.csv_processor.extract_process_from_Input_csv as input
import src.settings_init.common_valiables as com_val
#------------------------------------------------------------------------------------
# main

# 生データの入っているcsvファイルのフォルダパスを参照
data_dir = Path(__file__).resolve().parent/"data"/"Input_csv"
# フォルダが存在しないときにエラーを出す (デバッグ用)
if not data_dir.exists():
   raise FileNotFoundError(f"Output folder not found: {data_dir}")

# inputフォルダに格納されているcsvファイルを参照
for file_path in data_dir.glob("*.csv"):
        
   # ファイルに1Uの文字がある時
   if "1U" in file_path.name:
      main_1U.analysis_1U(file_path) # 1Uのプログラムを実行
   # 2Uの文字がある時
   elif "2U" in file_path.name:
      main_2U.analysis_2U(file_path) # 2Uのプログラムを実行
   else:
      continue



#-----------------------------------------------------------------------------------
# おまけ機能
# 1. 任意のutc時刻をobc_time(秒)に変換する
if com_val.wanna_convert_enable == 1:
        print(f"1U_obctime   {input.convert_given_utc_to_obc(
            com_val.wanna_convert_obc_time_1U,
            com_val.OBC_time_sample_1U,
            com_val.UTC_time_sample_1U
        )}"
        )
        print(f"2U_obctime   {input.convert_given_utc_to_obc(
            com_val.wanna_convert_obc_time_2U,
            com_val.OBC_time_sample_2U,
            com_val.UTC_time_sample_2U
        )}"
        )
