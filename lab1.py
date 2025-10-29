# task1
def print_thailand_flag():
    red = '\033[41m'
    white = '\033[47m'
    blue = '\033[44m'
    reset = '\033[0m'

    width = 30

    for _ in range(2):
        print(f"{red}{' ' * width}{reset}")
    for _ in range(2):
        print(f"{white}{' ' * width}{reset}")
    for _ in range(4):
        print(f"{blue}{' ' * width}{reset}")
    for _ in range(2):
        print(f"{white}{' ' * width}{reset}")
    for _ in range(2):
        print(f"{red}{' ' * width}{reset}")


print_thailand_flag()


# task2
def draw_symbol():
    black = '\033[40m'
    reset = '\033[0m'

    print(f"      {black} {reset}")
    print(f"     {black}   {reset}")
    print(f"     {black}   {reset}")
    print(f"   {black}   {reset} {black}   {reset}")
    print(f" {black}    {reset}   {black}    {reset}")
    # print(f"{black}  {reset}" + " " * 5 + f"{black}  {reset}")

for i in range(5):
    draw_symbol()


# task3
WIDTH = 40
HEIGHT = 12

for y in range(HEIGHT, -1, -1):
    line = ""
    for x in range(1, WIDTH + 1):
        fx = 1 / x
        fy = int(fx * HEIGHT)
        if fy == y:
            line += "*"
        elif y == 0:
            line += "-"   # x-axis
        elif x == 1:
            line += "|"   # y-axis
        else:
            line += " "
    print(line)

print("\nGraph of function y = 1/x (first quadrant with axes)")


# task4
import plt
with open("sequence.txt", "r") as f:
    numbers = [float(line.strip()) for line in f if line.strip()]

positive_numbers = [x for x in numbers if x >= 0]
less_than_5 = [x for x in positive_numbers if x < 5]
greater_than_5 = [x for x in positive_numbers if x > 5]

count_less = len(less_than_5)
count_greater = len(greater_than_5)
total = count_less + count_greater

percent_less = count_less / total * 100
percent_greater = count_greater / total * 100

labels = ['< 5', '> 5']
sizes = [percent_less, percent_greater]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Percentage ratio of numbers')
plt.show()