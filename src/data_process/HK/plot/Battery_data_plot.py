"""
create date: 2026/05/18
author: ikuta
content: this file for battery plot
"""

#-------------------------------------
# import
import src.settings_init.HK.plot_HK as plt_HK
import pandas as pd
import src.utils.plot_functions as pf
#-------------------------------------
#-------------------------------------
# functions

# 1. バッテリー電圧電流の時刻歴を表示する関数
def battery_voltage_timestamp(extracted_list):

    pf.plot_dual_axis(
        extracted_list,
        "UTC Time",
        ["vols_2ndbat"],
        ["curs_2ndbat"],
        graph_title=plt_HK.title_BAT_vols_and_curs_2bat,
        
        left_colors=[plt_HK.color_1],
        right_colors=[plt_HK.color_2],

        x_label=plt_HK.time_label,
        y_left_label=plt_HK.vols_label,
        y_right_label=plt_HK.curs_label,

        # 目盛
        x_tick_interval=plt_HK.time_tick_interval,
        
        enable_fit=plt_HK.plot_style, # プロットの種類
        fitting_lebel=plt_HK.fitting_lebel, # 外挿曲線のフィッティングの緩さ
        
        # 抽出条件：一番古いデータから～分後までのデータ 
        time_condition = lambda df, _: (
            df["UTC Time"] <= df["UTC Time"].min() + pd.Timedelta(minutes=plt_HK.plot_timerange)
        ),

        apply_time_condition=plt_HK.enable_timerange
    )

# 2. バッテリー温度とバッテリー消費電力・電流の関係を表示する関数
def battery_temp_consume_coleration(extracted_list):
    # 消費電力と温度の関係
    pf.plot_from_dict(
        extracted_list,
        "Battery_charge",                # x軸にするキー
        ["temp_2ndbat1", "temp_2ndbat2", "temp_2ndbat3", "temp_2ndbat4"],        # y軸にするキー
        graph_title = plt_HK.title_BAT_pwr_and_temp, # タイトル
        legend_loc = "upper left", # 凡例位置（外に出す前提に変更）
        # グラフの色設定
        colors = [plt_HK.color_1, plt_HK.color_2, plt_HK.color_3, plt_HK.color_4],

        x_label=plt_HK.power_label, # x軸ラベル
        y_label=plt_HK.temp_label, # y軸ラベル

        x_tick_interval=plt_HK.x1_tick_interval, # x軸の目盛り間隔
        y_tick_interval=plt_HK.y1_tick_interval, # y軸の目盛り間隔
        x_range=plt_HK.x1_range, # x軸のグラフ範囲
        y_range=plt_HK.y1_range, # y軸のグラフ範囲

        enable_fit=plt_HK.plot_style, # プロットの種類
        fitting_lebel=plt_HK.fitting_lebel, # 外挿曲線のフィッティングの緩さ
        
        # 抽出条件：一番古いデータから～分後までのデータ  
        time_condition = lambda df, _: (
            (df["UTC Time"] <= df["UTC Time"].min() + pd.Timedelta(minutes=plt_HK.plot_timerange)) 
        ),

        apply_time_condition=plt_HK.enable_timerange
    )

    # 電流と温度の関係
    pf.plot_from_dict(
        extracted_list,
        "curs_2ndbat",                # x軸にするキー
        ["temp_2ndbat1", "temp_2ndbat2", "temp_2ndbat3", "temp_2ndbat4"],        # y軸にするキー
        graph_title = plt_HK.title_BAT_curs_and_temp, # タイトル
        legend_loc = "upper left", # 凡例位置（外に出す前提に変更）
        # グラフの色設定
        colors = [plt_HK.color_1, plt_HK.color_2, plt_HK.color_3, plt_HK.color_4],

        x_label=plt_HK.curs_label, # x軸ラベル
        y_label=plt_HK.temp_label, # y軸ラベル

        x_tick_interval=plt_HK.x1_tick_interval, # x軸の目盛り間隔
        y_tick_interval=plt_HK.y1_tick_interval, # y軸の目盛り間隔
        x_range=plt_HK.x1_range, # x軸のグラフ範囲
        y_range=plt_HK.y1_range, # y軸のグラフ範囲

        enable_fit=plt_HK.plot_style, # プロットの種類
        fitting_lebel=plt_HK.fitting_lebel, # 外挿曲線のフィッティングの緩さ
        
        # 抽出条件：一番古いデータから～分後までのデータ  
        time_condition = lambda df, _: (
            (df["UTC Time"] <= df["UTC Time"].min() + pd.Timedelta(minutes=plt_HK.plot_timerange)) 
        ),

        apply_time_condition=plt_HK.enable_timerange
    )

