import random
import pyautogui

ope = ['+', '-']
for i in range(5):
    sel = random.choice(ope)
    num1 = random.randint(100, 1000)
    num2 = random.randint(100, 1000)

    def que():
        box1 = pyautogui.prompt(title='Vrushank', text=f"{num1} {sel} {num2}")
        correct1 = num1 - num2
        correct2 = num1 + num2

        if box1 == str(correct1) or box1 == str(correct2):
            print(pyautogui.alert(text="Good!", title='Awesome!!'))
        else:
            print(pyautogui.alert(text="ans is wrong!!", title=' '))

    que()  # loaded
