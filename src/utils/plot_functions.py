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
import src.settings_init.common_valiables as com_val
from statsmodels.nonparametric.smoothers_lowess import lowess
#------------------------------------------------------------
# functions

# 同じx, y軸に任意の種類のグラフを出力する関数
def plot_from_dict(
    data_dict,
    x_key,                
    y_keys,              
    graph_title="Graph",
    legend_loc="upper left",
    
    colors=None,

    x_label=None,
    y_label=None,

    x_tick_interval=None,
    y_tick_interval=None,
    x_range=None,
    y_range=None,
    
    enable_fit=None,
    fitting_lebel=None,

    time_condition=None,
    other_condition=None
):

    # ✅ LOESS関数
    # 外挿曲線を入れる場合
    if enable_fit == 1:
        def plot_loess(x, y, color):
            
            # 空チェック
            if len(x) == 0:
                return

            if isinstance(x.iloc[0], (pd.Timestamp, np.datetime64)):
                x_num = mdates.date2num(x)
            else:
                x_num = x.values

            # 必要なら frac 調整
            smoothed = lowess(y, x_num, frac=fitting_lebel, return_sorted=True)

            plt.plot(
                smoothed[:, 0],
                smoothed[:, 1],
                color=color if color else "black",
                linewidth=2,
                alpha=0.9
            )

    plt.figure()
    
    # y_keysについて、文字列 → 辞書のヘッダー形式に変換
    if isinstance(y_keys, str):
        y_keys = [y_keys]

    # colorsの処理
    if colors is None:
        colors = [None] * len(y_keys)
    elif isinstance(colors, str):
        colors = [colors]
    
    # ======================
    # DataFrame化（list対策）
    # ======================
    data_dict = pd.DataFrame(data_dict)
    if "UTC Time" in data_dict.columns:
        data_dict["UTC Time"] = pd.to_datetime(data_dict["UTC Time"])

    # x軸用データ
    if x_key == "UTC Time":
        x = pd.to_datetime(data_dict[x_key])
    else:
        x = data_dict[x_key]

    # mask
    mask = np.ones(len(x), dtype=bool)

    if com_val.apply_time_condition and callable(time_condition):
        mask &= np.array(time_condition(data_dict, x))
    if callable(other_condition):
        mask &= np.array(other_condition(data_dict, x))

    x = x[mask]

    # ======================
    # y軸用データ
    # ======================
    for i, key in enumerate(y_keys):
        y = np.array(data_dict[key])[mask]

        color = colors[i] if i < len(colors) else None

        # ✅ 点（そのまま）
        plt.scatter(x, y, label=key, color=color)

        # ✅ LOESS追加
        if enable_fit == 1:
            plot_loess(x, pd.Series(y), color)

    plt.title(graph_title)

    # 凡例
    plt.legend(loc=legend_loc, bbox_to_anchor=(1.05, 1), borderaxespad=0)

    # 軸ラベル
    plt.xlabel(x_label if x_label else x_key)
    plt.ylabel(y_label if y_label else "Value")

    # 軸範囲
    if x_range is not None:
        plt.xlim(*x_range)

    if y_range is not None:
        plt.ylim(*y_range)

    # ======================
    # 目盛
    # ======================
    if x_tick_interval is not None:
        ax = plt.gca()

        if isinstance(x.iloc[0], (pd.Timestamp, np.datetime64)):
            ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=x_tick_interval))
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%y-%m-%d %H:%M'))

            for label in ax.get_xticklabels():
                label.set_fontsize(com_val.utc_fontsize)
        else:
            x_min, x_max = plt.xlim()
            plt.xticks(np.arange(x_min, x_max + x_tick_interval, x_tick_interval))

    if y_tick_interval is not None:
        y_min, y_max = plt.ylim()
        plt.yticks(np.arange(y_min, y_max + y_tick_interval, y_tick_interval))

    plt.grid()

    plt.tight_layout()
    plt.show()