# 3. パネル温度とバッテリー温度の時刻歴を表示する関数
def battery_panel_temp_timestamp(extracted_list):
    # バッテリー温度
    pf.plot_from_dict(
        extracted_list,
        "UTC Time",                # x軸にするキー
        ["temp_2ndbat1", "temp_2ndbat2", "temp_2ndbat3", "temp_2ndbat4"],  # y軸にするキー
        graph_title = plt_HK.title_BAT_temp_timestamp, # タイトル
        legend_loc = "upper left", # 凡例位置（外に出す前提に変更）
        # グラフの色設定
        colors = [plt_HK.color_1, plt_HK.color_2, plt_HK.color_3, plt_HK.color_4],

        x_label=plt_HK.time_label, # x軸ラベル
        y_label=plt_HK.temp_label, # y軸ラベル

        x_tick_interval=plt_HK.time_tick_interval, # x軸の目盛り間隔
        y_tick_interval=plt_HK.y1_tick_interval, # y軸の目盛り間隔
        x_range=plt_HK.x1_range, # x軸のグラフ範囲
        y_range=plt_HK.y1_range, # y軸のグラフ範囲

        enable_fit=plt_HK.plot_style, # プロットの種類
        fitting_lebel=plt_HK.fitting_lebel, # 外挿曲線のフィッティングの緩さ
        
        # 抽出条件：一番古いデータから～分後までのデータ  
        time_condition = lambda df, _: (
            (df["UTC Time"] <= df["UTC Time"].min() + pd.Timedelta(minutes=plt_HK.plot_timerange)) 
        ), 

        apply_time_condition=plt_HK.enable_timerange
    )

    # パネル温度
    pf.plot_from_dict(
        extracted_list,
        "UTC Time",                # x軸にするキー
        ["temp_strmx", "temp_strmy", "temp_strmz", "temp_strpx", "temp_strpy", "temp_strpz"], # y軸にするキー
        graph_title = plt_HK.title_panel_temp_timestamp, # タイトル
        legend_loc = "upper left", # 凡例位置（外に出す前提に変更）
        # グラフの色設定
        colors = [plt_HK.color_1, plt_HK.color_2, plt_HK.color_3, plt_HK.color_4, plt_HK.color_5, plt_HK.color_6],

        x_label=plt_HK.time_label, # x軸ラベル
        y_label=plt_HK.temp_label, # y軸ラベル

        x_tick_interval=plt_HK.time_tick_interval, # x軸の目盛り間隔
        y_tick_interval=plt_HK.y1_tick_interval, # y軸の目盛り間隔
        x_range=plt_HK.x1_range, # x軸のグラフ範囲
        y_range=plt_HK.y1_range, # y軸のグラフ範囲

        enable_fit=plt_HK.plot_style, # プロットの種類
        fitting_lebel=plt_HK.fitting_lebel, # 外挿曲線のフィッティングの緩さ
        
        # 抽出条件：一番古いデータから～分後までのデータ  
        time_condition = lambda df, _: (
            (df["UTC Time"] <= df["UTC Time"].min() + pd.Timedelta(minutes=plt_HK.plot_timerange)) 
        ),

        apply_time_condition=plt_HK.enable_timerange
    )

#-------------------------------------
# main

# バッテリーに関するプロットをまとめる関数
def BAT_plot(extracted_list):
    # 1のプロット
    battery_voltage_timestamp(extracted_list)
    # 2のプロット
    battery_temp_consume_coleration(extracted_list)
    # 3のプロット
    battery_panel_temp_timestamp(extracted_list)