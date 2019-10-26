from math import pi
import numpy as np
import matplotlib.pyplot as plt
import random

def main():
    #Входные данные
    m = 7
    n = 2
    alpha = 5
    X = alpha*np.random.random((m,n))
    #Генератор точек Парето P
    P = np.vectorize(random.paretovariate)(X)
    #P = np.vectorize(random.paretovariate)(alpha*np.ones((m,n)))
    #Отображение
    lag = 2*pi/m
    angles = np.arange(0, 2*pi , lag)
    fig = plt.figure(figsize=(10,5))
    ax = fig.add_subplot(120+1, projection='polar')
    for i in range(n):
        rgb = np.random.random(3)
        #X[i]
        #ax.plot(angles, X[:,i], color=rgb, linewidth=1.)
        #ax.plot((angles[-1],angles[0]),(X[-1,i],X[0,i]), color=rgb, linewidth=1.)
        #P[i]
        ax.plot(angles, P[:,i], color=rgb, linewidth=1.)
        ax.plot((angles[-1],angles[0]),(P[-1,i],P[0,i]), color=rgb, linewidth=1.)

    #Координаты шли против часовой стрелки, поставим ох по часовой
    ax.set_theta_direction(-1)
    #Поставим начало сверху
    ax.set_theta_offset(pi/2)
    #Делим окружность на m кусков
    ax.set_xticks(np.arange(0, 2*pi, lag))

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
