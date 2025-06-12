import datetime

def save_current_datetime():
    current_datetime = datetime.datetime.now()
    with open('datetime.txt', 'w') as file:
        file.write(current_datetime.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    save_current_datetime()