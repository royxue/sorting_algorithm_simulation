# TCSS 598 LIJUN XUE Soring Algos
# For Drawing graphs

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


plt.figure(1)
plt.title("Sythnetic 30000 FLOAT(Runtime X Datasize)")
plt.xlabel("datasize")
plt.ylabel("runtime/sec")
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
quicksort = plt.plot(x, y5, 'y')
patches = [mpatches.Patch(color='r'), mpatches.Patch(color='b'), mpatches.Patch(color='g'), mpatches.Patch(color='k'), mpatches.Patch(color='yellow')]
plt.legend(patches, ('insertionsort', 'selectionsort', 'bubblesort', 'mergesort', 'quicksort'), 'best', fontsize="small", ncol=2)

plt.figure(2)
plt.title("Sythnetic 30000 FLOAT (Runtime X Sortedness)")
plt.xlabel("sortedness")
plt.ylabel("runtime/sec")
x = [14074135, 56212165, 127157218, 224364408]
y1 = [2.44175100327, 9.95923709869, 24.4400219917, 43.5649938583]
y2 = [2.1013600826263428, 10.35594892501831, 33.96936798095703, 70.82162499427795]
y3 = [5.075958013534546, 20.517974853515625, 46.82105302810669, 88.88357400894165]
y4 = [0.05208611488342285, 0.10231304168701172, 0.16138005256652832, 0.22714900970458984]
y5 = [0.03648805618286133, 0.07793593406677246, 0.10253500938415527, 0.10337686538696289]
insertsort = plt.plot(x, y1, 'r')
selectsort = plt.plot(x, y2, 'b')
bubblesort = plt.plot(x, y3, 'g')
mergesort = plt.plot(x, y4, 'k')
quicksort = plt.plot(x, y5, 'y')
patches = [mpatches.Patch(color='r'), mpatches.Patch(color='b'), mpatches.Patch(color='g'), mpatches.Patch(color='k'), mpatches.Patch(color='yellow')]
plt.legend(patches, ('insertionsort', 'selectionsort', 'bubblesort', 'mergesort', 'quicksort'), 'best', fontsize="small", ncol=2)


plt.figure(3)
plt.title("Sythnetic 30000 FLOAT(Memory X Datasize)")
plt.xlabel("datasize")
plt.ylabel("memory/MB")
x = [7500, 15000, 22500, 30000]
y1 = [0.0002, 0.0004, 0.0006, 0.0010]
y2 = [0.0002, 0.0004, 0.0005, 0.0013]
y3 = [0.0002, 0.0004, 0.0007, 0.0011]
y4 = [0.0117, 0.0430, 0.1797, 0.4961]
y5 = [0.1523, 0.2930, 0.6133, 1.2852]
insertsort = plt.plot(x, y1, 'r')
selectsort = plt.plot(x, y2, 'b')
bubblesort = plt.plot(x, y3, 'g')
mergesort = plt.plot(x, y4, 'k')
quicksort = plt.plot(x, y5, 'y')
patches = [mpatches.Patch(color='r'), mpatches.Patch(color='b'), mpatches.Patch(color='g'), mpatches.Patch(color='k'), mpatches.Patch(color='yellow')]
plt.legend(patches, ('insertionsort', 'selectionsort', 'bubblesort', 'mergesort', 'quicksort'), 'best', fontsize="small", ncol=2)

plt.figure(4)
plt.title("Sythnetic 30000 FLOAT (Memory X Sortedness)")
plt.xlabel("sortedness")
plt.ylabel("memory/MB")
x = [14074135, 56212165, 127157218, 224364408]
y1 = [0.0002, 0.0004, 0.0006, 0.0010]
y2 = [0.0002, 0.0004, 0.0005, 0.0013]
y3 = [0.0002, 0.0004, 0.0007, 0.0011]
y4 = [0.0117, 0.0430, 0.1797, 0.4961]
y5 = [0.1523, 0.2930, 0.6133, 1.2852]
insertsort = plt.plot(x, y1, 'r')
selectsort = plt.plot(x, y2, 'b')
bubblesort = plt.plot(x, y3, 'g')
mergesort = plt.plot(x, y4, 'k')
quicksort = plt.plot(x, y5, 'y')
patches = [mpatches.Patch(color='r'), mpatches.Patch(color='b'), mpatches.Patch(color='g'), mpatches.Patch(color='k'), mpatches.Patch(color='yellow')]
plt.legend(patches, ('insertionsort', 'selectionsort', 'bubblesort', 'mergesort', 'quicksort'), 'best', fontsize="small", ncol=2)


