from math import cos, sin, tan, log
import matplotlib.pyplot as plt
from numpy import arange
import sys
from PyQt5 import QtWidgets, uic


def ctg(x):
    return 1 / tan(x)


ln = log
tg = tan


def red_func(st_func):  # str
    """Редактор функий - редактитирует функции
    для упрощения их обработки"""
    st_func: str
    st_func = st_func.lower()

    f = [["^", "**"], [" ", ""], [":", "/"], [',', '.']]
    for i in f:
        st_func = st_func.replace(i[0], i[1])

    ex = {'5', '2', '9', '6', '+', '-', '*', '8', '/', '7',
          '4', '1', '0', '3'}  # exeption
    st_func2 = list(st_func)
    for i in range(len(st_func2)):
        if st_func2[i] in "1234567890x":
            if i > 0 and not st_func2[i - 1][0] in ex and st_func2[i - 1][0] != "(":
                st_func2[i - 1] += "*"
            if i < len(st_func2) - 1 and not st_func2[i + 1][0] in ex and st_func2[i + 1][0] != ")":
                st_func2[i] += "*"
    st_func = "".join(st_func2)

    return st_func


def graph_built(form=str, x_l=None, y_l=None):
    if y_l is None:
        y_l = (-10, 10)
    if x_l is None:
        x_l = (-10, 10)

    x = [round(i, 2) for i in arange(x_l[0], x_l[1], 0.01) if round(i, 2) != 0]
    y = [round(eval(form.replace("x", "i")), 5) for i in x]

    plt.xlim(x_l)
    plt.ylim(y_l)

    if x_l[0] < 0 < x_l[1]:
        plt.plot(x_l, (0, 0), color="grey")
    if y_l[0] < 0 < y_l[1]:
        plt.plot((0, 0), y_l, color="grey")

    plt.plot(x, y)
    plt.title(form)
    plt.grid(True)
    plt.show()


def st():
    if win.Form_line.text() != "":
        x_lims = (int(win.x_ot.text()), int(win.x_do.text()))
        y_lims = (int(win.y_ot.text()), int(win.y_do.text()))
        func = red_func(win.Form_line.text())
        graph_built(func, x_lims, y_lims)
    else:
        pass


def main():
    global win
    app = QtWidgets.QApplication([])
    win = uic.loadUi("graph.ui")
    win.btn.clicked.connect(st)
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
