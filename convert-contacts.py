## Modules used
import sys
import csv

# print ("This is the name of the script: ", sys.argv[0])
# print ("Number of arguments: ", len(sys.argv))
# print ("The arguments are: " , str(sys.argv))

## Parse the arguments to the script file and assign them name strings
if len(sys.argv) == 1:
    sys.exit("\nThis script reqires at least 1 file parameter. \n")
elif len(sys.argv) == 2:
    inputName = sys.argv[1]
    outputName = "8821_" + sys.argv[1]
else:
    inputName = sys.argv[1]
    outputName = sys.argv[2]


## Uncomment for troubleshooting:
#  print("\nThe Name of the input File is ",inputName)
#  print("\nThe Name of the output File is ",outputName)
#    sys.exit("\nThe Program ended as expected\n")

outputFile = open(outputName,"w")

## This loop progreessively scans through the input file one line at a time re-ordering the fields into the desginated 8821 format.

with open(inputName) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
#            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            workPrimary = False
            homePrimary = False
            mobilePrimary = False
            if {row[29]} == {row[21]}:
                workPrimary = True
            elif {row[29]} == {row[27]}:
                homePrimary = True
            elif {row[29]} == {row[23]}:
                mobilePrimary = True
#                print('The work phone is the primary number')
            print(f'{row[2]},{row[4]},{row[6]},{row[7]},{row[21]},{row[27]},{row[23]},{row[30]},', str(workPrimary).lower(),",", str(homePrimary).lower(), ",", str(mobilePrimary).lower(),",,", sep = '', file = outputFile)
            line_count += 1
    print(f'Processed {line_count} lines.')

outputFile.close()