# ---------------

plt.figure(5)
plt.title("Sythnetic 30000 INT (Runtime X Datasize)")
plt.xlabel("datasize")
plt.ylabel("runtime/sec")
x = [7500, 15000, 22500, 30000]
y1 = [2.44175100327, 9.95923709869, 24.4400219917, 43.5649938583]
y2 = [1.9015429019927979, 7.939335107803345, 23.03061604499817, 48.071646213531494]
y3 = [4.93612813949585, 20.1737961769104, 46.68593502044678, 85.1890058517456]
y4 = [0.046289920806884766, 0.09889698028564453, 0.151641845703125, 0.2412409782409668]
y5 = [0.032392024993896484, 0.04657888412475586, 0.07185006141662598, 0.14335107803344727]
insertsort = plt.plot(x, y1, 'r')
selectsort = plt.plot(x, y2, 'b')
bubblesort = plt.plot(x, y3, 'g')
mergesort = plt.plot(x, y4, 'k')
quicksort = plt.plot(x, y5, 'y')
patches = [mpatches.Patch(color='r'), mpatches.Patch(color='b'), mpatches.Patch(color='g'), mpatches.Patch(color='k'), mpatches.Patch(color='yellow')]
plt.legend(patches, ('insertionsort', 'selectionsort', 'bubblesort', 'mergesort', 'quicksort'), 'best', fontsize="small", ncol=2)


plt.figure(6)
plt.title("Sythnetic 30000 INT (Runtime X Sortedness)")
plt.xlabel("sortedness")
plt.ylabel("runtime/sec")
x = [13998529, 56632206, 127005317, 225804729]
y1 = [2.44175100327, 9.95923709869, 24.4400219917, 43.5649938583]
y2 = [1.9015429019927979, 7.939335107803345, 23.03061604499817, 48.071646213531494]
y3 = [4.93612813949585, 20.1737961769104, 46.68593502044678, 85.1890058517456]
y4 = [0.046289920806884766, 0.09889698028564453, 0.151641845703125, 0.2412409782409668]
y5 = [0.032392024993896484, 0.04657888412475586, 0.07185006141662598, 0.14335107803344727]
insertsort = plt.plot(x, y1, 'r')
selectsort = plt.plot(x, y2, 'b')
bubblesort = plt.plot(x, y3, 'g')
mergesort = plt.plot(x, y4, 'k')
quicksort = plt.plot(x, y5, 'y')
patches = [mpatches.Patch(color='r'), mpatches.Patch(color='b'), mpatches.Patch(color='g'), mpatches.Patch(color='k'), mpatches.Patch(color='yellow')]
plt.legend(patches, ('insertionsort', 'selectionsort', 'bubblesort', 'mergesort', 'quicksort'), 'best', fontsize="small", ncol=2)


plt.figure(7)
plt.title("Sythnetic 30000 INT(Memory X Datasize)")
plt.xlabel("datasize")
plt.ylabel("memory/MB")
x = [7500, 15000, 22500, 30000]
y1 = [0.0002, 0.0004, 0.0006, 0.0010]
y2 = [0.0001, 0.0004, 0.0005, 0.0013]
y3 = [0.0002, 0.0004, 0.0007, 0.0011]
y4 = [0.0195, 0.0469, 0.8398, 1.0078]
y5 = [0.0823, 0.1877, 0.3752, 0.8012]
insertsort = plt.plot(x, y1, 'r')
selectsort = plt.plot(x, y2, 'b')
bubblesort = plt.plot(x, y3, 'g')
mergesort = plt.plot(x, y4, 'k')
quicksort = plt.plot(x, y5, 'y')
patches = [mpatches.Patch(color='r'), mpatches.Patch(color='b'), mpatches.Patch(color='g'), mpatches.Patch(color='k'), mpatches.Patch(color='yellow')]
plt.legend(patches, ('insertionsort', 'selectionsort', 'bubblesort', 'mergesort', 'quicksort'), 'best', fontsize="small", ncol=2)

