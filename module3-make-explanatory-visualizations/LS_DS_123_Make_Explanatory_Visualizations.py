#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'module3-make-explanatory-visualizations'))
	#print(os.getcwd())
except:
	pass
#%% [markdown]

#%% [markdown]
# _Lambda School Data Science_
# 
# # Make Explanatory Visualizations
# 
# ### Objectives
# 
# - identify misleading visualizations and how to fix them
# - use Seaborn to visualize distributions and relationships with continuous and discrete variables
# - add emphasis and annotations to transform visualizations from exploratory to explanatory
# - remove clutter from visualizations
# 
# ### Links
# 
# - [How to Spot Visualization Lies](https://flowingdata.com/2017/02/09/how-to-spot-visualization-lies/)
# - [Visual Vocabulary - Vega Edition](http://ft.com/vocabulary)
# - [Choosing a Python Visualization Tool flowchart](http://pbpython.com/python-vis-flowchart.html)
# - [Searborn example gallery](http://seaborn.pydata.org/examples/index.html) & [tutorial](http://seaborn.pydata.org/tutorial.html)
# - [Strong Titles Are The Biggest Bang for Your Buck](http://stephanieevergreen.com/strong-titles/)
# - [Remove to improve (the data-ink ratio)](https://www.darkhorseanalytics.com/blog/data-looks-better-naked)
# - [How to Generate FiveThirtyEight Graphs in Python](https://www.dataquest.io/blog/making-538-plots/)
#%% [markdown]
# # Avoid Misleading Visualizations
# 
# Did you find/discuss any interesting misleading visualizations in your Walkie Talkie?
#%% [markdown]
# ## What makes a visualization misleading?
# 
# [5 Ways Writers Use Misleading Graphs To Manipulate You](https://venngage.com/blog/misleading-graphs/)
#%% [markdown]
# ## Two y-axes
# 
# ![two-y-axis](https://kieranhealy.org/files/misc/two-y-by-four-sm.jpg)
# 
#  
#  Other Examples: 
#  - [Spurious Correlations](https://tylervigen.com/spurious-correlations)
#  - <https://blog.datawrapper.de/dualaxis/>
#  - <https://kieranhealy.org/blog/archives/2016/01/16/two-y-axes/>
#  - <http://www.storytellingwithdata.com/blog/2016/2/1/be-gone-dual-y-axis>
#%% [markdown]
# ##  Y-axis doesn't start at zero.
# 
# <img src="https://i.pinimg.com/originals/22/53/a9/2253a944f54bb61f1983bc076ff33cdd.jpg" width="600">
#%% [markdown]
# ## Pie Charts are bad
# 
# <img src="https://i1.wp.com/flowingdata.com/wp-content/uploads/2009/11/Fox-News-pie-chart.png?fit=620%2C465&ssl=1" width="600">
#%% [markdown]
# ## Pie charts that omit data are extra bad
#  
# - A guy makes a misleading chart that goes viral
# 
#  What does this chart imply at first glance? You don't want your user to have to do a lot of work in order to be able to interpret you graph correctly. You want that first-glance conclusions to be the correct ones.
# 
#  <img src="https://pbs.twimg.com/media/DiaiTLHWsAYAEEX?format=jpg&name=medium" width='600'>
#  
#  <https://twitter.com/michaelbatnick/status/1019680856837849090?lang=en>
#  
# - It gets picked up by overworked journalists (assuming incompetency before malice)
#  
#  <https://www.marketwatch.com/story/this-1-chart-puts-mega-techs-trillions-of-market-value-into-eye-popping-perspective-2018-07-18>
#  
# - Even after the chart's implications have been refuted, it's hard a bad (although compelling) visualization from being passed around.
# 
#  <https://www.linkedin.com/pulse/good-bad-pie-charts-karthik-shashidhar/>
# 
# **["yea I understand a pie chart was probably not the best choice to present this data."](https://twitter.com/michaelbatnick/status/1037036440494985216)**
#%% [markdown]
# ## Pie Charts that compare unrelated things are next-level extra bad
# 
# <img src="http://www.painting-with-numbers.com/download/document/186/170403+Legalizing+Marijuana+Graph.jpg" width="600">
# 
#%% [markdown]
# ## Be careful about how you use volume to represent quantities:
# 
# radius vs diameter vs volume
# 
# <img src="https://static1.squarespace.com/static/5bfc8dbab40b9d7dd9054f41/t/5c32d86e0ebbe80a25873249/1546836082961/5474039-25383714-thumbnail.jpg?format=1500w" width="600">
#%% [markdown]
# ## Don't cherrypick timelines or specific subsets of your data:
# 
# <img src="https://wattsupwiththat.com/wp-content/uploads/2019/02/Figure-1-1.png" width="600">
# 
# Look how specifically the writer has selected what years to show in the legend on the right side.
# 
# <https://wattsupwiththat.com/2019/02/24/strong-arctic-sea-ice-growth-this-year/>
# 
# Try the tool that was used to make the graphic for yourself
# 
# <http://nsidc.org/arcticseaicenews/charctic-interactive-sea-ice-graph/>
#                                                                                            
#%% [markdown]
# ## Use Relative units rather than Absolute Units
# 
# <img src="https://imgs.xkcd.com/comics/heatmap_2x.png" width="600">
#%% [markdown]
# ## Avoid 3D graphs unless having the extra dimension is effective
# 
# Usually you can Split 3D graphs into multiple 2D graphs
# 
# 3D graphs that are interactive can be very cool. (See Plotly and Bokeh)
# 
# <img src="https://thumbor.forbes.com/thumbor/1280x868/https%3A%2F%2Fblogs-images.forbes.com%2Fthumbnails%2Fblog_1855%2Fpt_1855_811_o.jpg%3Ft%3D1339592470" width="600">
#%% [markdown]
# ## Don't go against typical conventions
# 
# <img src="http://www.callingbullshit.org/twittercards/tools_misleading_axes.png" width="600">
#%% [markdown]
# # Tips for choosing an appropriate visualization:
#%% [markdown]
# ## Use Appropriate "Visual Vocabulary"
# 
# [Visual Vocabulary - Vega Edition](http://ft.com/vocabulary)
#%% [markdown]
# ## What are the properties of your data?
# - Is your primary variable of interest continuous or discrete?
# - Is in wide or long (tidy) format?
# - Does your visualization involve multiple variables?
# - How many dimensions do you need to include on your plot?
# 
# Can you express the main idea of your visualization in a single sentence?
# 
# How hard does your visualization make the user work in order to draw the intended conclusion?
#%% [markdown]
# ## Which Visualization tool is most appropriate? 
# 
# [Choosing a Python Visualization Tool flowchart](http://pbpython.com/python-vis-flowchart.html)
#%% [markdown]
# ## Anatomy of a Matplotlib Plot
# 
# ![Axes vs Axis vs Figure - Matplotlib](https://nbviewer.jupyter.org/github/matplotlib/AnatomyOfMatplotlib/blob/master/images/figure_axes_axis_labeled.png)

