#imports
import os
import csv

#execute code
dataFilePath = "./budget_data_1.csv"
finAnalysis = {
    'total_months': 0,
    'total_revenue': 0,
    'avg_rev_chg': 0,
    'grtst_inc_rev': 0,
    'grtst_dec_rev': 0
}

print(os.listdir())
for file in os.listdir():
    filepath = os.getcwd() + "\\" + file
    file_ext = os.path.splitext(filepath)
    if file_ext[1] == '.csv':
        with open( file ) as sourcefile:
            filereader = csv.reader(sourcefile)
            # openfile = "combinedcsvs.csv"
            # createdfile = open(openfile, 'a')
            for line in filereader:
                if (line[1] != "Revenue"):
                    finAnalysis['total_revenue'] = finAnalysis['total_revenue'] + int(line[1])
                    finAnalysis['total_months'] = finAnalysis['total_months'] + 1
            # createdfile.close()


print(finAnalysis['total_revenue'])
print(finAnalysis['total_months'])

finAnalysis['avg_rev_chg'] = finAnalysis['total_revenue'] / finAnalysis['total_months']
print(finAnalysis['avg_rev_chg'])




# with open( dataFilePath ) as csvfile:
#     dataFile = csv.reader(csvfile, delimiter = ',')
#     for row in dataFile:
#         # print(row[1])