plt.figure(8)
plt.title("Sythnetic 30000 INT(Memory X Sortedness)")
plt.xlabel("sortedness")
plt.ylabel("memory/MB")
x = [14074135, 56212165, 127157218, 224364408]
y1 = [0.0002, 0.0004, 0.0006, 0.0010]
y2 = [0.0002, 0.0004, 0.0005, 0.0013]
y3 = [0.0001, 0.0004, 0.0007, 0.0011]
y4 = [0.0195, 0.0469, 0.8398, 1.0078]
y5 = [0.0823, 0.1877, 0.3752, 0.8012]
insertsort = plt.plot(x, y1, 'r')
selectsort = plt.plot(x, y2, 'b')
bubblesort = plt.plot(x, y3, 'g')
mergesort = plt.plot(x, y4, 'k')
quicksort = plt.plot(x, y5, 'y')
patches = [mpatches.Patch(color='r'), mpatches.Patch(color='b'), mpatches.Patch(color='g'), mpatches.Patch(color='k'), mpatches.Patch(color='yellow')]
plt.legend(patches, ('insertionsort', 'selectionsort', 'bubblesort', 'mergesort', 'quicksort'), 'best', fontsize="small", ncol=2)

#-------------------

plt.figure(9)
plt.title("Real Weather 35774 INT(Runtime X Datasize)")
plt.xlabel("datasize")
plt.ylabel("runtime/sec")
x = [8943, 17887, 26830, 35774]
y1 = [2.44175100327, 9.95923709869, 24.4400219917, 43.5649938583]
y2 = [2.1013600826263428, 10.35594892501831, 33.96936798095703, 70.82162499427795]
y3 = [6.79813814163208, 28.477667093276978, 66.6794581413269, 117.88545894622803]
y4 = [0.06885504722595215, 0.15960001945495605, 0.18854808807373047, 0.2502269744873047]
y5 = [0.1178898811340332, 0.44391393661499023, 0.7093470096588135, 1.1623060703277588]
insertsort = plt.plot(x, y1, 'r')
selectsort = plt.plot(x, y2, 'b')
bubblesort = plt.plot(x, y3, 'g')
mergesort = plt.plot(x, y4, 'k')
quicksort = plt.plot(x, y5, 'y')
patches = [mpatches.Patch(color='r'), mpatches.Patch(color='b'), mpatches.Patch(color='g'), mpatches.Patch(color='k'), mpatches.Patch(color='yellow')]
plt.legend(patches, ('insertionsort', 'selectionsort', 'bubblesort', 'mergesort', 'quicksort'), 'best', fontsize="small", ncol=2)


plt.figure(10)
plt.title("Real Weather 35774 INT(Runtime X Sortedness)")
plt.xlabel("sortedness")
plt.ylabel("runtime/sec")
x = [20447543, 84691419, 204933836, 359520943]
y1 = [2.44175100327, 9.95923709869, 24.4400219917, 43.5649938583]
y2 = [2.1013600826263428, 10.35594892501831, 33.96936798095703, 70.82162499427795]
y3 = [6.79813814163208, 28.477667093276978, 66.6794581413269, 117.88545894622803]
y4 = [0.06885504722595215, 0.15960001945495605, 0.18854808807373047, 0.2502269744873047]
y5 = [0.1178898811340332, 0.44391393661499023, 0.7093470096588135, 1.1623060703277588]
insertsort = plt.plot(x, y1, 'r')
selectsort = plt.plot(x, y2, 'b')
bubblesort = plt.plot(x, y3, 'g')
mergesort = plt.plot(x, y4, 'k')
quicksort = plt.plot(x, y5, 'y')
patches = [mpatches.Patch(color='r'), mpatches.Patch(color='b'), mpatches.Patch(color='g'), mpatches.Patch(color='k'), mpatches.Patch(color='yellow')]
plt.legend(patches, ('insertionsort', 'selectionsort', 'bubblesort', 'mergesort', 'quicksort'), 'best', fontsize="small", ncol=2)


