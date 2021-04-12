import csv
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter



def dist() :
    Education = [[],[],[],[]]
    with open('person!10pct!sample!v3_F1.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        line_count = 0
        for row in csv_reader:
            if int(f'{row[3]}') > 19 and int(f'{row[3]}')<30:
                if ((f'{row[37]}') == '3' or (f'{row[37]}') == '2') and ((f'{row[39]}') == '3' or (f'{row[39]}') == '2'):
                    
                    if int(f'{row[45]}') == 98 :
                        Education[0].append(30)
                    else:
                        Education[0].append(int(f'{row[45]}'))
                        

                if ((f'{row[37]}') == '2' or (f'{row[37]}') == '3') and ((f'{row[39]}') == '1'):
                    
                    if int(f'{row[45]}') == 98 :
                        Education[1].append(30)
                    else:
                        Education[1].append(int(f'{row[45]}'))

                if ((f'{row[37]}') == '1') and ((f'{row[39]}') == '3' or (f'{row[39]}') == '2'):
                    
                   if int(f'{row[45]}') == 98 :
                        Education[2].append(30)
                   else:
                        Education[2].append(int(f'{row[45]}'))

                if ((f'{row[37]}') == '1') and ((f'{row[39]}') == '1'):
                    
                    if int(f'{row[45]}') == 98 :
                        Education[3].append(30)
                    else:
                        Education[3].append(int(f'{row[45]}'))
                    
                
                
            
            line_count += 1
   
    #---------------------------------------------------------------------------------------------        
##    y_pos = np.arange(31)
##    plt.hist(Education[0], weights=np.ones(len(Education[0])) / len(Education[0]), bins=30)
##    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
##    plt.xlabel('Level of Education')
##    plt.xticks(y_pos,["Grade 0","Grade 1","Grade 2","Grade 3","Grade 4","Grade 5","Grade 6","Grade 7","Grade 8","Grade 9","Grade 10","Grade 11","Grade 12","N1","N2","N3","N4","N5","N6","Certificate no Gr12","Certificate + Gr12","Diploma + Gr12","Higher Diploma","Post Higher Diploma","Bachelors Degree","Bachelors + Diploma","Honours Degree","Higher Degree","Other","No Schooling"])
##    plt.xticks(rotation = 90)
##    plt.xticks(fontsize=4)
##    plt.ylabel('Percentage')
##    plt.title('Level of Education With No Parents')
##    plt.show()
##
##    y_pos = np.arange(31)
##    plt.hist(Education[1], weights=np.ones(len(Education[1])) / len(Education[1]), bins =30)
##    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
##    plt.xlabel('Level of Education')
##    plt.xticks(y_pos,["Grade 0","Grade 1","Grade 2","Grade 3","Grade 4","Grade 5","Grade 6","Grade 7","Grade 8","Grade 9","Grade 10","Grade 11","Grade 12","N1","N2","N3","N4","N5","N6","Certificate no Gr12","Certificate + Gr12","Diploma + Gr12","Higher Diploma","Post Higher Diploma","Bachelors Degree","Bachelors + Diploma","Honours Degree","Higher Degree","Other","No Schooling"])
##    plt.xticks(rotation = 90)
##    plt.xticks(fontsize=4)
##    plt.ylabel('Percentage')
##    plt.title('Level of Education With Only A Father')
##    plt.show()
##
##    y_pos = np.arange(31)
##    plt.hist(Education[2], weights=np.ones(len(Education[2])) / len(Education[2]), bins = 30)
##    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
##    plt.xlabel('Level of Education')
##    plt.xticks(y_pos,["Grade 0","Grade 1","Grade 2","Grade 3","Grade 4","Grade 5","Grade 6","Grade 7","Grade 8","Grade 9","Grade 10","Grade 11","Grade 12","N1","N2","N3","N4","N5","N6","Certificate no Gr12","Certificate + Gr12","Diploma + Gr12","Higher Diploma","Post Higher Diploma","Bachelors Degree","Bachelors + Diploma","Honours Degree","Higher Degree","Other","No Schooling"])
##    plt.xticks(rotation = 90)
##    plt.xticks(fontsize=4)
##    plt.ylabel('Number')
##    plt.title('Level of Education With Only A Mother')
##    plt.show()
##
##    y_pos = np.arange(31)
##    plt.hist(Education[3], weights=np.ones(len(Education[3])) / len(Education[3]), bins = 30)
##    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
##    plt.xlabel('Level of Education')
##    plt.xticks(y_pos,["Grade 0","Grade 1","Grade 2","Grade 3","Grade 4","Grade 5","Grade 6","Grade 7","Grade 8","Grade 9","Grade 10","Grade 11","Grade 12","N1","N2","N3","N4","N5","N6","Certificate no Gr12","Certificate + Gr12","Diploma + Gr12","Higher Diploma","Post Higher Diploma","Bachelors Degree","Bachelors + Diploma","Honours Degree","Higher Degree","Other","No Schooling"])
##    plt.xticks(rotation = 90)
##    plt.xticks(fontsize=4)
##    plt.ylabel('Percentage')
##    plt.title('Level of Education With Both Parents')
##    plt.show()

    y_pos = np.arange(31)
    plt.hist(Education[0], label = 'No Parents', weights=np.ones(len(Education[0])) / len(Education[0]), bins = 30, alpha = 0.7)
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))

    plt.hist(Education[2],  label = 'Mother Only',weights=np.ones(len(Education[2])) / len(Education[2]), bins = 30)
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    
    plt.hist(Education[1], label = 'Father Only',weights=np.ones(len(Education[1])) / len(Education[1]), bins = 30)
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    
    


    plt.hist(Education[3], label = 'Both Parents', weights=np.ones(len(Education[3])) / len(Education[3]), bins = 30, alpha = 0.7)
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    
    

    


    plt.xlabel('Level of Education')
    plt.xticks(y_pos,["Grade 0","Grade 1","Grade 2","Grade 3","Grade 4","Grade 5","Grade 6","Grade 7","Grade 8","Grade 9","Grade 10","Grade 11","Grade 12","N1","N2","N3","N4","N5","N6","Certificate no Gr12","Certificate + Gr12","Diploma + Gr12","Higher Diploma","Post Higher Diploma","Bachelors Degree","Bachelors + Diploma","Honours Degree","Higher Degree","Other","No Schooling"])
    plt.xticks(rotation = 90)
    plt.xticks(fontsize=4)
    plt.ylabel('Percentage')
    plt.title('Relative Percentage of all')
    plt.legend()
    plt.show()

    

dist()  



    
