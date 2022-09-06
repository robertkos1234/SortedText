import random

# Считывает слова из файла(file)
def get_words(file):
    with open(file,"r") as f:
        words = f.readlines()
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



f_trash = "trash.txt"
f_good = "good.txt"
words = ['hai','goodbye','love','you','I']


def main(f_trash,f_good,f_words):
    words = get_words(f_words)
    line = (generate_line(words,3))
    if user_answer(line):
        push_line(line,f_good)
    else:
        push_line(line,f_trash)
    print("-----------------")

