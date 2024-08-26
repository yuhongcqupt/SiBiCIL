import matplotlib.pyplot as plt
import numpy as np

# Method list
methods = ['SiBiCIL', 'Foster', 'DER', 'Coil', 'WA', 'LUCIR', 'GEM', 'iCaRL']

# Create a Figure object with five subgraphs arranged horizontally
fig, axs = plt.subplots(1, 5, figsize=(20, 5))

# Data for different subgraphs
data_sets = [
    {
        'memory_values_A': [3.74, 3.74, 3.74, 3.74, 3.74, 3.74, 3.74, 3.74],
        'free_memory_B': [0, 0, 0, 0, 0, 0, 0, 0],
        'Average accuracy': [39.38, 29.74, 31.95, 31.85, 26.03, 35.05, 30.61, 28.59],
        'percent': [100, 100, 100, 100, 100, 100, 100, 100],
        'memory_line': 3.74,
        'y1': 4.6,
        'y2': 100,
        'memory_size': 3
    },
    # different data for each subgraph
    {
        'memory_values_A': [3.74, 6.23, 6.23, 6.23, 6.23, 6.23, 6.23, 6.23],
        'free_memory_B': [2.49, 0, 0, 0, 0, 0, 0, 0],
        'Average accuracy': [39.38, 32.17, 33.48, 30.7, 28.31, 34.25, 30.7, 29.87],
        'percent': [60, 100, 100, 100, 100, 100, 100, 100],
        'memory_line': 6.23,
        'y1': 7.5,
        'y2': 100,
        'memory_size': 5
    },
    # different data for each subgraph
    {
        'memory_values_A': [3.74, 9.97, 9.97, 9.97, 9.97, 9.97, 9.97, 9.97],
        'free_memory_B': [6.23, 0, 0, 0, 0, 0, 0, 0],
        'Average accuracy': [39.38, 30.31, 34.85, 30.05, 29.78, 33.59, 28.22, 30.91],
        'percent': [38, 100, 100, 100, 100, 100, 100, 100],
        'memory_line': 9.97,
        'y1': 12,
        'y2': 100,
        'memory_size': 8
    },
    # different data for each subgraph
    {
        'memory_values_A': [3.74, 12.46, 12.46, 12.46, 12.46, 12.46, 12.46, 12.46],
        'free_memory_B': [8.72, 0, 0, 0, 0, 0, 0, 0],
        'Average accuracy': [39.38, 30.81, 33.36, 32.41, 30.00, 34.96, 30.14, 28.92],
        'percent': [30, 100, 100, 100, 100, 100, 100, 100],
        'memory_line': 12.46,
        'y1': 15,
        'y2': 100,
        'memory_size': 10
    },
    # different data for each subgraph
    {
        'memory_values_A': [3.74, 24.92, 24.92, 24.92, 24.92, 24.92, 24.92, 24.92],
        'free_memory_B': [21.18, 0, 0, 0, 0, 0, 0, 0],
        'Average accuracy': [39.38, 34.6, 33.54, 32.15, 29.22, 34.28, 31.42, 29.81],
        'percent': [15, 100, 100, 100, 100, 100, 100, 100],
        'memory_line': 24.92,
        'y1': 30,
        'y2': 100,
        'memory_size': 20
    },
]

# Column width
width = 0.4

# X-axis coordinates, in order
x = np.arange(1, len(methods) + 1)

# Draw five subplots
for i in range(5):

    # Gets the data for the current subgraph
    data = data_sets[i]

    # Draw a bar chart in the subgraph
    custom_blue = '#2F4F4F'
    bars1 = axs[i].bar(x, data['memory_values_A'], width, label='Buffer budget', color=custom_blue)
    bars2 = axs[i].bar(x, data['free_memory_B'], width, color='#C0C0C0', bottom=data['memory_values_A'], label='Free memory_size')

    # dd a Memory splitter
    #axs[i].axhline(y=data['memory_line'], color='red', linestyle='--', label='Memory_size')
    axs[i].axhline(y=data['memory_line'], color='red', linestyle='--', label=f'Memory_size={data["memory_size"]}/class')

    # Set the X-axis label
    axs[i].set_xlabel('Methods')

    # Set the Y-axis label
    axs[i].set_ylabel('Buffer budget(KB)')
    axs[i].set_ylim(0, data['y1'])

    # Add the another Y-axis
    ax2 = axs[i].twinx()
    ax2.set_ylabel('Average accuracy')
    ax2.set_ylim(0, 100)

    # Connect the ACC values with a polyline
    ax2.plot(x, data['Average accuracy'], marker='o', label='Average accuracy', color='#D2691E')

    # Set the X-axis scale
    axs[i].set_xticks(x)
    axs[i].set_xticklabels(methods, rotation=45)

    # Add the legend
    lines, labels = axs[i].get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    custom_lines = [lines[1], lines[2], lines[0], lines2[0]]
    custom_labels = [labels[1], labels[2], labels[0], labels2[0]]
    axs[i].legend(custom_lines, custom_labels, loc='best')
    axs[i].invert_xaxis()

    # Displays the percent value above the red dotted line
    font_style = 'italic'
    for j, percent_value in enumerate(data['percent']):
        axs[i].text(j + 1, data['memory_line'] + 0.2, f'{percent_value}%', ha='center', va='bottom', color='black', rotation=45)

# show and save
plt.tight_layout()
plt.savefig('buffer_base2_inc1.eps', format='eps')
plt.show()