plt.figure(11)
plt.title("Real Weather 35774 INT(Memory X Datasize)")
plt.xlabel("datasize")
plt.ylabel("memory/MB")
x = [8943, 17887, 26830, 35774]
y1 = [0.0002, 0.0004, 0.0006, 0.0010]
y2 = [0.0002, 0.0004, 0.0005, 0.0013]
y3 = [0.0002, 0.0004, 0.0007, 0.0011]
y4 = [0.7656, 0.9297, 1.2422, 1.2891]
y5 = [1.1523, 1.4512, 2.0200, 2.8721]
insertsort = plt.plot(x, y1, 'r')
selectsort = plt.plot(x, y2, 'b')
bubblesort = plt.plot(x, y3, 'g')
mergesort = plt.plot(x, y4, 'k')
quicksort = plt.plot(x, y5, 'y')
patches = [mpatches.Patch(color='r'), mpatches.Patch(color='b'), mpatches.Patch(color='g'), mpatches.Patch(color='k'), mpatches.Patch(color='yellow')]
plt.legend(patches, ('insertionsort', 'selectionsort', 'bubblesort', 'mergesort', 'quicksort'), 'best', fontsize="small", ncol=2)


plt.figure(12)
plt.title("Real Weather 35774 INT(Memory X Sortedness)")
plt.xlabel("sortedness")
plt.ylabel("memory/MB")
x = [20447543, 84691419, 204933836, 359520943]
y1 = [0.0002, 0.0003, 0.0006, 0.0010]
y2 = [0.0002, 0.0004, 0.0005, 0.0013]
y3 = [0.0002, 0.0004, 0.0007, 0.0011]
y4 = [0.7656, 0.9297, 1.2422, 1.2891]
y5 = [1.1523, 1.4512, 2.0200, 2.8721]
insertsort = plt.plot(x, y1, 'r')
selectsort = plt.plot(x, y2, 'b')
bubblesort = plt.plot(x, y3, 'g')
mergesort = plt.plot(x, y4, 'k')
quicksort = plt.plot(x, y5, 'y')
patches = [mpatches.Patch(color='r'), mpatches.Patch(color='b'), mpatches.Patch(color='g'), mpatches.Patch(color='k'), mpatches.Patch(color='yellow')]
plt.legend(patches, ('insertionsort', 'selectionsort', 'bubblesort', 'mergesort', 'quicksort'), 'best', fontsize="small", ncol=2)


# ---------


plt.figure(13)
plt.title("Real Weather 30997 INT(Runtime X Datasize)")
plt.xlabel("datasize")
plt.ylabel("runtime/sec")
x = [7749, 15498, 23247, 30997]
y1 = [2.44175100327, 9.95923709869, 24.4400219917, 43.5649938583]
y2 = [2.1013600826263428, 10.35594892501831, 33.96936798095703, 70.82162499427795]
y3 = [4.4419169425964355, 22.545562982559204, 51.350425004959106, 88.85157704353333]
y4 = [0.07030916213989258, 0.1486220359802246, 0.16873908042907715, 0.23950600624084473]
y5 = [0.06801915168762207, 0.13188600540161133, 0.27994608879089355, 0.33770084381103516]
insertsort = plt.plot(x, y1, 'r')
selectsort = plt.plot(x, y2, 'b')
bubblesort = plt.plot(x, y3, 'g')
mergesort = plt.plot(x, y4, 'k')
quicksort = plt.plot(x, y5, 'y')
patches = [mpatches.Patch(color='r'), mpatches.Patch(color='b'), mpatches.Patch(color='g'), mpatches.Patch(color='k'), mpatches.Patch(color='yellow')]
plt.legend(patches, ('insertionsort', 'selectionsort', 'bubblesort', 'mergesort', 'quicksort'), 'best', fontsize="small", ncol=2)

