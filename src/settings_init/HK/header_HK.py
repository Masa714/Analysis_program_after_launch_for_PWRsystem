"""
date:2026/05/11
author:ikuta
this file for header_HK
"""

#----------------------------------------------------
#  header list (他ファイルで使用しているヘッダー名と厳密に同じにすること！)

# 抽出方法について　(基本はfloatとして抽出される)
non_float_header = ["OBC Time"] # floatに変換してほしくないものを記載 (時刻など)

# 抽出するデータについて (HKの表記に合わせる)
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
            "curs_mtqx", # MTQA_X
            "curs_mtqy", # MTQA_Y
            "curs_mtqz1", # MTQA_Z
            "curs_mtqz2", # MTQO
            "curs_mtqz3", # MTQO
            "curs_mtqz4", # MTQO
            "vols_mtqa",
            "vols_mtqo_plasma",
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

# データを出力する際に, ヘッダーに単位を付ける  (内部処理には左側の文字列を使用している) 
# 新しく項目を追加するときは, ここと下のextractリストに追加すること！)
# 左：単位無し,  右：単位付き
header_map = {
            "curs_sap1_px":"curs_sap1_px [mA]",
            "curs_sap1_py":"curs_sap1_py [mA]",
            "curs_sap1_pz":"curs_sap1_pz [mA]",
            "curs_sap2_mx":"curs_sap2_mx [mA]",
            "curs_sap2_my":"curs_sap2_my [mA]",
            "curs_2ndbat":"curs_2ndbat [mA]",
            "curs_bus":"curs_bus [mA]",
            "curs_mtqx":"curs_mtqa_x [mA]",
            "curs_mtqy":"curs_mtqa_y [mA]",
            "curs_mtqz1":"curs_mtqa_z [mA]",
            "curs_mtqz2":"curs_mtqo_z2 [mA]",
            "curs_mtqz3":"curs_mtqo_z3 [mA]",
            "curs_mtqz4":"curs_mtqo_z4 [mA]",
            "vols_mtqa":"vols_mtqa [V]",
            "vols_mtqo_plasma":"vols_mtqo_plasma [V]",
            "vols_sap1":"vols_sap1 [V]",
            "vols_sap2":"vols_sap2 [V]",
            "vols_2ndbat":"vols_2ndbat [V]",
            "vols_bus":"vols_bus [V]",
            "pwr_sap_px":"pwr_sap_px [mW]",
            "pwr_sap_py":"pwr_sap_py [mW]",
            "pwr_sap_pz":"pwr_sap_pz [mW]",
            "pwr_sap_mx":"pwr_sap_mx [mW]",
            "pwr_sap_my":"pwr_sap_my [mW]",
            "est_max_pwr_px":"est_max_pwr_px [mW]",
            "est_max_pwr_py":"est_max_pwr_py [mW]",
            "est_max_pwr_pz":"est_max_pwr_pz [mW]",
            "est_max_pwr_mx":"est_max_pwr_mx [mW]",
            "est_max_pwr_my":"est_max_pwr_my [mW]",
            "pwr_sap_P":"pwr_sap_P [mW]",
            "pwr_sap_M":"pwr_sap_M [mW]",
            "pwr_mtqa_x":"pwr_mtqa_x [mW]",
            "pwr_mtqa_y":"pwr_mtqa_y [mW]",
            "pwr_mtqa_z":"pwr_mtqa_z [mW]",
            "pwr_mtqo_z2":"pwr_mtqo_z2 [mW]",
            "pwr_mtqo_z3":"pwr_mtqo_z3 [mW]",
            "pwr_mtqo_z4":"pwr_mtqo_z4 [mW]",
            "pwr_mtqa_total":"pwr_mtqa_total [mW]",
            "pwr_mtqo_total":"pwr_mtqo_total [mW]",
            "pwr_sap_total":"pwr_sap_total [mW]",
            "Battery_charge":"Battery_charge [mW]",
            "Bus_consumption":"Bus_consumption [mW]",
            "budget_check":"budget_check [mW]",
            "temp_strmx":"temp_strmx [℃]",
            "temp_strmy":"temp_strmy [℃]",
            "temp_strmz":"temp_strmz [℃]",
            "temp_strpx":"temp_strpx [℃]",
            "temp_strpy":"temp_strpy [℃]",
            "temp_strpz":"temp_strpz [℃]",
            "temp_2ndbat1":"temp_2ndbat1 [℃]",
            "temp_2ndbat2":"temp_2ndbat2 [℃]",
            "temp_2ndbat3":"temp_2ndbat3 [℃]",
            "temp_2ndbat4":"temp_2ndbat4 [℃]"
            }

