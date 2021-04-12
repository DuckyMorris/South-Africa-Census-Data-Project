import csv
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew 
import numpy as np  
import pylab as p  
#------------------------------------------------------------------------------------------------------------
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
#-------------------------------------------------------------------------------------------------
def dist(num) :
    test = {}
    a = 0
    with open('person!10pct!sample!v3_F1.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        line_count = 0
        for row in csv_reader:
            if (f'{row[41]}') == num:
                #highincomeearnerage[a] = int(f'{row[3]}')
                test[a] = int(f'{row[3]}')
                a = a +1

            line_count += 1

    t = len(test)
    highincomeearnerage = [0]*t
    for x in range(t):
        highincomeearnerage[x] = test[x]
        
    #---------------------------------------------------------------------------------------------        
    plt.hist(highincomeearnerage, bins=max(highincomeearnerage) - min(highincomeearnerage)+1)
    plt.xlabel('Age')
    plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120,125, 130])
    plt.xticks(rotation = 90)
    plt.ylabel('Number of people earning in the "' + num +'" income bracket')
    plt.title('Histogram showing income age distribution for the "'+num+'" income bracket')
    plt.show()
    print("Skewness of income bracket " + num + " is " + str(skew(highincomeearnerage)))

dist('99')
dist('1')
dist('2')
dist('3')
dist('4')
dist('5')
dist('6')
dist('7')
dist('8')
dist('9')
dist('10')
dist('11')
dist('12')


