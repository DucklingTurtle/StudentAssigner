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
        days_available_list = sorted(days_available_list)
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
    day_col = {
        1: day_1_col,
        2: day_2_col,
        3: day_3_col,
        4: day_4_col,
        5: day_5_col,
        6: day_6_col,
        7: day_7_col,
        8: day_8_col,
        9: day_9_col,
        10: day_10_col,
    }
# remove headers from data
    name_col.pop(0)
    focus1_col.pop(0)
    focus2_col.pop(0)
    days_avail_col.pop(0)
    number = 0
    for x in day_col:
        day_col[x].pop(0)
    # for x in range(10):
    #     number += 1
    #     command = f"day_{number}_col.pop(0)"
    #     exec(command)
# loop through and verify data
    # for loop, runs as many times as there are items in column
    days = days_avail_col
    for index in range(0, 50):
        print("Index: " + str(index))
        # focus check
        if focus1_col[index] != focus2_col[index]:
            pass
        else:
            print("Error: Focus 1 and Focus 2 match! Index: " + str(index))
    # check all days have data
        # sort and get day data
        day = days[index]
        day = day.split(", ")
        day = list(map(int, day))
        day = sorted(day)
        # check
        # print("day: " + str(day))
        # print(day_col[2][49])
        for day_num in day:
            # print("day_num: " + str(day_num))
            for cur_day in range(1, 11):
                # print("cur_day: " + str(cur_day))
                if day_num == cur_day:
                    try:
                        # print("in try")
                        if day_col[cur_day][index] == "":
                            print("Missing")
                    except:
                        print("Missing")
                        pass
run()
verify()