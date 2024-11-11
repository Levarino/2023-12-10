import threading
import time


class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = 100
        self.day = 0

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemies > 0:         # создаем условия для цикла
            time.sleep(1)               # задержка в 1 секунду
            self.day += 1               # увеличиваем счетчик дней
            self.enemies -= self.power  # уменьшаем количество воинов
            if self.enemies <= 0:       # если количество воинов меньше или равно нулю
                break                   # выходим из цикла
            print(f'{self.name} сражается {self.day} день, осталось {self.enemies} воинов.')
        print(f"{self.name} одержал победу спустя {self.day} дней(дня)!")


# Создание экземпляров класса Knight
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

# Вывод строки об окончании битвы
print("Все битвы закончились!")
print("Обалденное домашнее задание!!!")