#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter

np.random.seed(19680801)

X = np.linspace(0.5, 3.5, 100)
Y1 = 3+np.cos(X)
Y2 = 1+np.cos(1+X/0.75)/2
Y3 = np.random.uniform(Y1, Y2, len(X))

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1, aspect=1)


def minor_tick(x, pos):
    if not x % 1.0:
        return ""
    return "%.2f" % x

ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(4))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(4))
ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))

ax.set_xlim(0, 4)
ax.set_ylim(0, 4)

ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=10)
ax.tick_params(which='minor', width=1.0, labelsize=10)
ax.tick_params(which='minor', length=5, labelsize=10, labelcolor='0.25')

ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)

ax.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Blue signal", zorder=10)
ax.plot(X, Y2, c=(1.00, 0.25, 0.25), lw=2, label="Red signal")
ax.plot(X, Y3, linewidth=0,
        marker='o', markerfacecolor='w', markeredgecolor='k')

ax.set_title("Anatomy of a figure", fontsize=20, verticalalignment='bottom')
ax.set_xlabel("X axis label")
ax.set_ylabel("Y axis label")

ax.legend()


def circle(x, y, radius=0.15):
    from matplotlib.patches import Circle
    from matplotlib.patheffects import withStroke
    circle = Circle((x, y), radius, clip_on=False, zorder=10, linewidth=1,
                    edgecolor='black', facecolor=(0, 0, 0, .0125),
                    path_effects=[withStroke(linewidth=5, foreground='w')])
    ax.add_artist(circle)