# 出力データについて (抽出データに含まれるものは名前を一致させること！！！)
# 1. 発電量関係について
columns_gene = [# 時刻関係
               "OBC Time",
               "UTC Time",
               # 電源関係
               "curs_sap1_px",
               "curs_sap1_py",
               "curs_sap1_pz",
               "curs_sap2_mx",
               "curs_sap2_my",
               "vols_sap1",
               "vols_sap2",
               "pwr_sap_px",
               "pwr_sap_py",
               "pwr_sap_pz",
               "pwr_sap_mx",
               "pwr_sap_my",
               "est_max_pwr_px", # px面に正面から太陽が当たったときの発電量の概算結果, 発電量がcos則に従うこと・SUNSの値が正確であることを仮定
               "est_max_pwr_py", # py面に正面から太陽が当たったときの発電量の概算結果, 発電量がcos則に従うこと・SUNSの値が正確であることを仮定
               "est_max_pwr_pz", # pz面に正面から太陽が当たったときの発電量の概算結果, 発電量がcos則に従うこと・SUNSの値が正確であることを仮定
               "est_max_pwr_mx", # mx面に正面から太陽が当たったときの発電量の概算結果, 発電量がcos則に従うこと・SUNSの値が正確であることを仮定
               "est_max_pwr_my", # my面に正面から太陽が当たったときの発電量の概算結果, 発電量がcos則に従うこと・SUNSの値が正確であることを仮定
               "pwr_sap_P",
               "pwr_sap_M",
               "pwr_sap_total",
               # 温度関係
               "temp_strmx",
               "temp_strmy",
               "temp_strmz",
               "temp_strpx",
               "temp_strpy",
               "temp_strpz",
               # 太陽センサ(太陽方向)
               "sunx",
               "suny",
               "sunz"
               ]

# 2. バッテリー関係について
columns_BAT = [# 時刻関係
              "OBC Time",
              "UTC Time",
              # 電源関係
              "curs_2ndbat",
              "curs_bus",
              "vols_2ndbat",
              "vols_bus",
              "Battery_charge",
              "pwr_sap_total",
              "pwr_mtqa_total",
              "pwr_mtqo_total", 
              "Bus_consumption"
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
              # 太陽センサ
              "sunx",
              "suny",
              "sunz"
              ]

# 3. 電力収支関係
columns_budget =  [# 時刻関係
                  "OBC Time",
                  "UTC Time",
                  # 電源関係
                  "curs_mtqx", # MTQA_X
                  "curs_mtqy", # MTQA_Y
                  "curs_mtqz1", # MTQA_Z
                  "curs_mtqz2", # MTQO
                  "curs_mtqz3", # MTQO
                  "curs_mtqz4", # MTQO
                  "vols_mtqa",
                  "vols_mtqo_plasma",
                  "pwr_mtqa_x",
                  "pwr_mtqa_y",
                  "pwr_mtqa_z",
                  "pwr_mtqo_z2",
                  "pwr_mtqo_z3",
                  "pwr_mtqo_z4",
                  "pwr_mtqa_total",
                  "pwr_mtqo_total",
                  "pwr_sap_total",
                  "Battery_charge",
                  "Bus_consumption",
                  "budget_check",
                  "temp_strmx",
                  "temp_strmy",
                  "temp_strmz",
                  "temp_strpx",
                  "temp_strpy",
                  "temp_strpz"
                  ]
