from datetime import date
import random
import os, sys
import time
import datetime

def slow_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)


if not os.path.isfile("add.txt"):
    file = open("add.txt", "w+")
    file.close()
if not os.path.isfile("sub.txt"):
    file = open("sub.txt", "w+")
    file.close()
if not os.path.isfile("multi.txt"):
    file = open("multi.txt", "w+")
    file.close()
if not os.path.isfile("div.txt"):
    file = open("div.txt", "w+")
    file.close()
if not os.path.isfile("expo.txt"):
    file = open("expo.txt", "w+")
    file.close()


#print("\033[H\033[J")
def start():
    os.system("cls")
    slow_print("\n\nWelcome to the Math-Test-v1.2!")
    time.sleep(0.3)
    os.system("cls")
    slow_print("""\n\n
    (1) ========= Play =========
    (2) === View Leaderboard ===
    (3) ======= Settings =======
    (4) ========= Exit =========""")
    select = input("\n\n")
    os.system("cls")
    if select == "1":
        menu()
    if select == "2":
        leaderboard_menu()
    if select == "3":
        settings()
    if select == "4":
        slow_print("\nSee you next time!")
        exit()

def settings():
    os.system("cls")
    slow_print("""
    (1) - Clear (+)-Lb
    (2) - Clear (-)-Lb
    (3) - Clear (*)-Lb
    (4) - Clear (/)-Lb
    (5) - Clear (^)-Lb
    (6) - Clear ALL
    """)
    x = input("\n")
    if x in ("1", "+"):
        open("add.txt", "w").close()
        slow_print("\nDone.")
        time.sleep(2)
        settings()
    if x in ("2", "-"):
        open("sub.txt", "w").close()
        slow_print("\nDone.")
        time.sleep(2)
        settings()
    if x in ("3", "*"):
        open("multi.txt", "w").close()
        slow_print("\nDone.")
        time.sleep(2)
        settings()
    if x in ("4", "/"):
        open("div.txt", "w").close()
        slow_print("\nDone.")
        time.sleep(2)
        settings()
    if x in ("5", "^"):
        open("expo.txt", "w").close()
        slow_print("\nDone.")
        time.sleep(2)
        settings()
    if x in ("6"):
        open("add.txt", "w").close()
        open("sub.txt", "w").close()
        open("multi.txt", "w").close()
        open("div.txt", "w").close()
        open("expo.txt", "w").close()
        slow_print("Done.")
        time.sleep(2)
        settings()


def leaderboard_menu():
    os.system("cls")
    print("Choose a leaderboard.\n")
    slow_print("""
    (1) - Addition
    (2) - Subtraction
    (3) - Multiplication
    (4) - Division
    (5) - Exponent
    (6) - Menu
    """)
    lb = input("\n\n")
    if lb in ("1"):
        print(os.system("cls"))
        print ("\n ⬇ Leaderboard ⬇\nNAME  \tSCORE    TIME\t       DATE\t Values")
        with open("add.txt") as f:
            lines = [i.strip().split(",") for i in f]
            sortedList = sorted(lines, key = lambda y: y[2])
            sortedList = sorted(sortedList, key = lambda y: (float(y[1])), reverse=True)
            for name, score, times, date, mini, maxi in sortedList[:5]:
                print(name+ "\t " + score + "\t" +times + "     " + date + "\t  "+mini+"/"+maxi)
        opt = input("\n(1) - Menu; (2) - Exit: ")
        if opt in ("1"):
            start()
        elif opt in ("2"):
            slow_print("See you next time!")
            exit()
    elif lb in ("2"):
        print(os.system("cls"))
        print ("\n ⬇ Leaderboard ⬇\nNAME  \tSCORE    TIME\t       DATE\t Values")
        with open("sub.txt") as f:
            lines = [i.strip().split(",") for i in f]
            sortedList = sorted(lines, key = lambda y: y[2])
            sortedList = sorted(sortedList, key = lambda y: (float(y[1])), reverse=True)
            for name, score, times, date, mini, maxi in sortedList[:5]:
                print(name+ "\t " + score + "\t" +times + "     " + date + "\t  "+mini+"/"+maxi)
        opt = input("\n(1) - Menu; (2) - Exit: ")
        if opt in ("1"):
            start()
        elif opt in ("2"):
            slow_print("See you next time!")
            exit()
    elif lb in ("3"):
        print(os.system("cls"))
        print ("\n ⬇ Leaderboard ⬇\nNAME  \tSCORE    TIME\t       DATE\t Values")
        with open("multi.txt") as f:
            lines = [i.strip().split(",") for i in f]
            sortedList = sorted(lines, key = lambda y: y[2])
            sortedList = sorted(sortedList, key = lambda y: (float(y[1])), reverse=True)
            for name, score, times, date, mini, maxi in sortedList[:5]:
                print(name+ "\t " + score + "\t" +times + "     " + date + "\t  "+mini+"/"+maxi)
        opt = input("\n(1) - Menu; (2) - Exit: ")
        if opt in ("1"):
            start()
        elif opt in ("2"):
            slow_print("See you next time!")
            exit()
    elif lb in ("4"):
        print(os.system("cls"))
        print ("\n ⬇ Leaderboard ⬇\nNAME  \tSCORE    TIME\t       DATE\t Values")
        with open("div.txt") as f:
            lines = [i.strip().split(",") for i in f]
            sortedList = sorted(lines, key = lambda y: y[2])
            sortedList = sorted(sortedList, key = lambda y: (float(y[1])), reverse=True)
            for name, score, times, date, mini, maxi in sortedList[:5]:
                print(name+ "\t " + score + "\t" +times + "     " + date + "\t  "+mini+"/"+maxi)
        opt = input("\n(1) - Menu; (2) - Exit: ")
        if opt in ("1"):
            start()
        elif opt in ("2"):
            slow_print("See you next time!")
            exit()
    elif lb in ("5"):
        print(os.system("cls"))
        print ("\n ⬇ Leaderboard ⬇\nNAME  \tSCORE    TIME\t       DATE\t  Val\t ExpoVal")
        with open("expo.txt") as f:
            lines = [i.strip().split(",") for i in f]
            sortedList = sorted(lines, key = lambda y: y[2])
            sortedList = sorted(sortedList, key = lambda y: (float(y[1])), reverse=True)
            for name, score, times, date, mini, maxi, expomini, expomaxi in sortedList[:5]:
                print(name+ "\t " + score + "\t" +times + "     " + date + "\t  "+mini+"/"+maxi+"\t   "+expomini+"/"+expomaxi)
        opt = input("\n(1) - Menu; (2) - Exit: ")
        if opt in ("1"):
            start()
        elif opt in ("2"):
            slow_print("See you next time!")
            exit()
    elif lb in ("6"):
        menu()

