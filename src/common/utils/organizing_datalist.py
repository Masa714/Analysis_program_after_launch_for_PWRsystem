"""
date: 2026/05/04
author: ikuta
this file for organizing data list 
"""

#-----------------------------------------------------
# import
import src.settings_init.HK_valiables as able
import src.common.Data_processing.extract_process_from_Input_csv as input
#-----------------------------------------------------
# functions

# 既存の辞書に指定のヘッダー名で、新しいリストの値を追加する関数
def dict_append(header_str, append_list, dict_list):
    dict_list[header_str] = append_list
    return dict_list

# ヘッダーを正規化する関数
def normalize(col):
    col = col.strip().lower()

    # 単位を削除
    if "[" in col and "]" in col:
        col = col.split("[")[0].strip()

    return col


