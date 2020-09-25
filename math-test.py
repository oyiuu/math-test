from datetime import date
import random
import os, sys
import time
import datetime

def slow_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.02)

#print("\033[H\033[J")
def start():
    os.system("cls")
    slow_print("\n\nWelcome to the Math-Test-1.0!")
    time.sleep(0.3)
    os.system("cls")
    slow_print("\n\n(1) ========= Play =========\n(2) === View Leaderboard ===\n(3) ========= Exit =========")
    select = input("\n\n")
    os.system("cls")
    if select == "1":
        menu()
    if select == "2":
        leaderboard()
    if select == "3":
        slow_print("See you next time!")
        exit()

def leaderboard():
    try:
        print(os.system("cls"))
        print ("\n ⬇ Leaderboard ⬇\nNAME  \tSCORE    TIME\t       DATE") #LEADERBOARD SECTION
        with open("lb.txt") as f:
            lines = [i.strip().split(",") for i in f]
            #sortedList = sorted(lines, key = lambda y: (float(y[1])), reverse=True); Idk if I need this (probably not)
            sortedList = sorted(lines, key = lambda y: y[2])
            sortedList = sorted(sortedList, key = lambda y: (float(y[1])), reverse=True)
            for name, score, times, date in sortedList[:5]:
                print(name+ "\t " +score + "\t" +times + "     " + date)
        opt = input("\n(1) - Menu; (2) - Exit: ")
        if opt in ("1"):
            start()
        elif opt in ("2"):
            slow_print("See you next time!")
            exit()
    except FileNotFoundError:
        file = open("lb.txt", "w+")
        file.close()
        leaderboard()

def menu():
    slow_print("Choose an operator.")
    slow_print("\n\n(1) - Addition (+)\n(2) - Subtraction (-)\n(3) - Multiplication (*)\n(4) - Division (/)")
    operator = input("\n\n")
    if operator in ("1", "+"):
        addition()
    elif operator in ("2", "-"):
        sub()
    elif operator in ("3", "*"):
        multi()
    elif operator in ("4", "/"):
        div()
    else:
        print("Please enter a valid operator.")
        operator = input("\n")


def addition():
    os.system("cls")
    minimum = input("Min: ")
    maximum = input("Max: ")
    os.system("cls")
    slow_print("Test begins in 3...")
    time.sleep(0.8)
    slow_print("2...")
    time.sleep(1)
    slow_print("1...")
    time.sleep(1)
    os.system("cls")
    start = time.time()
    question = 1
    correct = 0
    false = 0
    while question <= 20:
        rdm_1 = random.randint(int(minimum),int(maximum))
        rdm_2 = random.randint(int(minimum),int(maximum))
        answered = rdm_1 + rdm_2
        print(f"\n{rdm_1} + {rdm_2} ({question}/20)")
        answer = input("\n")
        question += 1
        if int(answer) == answered:
            correct += 1
            print("\nCorrect!\n━━━━━━━━━━━━")
        else:
            print(f"\nWrong. The answer is {answered}.\n━━━━━━━━━━━━")
    acc = correct / 20 * 100
    end = time.time()
    timing = str(datetime.timedelta(seconds=round(end-start)))
    slow_print("\nYou answered {}/20 questions correctly. ({}%)\n".format(correct, int(acc)))
    score = int(acc)
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    file = open ("lb.txt", "a")
    user = input("Enter a name to save your highscore: ")
    file.write(user+","+str(score)+","+timing+","+d1)
    file.write("\n")
    menu()

def sub():
    os.system("cls")
    minimum = input("Min: ")
    maximum = input("Max: ")
    os.system("cls")
    slow_print("Test begins in 3...")
    time.sleep(0.8)
    slow_print("2...")
    time.sleep(1)
    slow_print("1...")
    time.sleep(1)
    os.system("cls")
    question = 1
    correct = 0
    false = 0
    while question <= 20:
        rdm_1 = random.randint(int(minimum),int(maximum))
        rdm_2 = random.randint(int(minimum),int(maximum))
        answered = rdm_1 - rdm_2
        print(f"\n{rdm_1} - {rdm_2} ({question}/20)")
        answer = input("\n")
        question += 1
        if str(answer) == str(answered):
            correct += 1
            print("\nCorrect!\n━━━━━━━━━━━━")
        else:
            print(f"\nWrong. The answer is {answered}.\n━━━━━━━━━━━━")
    acc = correct / 20 * 100
    end = time.time()
    timing = str(datetime.timedelta(seconds=round(end-start)))
    slow_print("\nYou answered {}/20 questions correctly. ({}%)\n".format(correct, int(acc)))
    score = int(acc)
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    file = open ("lb.txt", "a")
    user = input("Enter a name to save your highscore: ")
    file.write(user+","+str(score)+","+timing+","+d1)
    file.write("\n")
    menu()

def multi():
    os.system("cls")
    minimum = input("Min: ")
    maximum = input("Max: ")
    os.system("cls")
    slow_print("Test begins in 3...")
    time.sleep(0.8)
    slow_print("2...")
    time.sleep(1)
    slow_print("1...")
    time.sleep(1)
    os.system("cls")
    start = time.time()
    question = 1
    correct = 0
    false = 0
    while question <= 20:
        rdm_1 = random.randint(int(minimum),int(maximum))
        rdm_2 = random.randint(int(minimum),int(maximum))
        answered = rdm_1 * rdm_2
        print(f"\n{rdm_1} * {rdm_2} ({question}/20)")
        answer = input("\n")
        question += 1
        if int(answer) == answered:
            correct += 1
            print("\nCorrect!\n━━━━━━━━━━━━")
        else:
            print(f"\nWrong. The answer is {answered}.\n━━━━━━━━━━━━")
    acc = correct / 20 * 100
    end = time.time()
    timing = str(datetime.timedelta(seconds=round(end-start)))
    slow_print("\nYou answered {}/20 questions correctly. ({}%)\n".format(correct, int(acc)))
    score = int(acc)
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    file = open ("lb.txt", "a")
    user = input("Enter a name to save your highscore: ")
    file.write(user+","+str(score)+","+timing+","+d1)
    file.write("\n")
    menu()

def div():
    os.system("cls")
    print("Results will be rounded to the 2nd decimal (e.g: 0.75). EXCEPT: whole nums/nums with only one decimal place (0.5).\n")
    minimum = input("Min: ")
    maximum = input("Max: ")
    os.system("cls")
    slow_print("Test begins in 3...")
    time.sleep(0.8)
    slow_print("2...")
    time.sleep(1)
    slow_print("1...")
    time.sleep(1)
    os.system("cls")
    start = time.time()
    question = 1
    correct = 0
    false = 0
    while question <= 20:
        rdm_1 = random.randint(int(minimum),int(maximum))
        rdm_2 = random.randint(int(minimum),int(maximum))
        answered = round(rdm_1 / rdm_2, 2)
        print(f"\n{rdm_1} / {rdm_2} ({question}/20)")
        answer = input("\n")
        question += 1
        if float(answer) == answered:
            correct += 1
            print("\nCorrect!\n━━━━━━━━━━━━")
        else:
            print(f"\nWrong. The answer is {answered}.\n━━━━━━━━━━━━")
    acc = correct / 20 * 100
    end = time.time()
    timing = str(datetime.timedelta(seconds=round(end-start)))
    slow_print("\nYou answered {}/20 questions correctly. ({}%)\n".format(correct, int(acc)))
    score = int(acc)
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    file = open ("lb.txt", "a")
    user = input("Enter a name to save your highscore: ")
    file.write(user+","+str(score)+","+timing+","+d1)
    file.write("\n")
    menu()

start()