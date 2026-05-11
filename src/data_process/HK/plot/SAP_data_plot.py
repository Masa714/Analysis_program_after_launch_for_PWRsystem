"""
date: 2026/05/04
author: ikuta
this file for data plot related to SAP
"""

#--------------------------------------------
# import 
import src.utils.plot_functions as pf
import src.settings_init.HK.plot_HK as plt_HK
import pandas as pd
#--------------------------------------------
# function

# 1. SAP各面の発電量の時刻歴をプロットする関数 (全ての面の合計発電量の時刻歴は, 電力収支の方で合わせてプロット)
def eath_SAP_power_plot(extracted_list):
    
    pf.plot_from_dict(
    extracted_list,
    "UTC Time",                # x軸にするキー
    ["pwr_sap_px", "pwr_sap_py", "pwr_sap_pz", "pwr_sap_mx", "pwr_sap_my"],          # y軸にするキー
    graph_title = plt_HK.title_eath_sap, # タイトル
    legend_loc = "upper left", # 凡例位置（外に出す前提に変更）
    # グラフの色設定
    colors = [plt_HK.color_1, plt_HK.color_2, plt_HK.color_3, plt_HK.color_4, plt_HK.color_5],

    x_label=plt_HK.time_label, # x軸ラベル
    y_label=plt_HK.power_label, # y軸ラベル

    x_tick_interval=plt_HK.time_tick_interval, # x軸の目盛り間隔
    y_tick_interval=plt_HK.y1_tick_interval, # y軸の目盛り間隔
    x_range=plt_HK.x1_range, # x軸のグラフ範囲
    y_range=plt_HK.y1_range, # y軸のグラフ範囲

    # 抽出条件：一番古いデータから～分後までのデータ
    condition = lambda df, _: (
            (df["UTC Time"] <= df["UTC Time"].min() + pd.Timedelta(minutes=plt_HK.plot_timerange)) 
    )    
    )
    
