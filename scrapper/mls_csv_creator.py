from datetime import datetime
import csv

class MLSDailyCSVCreator:
    fileName = ''
    allHeadings = []
    allRows = []

    def __init__(self, savedSearchKey):
        self.fileName = str(savedSearchKey) + '__' + datetime.today().strftime('%Y-%m-%d') + '.csv'
    
    def addListing(self, dictionary):
        headings = list(dictionary.keys())

        newRow = []

        for heading in self.allHeadings:
            if heading in headings:
                newRow.append(dictionary[heading])
            else:
                newRow.append('-')


        for heading in headings:
            if heading not in self.allHeadings:
                self.allHeadings.append(heading)
                newRow.append(dictionary[heading])

                for row in self.allRows:
                    row.append('-')
        
        self.allRows.append(newRow)

    def out(self):
        for heading in self.allHeadings:
            print(heading, end=' , ')

        print('')

        for row in self.allRows:
            print('')
            for col in row:
                print(col, end=', ')

    def createReport(self):
        with open(self.fileName, 'w', newline='\n') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_NONNUMERIC)

            wr.writerow(self.allHeadings)

            wr.writerows(self.allRows)
    
