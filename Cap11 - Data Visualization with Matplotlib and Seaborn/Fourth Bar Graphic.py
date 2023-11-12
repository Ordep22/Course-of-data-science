import matplotlib.pyplot as plt

ages  = [22,65,45,21,22,34,42,4,99,101,120,122]
bins  = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(ages, bins,histtype = 'bar', rwidth = 0.5)
plt.show()



