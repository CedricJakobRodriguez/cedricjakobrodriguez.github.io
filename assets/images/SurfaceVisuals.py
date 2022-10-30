# Import packages
#%matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Import AFM data
afm_data = np.loadtxt('./afm.txt')

# Print some of the AFM data
# print(afm_data[0:5])>>> [[4.8379e-08 4.7485e-08 4.6752e-08 ... 6.0293e-08 5.7804e-08 5.4779e-08]
#  [5.0034e-08 4.9139e-08 4.7975e-08 ... 5.7221e-08 5.4744e-08 5.1316e-08]
#  [5.2966e-08 5.2099e-08 5.1076e-08 ... 5.4061e-08 5.0873e-08 4.7128e-08]
#  [5.7146e-08 5.6070e-08 5.4871e-08 ... 5.1104e-08 4.6898e-08 4.1961e-08]
#  [6.2167e-08 6.0804e-08 5.9588e-08 ... 4.7038e-08 4.2115e-08 3.7258e-08]]

 # Convert data to nanometers (nm)
afm_data *= (10**9)

# Edit overall plot parameters# Font parameters
mpl.rcParams['font.family'] = 'Avenir'
mpl.rcParams['font.size'] = 18# Edit axes parameters
mpl.rcParams['axes.linewidth'] = 2# Tick properties
mpl.rcParams['xtick.major.size'] = 10
mpl.rcParams['xtick.major.width'] = 2
mpl.rcParams['xtick.direction'] = 'out'
mpl.rcParams['ytick.major.size'] = 10
mpl.rcParams['ytick.major.width'] = 2
mpl.rcParams['ytick.direction'] = 'out'

# Create figure and add axis
fig = plt.figure(figsize=(8,6))
ax = plt.subplot(111, projection='3d')

# Remove gray panes and axis grid
ax.xaxis.pane.fill = False
ax.xaxis.pane.set_edgecolor('white')
ax.yaxis.pane.fill = False
ax.yaxis.pane.set_edgecolor('white')
ax.zaxis.pane.fill = False
ax.zaxis.pane.set_edgecolor('white')
ax.grid(False)# Remove z-axis
ax.w_zaxis.line.set_lw(0.)
ax.set_zticks([])

# Create meshgrid
X, Y = np.meshgrid(np.linspace(0, 2, len(afm_data)), np.linspace(0, 2, len(afm_data)))

# Plot surface
plot = ax.plot_surface(X=X, Y=Y, Z=afm_data, cmap='viridis', vmin=0, vmax=200)

# Adjust plot view
ax.view_init(elev=50, azim=225)
ax.dist=11

# # Add colorbar
# cbar = fig.colorbar(plot, ax=ax, shrink=0.6)
# cbar.set_ticks([0, 50, 100, 150, 200])
# cbar.set_ticklabels(['0', '50', '100', '150', '200 nm'])

# Set tick marks
ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(0.5))
ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(0.5))# Set axis labels
# ax.set_xlabel(r'$\mathregular{\mu}$m', labelpad=20)
# ax.set_ylabel(r'$\mathregular{\mu}$m', labelpad=20)# Set z-limit
ax.set_zlim(50, 200)


plt.show()
# fig.show()
print("done")