def menu():
    slow_print("Choose an operator.")
    slow_print("""\n
    (1) - Addition (+)
    (2) - Subtraction (-)
    (3) - Multiplication (*)
    (4) - Division (/)
    (5) - Exponent (^)
    """)
    operator = input("\n\n")
    if operator in ("1", "+"):
        addition()
    elif operator in ("2", "-"):
        sub()
    elif operator in ("3", "*"):
        multi()
    elif operator in ("4", "/"):
        div()
    elif operator in ("5", "^"):
        expo()
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
    file = open ("add.txt", "a")
    user = input("Enter a name to save your highscore: ")
    file.write(user+","+str(score)+","+timing+","+d1+","+str(minimum)+","+str(maximum))
    file.write("\n")
    slow_print("\nPlay again? (Y/N)")
    again = input("\n")
    if again.lower() in ("y", "yes"):
        addition()
    elif again.lower() in ("n", "no"):
        start()

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
    start = time.time()
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
    file = open ("sub.txt", "a")
    user = input("Enter a name to save your highscore: ")
    file.write(user+","+str(score)+","+timing+","+d1+","+str(minimum)+","+str(maximum))
    file.write("\n")
    slow_print("\nPlay again? (Y/N)")
    again = input("\n")
    if again.lower() in ("y", "yes"):
        sub()
    elif again.lower() in ("n", "no"):
        start()

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
    file = open ("multi.txt", "a")
    user = input("Enter a name to save your highscore: ")
    file.write(user+","+str(score)+","+timing+","+d1+","+str(minimum)+","+str(maximum))
    file.write("\n")
    slow_print("\nPlay again? (Y/N)")
    again = input("\n")
    if again.lower() in ("y", "yes"):
        multi()
    elif again.lower() in ("n", "no"):
        start()

def div():
    os.system("cls")
    print("Results will be rounded UP to the 2nd decimal (e.g: 0.75, not 0.746). EXCEPT: whole nums/nums with only one decimal place (0.5).\n")
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
        if rdm_1 > rdm_2:    
            answered = round(rdm_1 / rdm_2, 2)
            print(f"\n{rdm_1} / {rdm_2} ({question}/20)")
            answer = input("\n")
            question += 1
            if float(answer) == answered:
                correct += 1
                print("\nCorrect!\n━━━━━━━━━━━━")
            else:
                print(f"\nWrong. The answer is {answered}.\n━━━━━━━━━━━━")
        elif rdm_2 > rdm_1:
            answered = round(rdm_2 / rdm_1, 2)
            print(f"\n{rdm_2} / {rdm_1} ({question}/20)")
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
    file = open ("div.txt", "a")
    user = input("Enter a name to save your highscore: ")
    file.write(user+","+str(score)+","+timing+","+d1+","+str(minimum)+","+str(maximum))
    file.write("\n")
    slow_print("\nPlay again? (Y/N)")
    again = input("\n")
    if again.lower() in ("y", "yes"):
        div()
    elif again.lower() in("n", "no"):
        start()

def expo():
    os.system("cls")
    minimum = input("Min: ")
    maximum = input("Max: ")
    expomin = input("Min for exponent: ")
    expomax = input("Max for exponent: ")
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
        rdm_2 = random.randint(int(expomin),int(expomax))
        answered = rdm_1 ** rdm_2
        print(f"\n{rdm_1}^{rdm_2} ({question}/20)")
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
    file = open ("expo.txt", "a")
    user = input("Enter a name to save your highscore: ")
    file.write(user+","+str(score)+","+timing+","+d1+","+str(minimum)+","+str(maximum)+","+str(expomin)+","+str(expomax))
    file.write("\n")
    slow_print("\nPlay again? (Y/N)")
    again = input("\n")
    if again.lower() in ("y", "yes"):
        addition()
    elif again.lower() in ("n", "no"):
        start()

start()
