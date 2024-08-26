######################################base2 inc1
import matplotlib.pyplot as plt
import numpy as np
# results on memory_size=220
x = [2, 3, 4, 5, 6, 7, 8 ,9, 10, 11]
y1 = [76.74,46.93,36.27,30.14,24.78,20.76,17.73,15.17,13.89,12.85]
y2 = [74.54,47.65,38.81,26.63,28.17,21.46,15.36,16.81,15.71,12.95]
y3 = [74.37,46.37,39.2,32.92,27.64,24.35,20.02,18.09,16.16,15.03]
y4 = [72.86,54.12,39.24,32.7,28.16,26.31,24.36,23.1,21.17,20.75]
y5 = [70.28,46.67,37.75,34.38,28.85,22.59,18.85,20.09,18.78,17.46]
y6 = [72.9,47.37,43.24,29.27,25.48,17.67,17.99,14.26,12.16,11.85]
y7 = [69.57,49.64,40.54,34.13,28.6,24.33,19.98,19.86,18.38,16.42]
y8 = [72.41,50.75,38.75,32.39,27.66,27.05,23.58,22.76,20.87,19.19]
y9 = [77.57,57.03,42.61,38.34,28.68,25.44,21.93,18.45,17.92,17.98]
y10 = [78.87,59.69,45.52,38.01,32.92,32.51,29.47,27.61,25.84,23.38]

# Create the canvas and coordinate system
fig, ax = plt.subplots()

# Draw a line chart
ax.plot(x, y1, marker='^', markersize=6, label='Finetune')
ax.plot(x, y2, marker='+', markersize=6, label='iCaRL')
ax.plot(x, y3, marker='s', markersize=6, label='GEM')
ax.plot(x, y4, marker='*', markersize=6, label='LUCIR')
ax.plot(x, y5, marker='p', markersize=6, label='Bic')
ax.plot(x, y6, marker='h', markersize=6, label='WA')
ax.plot(x, y7, marker='D', markersize=6, label='Coil')
ax.plot(x, y8, marker='v', markersize=6, label='DER')
ax.plot(x, y9, marker='x', markersize=6, label='Foster')
ax.plot(x, y10, marker='o', markersize=6, label='SiBiCIL')

# Set the axis and step
step = 1
ax.xaxis.set_ticks(np.arange(2, 12, step))
ax.xaxis.set_ticklabels(np.arange(2, 12, step))
ax.tick_params(axis='x', labelsize=14)
ax.tick_params(axis='y', labelsize=14)

# Set the title and axis labels
ax.set_xlabel('Number of Classes', fontsize=16)
ax.set_ylabel('Top-1 accuracy(%)', fontsize=16)
legend = ax.legend(loc='upper right', ncol=2, fontsize=12)
legend.get_frame().set_alpha(0)
legend.get_frame().set_facecolor('none')

# Show grid and save
plt.grid(True, which='both', color='#DDDDDD')
plt.show()
plt.savefig('base2_inc1.eps', format='eps')

######################################base3 inc2
# results on memory_size=220
x = [3, 5, 7, 9, 11]
y1 = [59.69,22.25,19.3,15.05,6.82]
y2 = [55.95,31.5,22.27,20.12,11.88]
y3 = [55.05,30.77,25.38,14.18,13.2]
y4 = [57.88,38.62,28.29,23.76,18.71]
y5 = [57.88,38.62,28.19,24.58,18.43]
y6 = [56.57,37.05,29.09,26.04,22.13]
y7 = [56.98,37.82,29.73,24.58,21.09]
y8 = [58.43,37.61,29.67,23.88,20.33]
y9 = [56.83,38.86,30.84,24.38,18.88]
y10 = [61.38,46.21,31.54,30.39,25.49]

# Create the canvas and coordinate system
fig, ax = plt.subplots()

# Draw a line chart
ax.plot(x, y1, marker='^', markersize=6, label='Finetune')
ax.plot(x, y2, marker='+', markersize=6, label='iCaRL')
ax.plot(x, y3, marker='s', markersize=6, label='GEM')
ax.plot(x, y4, marker='*', markersize=6, label='LUCIR')
ax.plot(x, y5, marker='p', markersize=6, label='Bic')
ax.plot(x, y6, marker='h', markersize=6, label='WA')
ax.plot(x, y7, marker='D', markersize=6, label='Coil')
ax.plot(x, y8, marker='v', markersize=6, label='DER')
ax.plot(x, y9, marker='x', markersize=6, label='Foster')
ax.plot(x, y10, marker='o', markersize=6, label='SiBiCIL')

# Set the axis and step
step = 2
ax.xaxis.set_ticks(np.arange(3, 12, step))
ax.xaxis.set_ticklabels(np.arange(3, 12, step))
ax.tick_params(axis='x', labelsize=14)
ax.tick_params(axis='y', labelsize=14)

# Set the title and axis labels
ax.set_xlabel('Number of Classes', fontsize=16)
ax.set_ylabel('Top-1 accuracy(%)', fontsize=16)
legend = ax.legend(loc='upper right', ncol=2, fontsize=12)
legend.get_frame().set_alpha(0)
legend.get_frame().set_facecolor('none')

# Show grid and save
plt.grid(True, which='both', color='#DDDDDD')
plt.show()
plt.savefig('base3_inc2.eps', format='eps')

######################################base5 inc2
#results on memory_size=220
x = [5, 7, 9, 11]
y1 = [46.59,29.33,19.38,14.62]
y2 = [41.5,30.86,24.41,19.05]
y3 = [41.68,27.18,17.05,15.38]
y4 = [41.74,29.29,25.23,20.44]
y5 = [44.76,32.77,26.6,22.24]
y6 = [42.29,30.67,26.2,21.2]
y7 = [42.61,30.38,24.91,20.92]
y8 = [42.43,32.14,25.11,20.44]
y9 = [40.72,29.71,24.08,19.99]
y10 = [44.68,32.92,30.11,25.68]

# Create the canvas and coordinate system
fig, ax = plt.subplots()

# Draw a line chart
ax.plot(x, y1, marker='^', markersize=6, label='Finetune')
ax.plot(x, y2, marker='+', markersize=6, label='iCaRL')
ax.plot(x, y3, marker='s', markersize=6, label='GEM')
ax.plot(x, y4, marker='*', markersize=6, label='LUCIR')
ax.plot(x, y5, marker='p', markersize=6, label='Bic')
ax.plot(x, y6, marker='h', markersize=6, label='WA')
ax.plot(x, y7, marker='D', markersize=6, label='Coil')
ax.plot(x, y8, marker='v', markersize=6, label='DER')
ax.plot(x, y9, marker='x', markersize=6, label='Foster')
ax.plot(x, y10, marker='o', markersize=6, label='SiBiCIL')

# Set the axis and step
step = 2
ax.xaxis.set_ticks(np.arange(5, 12, step))
ax.xaxis.set_ticklabels(np.arange(5, 12, step))
ax.tick_params(axis='x', labelsize=14)
ax.tick_params(axis='y', labelsize=14)

# Set the title and axis labels
ax.set_xlabel('Number of Classes', fontsize=16)
ax.set_ylabel('Top-1 accuracy(%)', fontsize=16)
legend = ax.legend(loc='upper right', ncol=2, fontsize=12)
legend.get_frame().set_alpha(0)
legend.get_frame().set_facecolor('none')

# Show grid and save
plt.grid(True, which='both', color='#DDDDDD')
plt.show()
plt.savefig('base5_inc2.eps', format='eps')




