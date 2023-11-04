"""Игра угадай число
Компьютер сам загадывает и сам угадывает число , учитывая инфомацию
о том, больше или меньше загаданное число
"""

import numpy as np


def game_core_v3(number: int = np.random.randint(1, 101)) -> int:
    """
    Args:
        number (int, optional): Загаданное число. 

    Returns:
        int: Число попыток
    """
  
    count = 0     # Количество попыток
    predict = np.random.randint(1, 101)  # Загадываем число
    max_number = 100
    min_number = 0
    while True:
        count += 1
        if number > predict:
            min_number = predict +1
            predict = (max_number + min_number) // 2
        elif number < predict:
            max_number  = predict - 1
            predict = (max_number + min_number) // 2
        else:
            break   
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки") 
    return score

score_game(game_core_v3)  
if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)
