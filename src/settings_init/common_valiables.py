"""
date:2026/04/26
author:ikuta
this file for valiables 
"""

#---------------------------------------------------
# Parameters

orbit_cycle = 6000 # 軌道1周の周期[s]
excel_base_time = "1900/01/01 0:00:00.00" # OBC_Timeが0の時のcsvファイル表記

# 以下はRTCのHK D/Lの際にモニターに出てくる値 (PC TimeとOBC Time)で更新　 
# MOBC再起動したら更新すること！
# 1U
OBC_time_sample_1U = "168:43:01.000" # OBCtimeをUTCに変換する際に使用 (HKのcsvにあるOBC Timeを入れないこと！ 時刻表記ではなく, 累積時間表記で記入)
UTC_time_sample_1U = "2026/05/06 16:41:33.826073" # OBCtimeをUTCに変換する際に使用 (PC Timeを使用)
# 2U
OBC_time_sample_2U = "371:27:25.000" # OBCtimeをUTCに変換する際に使用 (HKのcsvにあるOBC Timeを入れないこと！ 時刻表記ではなく, 累積時間表記で記入)
UTC_time_sample_2U = "2026/05/10 14:37:46.763375" # OBCtimeをUTCに変換する際に使用(PC Timeを使用)



