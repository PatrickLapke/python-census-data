from os import path
import csv

def skip_lines(file_connection, lines_skipped):
    """
    A function to skip lines at the top of a file.
    """
    for i in range(lines_skipped):
        x = (file_connection.readline().strip())
        if x == "":
            return False
        if i == lines_skipped:
            return True
            
        
class CensusData:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data_dict = {}

    def __repr__(self):
        return f"File Name = {self.file_name} Data Dictionary = {self.data_dict}"

    def load(self):
        """
        A function to read a csv file and input regions and their
        corresponding range/population into an empty dictionary.
        """
        if path.exists(self.file_name) == False:
            return False
        csv_file = open(self.file_name, "r", newline = '', encoding = "iso-8859-1")
        skip_lines(csv_file, 4)
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            region = row["Region"]
            range = row["Range"]
            people = row["All people"]
            if region not in self.data_dict.keys():
                self.data_dict[region] = {}
            if region in self.data_dict.keys():
                self.data_dict[region][range] = people
        csv_file.close()
        return True

    def regions(self):
        """
        A function to provide a list of all
        the available regions.
        """
        lst = []
        for region in self.data_dict.keys():
            lst.append(region)
        return lst

    def total_population(self, input_region, input_age):
        """
        A function to first check if the input region
        is in the dictionary and return a sum of population
        up to and including an inputted range.
        """
        for region in self.regions():
            if input_region not in self.regions():
                return 0
        sum = 0
        region = self.data_dict[input_region]
        for age, pop in region.items():
            if age == "All people":
                continue
            if age == "Under 1":
                age = "0"
            if age == "85 to 89":
                age = "89"
            if age  == "90 to 94":
                age = "94"
            if age == "95 and over":
                age = "100"
            if int(age) <= input_age:
                sum += int(pop)
        return sum

    

class SIMD_Data:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data_dict = {}

    def __repr__(self):
        return f"File Name : {self.file_name}.  Data Dict = {self.data_dict}"

    def load(self):
        """
        A function to read a csv file and input
        an average SIMD rank into the corresponding
        region in the data_dict dictionary
        """
        if path.exists(self.file_name) == False:
            return False
        csv_file = open(self.file_name, "r", newline = '', encoding = "iso-8859-1")
        csv_reader = csv.DictReader(csv_file)
        average_dict = {}
        for row in csv_reader:
            rank = int(row["SIMD2020v2_Rank"])
            mmw_name = row["MMWname"]
            if mmw_name not in average_dict.keys():
                average_dict[mmw_name] = []
            if mmw_name in average_dict.keys():
                average_dict[mmw_name].append(rank)

        for x, y in average_dict.items():
            summ = sum(y)
            average = summ / len(y)
            self.data_dict[x] = average
        csv_file.close()
        return True

    
    def regions(self):
        lst = []
        for region in self.data_dict.keys():
            lst.append(region)
        return lst

    
    def lowest_simd(self):
        return (min(self.data_dict, key = self.data_dict.get))

            
if __name__ == "__main__":
    def main():
        census_data = CensusData("DC1117SC.csv")
        if not census_data.load():
            return 'No Census Data'
        simd_data = SIMD_Data("SIMD_2020v2csv.csv")
        if not simd_data.load():
            return 'No Simd Data'
        print("Lowest average SIMD rank region: " + simd_data.lowest_simd())
        print("Lowest average SIMD rank: " + str(simd_data.data_dict["Canal"]))
        print("15 and under population: " + 
              str(census_data.total_population("Canal", 15)))
    main()






        