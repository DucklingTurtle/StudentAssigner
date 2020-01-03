# make random teachers
import gspread, random, time, sys
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
# debug tools
name_list = []
focus1_list = []
focus2_list = []
days_available_list2 = []


def run():
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
        name_list.append(name)
        # focus 1
        ws.update_cell(x, 3, focus1)

        # focus 2
        ws.update_cell(x, 4, focus2)
        # number of days
        days_available_list = []
        num_of_days = random.randint(1, 10)
        print("num_of_days: " + str(num_of_days))
        for element in range(num_of_days):
            rand_day = random.randint(1, 10)
            while True:
                if not any(x == rand_day for x in days_available_list) or not days_available_list:
                    days_available_list.append(rand_day)
                    break
                else:
                    rand_day = random.randint(1, 10)
                    # print("rand_day: " + str(rand_day))
        days_available_list.sort()
        days_available = str(days_available_list)[1:-1]
        # days available
        print("days_available: " + days_available)
        ws.update_cell(x, 5, days_available)
        # hours for days
        # hours_dict = {}
        cell = 5
        print(days_available_list)
        for day in days_available_list:
            print("Day: " + str(day))
            num_hours = random.randint(1, 3)
            hours = []
            # cell += 1
            hours_selected = []
            hours_text = ["9AM-11AM", "11AM-1PM", "1PM-3PM"]
            print("num_hours: " + str(num_hours))
            for number in range(num_hours):
                while True:
                    chosen_hour = random.choice(hours_text)
                    if not any(x == chosen_hour for x in hours):
                        hours.append(chosen_hour)
                        break
            day_hours = ",".join(hours)
            print(day_hours)
            days_pool = days_available_list
            # for day1 in days_pool:
                # for i in range(1, 11):
                #     if day1 == i:
                        # days_pool.remove(day1)
            index = day + 5
            ws.update_cell(x, index, day_hours)
                # time.sleep(1)
            time.sleep(10)

def verify():
    global name_col
    global focus1_col
    global focus2_col
    global days_avail_col
    global day_1_col
    global day_2_col
    global day_3_col
    global day_4_col
    global day_5_col
    global day_6_col
    global day_7_col
    global day_8_col
    global day_9_col
    global day_10_col
    name_col = ws.col_values(2)
    focus1_col = ws.col_values(3)
    focus2_col = ws.col_values(4)
    days_avail_col = ws.col_values(5)
    day_1_col = ws.col_values(6)
    day_2_col = ws.col_values(7)
    day_3_col = ws.col_values(8)
    day_4_col = ws.col_values(9)
    day_5_col = ws.col_values(10)
    day_6_col = ws.col_values(11)
    day_7_col = ws.col_values(12)
    day_8_col = ws.col_values(13)
    day_9_col = ws.col_values(14)
    day_10_col = ws.col_values(15)
    test_list = {"name_col": name_col, "focus1_col": focus1_col, "focus2_col": focus2_col, "days_avail_col": days_avail_col, "day_1_col": day_1_col, "day_2_col": day_2_col, "day_3_col": day_3_col, "day_4_col": day_4_col,
                 "day_5_col": day_5_col, "day_6_col": day_6_col, "day_7_col": day_7_col, "day_8_col": day_8_col, "day_9_col": day_9_col, "day_10_col": day_10_col}
    for index in range(len(name_col)):
        # focus check
        if focus1_col[index] != focus2_col[index]:
            pass
        else:
            print("Error: Focus 1 and Focus 2 match! Index: " + str(index))
        # all days have data
        days = days_avail_col
        # days = days.split(", ")
        print("days: " + str(days))
        day_counter = 0
        for day in days:
            print(days)
            for i in range(1, 10):
                # day_col = i + 5
                global hold_var
                # hold_var = ""
                _locals = locals()
                command = "global hold_var; global day_1_col; hold_var = day_" + str(i) + "_col; print(\"works\")"
                # print(command)
                exec(command, globals(), _locals)
                print("hold_var: " + hold_var[0])
                sys.exit()
                # print(_locals)
        # for day in

# run()
verify()