# 2. I-V曲線プロットする関数 (各面で一つずつプロットしたほうが見やすい)
def IV_plot(extracted_list):
    
    #px面
    pf.plot_from_dict(
    extracted_list,
    "vols_sap1",                # x軸にするキー
    "curs_sap1_px",          # y軸にするキー
    graph_title = plt_HK.title_IV_px, # タイトル
    legend_loc = "upper left", # 凡例位置（外に出す前提に変更）
    # グラフの色設定
    colors =plt_HK.color_1,

    x_label=plt_HK.vols_label, # x軸ラベル
    y_label=plt_HK.curs_label, # y軸ラベル

    x_tick_interval=plt_HK.x1_tick_interval, # x軸の目盛り間隔
    y_tick_interval=plt_HK.y1_tick_interval, # y軸の目盛り間隔
    x_range=plt_HK.x1_range, # x軸のグラフ範囲
    y_range=plt_HK.y1_range, # y軸のグラフ範囲

    # 抽出条件：一番古いデータから～分後までのデータ & 太陽ベクトルが0.8以上 (ほぼ正面から日射) & 電圧4V以上
    condition = lambda df, _: (
        (df["UTC Time"] <= df["UTC Time"].min() + pd.Timedelta(minutes=plt_HK.plot_timerange)) 
        &(df["sunx"] >= 0.8)
        &(df["vols_sap1"] >= 4)
    )
    )

    #py面
    pf.plot_from_dict(
    extracted_list,
    "vols_sap1",                # x軸にするキー
    "curs_sap1_py",          # y軸にするキー
    graph_title = plt_HK.title_IV_py, # タイトル
    legend_loc = "upper left", # 凡例位置（外に出す前提に変更）
    # グラフの色設定
    colors =plt_HK.color_1,

    x_label=plt_HK.vols_label, # x軸ラベル
    y_label=plt_HK.curs_label, # y軸ラベル

    x_tick_interval=plt_HK.x1_tick_interval, # x軸の目盛り間隔
    y_tick_interval=plt_HK.y1_tick_interval, # y軸の目盛り間隔
    x_range=plt_HK.x1_range, # x軸のグラフ範囲
    y_range=plt_HK.y1_range, # y軸のグラフ範囲

    # 抽出条件：一番古いデータから～分後までのデータ & 太陽ベクトルが0.8以上 (ほぼ正面から日射) & 電圧4V以上
    condition = lambda df, _: (
        (df["UTC Time"] <= df["UTC Time"].min() + pd.Timedelta(minutes=plt_HK.plot_timerange)) 
        &(df["suny"] >= 0.8)
        &(df["vols_sap1"] >= 4)
    )
    )

    #pz面
    pf.plot_from_dict(
    extracted_list,
    "vols_sap1",                # x軸にするキー
    "curs_sap1_pz",          # y軸にするキー
    graph_title = plt_HK.title_IV_pz, # タイトル
    legend_loc = "upper left", # 凡例位置（外に出す前提に変更）
    # グラフの色設定
    colors =plt_HK.color_1,

    x_label=plt_HK.vols_label, # x軸ラベル
    y_label=plt_HK.curs_label, # y軸ラベル

    x_tick_interval=plt_HK.x1_tick_interval, # x軸の目盛り間隔
    y_tick_interval=plt_HK.y1_tick_interval, # y軸の目盛り間隔
    x_range=plt_HK.x1_range, # x軸のグラフ範囲
    y_range=plt_HK.y1_range, # y軸のグラフ範囲

    # 抽出条件：一番古いデータから～分後までのデータ & 太陽ベクトルが0.8以上 (ほぼ正面から日射) & 電圧4V以上
    condition = lambda df, _: (
        (df["UTC Time"] <= df["UTC Time"].min() + pd.Timedelta(minutes=plt_HK.plot_timerange)) 
        &(df["sunz"] >= 0.8)
        &(df["vols_sap1"] >= 4)
    )
    )

    #mx面
    pf.plot_from_dict(
    extracted_list,
    "vols_sap2",                # x軸にするキー
    "curs_sap2_mx",          # y軸にするキー
    graph_title = plt_HK.title_IV_mx, # タイトル
    legend_loc = "upper left", # 凡例位置（外に出す前提に変更）
    # グラフの色設定
    colors =plt_HK.color_1,

    x_label=plt_HK.vols_label, # x軸ラベル
    y_label=plt_HK.curs_label, # y軸ラベル

    x_tick_interval=plt_HK.x1_tick_interval, # x軸の目盛り間隔
    y_tick_interval=plt_HK.y1_tick_interval, # y軸の目盛り間隔
    x_range=plt_HK.x1_range, # x軸のグラフ範囲
    y_range=plt_HK.y1_range, # y軸のグラフ範囲

    # 抽出条件：一番古いデータから～分後までのデータ & 太陽ベクトルが-0.8以下 (ほぼ正面から日射) & 電圧4V以上
    condition = lambda df, _: (
        (df["UTC Time"] <= df["UTC Time"].min() + pd.Timedelta(minutes=plt_HK.plot_timerange)) 
        &(df["sunx"] <= -0.8)
        &(df["vols_sap2"] >= 4)
    )
    )

    #my面
    pf.plot_from_dict(
    extracted_list,
    "vols_sap2",                # x軸にするキー
    "curs_sap2_my",          # y軸にするキー
    graph_title = plt_HK.title_IV_my, # タイトル
    legend_loc = "upper left", # 凡例位置（外に出す前提に変更）
    # グラフの色設定
    colors =plt_HK.color_1,

    x_label=plt_HK.vols_label, # x軸ラベル
    y_label=plt_HK.curs_label, # y軸ラベル

    x_tick_interval=plt_HK.x1_tick_interval, # x軸の目盛り間隔
    y_tick_interval=plt_HK.y1_tick_interval, # y軸の目盛り間隔
    x_range=plt_HK.x1_range, # x軸のグラフ範囲
    y_range=plt_HK.y1_range, # y軸のグラフ範囲

    # 抽出条件：一番古いデータから～分後までのデータ & 太陽ベクトルが-0.8以下 (ほぼ正面から日射) & 電圧4V以上
    condition = lambda df, _: (
        (df["UTC Time"] <= df["UTC Time"].min() + pd.Timedelta(minutes=plt_HK.plot_timerange)) 
        &(df["suny"] <= -0.8)
        &(df["vols_sap2"] >= 4)
    )
    )

