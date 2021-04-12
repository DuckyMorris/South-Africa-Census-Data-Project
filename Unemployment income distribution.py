import csv
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
#------------------------------------------------------------------------------------------------------------
def dist(num) :
    test = {}
    a = 0
    with open('person!10pct!sample!v3_F1.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        line_count = 0
        for row in csv_reader:
            if (f'{row[81]}') == num:
                #highincomeearnerage[a] = int(f'{row[3]}')
                test[a] = int(f'{row[41]}')
                a = a +1

            line_count += 1

    t = len(test)
    bracket= [0]*t
    tot = 0
    for x in range(t):
        if test[x] == 99: 
            bracket[x] = 0
        else:
            bracket[x] = test[x]

        if test[x] == 1:
            tot = tot+1
               
    print(len(test))
    plt.hist(bracket, bins=12)
    plt.xlabel('Income Bracket')
    plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12])
    plt.ylabel('')
    plt.title('Showing the income bracket distrinution of the unemployed')
    print(tot, tot/len(test))
    plt.show()
#--------------------------------------------------------------------------------------------- 
dist('2')#unemployment number
