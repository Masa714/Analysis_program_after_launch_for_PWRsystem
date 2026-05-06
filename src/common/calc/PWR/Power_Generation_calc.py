"""
date:2026/05/04
author ikuta
this file for SAP Power Generation
"""
#--------------------------------------------------------
#import

import numpy as np
from src.settings_init.HK_valiables import HK_able
import src.common.Data_processing.extract_process_from_Input_csv as input
#---------------------------------------------------------
# function

# 1. SAP発電量を計算する関数
def SAP_generation_func(curs_px, curs_py, curs_pz, curs_mx, curs_my, vols_sap1, vols_sap2):

    # 各面のSAP発電量計算
    gene_px = curs_px * vols_sap1 #px面
    gene_py = curs_py * vols_sap1 #py面
    gene_pz = curs_pz * vols_sap1 #pz面
    gene_px = curs_mx * vols_sap2 #mx面
    gene_px = curs_my * vols_sap2 #my面
    
    # SAPのP,M面の合計
    

# 2. 軌道1周での平均発電量を計算する関数


#----------------------------------------------------------------------------------------
# main

# SAP関連の計算を行い, 結果を全てリストに格納する
def SAP_calc_result():