# 3. P-V曲線プロットする関数 (各面で一つずつプロットしたほうが見やすい)
def PV_plot(extracted_list):

    #px面
    pf.plot_from_dict(
    extracted_list,
    "vols_sap1",                # x軸にするキー
    "pwr_sap_px",          # y軸にするキー
    graph_title = plt_HK.title_PV_px, # タイトル
    legend_loc = "upper left", # 凡例位置（外に出す前提に変更）
    # グラフの色設定
    colors =plt_HK.color_1,

    x_label=plt_HK.vols_label, # x軸ラベル
    y_label=plt_HK.power_label, # y軸ラベル

    x_tick_interval=plt_HK.x1_tick_interval, # x軸の目盛り間隔
    y_tick_interval=plt_HK.y1_tick_interval, # y軸の目盛り間隔
    x_range=plt_HK.x1_range, # x軸のグラフ範囲
    y_range=plt_HK.y1_range, # y軸のグラフ範囲

    # 抽出条件：一番古いデータから～分後までのデータ & 太陽ベクトルが0.8以上 (ほぼ正面から日射) &電圧4V以上
    condition = lambda df, _: (
        (df["UTC Time"] <= df["UTC Time"].min() + pd.Timedelta(minutes=plt_HK.plot_timerange)) 
        &(df["sunx"] >= 0.8)
        &(df["vols_sap1"] >= 4)
    )
    )

    #py面
    pf.plot_from_dict(
    extracted_list,
    "vols_sap1",                # x軸にするキー
    "pwr_sap_py",          # y軸にするキー
    graph_title = plt_HK.title_PV_py, # タイトル
    legend_loc = "upper left", # 凡例位置（外に出す前提に変更）
    # グラフの色設定
    colors =plt_HK.color_1,

    x_label=plt_HK.vols_label, # x軸ラベル
    y_label=plt_HK.power_label, # y軸ラベル

    x_tick_interval=plt_HK.x1_tick_interval, # x軸の目盛り間隔
    y_tick_interval=plt_HK.y1_tick_interval, # y軸の目盛り間隔
    x_range=plt_HK.x1_range, # x軸のグラフ範囲
    y_range=plt_HK.y1_range, # y軸のグラフ範囲

    # 抽出条件：一番古いデータから～分後までのデータ & 太陽ベクトルが0.8以上 (ほぼ正面から日射) & 電圧4V以上
    condition = lambda df, _: (
        (df["UTC Time"] <= df["UTC Time"].min() + pd.Timedelta(minutes=plt_HK.plot_timerange)) 
        &(df["suny"] >= 0.8)
        &(df["vols_sap1"] >= 4)
    )
    )

    #pz面
    pf.plot_from_dict(
    extracted_list,
    "vols_sap1",                # x軸にするキー
    "pwr_sap_pz",          # y軸にするキー
    graph_title = plt_HK.title_PV_pz, # タイトル
    legend_loc = "upper left", # 凡例位置（外に出す前提に変更）
    # グラフの色設定
    colors =plt_HK.color_1,

    x_label=plt_HK.vols_label, # x軸ラベル
    y_label=plt_HK.power_label, # y軸ラベル

    x_tick_interval=plt_HK.x1_tick_interval, # x軸の目盛り間隔
    y_tick_interval=plt_HK.y1_tick_interval, # y軸の目盛り間隔
    x_range=plt_HK.x1_range, # x軸のグラフ範囲
    y_range=plt_HK.y1_range, # y軸のグラフ範囲

    # 抽出条件：一番古いデータから～分後までのデータ & 太陽ベクトルが0.8以上 (ほぼ正面から日射) & 電圧4V以上
    condition = lambda df, _: (
        (df["UTC Time"] <= df["UTC Time"].min() + pd.Timedelta(minutes=plt_HK.plot_timerange)) 
        &(df["sunz"] >= 0.8)
        &(df["vols_sap1"] >= 4)
    )
    )

    #mx面
    pf.plot_from_dict(
    extracted_list,
    "vols_sap2",                # x軸にするキー
    "pwr_sap_mx",          # y軸にするキー
    graph_title = plt_HK.title_PV_mx, # タイトル
    legend_loc = "upper left", # 凡例位置（外に出す前提に変更）
    # グラフの色設定
    colors =plt_HK.color_1,

    x_label=plt_HK.vols_label, # x軸ラベル
    y_label=plt_HK.power_label, # y軸ラベル

    x_tick_interval=plt_HK.x1_tick_interval, # x軸の目盛り間隔
    y_tick_interval=plt_HK.y1_tick_interval, # y軸の目盛り間隔
    x_range=plt_HK.x1_range, # x軸のグラフ範囲
    y_range=plt_HK.y1_range, # y軸のグラフ範囲

    # 抽出条件：一番古いデータから～分後までのデータ & 太陽ベクトルが-0.8以下 (ほぼ正面から日射) & 電圧4V以上
    condition = lambda df, _: (
        (df["UTC Time"] <= df["UTC Time"].min() + pd.Timedelta(minutes=plt_HK.plot_timerange)) 
        &(df["sunx"] <= -0.8)
        &(df["vols_sap2"] >= 4)
    )
    )

    #my面
    pf.plot_from_dict(
    extracted_list,
    "vols_sap2",                # x軸にするキー
    "pwr_sap_my",          # y軸にするキー
    graph_title = plt_HK.title_PV_my, # タイトル
    legend_loc = "upper left", # 凡例位置（外に出す前提に変更）
    # グラフの色設定
    colors =plt_HK.color_1,

    x_label=plt_HK.vols_label, # x軸ラベル
    y_label=plt_HK.power_label, # y軸ラベル

    x_tick_interval=plt_HK.x1_tick_interval, # x軸の目盛り間隔
    y_tick_interval=plt_HK.y1_tick_interval, # y軸の目盛り間隔
    x_range=plt_HK.x1_range, # x軸のグラフ範囲
    y_range=plt_HK.y1_range, # y軸のグラフ範囲

    # 抽出条件：一番古いデータから～分後までのデータ & 太陽ベクトルが0.8以下 (ほぼ正面から日射) & 電圧4V以上
    condition = lambda df, _: (
        (df["UTC Time"] <= df["UTC Time"].min() + pd.Timedelta(minutes=plt_HK.plot_timerange)) 
        &(df["suny"] <= -0.8)
        &(df["vols_sap2"] >= 4)
    )
    )

