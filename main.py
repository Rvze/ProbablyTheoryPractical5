import math
import matplotlib.pyplot as plt

from colorama import Fore, Style

FILE_INPUT = "/Users/nurgunmakarov/PycharmProjects/ProbablyTheory#1/input.txt"
FILE_OUTPUT = "/Users/nurgunmakarov/PycharmProjects/ProbablyTheory#1/output.txt"
selection = []
xi = []
cnti = []
probablyi = []


def empirical_function():
    print(Fore.GREEN + "Эмперическая функция F(x):" + Style.RESET_ALL)
    prob = probablyi[0]
    print("0, если -inf < x <= {0}".format(xi[0]))
    for i in range(len(xi) - 1):
        print("%.2f" % prob + ", если {0} < x <= {1}".format(xi[i], xi[i + 1]))
        prob += probablyi[i + 1]
    print("1 если {0} <x <= inf".format(xi[len(xi) - 1]))


def work_piece():
    selects = selection["selection"]
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel('x')
    ax.set_ylabel('p')
    h = (selects[len(selects) - 1] - selects[0]) / (1 + (math.log(len(selects)) / math.log(2)))
    m = math.ceil(1 + math.log(len(selects)) / math.log(2))
    x = selects[0] - h / 2
    draw_poligon(selects, fig, m, x, h)
    draw_histogram(selects, fig, m, x, h)


def draw_poligon(selects, fig, m, x, h):
    xs = []
    ys = []
    fig.suptitle('Полигон частот')
    for i in range(m):
        c = 0
        for k in selects:
            if x <= k < (x + h):
                c += 1
        xs.append(x + h / 2)
        ys.append(c / len(selects))
        x += h
    plt.plot(xs, ys, linestyle="--", c="blue")
    plt.show()


def draw_histogram(selects, fig, m, x, h):
    fig.suptitle('Гистограмма частот')
    ax = fig.add_subplot()
    ax.set_xlabel('x')
    ax.set_ylabel('p')
    for i in range(m):
        c = 0
        for k in selects:
            if x <= k < (x + h):
                c += 1
        plt.plot([x, x + h], [c / len(selects) / h, c / len(selects) / h])
        plt.fill_between([x, x + h], [c / len(selects) / h, c / len(selects) / h])
        x += h
    plt.show()


def draw_empirical_function():
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    fig.suptitle('График эмперической функции')
    h = probablyi[0]
    plt.plot([xi[0] - 0.5, xi[0]], [0, 0], c="blue")
    plt.axvline(x=xi[0], c="black", linestyle='--', linewidth=0.5)
    plt.axhline(y=h, c="black", linestyle="--", linewidth=0.5)
    for i in range(len(xi) - 1):
        plt.plot([xi[i], xi[i + 1]], [h, h], c="blue")
        plt.axvline(xi[i], c="black", linestyle='--', linewidth=0.5)
        plt.axhline(y=h, c="black", linestyle="--", linewidth=0.5)
        h += probablyi[i + 1]
    plt.axvline(x=xi[len(xi) - 1], c="black", linestyle='--', linewidth=0.5)
    plt.grid()
    plt.show()


def standard_deviation(variance):
    standard_dev = math.sqrt(variance)
    print(Fore.GREEN + "Среднеквадратичное отклонение: " + Style.RESET_ALL)
    print((float('{:.3f}'.format(standard_dev))))


def math_expectation():
    unique_val = list(set(selection["selection"]))
    unique_val.sort()
    estimation = 0
    n = len(selection["selection"])
    for i in unique_val:
        count = 0
        xi.append(i)
        for j in selection["selection"]:
            if j == i:
                count += 1
        cnti.append(count)
        probablyi.append(count / n)
    for i in range(len(xi)):
        estimation += xi[i] * probablyi[i]
    print(float('{:.3f}'.format(estimation)))
    variance = 0
    for i in range(len(xi)):
        variance += pow(xi[i] - estimation, 2) * probablyi[i]
    variance = variance * (1 / n)
    standard_deviation(variance)


if __name__ == '__main__':
    selection = {"selection": []}
    with open(FILE_INPUT, "rt", encoding="UTF-8") as f:
        for line in f:
            selection["selection"].append(float(line))
    selection["selection"].sort()
    print(Fore.GREEN + "Вариационный ряд: " + Style.RESET_ALL)
    print(selection["selection"])
    print(Fore.GREEN + "Экстремальные значения: " + Style.RESET_ALL)
    print(Fore.YELLOW + "Min = {0}\nMax = {1}".format(selection["selection"][0],
                                                      selection["selection"][
                                                          len(selection["selection"]) - 1]) + Style.RESET_ALL)
    print(Fore.GREEN + "Размах выборки: " + Style.RESET_ALL)
    print(((selection["selection"][len(selection["selection"]) - 1]) + (selection["selection"][0])))
    print(Fore.GREEN + "Оценка математического ожидания: " + Style.RESET_ALL)
    math_expectation()
    draw_empirical_function()
    work_piece()
    empirical_function()
