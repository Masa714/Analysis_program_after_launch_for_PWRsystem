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