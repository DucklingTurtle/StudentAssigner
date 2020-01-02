# make random teachers
import gspread, random, time
from oauth2client.service_account import ServiceAccountCredentials

focus_list = [
    "AP", "CP", "IR", "MT", "TH"
]

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials_studentassigner2.json", scope)
client = gspread.authorize(creds)
gc = gspread.authorize(creds)

sh = gc.open("Teacher Input 2 Sheet")
ws = sh.get_worksheet(0)
name_num = 0
for i in range(50):
    i += 2
    # create random values
    name_num += 1
    name = "First" + str(name_num) + "" + "Last" + str(name_num)
    focus1 = random.choice(focus_list)
    focus2 = random.choice(focus_list)
    while True:
        if focus2 == focus1:
            focus2 = random.choice(focus_list)
        else:
            break
    # name
    ws.update_cell(i, 2, name)
    # focus 1
    ws.update_cell(i, 3, focus1)
    # focus 2
    ws.update_cell(i, 4, focus2)
    # number of days
    days_available_list = []
    num_of_days = random.choice(range(1, 11))
    for element in range(num_of_days + 1):
        while True:
            rand_day = random.choice(range(1, 11))
            if not any(x == rand_day for x in days_available_list):
                days_available_list.append(rand_day)
                break
    days_available = str(days_available_list[1:-1])
    # days available
    ws.update_cell(i, 5, days_available)
    # hours for days
    # hours_dict = {}
    cell = 5
    for day in days_available_list:
        num_hours = random.choice(range(1, 4))
        hours = []
        cell += 1
        for number in range(num_hours):
            print("works")
            print(number)
            choosen_hour = random.choice(range(1, 4))
            while True:
                if any(x == choosen_hour for x in hours):
                    choosen_hour = random.choice(range(1, 4))
                else:
                    if choosen_hour == 1:
                        choosen_hour = "9AM-11AM"
                    elif choosen_hour == 2:
                        choosen_hour = "11AM-1PM"
                    elif choosen_hour == 3:
                        choosen_hour = "1PM-3PM"
                    hours.append(choosen_hour)
                    break
        day_hours = ",".join(hours)
        ws.update_cell(i, cell, day_hours)
        time.sleep(5)
    time.sleep(10)