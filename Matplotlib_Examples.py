
# Basic Data Visualization w/ matplotlib

import matplotlib.pyplot as plt
import pandas as pd

# import data
PitcherData = pd.read_csv('PitcherData.csv')

# use to clear any previous plot
plt.clf()

##########

# LINE PLOT
plt.plot(PitcherData['ERA'])
plt.xlabel('ERA Rank Among Qualified Starting Pitchers')
plt.ylabel('Earned Run Average')
plt.show()

##########

# basic SCATTER PLOT
plt.scatter(PitcherData['SwStr'], PitcherData['FIP'])
plt.show()

##########

# SCATTER PLOT w/ CUSTOMIZATIONS
plt.scatter(PitcherData['SwStr'], PitcherData['FIP'], s=50, c = 'red', alpha=0.7)
plt.xlabel('Swinging Strike Rate')
plt.ylabel('Fielding Independent Pitching (FIP)')
plt.title('Effect of Swinging Strike Rate on FIP')
plt.text(.145, 3, 'Scherzer')
plt.text(.085, 6.1, 'Shields')
plt.grid(True)
plt.show()

##########

# HISTOGRAM
plt.hist(PitcherData['WAR'], bins=7)
plt.xlabel('Wins Above Replacement')
plt.ylabel('Count of Pitchers')
plt.show()