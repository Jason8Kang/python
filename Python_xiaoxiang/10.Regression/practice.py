import numpy as np
import matplotlib.pyplot as plt
#
# x=np.linspace(-3,3,10)
# y1=x**2
# y2=2*x+1
# plt.figure()
# plt.plot(x,y1,label='linear line')
# #  plt.figure(num=3,figsize=(8,5))
# plt.plot(x,y2,color="red",linewidth=1.0,linestyle='--',label='square line')
# plt.xlim((-3, 3))
# plt.ylim((-3, 3))
# plt.xlabel('I am x')
# plt.ylabel('I am y')
# new_ticks = np.linspace(-3, 3, 10)
# plt.xticks(new_ticks)
# plt.yticks([-2, -1.8, -1, 1.22, 3],[r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
# ax = plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position("bottom")
# ax.yaxis.set_ticks_position('left')
# ax.spines['bottom'].set_position(('data',-1))
# ax.spines['left'].set_position(('data',0))
# plt.legend(loc='upper left')
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(-3, 3, 50)
# y = 2*x + 1
#
# plt.figure(num=1, figsize=(8, 5),)
# plt.plot(x, y,)
#
# ax = plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.spines['bottom'].set_position(('data', 0))
# ax.yaxis.set_ticks_position('left')
# ax.spines['left'].set_position(('data', 0))
#
# x0 = 1
# y0 = 2*x0 + 1
# #plt.plot([x0, x0,], [0, y0,], 'k--', linewidth=2.5)
# plt.plot([x0, x0], [y0,0 ], 'k--', linewidth=2.5)
# #plt.scatter([x0,], [y0, ], s=50, color='b')
# plt.scatter(x0,y0, s=50, color='b')
# plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
#              textcoords='offset points', fontsize=16,
#              arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
# plt.show()

# n = 1024    # data size
# X = np.random.normal(0, 1, n)
# Y = np.random.normal(0, 1, n)
# T = np.arctan2(Y, X)    # for color later on
#
# plt.scatter(X, Y, s=75, c=T, alpha=.5)
#
# plt.xlim(-1.5, 1.5)
# #plt.xticks(())  # ignore xticks
# plt.ylim(-1.5, 1.5)
# plt.yticks(())  # ignore yticks
#
# plt.show()

#
# n = 12
# X = np.arange(n)
# Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
# Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
#
# plt.bar(X, +Y1)
# plt.bar(X, -Y2)
#
# plt.xlim(-.5, n)
# plt.xticks(())
# plt.ylim(-1.25, 1.25)
# plt.yticks(())
#
# plt.show()
#
# plt.figure(figsize=(6, 4))
# # plt.subplot(n_rows, n_cols, plot_num)
# plt.subplot(2, 2, 1)
# plt.plot([0, 1], [0, 1])
#
# plt.subplot(222)
# plt.plot([0, 1], [0, 2])
#
# plt.subplot(223)
# plt.plot([0, 1], [0, 3])
#
# plt.subplot(224)
# plt.plot([0, 1], [0, 4])
#
# plt.tight_layout()
# plt.show()


plt.figure(figsize=(6, 4))
# plt.subplot(n_rows, n_cols, plot_num)
plt.subplot(2, 1, 1)
# figure splits into 2 rows, 1 col, plot to the 1st sub-fig
plt.plot([0, 1], [0, 1])

plt.subplot(234)
# figure splits into 2 rows, 3 col, plot to the 4th sub-fig
plt.plot([0, 1], [0, 2])

plt.subplot(235)
# figure splits into 2 rows, 3 col, plot to the 5th sub-fig
plt.plot([0, 1], [0, 3])

plt.subplot(236)
# figure splits into 2 rows, 3 col, plot to the 6th sub-fig
plt.plot([0, 1], [0, 4])


plt.tight_layout()
plt.show()