# 4. 太陽ベクトルの時刻歴をプロットする関数
def sun_vec_plot(extracted_list):

    pf.plot_from_dict(
    extracted_list,
    "UTC Time",                # x軸にするキー
    ["sunx", "suny", "sunz"],        # y軸にするキー
    graph_title = plt_HK.title_suns, # タイトル
    legend_loc = "upper left", # 凡例位置（外に出す前提に変更）
    # グラフの色設定
    colors = [plt_HK.color_1, plt_HK.color_2, plt_HK.color_3],

    x_label=plt_HK.time_label, # x軸ラベル
    y_label=plt_HK.vec_label, # y軸ラベル

    x_tick_interval=plt_HK.time_tick_interval, # x軸の目盛り間隔
    y_tick_interval=plt_HK.y1_tick_interval, # y軸の目盛り間隔
    x_range=plt_HK.x1_range, # x軸のグラフ範囲
    y_range=plt_HK.y1_range, # y軸のグラフ範囲

 # 抽出条件：一番古いデータから～分後までのデータ  
    condition = lambda df, _: (
        (df["UTC Time"] <= df["UTC Time"].min() + pd.Timedelta(minutes=plt_HK.plot_timerange)) 
    )
    )

# 5. 太陽ベクトル(横軸)と温度, 発電量の相関をプロットする関数
def paneltemp_power_sap_plot(extracted_list):

    # 太陽ベクトルx成分を横軸
    pf.plot_dual_axis(
        extracted_list,
        "sunx",
        ["temp_strpx", "temp_strmx"],
        ["pwr_sap_px","pwr_sap_mx"],
        graph_title=plt_HK.title_temp_power_vs_sunvecx,
        
        left_colors=[plt_HK.color_1, plt_HK.color_2],
        right_colors=[plt_HK.color_1, plt_HK.color_2],

        x_label=None,
        y_left_label=plt_HK.temp_label,
        y_right_label=plt_HK.power_label,

        # 目盛
        x_tick_interval=plt_HK.x1_tick_interval,
        
         # 抽出条件：一番古いデータから～分後までのデータ & 電圧が4V以上  
        condition = lambda df, _: (
            (df["UTC Time"] <= df["UTC Time"].min() + pd.Timedelta(minutes=plt_HK.plot_timerange)) 
            &(df["vols_sap1"] >= 4)
    )
    )

    # 太陽ベクトルy成分を横軸
    pf.plot_dual_axis(
        extracted_list,
        "suny",
        ["temp_strpy", "temp_strmy"],
        ["pwr_sap_py", "pwr_sap_my"],
        graph_title=plt_HK.title_temp_power_vs_sunvecy,

        left_colors=[plt_HK.color_1, plt_HK.color_2],
        right_colors=[plt_HK.color_1, plt_HK.color_2],

        x_label=None,
        y_left_label=plt_HK.temp_label,
        y_right_label=plt_HK.power_label,

        # 目盛
        x_tick_interval=plt_HK.x1_tick_interval,
      
        # 抽出条件：一番古いデータから～分後までのデータ & 電圧が4V以上  
        condition = lambda df, _: (
            (df["UTC Time"] <= df["UTC Time"].min() + pd.Timedelta(minutes=plt_HK.plot_timerange)) 
            &(df["vols_sap1"] >= 4)
    )
    )

    # 太陽ベクトルz成分を横軸
    pf.plot_dual_axis(
        extracted_list,
        "sunz",
        ["temp_strpz", "temp_strmz"],
        ["pwr_sap_pz"],
        graph_title=plt_HK.title_temp_power_vs_sunvecz,

        left_colors=[plt_HK.color_1, plt_HK.color_2],
        right_colors=[plt_HK.color_1],

        x_label=None,
        y_left_label=plt_HK.temp_label,
        y_right_label=plt_HK.power_label,

        # 目盛
        x_tick_interval=plt_HK.x1_tick_interval,

        # 抽出条件：一番古いデータから～分後までのデータ & 電圧が4V以上  
        condition = lambda df, _: (
            (df["UTC Time"] <= df["UTC Time"].min() + pd.Timedelta(minutes=plt_HK.plot_timerange)) 
            &(df["vols_sap1"] >= 4)
    )
    )
    
#-----------------------------------------------------------
# main 

# 太陽電池関係のグラフをまとめて出力する関数
def sap_plot(extracted_list):

    # 1. 各面発電量の時刻歴プロット
    eath_SAP_power_plot(extracted_list)
    # 2. I-V曲線プロット
    IV_plot(extracted_list)
    # 3. P-V曲線プロット
    PV_plot(extracted_list)
    # 4. 太陽ベクトルの時刻歴
    sun_vec_plot(extracted_list)
    # 5. 温度, 各面発電量と太陽ベクトルの相関
    paneltemp_power_sap_plot(extracted_list)