def text(x, y, text):
    ax.text(x, y, text, backgroundcolor="white",
            ha='center', va='top', weight='bold', color='blue')

# Minor tick
circle(0.50, -0.10)
text(0.50, -0.32, "Minor tick label")

# Major tick
circle(-0.03, 4.00)
text(0.03, 3.80, "Major tick")

# Minor tick
circle(0.00, 3.50)
text(0.00, 3.30, "Minor tick")

# Major tick label
circle(-0.15, 3.00)
text(-0.15, 2.80, "Major tick label")

# X Label
circle(1.80, -0.27)
text(1.80, -0.45, "X axis label")

# Y Label
circle(-0.27, 1.80)
text(-0.27, 1.6, "Y axis label")

# Title
circle(1.60, 4.13)
text(1.60, 3.93, "Title")

# Blue plot
circle(1.75, 2.80)
text(1.75, 2.60, "Line\n(line plot)")

# Red plot
circle(1.20, 0.60)
text(1.20, 0.40, "Line\n(line plot)")

# Scatter plot
circle(3.20, 1.75)
text(3.20, 1.55, "Markers\n(scatter plot)")

# Grid
circle(3.00, 3.00)
text(3.00, 2.80, "Grid")

# Legend
circle(3.70, 3.80)
text(3.70, 3.60, "Legend")

# Axes
circle(0.5, 0.5)
text(0.5, 0.3, "Axes")

# Figure
circle(-0.3, 0.65)
text(-0.3, 0.45, "Figure")

color = 'blue'
ax.annotate('Spines', xy=(4.0, 0.35), xytext=(3.3, 0.5),
            weight='bold', color=color,
            arrowprops=dict(arrowstyle='->',
                            connectionstyle="arc3",
                            color=color))

ax.annotate('', xy=(3.15, 0.0), xytext=(3.45, 0.45),
            weight='bold', color=color,
            arrowprops=dict(arrowstyle='->',
                            connectionstyle="arc3",
                            color=color))

ax.text(4.0, -0.4, "Made with http://matplotlib.org",
        fontsize=10, ha="right", color='.5')

plt.show()

#%% [markdown]
# # Making Explanatory Visualizations with Matplotlib
#%% [markdown]
# Today we will reproduce this [example by FiveThirtyEight:](https://fivethirtyeight.com/features/al-gores-new-movie-exposes-the-big-flaw-in-online-movie-ratings/)
# 
# 

#%%
from IPython.display import display, Image

url = 'https://fivethirtyeight.com/wp-content/uploads/2017/09/mehtahickey-inconvenient-0830-1.png'
example = Image(url=url, width=400)

display(example)

#%% [markdown]
# Using this data: https://github.com/fivethirtyeight/data/tree/master/inconvenient-sequel
#%% [markdown]
# Links
# - [Strong Titles Are The Biggest Bang for Your Buck](http://stephanieevergreen.com/strong-titles/)
# - [Remove to improve (the data-ink ratio)](https://www.darkhorseanalytics.com/blog/data-looks-better-naked)
# - [How to Generate FiveThirtyEight Graphs in Python](https://www.dataquest.io/blog/making-538-plots/)
#%% [markdown]
# ## Make prototypes
# 
# This  helps us understand the problem

#%%
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


plt.style.use('fivethirtyeight')

fake = pd.Series([38, 3, 2, 1, 2, 4, 6, 5, 5, 33], 
                 index=range(1,11))

fake.plot.bar(color='C1', width=0.9);


#%%
fake2 = pd.Series(
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     2, 2, 2, 
     3, 3, 3,
     4, 4,
     5, 5, 5,
     6, 6, 6, 6,
     7, 7, 7, 7, 7,
     8, 8, 8, 8,
     9, 9, 9, 9, 
     10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])

fake2.value_counts().sort_index().plot.bar(color='C1', width=0.9);

#%% [markdown]
# ## Annotate with text

#%%


#%% [markdown]
# ## Reproduce with real data

#%%
df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/inconvenient-sequel/ratings.csv')


#%%



