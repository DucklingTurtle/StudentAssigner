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
for x in range(50):
    days_pool = []
    x += 2
    # create random values
    name_num += 1
    name = "First" + str(name_num) + " Last" + str(name_num)
    focus1 = random.choice(focus_list)
    focus2 = random.choice(focus_list)
    while True:
        if focus2 == focus1:
            focus2 = random.choice(focus_list)
        else:
            break
    # name
    ws.update_cell(x, 2, name)
    # focus 1
    ws.update_cell(x, 3, focus1)
    # focus 2
    ws.update_cell(x, 4, focus2)
    # number of days
    days_available_list = []
    num_of_days = random.choice(range(1, 11))
    print("num_of_days: " + str(num_of_days))
    for element in range(num_of_days):
        rand_day = random.choice(range(1, 11))
        while True:
            if not any(x == rand_day for x in days_available_list):
                days_available_list.append(rand_day)
                break
            else:
                rand_day = random.choice(range(1, 11))
                print("rand_day: " + str(rand_day))
    days_available = str(days_available_list)[1:-1]
    # days available
    print("days_available: " + days_available)
    ws.update_cell(x, 5, days_available)
    # hours for days
    # hours_dict = {}
    cell = 5
    for day in days_available_list:
        num_hours = random.choice(range(1, 4))
        hours = []
        cell += 1
        for number in range(num_hours):
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
        days_pool = days_available_list
        for e in days_pool:
            for i in range(1, 11):
                if e == i:
                    days_pool.remove(e)
                    index = i + 5
                    ws.update_cell(x, index, day_hours)
        time.sleep(1)
    time.sleep(10)