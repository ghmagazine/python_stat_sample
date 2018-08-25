import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.ticker import MultipleLocator
from ipywidgets import interact
from itertools import chain


def plot_dev(scores, x_range=None):
    if x_range is None:
        x_range = (np.min(scores) - 3, np.min((np.max(scores) + 3, 100)))
    y_range = (-0.5, 10 * 0.5 + 0.5)
    heights = (np.arange(10) * 0.5 + 0.5)[::-1]
    mean = np.mean(scores)

    fig = plt.figure(figsize=(15, 6))
    ax = fig.add_subplot(111)
    ax.grid(False)

    ax.hlines(0, *x_range, linewidths=1)
    ax.hlines(heights, mean, scores, linewidths=1, color='c', alpha=0.7)

    ax.vlines(scores, 0.27, y_range[1], linestyle='--', linewidths=1)
    ax.vlines(mean, 0, y_range[1], linewidths=2, alpha=0.5)

    ax.scatter(scores, [0]*len(scores), s=30, color='gray', zorder=9)
    ax.scatter(mean, 0, s=80, color='b', zorder=9)

    names = ['A', 'B', 'C', 'D', 'E',
             'F', 'G', 'H', 'I', 'J']
    for score, name in zip(scores, names):
        ax.text(score, 0.15, name, ha='center', va='center', size=16, zorder=9)

    ax.set_xlim(*x_range)
    ax.set_ylim(*y_range)
    ax.set_xticks(np.arange(*x_range), minor=True)
    ax.set_yticks([])
    ax.set_xlabel('点数', fontsize=16)

    plt.show()


def plot_var_interact(scores):
    scores = scores[:4]
    majorLocator = MultipleLocator(5)
    minorLocator = MultipleLocator(1)

    @interact(A=(1, 100, 1), B=(1, 100, 1),
              C=(1, 100, 1), D=(1, 100, 1))
    def plot(A=scores[0], B=scores[1],
             C=scores[2], D=scores[3]):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111)
        ax.grid(False)

        scores = [A, B, C, D]
        names = ['A', 'B', 'C', 'D']
        mean = np.mean(scores)
        std = np.std(scores)

        for score, name in zip(scores, names):
            ax.text(score, score, name, ha='center', va='center', size=16)

        ax.hlines(mean, 0, 100, alpha=0.3)
        ax.vlines(mean, 0, 100, alpha=0.3)

        for dev in scores-mean:
            ax.add_patch(patches.Rectangle((mean, mean), dev, dev,
                                           alpha=0.3, color='gray'))
        ax.add_patch(patches.Rectangle((mean-std/2, mean-std/2), std, std,
                                       alpha=0.5, color='c'))

        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.set_xlabel('点数', fontsize=16)
        ax.set_ylabel('点数', fontsize=16)

        ax.xaxis.set_major_locator(MultipleLocator(5))
        ax.xaxis.set_minor_locator(MultipleLocator(1))
        ax.yaxis.set_major_locator(MultipleLocator(5))
        ax.yaxis.set_minor_locator(MultipleLocator(1))

        plt.show()


def plot_std_interact(scores):
    x_range = (0, 100)
    y_range = (-0.5, 10 * 0.5 + 0.5)
    heights = (np.arange(10) * 0.5 + 0.5)[::-1]

    @interact(A=(1, 100, 1), B=(1, 100, 1),
              C=(1, 100, 1), D=(1, 100, 1),
              E=(1, 100, 1), F=(1, 100, 1),
              G=(1, 100, 1), H=(1, 100, 1),
              I=(1, 100, 1), J=(1, 100, 1))
    def plot(A=scores[0], B=scores[1],
             C=scores[2], D=scores[3],
             E=scores[4], F=scores[5],
             G=scores[6], H=scores[7],
             I=scores[8], J=scores[9]):
        fig = plt.figure(figsize=(15, 6))
        ax = fig.add_subplot(111)
        ax.grid(False)

        scores = [A, B, C, D, E,
                  F, G, H, I, J]
        names = ['A', 'B', 'C', 'D', 'E',
                 'F', 'G', 'H', 'I', 'J']
        mean = np.mean(scores)
        std = np.std(scores)

        ax.hlines(0, *x_range, linewidths=1)
        ax.hlines(heights, mean, scores, linewidths=1, color='c', alpha=0.7)

        ax.vlines(scores, 0.27, y_range[1], linestyle='--', linewidths=1)
        ax.vlines(mean, 0, y_range[1], linewidths=2, alpha=0.5)

        ax.scatter(scores, [0]*len(scores), s=30, color='gray', zorder=9)
        ax.scatter(mean, 0, s=80, color='b', zorder=9)

        for score, name in zip(scores, names):
            ax.text(score, 0.15, name, ha='center', va='center', size=16, zorder=9)

        ax.add_patch(patches.Rectangle((mean-std/2, 0), std, -0.5, color='c'))
        ax.add_patch(patches.Rectangle((mean-std, 0), 2*std, -0.5,
                                       alpha=0.5, color='c'))
        ax.add_patch(patches.Rectangle((mean-std*3/2, 0), 3*std, -0.5,
                                       alpha=0.3, color='c'))

        ax.set_xlim(*x_range)
        ax.set_ylim(*y_range)
        ax.set_xticks(np.arange(*x_range), minor=True)
        ax.set_yticks([])
        ax.set_xlabel('点数', fontsize=16)

        plt.show()