# y軸の異なるデータを同じグラフにプロットする関数 (複数種のデータの相関用)
def plot_dual_axis(
    data_dict,
    x_key,
    y_left_keys,
    y_right_keys,
    graph_title="Graph",

    # 色を引数で指定できるように
    left_colors=None,
    right_colors=None,
    
    #軸ラベル
    x_label=None,
    y_left_label=None,
    y_right_label=None,

    # 目盛
    x_tick_interval=None,

    # 外挿曲線のフィッティングについて
    enable_fit=None,
    fitting_lebel=None,

    # フィルタ条件設定
    time_condition=None,
    other_condition=None
):
    from statsmodels.nonparametric.smoothers_lowess import lowess

    # 自動スケール用関数（nice numbers）
    def nice_step(y_min, y_max, target_div=4):
        range_val = y_max - y_min
        raw_step = range_val / target_div

        exponent = np.floor(np.log10(raw_step))
        fraction = raw_step / (10 ** exponent)

        if fraction <= 1:
            nice_fraction = 1
        elif fraction <= 2:
            nice_fraction = 2
        elif fraction <= 5:
            nice_fraction = 5
        else:
            nice_fraction = 10

        return nice_fraction * (10 ** exponent)

    # ✅ LOESS曲線
    # 外挿曲線を挿入する場合
    if enable_fit == 1:
        def plot_loess(x, y, ax, color):
            # datetime対応
            # 空チェック
            if len(x) == 0:
                return

            if isinstance(x.iloc[0], (pd.Timestamp, np.datetime64)):
                x_num = mdates.date2num(x)
            else:
                x_num = x.values

            smoothed = lowess(y, x_num, frac=fitting_lebel, return_sorted=True)

            ax.plot(
                smoothed[:, 0],
                smoothed[:, 1],
                color=color,
                linewidth=2,
                alpha=0.9
            )

    # フォントサイズ
    plt.rcParams.update({
        "font.size": 8,
        "axes.titlesize": 9,
        "axes.labelsize": 8,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "legend.fontsize": 8
    })

    # 上下2段
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

    # ======================
    # DataFrame化
    # ======================
    data_dict = pd.DataFrame(data_dict)
    if "UTC Time" in data_dict.columns:
        data_dict["UTC Time"] = pd.to_datetime(data_dict["UTC Time"])

    # ======================
    # x取得
    # ======================
    x = pd.to_datetime(data_dict[x_key]) if x_key == "UTC Time" else data_dict[x_key]

    # ======================
    # mask作成
    # ======================
    mask = np.ones(len(x), dtype=bool)

    if com_val.apply_time_condition and callable(time_condition):
        mask &= np.array(time_condition(data_dict, x))

    if callable(other_condition):
        mask &= np.array(other_condition(data_dict, x))

    x = x[mask]

    # ======================
    # 左軸（下側）
    # ======================
    for i, key in enumerate(y_left_keys):
        y = np.array(data_dict[key])[mask]
        color = left_colors[i] if (left_colors and i < len(left_colors)) else None

        # ✅ 点のみ
        ax1.scatter(x, y, label=key, color=color, s=10)

        # ✅ LOESS追加（線の代替）
        if enable_fit == 1:
            plot_loess(x, y, ax1, color if color else "black")

    ax1.set_ylabel(y_left_label if y_left_label else "Left Y")

    if y_left_keys:
        y_all = np.concatenate([np.array(data_dict[k][mask]) for k in y_left_keys])
        margin = 0.05 * (y_all.max() - y_all.min() + 1e-9)
        y_min = y_all.min() - margin
        y_max = y_all.max() + margin
        ax1.set_ylim(y_min, y_max)

        # ✅ niceスケール
        step = nice_step(y_min, y_max)
        y_min_tick = step * np.floor(y_min / step)
        y_max_tick = step * np.ceil(y_max / step)
        ax1.set_yticks(np.arange(y_min_tick, y_max_tick + step, step))

    # ======================
    # 右軸（上側）
    # ======================
    if y_right_keys:
        for i, key in enumerate(y_right_keys):
            y = np.array(data_dict[key])[mask]
            color = right_colors[i] if (right_colors and i < len(right_colors)) else None

            # ✅ 点のみ
            ax2.scatter(x, y, label=key, color=color, marker='x', s=15)

            # ✅ LOESS追加
            if enable_fit == 1:
                plot_loess(x, y, ax2, color if color else "black")

        ax2.set_ylabel(y_right_label if y_right_label else "Right Y")

        y_all = np.concatenate([np.array(data_dict[k][mask]) for k in y_right_keys])
        margin = 0.05 * (y_all.max() - y_all.min() + 1e-9)
        y_min = y_all.min() - margin
        y_max = y_all.max() + margin
        ax2.set_ylim(y_min, y_max)

        # ✅ niceスケール
        step = nice_step(y_min, y_max)
        y_min_tick = step * np.floor(y_min / step)
        y_max_tick = step * np.ceil(y_max / step)
        ax2.set_yticks(np.arange(y_min_tick, y_max_tick + step, step))

    # ======================
    # x軸目盛
    # ======================
    if x_tick_interval is not None:
        if len(x) > 0 and isinstance(x.iloc[0], (pd.Timestamp, np.datetime64)):
            ax2.xaxis.set_major_locator(mdates.MinuteLocator(interval=x_tick_interval))
            ax2.xaxis.set_major_formatter(mdates.DateFormatter('%y-%m-%d %H:%M'))
        else:
            x_min, x_max = ax2.get_xlim()
            ax2.set_xticks(np.arange(x_min, x_max + x_tick_interval, x_tick_interval))

    ax2.set_xlabel(x_label if x_label else x_key)

    # ======================
    # 凡例
    # ======================
    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()

    fig.legend(
        handles1 + handles2,
        labels1 + labels2,
        loc="lower center",
        bbox_to_anchor=(0.5, 0.02),
        ncol=4,
        fontsize="small"
    )

    plt.suptitle(graph_title)

    ax1.grid(True)
    ax2.grid(True)

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.2)

    plt.show()