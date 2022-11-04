import datetime


class Data:
    def __init__(self, file: str):
        self.file = file

    def read_data(self):
        url_file = f"input_data/{self.file}"
        with open(file=url_file, encoding="utf-8") as open_file:
            list_total_data = open_file.read().split(" ")

        return list_total_data

    def clear_list(self):
        list_total_data = Data(self.file).read_data()
        clear_list_data = [item for item in list_total_data if item != ""]

        return clear_list_data

    def sort_data(self):
        clear_list_data = Data(self.file).clear_list()
        sort_dict_data = {"digits": [], "names": [], "patronymics": [], "surnames": []}
        for item in clear_list_data:
            if item.isdigit():
                sort_dict_data["digits"].append(int(item))
            elif item.isalpha():
                if item[-2:] == "ич" or item[-3:] == "вна" or item[-3:] == "чна":
                    sort_dict_data["patronymics"].append(item)
                elif item[-2:] == "ин" or item[-2:] == "ов" or item[-3:] == "ова":
                    sort_dict_data["surnames"].append(item)
                else:
                    sort_dict_data["names"].append(item)
        print(sort_dict_data)

        return sort_dict_data
