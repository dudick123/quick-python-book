# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests

def print_readme():
    # Use a breakpoint in the code line below to debug your script.

    r = requests.get('https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt')
    readme = r.text

    r = requests.get('https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-inventory.txt')
    inventory_txt = r.text

    r = requests.get('https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt')
    stations_txt = r.text

    # save both the inventory and stations files to disk, in case we need them

    with open("inventory.txt", "w") as inventory_file:
        inventory_file.write(inventory_txt)

    with open("stations.txt", "w") as stations_file:
        stations_file.write(stations_txt)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_readme()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
