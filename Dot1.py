# matplotlib
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-2, 2.1, 0.01)

print('x =', x)

y1 = x ** 2
y2 = 0.5*x + 1

print('y1 =', y1)
print('y2 =', y2)

plt.title('lines')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y1, color='red', label='y1')
plt.plot(x, y2, color='blue', label='y2')
plt.legend()


plt.xlim((-2,2))
plt.ylim((0,1))
# plt.xticks(np.linspace(-2, 2, 9))
# plt.yticks(np.linspace(0, 1, 11))

plt.xticks([-2, -1.6, -1.2, -0.8, -0.4, 0, 0.4, 0.8, 1.2, 1.6, 2])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2])


plt.legend(['y=x^2', 'y=0.5*x + 1'])

plt.grid(True)


plt.savefig('./tmp/y=x^2.png')




plt.show()









