"""
date: 2026/05/04
author: ikuta
this file for data plot related to SAP
"""

#--------------------------------------------
# import 
import src.common.utils.plot_functions as pf
import src.settings_init.HK_valiables as HK_able
import pandas as pd
#--------------------------------------------
# function

# 1. SAP各面の発電量の時刻歴をプロットする関数
def eath_SAP_power_plot(extracted_list):
    
    pf.plot_from_dict(
    extracted_list,
    "UTC Time",                # x軸にするキー
    ["pwr_sap_px", "pwr_sap_py", "pwr_sap_pz", "pwr_sap_mx", "pwr_sap_my"],          # y軸にするキー
    graph_title = HK_able.title_eath_sap, # タイトル
    legend_loc = "upper left", # 凡例位置（外に出す前提に変更）
    # グラフの色設定
    colors = [HK_able.color_1, HK_able.color_2, HK_able.color_3, HK_able.color_4, HK_able.color_5],

    x_label=HK_able.time_label, # x軸ラベル
    y_label=HK_able.power_label, # y軸ラベル

    x_tick_interval=HK_able.x1_tick_interval, # x軸の目盛り間隔
    y_tick_interval=HK_able.y1_tick_interval, # y軸の目盛り間隔
    x_range=HK_able.x1_range, # x軸のグラフ範囲
    y_range=HK_able.y1_range, # y軸のグラフ範囲

    condition=lambda d, x: x <= x[0] + pd.Timedelta(minutes=HK_able.plot_timerange) # 一番古いデータから～分間のデータをプロット
    )
    
#-----------------------------------------------------------
# main 

# 太陽電池関係のグラフをまとめて出力する関数
def sap_plot(extracted_list):
    # 各面発電量の時刻歴プロット
    eath_SAP_power_plot(extracted_list)

