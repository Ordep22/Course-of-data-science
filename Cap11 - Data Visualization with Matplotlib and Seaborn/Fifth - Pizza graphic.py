import matplotlib.pyplot as plt
import pandas as pd

pices  = [7,2,2,13]
activities = ["sleep","yeat", "go out", "work"]
colors = ['olive','lime','violet','royalblue']

plt.pie(pices, labels= activities, colors= colors, startangle=90, shadow= False, explode= (0,0.2,0,0))
plt.show()