plt.figure(14)
plt.title("Real Weather 30997 INT(Runtime X Sortedness)")
plt.xlabel("sortedness")
plt.ylabel("runtime/sec")
x = [9837125, 64390700, 138427355, 249204909]
y1 = [2.44175100327, 9.95923709869, 24.4400219917, 43.5649938583]
y2 = [2.1013600826263428, 10.35594892501831, 33.96936798095703, 70.82162499427795]
y3 = [4.4419169425964355, 22.545562982559204, 51.350425004959106, 88.85157704353333]
y4 = [0.07030916213989258, 0.1486220359802246, 0.16873908042907715, 0.23950600624084473]
y5 = [0.06801915168762207, 0.13188600540161133, 0.27994608879089355, 0.33770084381103516]
insertsort = plt.plot(x, y1, 'r')
selectsort = plt.plot(x, y2, 'b')
bubblesort = plt.plot(x, y3, 'g')
mergesort = plt.plot(x, y4, 'k')
quicksort = plt.plot(x, y5, 'y')
patches = [mpatches.Patch(color='r'), mpatches.Patch(color='b'), mpatches.Patch(color='g'), mpatches.Patch(color='k'), mpatches.Patch(color='yellow')]
plt.legend(patches, ('insertionsort', 'selectionsort', 'bubblesort', 'mergesort', 'quicksort'), 'best', fontsize="small", ncol=2)


plt.figure(15)
plt.title("Real Weather 30997 INT(Memory X Datasize)")
plt.xlabel("datasize")
plt.ylabel("memory/MB")
x = [7749, 15498, 23247, 30997]
y1 = [0.0002, 0.0004, 0.0006, 0.0010]
y2 = [0.0002, 0.0004, 0.0005, 0.0013]
y3 = [0.0002, 0.0003, 0.0007, 0.0011]
y4 = [0.7773, 0.9124, 1.0432, 1.3942]
y5 = [1.0117, 1.3729, 1.8523, 2.2311]
insertsort = plt.plot(x, y1, 'r')
selectsort = plt.plot(x, y2, 'b')
bubblesort = plt.plot(x, y3, 'g')
mergesort = plt.plot(x, y4, 'k')
quicksort = plt.plot(x, y5, 'y')
patches = [mpatches.Patch(color='r'), mpatches.Patch(color='b'), mpatches.Patch(color='g'), mpatches.Patch(color='k'), mpatches.Patch(color='yellow')]
plt.legend(patches, ('insertionsort', 'selectionsort', 'bubblesort', 'mergesort', 'quicksort'), 'best', fontsize="small", ncol=2)

plt.figure(16)
plt.title("Real Weather 30997 INT(Runtime X Sortedness)")
plt.xlabel("sortedness")
plt.ylabel("memory/MB")
x = [9837125, 64390700, 138427355, 249204909]
y1 = [0.0002, 0.0004, 0.0006, 0.0014]
y2 = [0.0003, 0.0004, 0.0005, 0.0013]
y3 = [0.0002, 0.0004, 0.0007, 0.0011]
y4 = [0.7773, 0.9124, 1.0432, 1.3942]
y5 = [1.0117, 1.3729, 1.8523, 2.2311]
insertsort = plt.plot(x, y1, 'r')
selectsort = plt.plot(x, y2, 'b')
bubblesort = plt.plot(x, y3, 'g')
mergesort = plt.plot(x, y4, 'k')
quicksort = plt.plot(x, y5, 'y')
patches = [mpatches.Patch(color='r'), mpatches.Patch(color='b'), mpatches.Patch(color='g'), mpatches.Patch(color='k'), mpatches.Patch(color='yellow')]
plt.legend(patches, ('insertionsort', 'selectionsort', 'bubblesort', 'mergesort', 'quicksort'), 'best', fontsize="small", ncol=2)


plt.show()