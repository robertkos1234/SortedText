from random import shuffle  # Библиотека которая позволяет генерировать случайные фразы
from math import factorial  # Библиотека которая позволяет считать факториал числа


# Считывает слова из файла(file)
def get_words(file):
    with open(file, "r") as f:
        words = f.read().split("\n")
        if words[-1] == "":
            words = words[:-1]
    return words


# Получаем ответ по длинне слова (Не используется)
def get_lenght(len_words):
    try:
        len_line = int(input("Введите длину фразы которою вы хотите сгенерировать: "))
        if len_line > len_words:
            print("Невозможно составить фразу такой длины\nНедостаточно исходных слов")
            return get_lenght(len_words)
        elif len_line <= 0:
            print("Невозможно составить фразу такой длины\nДлина фразы должна быть больше 0")
            return get_lenght(len_words)
        else:
            return (len_line)
    except:
        print("Введите пожалуйста целое число")
        return get_lenght(len_words)


# Получаем все фразы из файла(file)
def get_data(file):
    with open(file) as f:
        data = f.readlines()
    return data


# Создает новое предложение длинны - lenght из слов words
def generate_line(words, lenght, f_trash, f_good):
    shuffle(words)
    line = " ".join(list(words)[0:lenght])
    if check_line(line, f_trash) or check_line(line, f_good):
        return generate_line(words, lenght, f_trash, f_good)
    else:
        return line


# Возвращает 1 если фраза (line) есть в файле(file), 0 если нет
def check_line(line, file):
    if (line + "\n") in get_data(file):
        return 1
    else:
        return 0


# Возвращает 1 если сгенерирвоанны все фозможные фразы, иначе возвращает 0
def check_all_line(f_trah, f_good, len_words, lenght):
    if len_words <= lenght:
        max_words = factorial(len_words)  # кол-во перестановок без повторений
    else:
        max_words = factorial(len_words) / factorial(len_words - lenght)  # кол-во размещений без повторений
    count_words = len(get_data(f_trash)) + len(get_data(f_good))
    if max_words == count_words:
        return 1
    else:
        return 0


# Записывает предложение (line) в файл (file)
def push_line(line, file):
    with open(file, "r+") as f:
        data = f.readlines()
        out = line + "\n"
        if out in data:
            print("Такое предложение уже есть.")
        else:
            print("Предложение успешно записано.")
            f.write(out)


# Получает ответ пользователя подходит ли ему предложение (line), возвращает ответ в бинарном виде (True,False)
def user_answer(line):
    print(line)
    print("Подходит данная фраза? (Y/N/Q)")
    answ = input()
    answ = answ.lower()
    if answ == "y":
        return True
    elif answ == "n":
        return False
    elif answ == "q":
        print("Завершение программы...")
        exit()
    else:
        print("Неверно указан ответ попробуйте еще раз.")
        user_answer(line)


# основная main-функция
def main(f_trash, f_good, f_words, lenght):
    words = get_words(f_words)
    if check_all_line(f_trash, f_good, len(words), lenght):
        print("Все возможные фразы уже сгенерированны!")
    else:
        line = generate_line(words, lenght, f_trash, f_good)
        if user_answer(line):
            push_line(line, f_good)
        else:
            push_line(line, f_trash)
        print("-----------------")


# Для теста
# f_trash, f_good, f_words - файлы с которыми работаем
f_trash = "SortedText/trash.txt"  # Файл с подходящими фразами
f_good = "SortedText/good.txt"  # Файл с неподходящими фразами
f_words = "SortedText/words.txt"  # Файл с исходными словами
lenght = 2  # Длина фразы
k = 10 # Количество фраз которое нужно сгенерировать

for i in range(k):
    main(f_trash, f_good, f_words, lenght)
