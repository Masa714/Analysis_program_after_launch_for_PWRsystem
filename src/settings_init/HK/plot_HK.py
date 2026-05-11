"""
date:2026/04/26
author:ikuta
this file for HK plot settings 
"""

#--------------------------------------------------------
# plot_settings
plot_style = 0 # 0:点のみ,  1：点+外挿曲線
fitting_lebel = 0.05 # 外挿曲線のフィッティングの度合い (0～1までの範囲, 0に近いほどフィッティングが急になる)
# graph__title ----------------------------------------
#PWR
# 発電量関連
title_eath_sap = "PWR_eath_sap_vs_UTC" # 各パネルでの発電量の時刻歴
title_IV_px = "I-Vcurve_px" # px面のI-V曲線
title_IV_py = "I-Vcurve_py" # px面のI-V曲線
title_IV_pz = "I-Vcurve_pz" # px面のI-V曲線
title_IV_mx = "I-Vcurve_mx" # px面のI-V曲線
title_IV_my = "I-Vcurve_my" # px面のI-V曲線
title_PV_px = "P-Vcurve_px" # px面のI-V曲線
title_PV_py = "P-Vcurve_py" # px面のI-V曲線
title_PV_pz = "P-Vcurve_pz" # px面のI-V曲線
title_PV_mx = "P-Vcurve_mx" # px面のI-V曲線
title_PV_my = "P-Vcurve_my" # px面のI-V曲線
title_suns = "sunvec_vs_UTC" # 太陽ベクトルの時刻歴
title_temp_power_vs_sunvecx = "temp,power_vs_sunvec_x" # 温度, 各面の生成電力と太陽ベクトルの相関
title_temp_power_vs_sunvecy = "temp,power_vs_sunvec_y" # 温度, 各面の生成電力と太陽ベクトルの相関
title_temp_power_vs_sunvecz = "temp,power_vs_sunvec_z" # 温度, 各面の生成電力と太陽ベクトルの相関


#------------------------------------------------------
# axis_label ----------------------------------------------
time_label = "UTC_time" # 時刻歴の軸ラベル
curs_label = "Current [mA]" # 電流の軸ラベル
vols_label = "Voltage [V]" # 電圧の軸ラベル
power_label = "Power [mW]" # 電力の軸ラベル
temp_label = "temp [℃]" # 温度の軸ラベル
vec_label = "unit_vector" # 単位ベクトルの軸ラベル

#------------------------------------------------------
#plot_color ------------------------------------------
# 番号が小さい順に色が選択されます
color_1 = "red"
color_2 = "blue"
color_3 = "springgreen"
color_4 = "orange"
color_5 = "purple"
color_6 = "brown"

#-----------------------------------------------------
# plot_area-------------------------------------------
# 軸ラベルについては、ここで編集はできないようになっています
# 各種plotのところから変更をお願いします
plot_timerange = 100 # 時刻歴について、一番時刻が古いデータから何分間のデータをプロットするのか  TLCとRTCのHKが混ざったときの対策
utc_fontsize = 6 # 時刻歴の横軸メモリのフォントサイズ
time_tick_interval = int(plot_timerange * 0.2) # 時刻歴-横軸の目盛り間隔(整数)  timerangeの5分の1程度がいい, 自分で設定する際は「interval=数字(分)」で設定
x1_tick_interval = None # 横軸(時刻以外)の目盛り間隔　でフォルトは自動(NONE)で設定　自分で設定する際は「interval=整数」で設定
y1_tick_interval = None # 縦軸の目盛り間隔  デフォルトは自動で設定, 自分で設定する際は「interval=整数」で設定
y2_tick_interval = None # 2つy軸を使用するときの, 2つ目の縦軸の目盛り間隔  デフォルトは自動で設定, 自分で設定する際は「interval=整数」で設定
x1_range = None # 横軸のグラフ端　　デフォルトは自動で設定, 自分で設定する際は「range=(min, max)」で設定
y1_range = None # 縦軸のグラフ端　　デフォルトは自動で設定, 自分で設定する際は「range=(min, max)」で設定
y2_range = None # 2つy軸を使用するときの, 2つ目の縦軸のグラフ端　　デフォルトは自動で設定, 自分で設定する際は「range=(min, max)」で設定
