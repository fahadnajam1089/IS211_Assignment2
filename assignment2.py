# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import argparse
import logging
import datetime
import urllib.request

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def downloadData(url):
    with urllib.request.urlopen(url) as response:
        file_content = response.read().decode('utf-8')
    return file_content

def processData(file_content):
    logger = logging.getLogger("assignment2")
    data_list = file_content.split('\n')

    personData = {}
    lineum = 0
    for line in data_list:
        lineum = lineum +1
        info = line.split(',')
        if len(info) < 3 or lineum == 1:
            continue
        else:
            #print("**************")
            #print(info[2])
            #print( datetime.datetime.strptime(info[2], "%d/%m/%Y"))
            try:
                birthday =   datetime.datetime.strptime(info[2], "%d/%m/%Y")
                u_id = info[0]
                name = info[1]
                #birthday = info[2]
                #print(info[2])
            
                #print(birthday)
                data_tuple = (name, birthday)
                personData[u_id] = data_tuple
                #print("Not here") 
            except:
                #print("Here")
                logging.error("Error processing line #" + str(lineum) + "for ID #" +str(info[0]))
    return personData

def displayPerson(u_id, personData):
    u_id = str(u_id)
    #print(personData)
    if u_id in personData.keys():
        data_tuple = personData[u_id]
        name = data_tuple[0]
        birthdate = data_tuple[1]
        print ('Person # {} is {} with a birthday of {}'.format(u_id, name, birthdate))
    else:
        print("No user found with that id")

def main(url):
    print(f"Running main with URL = {url}...")
    try:
        file_content = downloadData(url)
        personData = processData(file_content)
        while True:
            val = int(input("Enter ID to lookup: "))
            if val <1:
                break
            displayPerson(val, personData)
    except Exception as e:
        print (str(e))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    logger = logging.getLogger("assignmet")
    logging.basicConfig(filename='errors.log', level=logging.ERROR)
    main(args.url)
