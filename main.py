import random #библиотека которая позволяет генерировать случайные фразы

# Считывает слова из файла(file)
def get_words(file):
    with open(file,"r") as f:
        words = f.read().split("\n")
        if words[-1] == "":
            words = words[:-1]
    return words

# Получаем ответ по длинне слова
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

# Создает новое предложение длинны - lenght из слов words
def generate_line(words,lenght):
    random.shuffle(words)
    line = " ".join(list(words)[0:lenght])
    return line

# Записывает предложение (line) в файл (file)
def push_line(line,file):
    with open(file,"r+") as f:
        data = f.readlines()
        out = line+"\n"
        if out in data:
            print("Такое предложение уже есть.")
        else:
            print("Предложение успешно записано.")
            f.write(out)

# Получает ответ пользователя подходит ли ему предложение (line), возвращает ответ в бинарном виде (True,False)
def user_answer(line):
    print(line)
    print("Подходит данная фраза? (Y/N)")
    answ = input()
    if answ == "Y":
        return True
    elif answ == "N":
        return False
    else:
        print("Неверно указан ответ попробуйте еще раз.")
        user_answer(line)

# основная main-функция
def main(f_trash,f_good,f_words):
    words = get_words(f_words)
    lenght = get_lenght(len(words))
    print(lenght)
    line = generate_line(words,lenght)
    if user_answer(line):
        push_line(line,f_good)
    else:
        push_line(line,f_trash)
    print("-----------------")

# Для теста
# f_trash, f_good, f_words - файлы с которыми работаем
f_trash = "SortedText/trash.txt" # Файл с подходящими фразами
f_good = "SortedText/good.txt" # Файл с неподходящими фразами
f_words = "SortedText/words.txt" # Файл с исходными словами

for i in range(5):
    main(f_trash,f_good,f_words)