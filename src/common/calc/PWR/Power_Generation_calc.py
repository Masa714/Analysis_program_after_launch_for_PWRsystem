"""
date:2026/05/04
author ikuta
this file for SAP Power Generation
"""
#--------------------------------------------------------
#import
import src.common.utils.organizing_datalist as org
#---------------------------------------------------------
# function

# 1. SAP発電量を計算する関数

def SAP_generation_func(curs_sap_px, curs_sap_py, curs_sap_pz, curs_sap_mx, curs_sap_my, vols_sap1, vols_sap2):

    # 各面のSAP発電量計算
    gene_px = curs_sap_px * vols_sap1 #px面
    gene_py = curs_sap_py * vols_sap1 #py面
    gene_pz = curs_sap_pz * vols_sap1 #pz面
    gene_mx = curs_sap_mx * vols_sap2 #mx面
    gene_my = curs_sap_my * vols_sap2 #my面
    
    # SAPのP,M面の合計
    gene_P = gene_px + gene_py + gene_pz
    gene_M = gene_mx + gene_my

    # SAPでの総発電量
    SAP_generation_total = gene_P + gene_M

    # 辞書で返す（ヘッダー付き）
    return {
        "SAP_generation_px":gene_px,
        "SAP_generation_py":gene_py,
        "SAP_generation_pz":gene_pz,
        "SAP_generation_mx":gene_mx,
        "SAP_generation_my":gene_my,
        "SAP_generation_P": gene_P,
        "SAP_generation_M": gene_M,
        "SAP_generation_total": SAP_generation_total
    }

#----------------------------------------------------------------------------------------
# main

# SAP関連の計算を行い, 結果を全てリストに格納する
def SAP_calc_result(extracted_list):
    
    #------------------------------------------------
    # 1.の関数
    # 値格納用のリストの作成
    SAP_px_list = []
    SAP_py_list = []
    SAP_pz_list = []
    SAP_mx_list = []
    SAP_my_list = []
    SAP_P_list = []
    SAP_M_list = []
    SAP_total_list = []

    # 発電量の計算
    for curs_sap_px, curs_sap_py, curs_sap_pz, curs_sap_mx, curs_sap_my, vols_sap1, vols_sap2 in zip(
        extracted_list["curs_sap1_px"],
        extracted_list["curs_sap1_py"],
        extracted_list["curs_sap1_pz"],
        extracted_list["curs_sap2_mx"],
        extracted_list["curs_sap2_my"],
        extracted_list["vols_sap1"],
        extracted_list["vols_sap2"]
    ):

        result = SAP_generation_func(
            curs_sap_px, curs_sap_py, curs_sap_pz, curs_sap_mx, curs_sap_my, vols_sap1, vols_sap2
        )
        
        # リストに値を格納
        SAP_px_list.append(result["SAP_generation_px"])
        SAP_py_list.append(result["SAP_generation_py"])
        SAP_pz_list.append(result["SAP_generation_pz"])
        SAP_mx_list.append(result["SAP_generation_mx"])
        SAP_my_list.append(result["SAP_generation_my"])
        SAP_P_list.append(result["SAP_generation_P"])
        SAP_M_list.append(result["SAP_generation_M"])
        SAP_total_list.append(result["SAP_generation_total"])
    #----------------------------------------------------------------------
    
    # extracted_listに列を追加
    org.dict_append("SAP_generation_px", SAP_px_list, extracted_list)
    org.dict_append("SAP_generation_py", SAP_py_list, extracted_list)
    org.dict_append("SAP_generation_pz", SAP_pz_list, extracted_list)
    org.dict_append("SAP_generation_mx", SAP_mx_list, extracted_list)
    org.dict_append("SAP_generation_my", SAP_my_list, extracted_list)
    org.dict_append("SAP_generation_P", SAP_P_list, extracted_list)
    org.dict_append("SAP_generation_M", SAP_M_list, extracted_list)
    org.dict_append("SAP_generation_total", SAP_total_list, extracted_list)
    
    return extracted_list








