import matplotlib.pyplot as plt

from mpl_toolkits.axisartist.axislines import AxesZero

fig = plt.figure()
fig.subplots_adjust(right=1)
ax = fig.add_subplot(axes_class=AxesZero)

# Make right and top axis invisible
ax.axis["right"].set_visible(False)
ax.axis["top"].set_visible(False)
ax.axis["left"].set_visible(False)

# Make xzero axis (horizontal axis line through y=0) visible.
ax.axis["xzero"].set_visible(True)
ax.axis["xzero"].label.set_text("Regla (mm³)")

ax.set_xlim(19500, 28500)
ax.set_xlabel("Calibre (mm³)")

# Fill the region between x=20 and x=28 with color orange
ax.fill_betweenx([-4, 0], 20000, 28000, color='orange',
                 alpha=0.3, label='Δ Regla')
ax.fill_betweenx([-4, 0], 27000, 27200, color='blue',
                 alpha=0.4, label='Δ Calibre')


# Plot the data
ax.plot([-2, 3, 2])
ax.set_ylim(-3, 0)

plt.legend(loc='upper left')

ax.axvline(x=27100, color='blue', linestyle='--',
           label='Vertical Line at x=27.1')
ax.axvline(x=24000, color='orange', linestyle='--',
           label='Vertical Line at x=27.1')
plt.show()
