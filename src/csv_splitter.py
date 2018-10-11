import csv

class CsvSplitter:

    @classmethod
    def split_csv(self, csv_path):

        output = []
        buffer = []

        with open (csv_path, 'rb') as csvfile:
            reader = csv.reader(csvfile, dialect='excel')
            for line in reader:
                if line[1] != "CUSTOMER PROFILE":
                    buffer.append(line)
                if line[1] == "CUSTOMER PROFILE":
                    output.append(buffer)
                    buffer = []

        return output


