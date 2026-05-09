"""
date: 2026/05/07
author: ikuta
plot functions are included in this file 
"""

#------------------------------------------------------------
# import
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates
#------------------------------------------------------------
# functions

# 同じx, y軸に任意の種類のグラフを出力する関数
def plot_from_dict(
    data_dict,
    x_key,                # x軸にするキー
    y_keys,               # y軸にするキー（リスト形式で複数設定可能）
    graph_title="Graph", # タイトル
    legend_loc="upper left", # 凡例位置（外に出す前提に変更）
    
    colors=None, # 色指定 (リスト形式で複数設定可能)

    x_label=None, # x軸ラベル
    y_label=None, # y軸ラベル

    x_tick_interval=None, # x軸の目盛り間隔
    y_tick_interval=None, # y軸の目盛り間隔
    x_range=None, # x軸のグラフ範囲
    y_range=None, # y軸のグラフ範囲

    condition=None  # プロット条件
):
    plt.figure()
    
    # y_keysについて、文字列 → 辞書のヘッダー形式に変換
    if isinstance(y_keys, str):
        y_keys = [y_keys]

    # colorsの処理　(文字列 → ヘッダー形式への変換)
    if colors is None:
        colors = [None] * len(y_keys)
    elif isinstance(colors, str):
        colors = [colors]

    # x軸用データ
    if x_key == "UTC Time": # 時刻歴(文字列)の場合
        x = pd.to_datetime(data_dict[x_key]) # 文字列をdatetime型に変換
    else: # 列に格納されているのが数値の場合
        x = data_dict[x_key]

    # ★条件フィルタ用maskを初期化（全部True）
    mask = np.ones(len(x), dtype=bool)

    # 条件式による抽出（xも他列もすべてここで判断）
    if condition is not None:
        mask &= np.array(condition(data_dict, x))  # True / False 配列

    # ★xを切り出し
    x = x[mask]

    # y軸用データ
    for i, key in enumerate(y_keys):
        y = data_dict[key]

        # xと同じ条件でyも切り出し
        y = np.array(y)[mask]

        # 色を取り出す
        color = colors[i] if i < len(colors) else None

        # colorを追加
        plt.scatter(x, y, label=key, color=color)

    plt.title(graph_title)

    # 凡例（グラフ外に表示）
    plt.legend(loc=legend_loc, bbox_to_anchor=(1.05, 1), borderaxespad=0)

    # 軸ラベル
    plt.xlabel(x_label if x_label else x_key)
    plt.ylabel(y_label if y_label else "Value")

    # 軸範囲
    if x_range is not None:
        plt.xlim(*x_range)

    if y_range is not None:
        plt.ylim(*y_range)

    # 目盛
    # x軸目盛（時刻と数値の両対応）
    if x_tick_interval is not None:
        ax = plt.gca()

        # datetime判定
        if isinstance(x[0], (pd.Timestamp, np.datetime64)):
            # 時刻用
            ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=x_tick_interval))
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%y-%m-%d %H:%M'))

            # フォントサイズ調整
            for label in ax.get_xticklabels():
                label.set_fontsize(6)

        else:
            # 数値用
            x_min, x_max = plt.xlim()
            plt.xticks(np.arange(x_min, x_max + x_tick_interval, x_tick_interval))

    # y軸目盛
    if y_tick_interval is not None:
        y_min, y_max = plt.ylim()
        plt.yticks(np.arange(y_min, y_max + y_tick_interval, y_tick_interval))

    plt.grid()

    # レイアウト調整（凡例が切れないようにする）
    plt.tight_layout()

    plt.show()


# y軸が異なる種類のデータをまとめて描画する関数
def plot_dual_axis(
    data_dict,
    x_key,
    y_left_keys,
    y_right_keys=None,
    graph_title="Graph",

    x_label=None,
    y_left_label=None,
    y_right_label=None,

    # 範囲
    x_range=None,
    y_left_range=None,
    y_right_range=None,

    # 目盛
    x_tick_interval=None,
    y_left_tick_interval=None,
    y_right_tick_interval=None
):
    fig, ax1 = plt.subplots()

    x = data_dict[x_key]

    # ======================
    # 左軸
    # ======================
    for key in y_left_keys:
        y = data_dict[key]
        ax1.plot(x, y, label=key)

    ax1.set_xlabel(x_label if x_label else x_key)
    ax1.set_ylabel(y_left_label if y_left_label else "Left Y")

    # 範囲
    if x_range is not None:
        ax1.set_xlim(*x_range)

    if y_left_range is not None:
        ax1.set_ylim(*y_left_range)

    # 目盛
    if x_tick_interval is not None:
        x_min, x_max = ax1.get_xlim()
        ax1.set_xticks(np.arange(x_min, x_max + x_tick_interval, x_tick_interval))

    if y_left_tick_interval is not None:
        y_min, y_max = ax1.get_ylim()
        ax1.set_yticks(np.arange(y_min, y_max + y_left_tick_interval, y_left_tick_interval))

    # ======================
    # 右軸
    # ======================
    if y_right_keys:
        ax2 = ax1.twinx()

        for key in y_right_keys:
            y = data_dict[key]
            ax2.plot(x, y, linestyle="--", label=key)

        ax2.set_ylabel(y_right_label if y_right_label else "Right Y")

        # 範囲
        if y_right_range is not None:
            ax2.set_ylim(*y_right_range)

        # 目盛
        if y_right_tick_interval is not None:
            y_min, y_max = ax2.get_ylim()
            ax2.set_yticks(np.arange(y_min, y_max + y_right_tick_interval, y_right_tick_interval))

        #  凡例まとめる（外に表示）
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()

        ax1.legend(
            lines1 + lines2,
            labels1 + labels2,
            loc="upper left",
            bbox_to_anchor=(1.05, 1),
            borderaxespad=0
        )

    else:
        # 凡例（外に表示）
        ax1.legend(
            loc="upper left",
            bbox_to_anchor=(1.05, 1),
            borderaxespad=0
        )

    plt.title(graph_title)
    plt.grid()

    # レイアウト調整（凡例のはみ出し防止）
    plt.tight_layout()

    plt.show()
