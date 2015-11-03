import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.figure(1)
plt.title("Sythnetic 30000 FLOAT(Runtime X Datasize)")
plt.xlabel("datasize")
plt.ylabel("runtime")
x = [7500, 15000, 22500, 30000]
y1 = [2.44175100327, 9.95923709869, 24.4400219917, 43.5649938583]
y2 = [2.1013600826263428, 10.35594892501831, 33.96936798095703, 70.82162499427795]
y3 = [5.075958013534546, 20.517974853515625, 46.82105302810669, 88.88357400894165]
y4 = [0.05208611488342285, 0.10231304168701172, 0.16138005256652832, 0.22714900970458984]
y5 = [0.03648805618286133, 0.07793593406677246, 0.10253500938415527, 0.10337686538696289]
insertsort = plt.plot(x, y1, 'r')
selectsort = plt.plot(x, y2, 'b')
bubblesort = plt.plot(x, y3, 'g')
mergesort = plt.plot(x, y4, 'k')
quicksort = plt.plot(x, y5, 'y', label='quci')
patches = [mpatches.Patch(color='r'), mpatches.Patch(color='b'), mpatches.Patch(color='g'), mpatches.Patch(color='k'), mpatches.Patch(color='yellow')]
plt.legend(patches, ('insertionsort', 'selectionsort', 'bubblesort', 'mergesort', 'quicksort'), 'best', fontsize="small", ncol=2)


plt.show()