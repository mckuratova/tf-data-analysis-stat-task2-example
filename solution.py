import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 906914964 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = sum(x) / len(x)
    shift = 0.017
    left = shift + (loc / p)
    right = shift + (loc / alpha)
    
    return left, right
