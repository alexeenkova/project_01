# Задача 1.2.
import random
from datetime import time
# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
playlist = random.choices(my_favorite_songs, k=3)
for k in playlist:
    Song_time = k[1] + k[1]
print(f'Три песни звучат {Song_time} минут')
# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
playlist = random.choices(list(my_favorite_songs_dict.values()), k=3)
song_time = playlist[0] + playlist[1] + playlist[2] 
print(f'Три песни звучат {song_time} минут')

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

# Задача 1
song_time_list = []
for song in my_favorite_songs:
    song_time_list.append(song[1])
playlist = random.choices(song_time_list, k=3)
for i in playlist:
    minutes, seconds = divmod(i, 60)
    sum_time_song = i + i
print(f'Три песни звучат {sum_time_song} минут')


# Задача 2

playlist = random.choices(list(my_favorite_songs_dict.values()), k=3)
for song_time in playlist:
    minutes, seconds = divmod(song_time, 60)
    sum_time_song = song_time + song_time
print(f'Три песни звучат {sum_time_song} минут')
