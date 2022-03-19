# Databricks notebook source
# MAGIC %matplotlib inline

# COMMAND ----------

# DBTITLE 1,Drawing a simple histogram with default parameters
# libraries & dataset
import seaborn as sns
import matplotlib.pyplot as plt
# set a grey background (use sns.set_theme() if seaborn version 0.11.0 or above) 
sns.set(style="darkgrid")
df = sns.load_dataset("iris")
sns.histplot(data=df, x="sepal_length")
plt.show()

# COMMAND ----------

# DBTITLE 1,You can add a kde curve to a histogram by setting the kde argument to True.
# libraries & dataset
import seaborn as sns
import matplotlib.pyplot as plt
# set a grey background (use sns.set_theme() if seaborn version 0.11.0 or above) 
sns.set(style="darkgrid")
df = sns.load_dataset("iris")

sns.histplot(data=df, x="sepal_length", kde=True)
plt.show()

# COMMAND ----------

# DBTITLE 1,displot does similar things
# libraries & dataset
import seaborn as sns
import matplotlib.pyplot as plt
# set a grey background (use sns.set_theme() if seaborn version 0.11.0 or above) 
sns.set(style="darkgrid")
df = sns.load_dataset("iris")

# note that 'kind' is 'hist' by default
sns.displot(data=df, x="sepal_length", kind='hist', kde=True)
plt.show()

# COMMAND ----------

# DBTITLE 1,More number of bins
# libraries & dataset
import seaborn as sns
import matplotlib.pyplot as plt
# set a grey background (use sns.set_theme() if seaborn version 0.11.0 or above) 
sns.set(style="darkgrid")
df = sns.load_dataset("iris")

sns.histplot(data=df, x="sepal_length", bins=20, kde=True)
plt.show()

# COMMAND ----------

import seaborn as sns;

sns.set_theme()
tips = sns.load_dataset("tips")

sns.displot(data=tips, x="total_bill", kde=True, rug=True)

# COMMAND ----------

import seaborn as sns;

sns.set_theme()
tips = sns.load_dataset("tips")

# Some nonsense about to modify kde args if you want the default
# https://github.com/mwaskom/seaborn/issues/2344
sns.displot(
  data=tips, 
  kind='hist', 
  x="total_bill", 
  rug=True, 
  stat="density"
)
sns.kdeplot(
  data=tips,
  x="total_bill", 
  **{"color": "g", "alpha": 0.3, "linewidth": 1, "shade": True}
)

plt.show()

# COMMAND ----------

# DBTITLE 1,Box plot and hist
# libraries & dataset
import seaborn as sns
import matplotlib.pyplot as plt
# set a grey background (use sns.set_theme() if seaborn version 0.11.0 or above) 
sns.set(style="darkgrid")
df = sns.load_dataset("iris")
 
# creating a figure composed of two matplotlib.Axes objects (ax_box and ax_hist)
f, (ax_box, ax_hist) = plt.subplots(
  2, 
  sharex=True, 
  gridspec_kw={"height_ratios": (.15, .85)}
)
 
# assigning a graph to each ax
sns.boxplot(data=df, x="sepal_length", ax=ax_box)
sns.histplot(data=df, x="sepal_length", ax=ax_hist)
 
# Remove x axis name for the boxplot
ax_box.set(xlabel='')
plt.show()

# COMMAND ----------

# DBTITLE 1,Plotting distributions on the same graph
# libraries & dataset
import seaborn as sns
import matplotlib.pyplot as plt
# set a grey background (use sns.set_theme() if seaborn version 0.11.0 or above) 
sns.set_theme()
df = sns.load_dataset("iris")

sns.histplot(
  data=df, 
  x="sepal_length", 
  color="skyblue",
  label="sepal length",
  kde=True
) 
sns.histplot(
  data=df, x="sepal_width", color="red", label="sepal width", kde=True
)
plt.legend() 
plt.show()

# COMMAND ----------

# DBTITLE 1,grid plot
# libraries & dataset
import seaborn as sns
import matplotlib.pyplot as plt
# set a grey background (use sns.set_theme() if seaborn version 0.11.0 or above) 
sns.set(style="darkgrid")
df = sns.load_dataset("iris")

fig, axs = plt.subplots(2, 2, figsize=(8, 8))

sns.histplot(data=df, x="sepal_length", kde=True, color="skyblue", ax=axs[0, 0])
sns.rugplot(data=df, x="sepal_length", ax=axs[0, 0])

sns.histplot(data=df, x="sepal_width", kde=True, color="olive", ax=axs[0, 1])
sns.rugplot(data=df, x="sepal_width", ax=axs[0, 1])

sns.histplot(data=df, x="petal_length", kde=True, color="gold", ax=axs[1, 0])
sns.rugplot(data=df, x="petal_length", ax=axs[1, 0])

sns.histplot(data=df, x="petal_width", kde=True, color="teal", ax=axs[1, 1])
sns.rugplot(data=df, x="petal_width", ax=axs[1, 1])

plt.show()

# COMMAND ----------

# library & dataset
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="darkgrid")
df = sns.load_dataset('iris')

# I dont know why label only works for scatter
# Custom the inside plot: options are: “scatter” | “reg” | “resid” | “kde” | “hex”
for i,opt in enumerate(["reg", "scatter", "resid", "kde", "hex"]):
  sns.jointplot(x=df["sepal_length"], y=df["sepal_width"], kind=opt, label=opt)
plt.show()
