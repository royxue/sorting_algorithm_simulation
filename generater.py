# UWTCSS 598 Master Seminar LIJUN XUE
# Script for generating large datasets for sorting algorithms simulation

import random


class Datasets(object):
    def __init__(self):
        self.list1 = self.fill_list(30000, 29, 1)
        self.list2 = self.fill_list(30000, 37)
        self.list3, self.list4 = self.fetch_natural_data()
        self.list = [self.list1, self.list2, self.list3, self.list4]

    def fill_list(self, length, luckynumber, ntype=0):
        # Fill the list with target list with total number of length numbers 
        # generated from random number(seed is luckynumber)
        random.seed(luckynumber)
        target = []
        for i in range(length):
            if ntype == 0:
                a = random.randint(0, 99999)
            else:
                a = random.random()
            target.append(a)
        return target

    def fetch_natural_data(self):
        # Data resource: http://www.ncdc.noaa.gov/qclcd/QCLCD?prior=N
        # Quality Controlled Local Climatological Data
        # 2015 Month March daily temperature data
        # Use monthly data Tmax and StnPressure
        l1 = []
        l2 = []
        file = open("201503daily.txt")
        line = file.readlines()
        for l in line:
            l = l.split(',')
            try:
                x = int(l[2])
                l1.append(x)
                y = float(l[32])
                l2.append(y)
            except ValueError:
                # print "One unavailable data"
                continue

        return l1, l2