def plot_cov(en_scores, ma_scores, plot_squares=False):
    x_range = (np.min(en_scores) - 3, np.min((np.max(en_scores) + 3, 100)))
    y_range = (np.min(ma_scores) - 3, np.min((np.max(ma_scores) + 3, 100)))

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    ax.grid(False)

    en_mean = np.mean(en_scores)
    ma_mean = np.mean(ma_scores)

    names = ['A', 'B', 'C', 'D', 'E',
             'F', 'G', 'H', 'I', 'J']
    for en_score, ma_score, name in zip(en_scores, ma_scores, names):
        ax.text(en_score, ma_score, name, ha='center', va='center', size=16)

    if plot_squares:
        plt_idx = [2, 4, 7]
        colors = ['gray' if (en_score - en_mean) * (ma_score - ma_mean) > 0 else 'cyan'
                  for en_score, ma_score in zip(en_scores[plt_idx], ma_scores[plt_idx])]
        for en_score, ma_score, color in zip(en_scores[plt_idx], ma_scores[plt_idx], colors):
            ax.add_patch(patches.Rectangle((en_mean, ma_mean),
                                           en_score - en_mean,
                                           ma_score - ma_mean,
                                           alpha=0.3, color=color))

    ax.hlines(ma_mean, 0, 100, color='gray')
    ax.vlines(en_mean, 0, 100, color='gray')

    ax.set_xlim(*x_range)
    ax.set_ylim(*y_range)
    ax.set_xlabel('英語の点数', fontsize=16)
    ax.set_ylabel('数学の点数', fontsize=16)

    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.yaxis.set_minor_locator(MultipleLocator(1))

    plt.show()


def plot_cov_interact(en_scores, ma_scores):
    en_scores = en_scores[:4]
    ma_scores = ma_scores[:4]
    x_range = (0, 100)
    y_range = (0, 100)

    @interact(Aさんの英語=x_range, Aさんの数学=y_range,
              Bさんの英語=x_range, Bさんの数学=y_range,
              Cさんの英語=x_range, Cさんの数学=y_range,
              Dさんの英語=x_range, Dさんの数学=y_range)
    def plot(Aさんの英語=en_scores[0], Aさんの数学=ma_scores[0],
             Bさんの英語=en_scores[1], Bさんの数学=ma_scores[1],
             Cさんの英語=en_scores[2], Cさんの数学=ma_scores[2],
             Dさんの英語=en_scores[3], Dさんの数学=ma_scores[3]):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111)
        ax.grid(False)

        names = ['A', 'B', 'C', 'D']
        en_scores = [Aさんの英語, Bさんの英語, Cさんの英語, Dさんの英語]
        ma_scores = [Aさんの数学, Bさんの数学, Cさんの数学, Dさんの数学]
        en_mean = np.mean(en_scores)
        ma_mean = np.mean(ma_scores)

        for en_score, ma_score, name in zip(en_scores, ma_scores, names):
            ax.text(en_score, ma_score, name, ha='center', va='center', size=16)

        ax.hlines(ma_mean, 0, 100, color='gray')
        ax.vlines(en_mean, 0, 100, color='gray')

        colors = ['gray' if (en_score - en_mean) * (ma_score - ma_mean) > 0 else 'cyan'
                  for en_score, ma_score in zip(en_scores, ma_scores)]
        for en_score, ma_score, color in zip(en_scores, ma_scores, colors):
            ax.add_patch(patches.Rectangle((en_mean, ma_mean),
                                           en_score - en_mean,
                                           ma_score - ma_mean,
                                           alpha=0.3, color=color))

        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.set_xlabel('英語の点数', fontsize=16)
        ax.set_ylabel('数学の点数', fontsize=16)

        ax.xaxis.set_major_locator(MultipleLocator(5))
        ax.xaxis.set_minor_locator(MultipleLocator(1))
        ax.yaxis.set_major_locator(MultipleLocator(5))
        ax.yaxis.set_minor_locator(MultipleLocator(1))

        plt.show()


def plot_coef():
    np.random.seed(0)
    rs = [-1, -0.8, -0.5,
          -0.2, 0, 0.2,
          0.5, 0.8, 1]

    fig, axes = plt.subplots(3, 3, figsize=(10, 10))
    for ax, r in zip(chain(*axes), rs):
        dt = np.random.multivariate_normal([0, 0], [[1, r], [r, 1]], 100)
        ax.grid(False)
        ax.scatter(dt[:, 0], dt[:, 1])
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(f'r={r}')
    plt.show()
