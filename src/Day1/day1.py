import datetime
import os.path


class Day1Service:

    def read_file_with_groups(self, data_file_name):

        with open(data_file_name) as data_file:
            raw_data_lines = data_file.readlines()

        calories_by_elf_list = []
        current_elf_list = []

        for raw_data_line in raw_data_lines:
            cleaned_data_line = raw_data_line.strip()

            if not cleaned_data_line:
                calories_by_elf_list.append(current_elf_list)
                current_elf_list = []
            else:
                calorie = int(cleaned_data_line)
                current_elf_list.append(calorie)

        # add the last one
        calories_by_elf_list.append(current_elf_list)

        return calories_by_elf_list

    def calculate_task_1(self, data_file_name):

        calories_by_elf_list = self.read_file_with_groups(data_file_name)

        max_elf_calorie = 0

        for calories_by_elf in calories_by_elf_list:

            # loop through the elf's list and sum  up
            elf_total_calorie = 0
            for calorie in calories_by_elf:
                elf_total_calorie += calorie

            if elf_total_calorie > max_elf_calorie:
                max_elf_calorie = elf_total_calorie

        return max_elf_calorie

    def calculate_task_2(self, data_file_name):

        calories_by_elf_list = self.read_file_with_groups(data_file_name)

        top_3_elf_calorie = 0

        sum_of_calories_by_elf = []

        for calories_by_elf in calories_by_elf_list:

            # loop through the elf's list and sum  up
            elf_total_calorie = 0
            for calorie in calories_by_elf:
                elf_total_calorie += calorie

            sum_of_calories_by_elf.append(elf_total_calorie)
        sum_of_calories_by_elf.sort(reverse=True)
        top_3_elf_calorie = sum_of_calories_by_elf[0] + sum_of_calories_by_elf[1] + sum_of_calories_by_elf[2]

        return top_3_elf_calorie


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    service = Day1Service()

    current_directory = os.path.dirname(os.path.abspath(__file__))
    datafile = current_directory + "/day_data.txt"
    # datafile = current_directory + "/example_data.txt"

    try:
        # value = service.calculate_task_1(datafile)
        # print(f"Task 1: The value is {value}")

        value = service.calculate_task_2(datafile)
        print(f"Task 2: The value is {value}")
    except Exception as exc:
        raise exc
