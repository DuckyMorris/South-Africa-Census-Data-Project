import csv
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter



def dist() :
    Income = [[],[],[],[]]
    with open('person!10pct!sample!v3_F1.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        line_count = 0
        for row in csv_reader:
            if int(f'{row[3]}') > 19 and int(f'{row[3]}')<30:
                if ((f'{row[37]}') == '3' or (f'{row[37]}') == '2') and ((f'{row[39]}') == '3' or (f'{row[39]}') == '2'):
                    if int(f'{row[41]}') != 99:
                        Income[0].append(int(f'{row[41]}'))
                        
                if ((f'{row[37]}') == '2' or (f'{row[37]}') == '3') and ((f'{row[39]}') == '1'):
                    if int(f'{row[41]}') != 99:
                        Income[1].append(int(f'{row[41]}'))

                if ((f'{row[37]}') == '1') and ((f'{row[39]}') == '3' or (f'{row[39]}') == '2'):
                    if int(f'{row[41]}') != 99:
                        Income[2].append(int(f'{row[41]}'))

                if ((f'{row[37]}') == '1') and ((f'{row[39]}') == '1'):
                    if int(f'{row[41]}') != 99:
                        Income[3].append(int(f'{row[41]}'))
                    
                
                
            
            line_count += 1
   
    #---------------------------------------------------------------------------------------------        
    y_pos = np.arange(12)
##    plt.hist(Income[0], weights=np.ones(len(Income[0])) / len(Income[0]), bins=11)
##    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
##    plt.xlabel('Level of Income')
##    #plt.xticks(y_pos,["Grade 0","Grade 1","Grade 2","Grade 3","Grade 4","Grade 5","Grade 6","Grade 7","Grade 8","Grade 9","Grade 10","Grade 11","Grade 12","N1","N2","N3","N4","N5","N6","Certificate no Gr12","Certificate + Gr12","Diploma + Gr12","Higher Diploma","Post Higher Diploma","Bachelors Degree","Bachelors + Diploma","Honours Degree","Higher Degree","Other","No Schooling"])
##    plt.xticks(y_pos,["","No Income","R 1 - R 4800","R 4801 - R 9600","R 9601 - R 19200 ","R 19201 - R 38400","R 38401 - R 76800","R 76801 - R 153600","R 153601 - R 307200","R 307201 - R 614400","R 614401- R 1228800","R 1228801 - R 2457600 ","R2457601 or more"])
##    plt.xticks(rotation = 90)
##    plt.xticks(fontsize=5)
##    plt.ylabel('Percentage')
##    plt.title('Level of Income With No Parents')
##    plt.show()
##
##
##    plt.hist(Income[1], weights=np.ones(len(Income[1])) / len(Income[1]), bins =11)
##    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
##    plt.xlabel('Level of Income')
##    #plt.xticks(y_pos,["Grade 0","Grade 1","Grade 2","Grade 3","Grade 4","Grade 5","Grade 6","Grade 7","Grade 8","Grade 9","Grade 10","Grade 11","Grade 12","N1","N2","N3","N4","N5","N6","Certificate no Gr12","Certificate + Gr12","Diploma + Gr12","Higher Diploma","Post Higher Diploma","Bachelors Degree","Bachelors + Diploma","Honours Degree","Higher Degree","Other","No Schooling"])
##    plt.xticks(y_pos,["","No Income","R 1 - R 4800","R 4801 - R 9600","R 9601 - R 19200 ","R 19201 - R 38400","R 38401 - R 76800","R 76801 - R 153600","R 153601 - R 307200","R 307201 - R 614400","R 614401- R 1228800","R 1228801 - R 2457600 ","R2457601 or more"])
##
##    plt.xticks(rotation = 90)
##    plt.xticks(fontsize=5)
##    plt.ylabel('Percentage')
##    plt.title('Level of Income With Only A Father')
##    plt.show()
##
##    #y_pos = np.arange(31)
##    plt.hist(Income[2], weights=np.ones(len(Income[2])) / len(Income[2]), bins = 11)
##    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
##    plt.xlabel('Level of Income')
##    #plt.xticks(y_pos,["Grade 0","Grade 1","Grade 2","Grade 3","Grade 4","Grade 5","Grade 6","Grade 7","Grade 8","Grade 9","Grade 10","Grade 11","Grade 12","N1","N2","N3","N4","N5","N6","Certificate no Gr12","Certificate + Gr12","Diploma + Gr12","Higher Diploma","Post Higher Diploma","Bachelors Degree","Bachelors + Diploma","Honours Degree","Higher Degree","Other","No Schooling"])
##    plt.xticks(y_pos,["","No Income","R 1 - R 4800","R 4801 - R 9600","R 9601 - R 19200 ","R 19201 - R 38400","R 38401 - R 76800","R 76801 - R 153600","R 153601 - R 307200","R 307201 - R 614400","R 614401- R 1228800","R 1228801 - R 2457600 ","R2457601 or more"])
##
##    plt.xticks(rotation = 90)
##    plt.xticks(fontsize=4)
##    plt.ylabel('Number')
##    plt.title('Level of Income With Only A Mother')
##    plt.show()
##
##    #s = np.arange(31)
##    plt.hist(Income[3], weights=np.ones(len(Income[3])) / len(Income[3]), bins = 11)
##    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
##    plt.xlabel('Level of Income')
##    #plt.xticks(y_pos,["Grade 0","Grade 1","Grade 2","Grade 3","Grade 4","Grade 5","Grade 6","Grade 7","Grade 8","Grade 9","Grade 10","Grade 11","Grade 12","N1","N2","N3","N4","N5","N6","Certificate no Gr12","Certificate + Gr12","Diploma + Gr12","Higher Diploma","Post Higher Diploma","Bachelors Degree","Bachelors + Diploma","Honours Degree","Higher Degree","Other","No Schooling"])
##    plt.xticks(y_pos,["","No Income","R 1 - R 4800","R 4801 - R 9600","R 9601 - R 19200 ","R 19201 - R 38400","R 38401 - R 76800","R 76801 - R 153600","R 153601 - R 307200","R 307201 - R 614400","R 614401- R 1228800","R 1228801 - R 2457600 ","R2457601 or more"])
##
##    plt.xticks(rotation = 90)
##    plt.xticks(fontsize=4)
##    plt.ylabel('Percentage')
##    plt.title('Level of Income With Both Parents')
##    plt.show()

    #y_pos = np.arange(31)
    plt.hist(Income[0], label = 'No Parents', weights=np.ones(len(Income[0])) / len(Income[0]), bins = 11, alpha = 0.5)
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))

    #plt.hist(Income[2],  label = 'Mother Only',weights=np.ones(len(Income[2])) / len(Income[2]), bins = 11, alpha = 0.5)
    #plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    
    #plt.hist(Income[1], label = 'Father Only',weights=np.ones(len(Income[1])) / len(Income[1]), bins = 11, alpha = 0.5)
    #plt.gca().yaxis.set_major_formatter(PercentFormatter(1))

    plt.hist(Income[3], label = 'Both Parents', weights=np.ones(len(Income[3])) / len(Income[3]), bins = 11, alpha = 0.5)
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))


    plt.xlabel('Level of Income')
    #plt.xticks(y_pos,["Grade 0","Grade 1","Grade 2","Grade 3","Grade 4","Grade 5","Grade 6","Grade 7","Grade 8","Grade 9","Grade 10","Grade 11","Grade 12","N1","N2","N3","N4","N5","N6","Certificate no Gr12","Certificate + Gr12","Diploma + Gr12","Higher Diploma","Post Higher Diploma","Bachelors Degree","Bachelors + Diploma","Honours Degree","Higher Degree","Other","No Schooling"])
    plt.xticks(y_pos,["","No Income","R 1 - R 4800","R 4801 - R 9600","R 9601 - R 19200 ","R 19201 - R 38400","R 38401 - R 76800","R 76801 - R 153600","R 153601 - R 307200","R 307201 - R 614400","R 614401- R 1228800","R 1228801 - R 2457600 ","R2457601 or more"])

    plt.xticks(rotation = 90)
    plt.xticks(fontsize=4)
    plt.ylabel('Percentage')
    plt.title('Relative Percentage of all')
    plt.legend()
    plt.show()


    plt.hist(Income[3], label = 'Both Parents', weights=np.ones(len(Income[3])) / len(Income[3]), bins = 11, alpha = 0.5)
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    
    plt.hist(Income[0], label = 'No Parents', weights=np.ones(len(Income[0])) / len(Income[0]), bins = 11, alpha = 0.5)
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))

    #plt.hist(Income[2],  label = 'Mother Only',weights=np.ones(len(Income[2])) / len(Income[2]), bins = 11, alpha = 0.5)
    #plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    
    #plt.hist(Income[1], label = 'Father Only',weights=np.ones(len(Income[1])) / len(Income[1]), bins = 11, alpha = 0.5)
    #plt.gca().yaxis.set_major_formatter(PercentFormatter(1))


    plt.xlabel('Level of Income')
    #plt.xticks(y_pos,["Grade 0","Grade 1","Grade 2","Grade 3","Grade 4","Grade 5","Grade 6","Grade 7","Grade 8","Grade 9","Grade 10","Grade 11","Grade 12","N1","N2","N3","N4","N5","N6","Certificate no Gr12","Certificate + Gr12","Diploma + Gr12","Higher Diploma","Post Higher Diploma","Bachelors Degree","Bachelors + Diploma","Honours Degree","Higher Degree","Other","No Schooling"])
    plt.xticks(y_pos,["","No Income","R 1 - R 4800","R 4801 - R 9600","R 9601 - R 19200 ","R 19201 - R 38400","R 38401 - R 76800","R 76801 - R 153600","R 153601 - R 307200","R 307201 - R 614400","R 614401- R 1228800","R 1228801 - R 2457600 ","R2457601 or more"])

    plt.xticks(rotation = 90)
    plt.xticks(fontsize=4)
    plt.ylabel('Percentage')
    plt.title('Relative Percentage of all')
    plt.legend()
    plt.show()

    
dist()  
