import random #библиотека которая позволяет генерировать случайные фразы

# Считывает слова из файла(file)
def get_words(file):
    with open(file,"r") as f:
        words = f.read().split("\n")
        if words[-1] == "":
            words = words[:-1]
    return words


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

# Получает ответ пользователя подходит ли ему предложение (line), возвращает ответ в бинарном виде (1,0)
def user_answer(line):
    print(line)
    print("Подходит данная фраза? (Y/N)")
    answ = input()
    if answ == "Y":
        return 1
    elif answ == "N":
        return 0
    else:
        print("Неверно указан ответ попробуйте еще раз.")
        user_answer(line)

# основная main-функция
def main(f_trash,f_good,f_words):
    words = get_words(f_words)
    len_line = int(input("Введите фразу какой длинны вы хотите сгенерировать: "))
    line = generate_line(words,len_line)
    if user_answer(line):
        push_line(line,f_good)
    else:
        push_line(line,f_trash)
    print("-----------------")

# Для теста
# f_trash, f_good, f_words - файлы с которыми работаем
f_trash = "SortedText/trash.txt"
f_good = "SortedText/good.txt"
f_words = "SortedText/words.txt"

main(f_trash,f_good,f_words)
