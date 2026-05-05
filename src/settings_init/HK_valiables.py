"""
date:2026/04/26
author:ikuta
this file for valiables 
"""

#---------------------------------------------------
# 1. Parameters

orbit_cycle = 6000 # 軌道1周の周期[s]
# 1U
OBC_time_sample_1U = "47:42:01.000" # OBCtimeをUTCに変換する際に使用
UTC_time_sample_1U = "2026/05/04" # OBCtimeをUTCに変換する際に使用 (PC Timeを使用)
# 2U
OBC_time_sample_2U = "228:12:18.000" # OBCtimeをUTCに変換する際に使用
UTC_time_sample_2U = "2026/05/04 15:22:51.276373" # OBCtimeをUTCに変換する際に使用(PC Timeを使用)
#---------------------------------------------------
# 2. Output_file_name

# 発電量関係のcsvファイル
Gene_name_1U = "SAP_generation_1U"
Gene_name_2U = "SAP_generation_2U"
# バッテリー関係のcsvファイル
BAT_name_1U = "Battery_status_1U"
BAT_name_2U = "Battery_status_2U"
# 電力収支関係のcsvファイル
budget_name_1U = "Power_budget_1U"
budget_name_2U = "Power_budget_2U"
#----------------------------------------------------
# 3. header list (他ファイルで使用しているヘッダー名と厳密に同じにすること！)

# 抽出方法について　(基本はfloatとして抽出される)
non_float_header = ["OBC Time"] # floatに変換してほしくないものを記載 (時刻など)

# 抽出するデータについて
columns_ext = [# OBC時刻
            "OBC Time",
            # 電源関係
            "curs_sap1_px",
            "curs_sap1_py",
            "curs_sap1_pz",
            "curs_sap2_mx",
            "curs_sap2_my",
            "curs_2ndbat",
            "curs_bus",
            "vols_sap1",
            "vols_sap2",
            "vols_2ndbat",
            "vols_bus",
            # 温度関係
            "temp_strmx",
            "temp_strmy",
            "temp_strmz",
            "temp_strpx",
            "temp_strpy",
            "temp_strpz",
            "temp_2ndbat1",
            "temp_2ndbat2",
            "temp_2ndbat3",
            "temp_2ndbat4",
            # 太陽センサ(太陽方向)
            "sunx",
            "suny",
            "sunz"
            ]

# 出力データについて
# 1. 発電量関係について
columns_gene = [# 時刻関係
               "UTC Time",
               # 電源関係
               "curs_sap1_px [mA]",
               "curs_sap1_py [mA]",
               "curs_sap1_pz [mA]",
               "curs_sap2_mx [mA]",
               "curs_sap2_my [mA]",
               "vols_sap1 [V]",
               "vols_sap2 [V]",
               "SAP_generation_px [mW]",
               "SAP_generation_py [mW]",
               "SAP_generation_pz [mW]",
               "SAP_generation_mx [mW]",
               "SAP_generation_my [mW]",
               "SAP_generation_P_total [mW]",
               "SAP_generation_M_total [mW]",
               "SAP_generation_total [mW]",
               # 温度関係
               "temp_strmx [℃]",
               "temp_strmy [℃]",
               "temp_strmz [℃]",
               "temp_strpx [℃]",
               "temp_strpy [℃]",
               "temp_strpz [℃]",
               # 太陽センサ(太陽方向)
               "sunx",
               "suny",
               "sunz"
               ]

# 2. バッテリー関係について
columns_BAT = [# 時刻関係
              "UTC Time",
              # 電源関係
              "curs_2ndbat [mA]",
              "curs_bus [mA]",
              "vols_2ndbat [V]",
              "vols_bus [V]",
              # 温度関係
              "temp_strmx [℃]",
              "temp_strmy [℃]",
              "temp_strmz [℃]",
              "temp_strpx [℃]",
              "temp_strpy [℃]",
              "temp_strpz [℃]",
              "temp_2ndbat1 [℃]",
              "temp_2ndbat2 [℃]",
              "temp_2ndbat3 [℃]",
              "temp_2ndbat4 [℃]"
              ]

# 3. 電力収支関係
columns_budget =  [# 時刻関係
                  "UTC Time",
                  # 電源関係
                  "SAP_generation_total [mW]",
                  "Battery_charge [mW]",
                  "Bus_consumption [mW]"
                  ]

#--------------------------------------------------------
# 4. plot_settings






