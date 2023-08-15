import datetime
# from dateutil import relativedelta

def get_days(date) -> str:
    return date.strftime('%a');

def is_independence_day() -> bool:
    id_independences = datetime.date(1945, 8, 17)
    if(id_independences.day == now_date.day and id_independences.month == now_date.month):
        return True;
    return False;

def is_kartini_day() -> bool:
    kartini_days = datetime.date(1879, 4, 21)
    if(kartini_days.day == now_date.day and kartini_days.month == now_date.month):
        return True;
    return False;

def is_youth_pledge() -> bool:
    youth_pledge_days = datetime.date(1928, 10, 28)
    if(youth_pledge_days.day == now_date.day and youth_pledge_days.month == now_date.month):
        return True;
    return False;

def is_thirty_sept() -> bool:
    thirty_sept_days = datetime.date(1965, 9, 30)
    if(thirty_sept_days.day == now_date.day and thirty_sept_days.month == now_date.month):
        return True;
    return False;

def weekDays() -> str:
    if(get_days(now_date) == 'Mon'):
        return "Why's monday so far from friday ? 👀";
    elif(get_days(now_date) == 'Tue'):
        return "It's just a second monday 😪";
    elif(get_days(now_date) == 'Wed'):
        return "Halfway through the week 🙃";
    elif(get_days(now_date) == 'Thu'):
        return "Yeay tomorrow is friday 😬";
    elif(get_days(now_date) == 'Fri'):
        return "We made it, It's finally friday 🥳";
    elif(get_days(now_date) == 'Sat'):
        return "Ahh, It's the weekend 😎";
    else:
        return "Tomorrow is monday again 😌";

def generateMarkdown() -> None:
    lines: list = [];

    with open('README.md', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        lines[17] = f"- 🛌 I've spent {round(((now_date-random_date).days * 7)/24)} days of my life asleep\n"
        if is_independence_day():
            lines[132] = f'<h5><i>"Happy Independece Indonesia 🇮🇩🔥"</i></h5>';
        elif is_kartini_day():
            lines[132] = f'<h5><i>"Happy Kartini Day 🇮🇩👵"</i></h5>';
        elif is_youth_pledge():
            lines[132] = f'<h5><i>"Happy Youth Pledge Day 🇮🇩✊👊"</i></h5>';
        elif is_thirty_sept():
            lines[132] = f'<h5>"Happy Independence Day 🇮🇩🛡🔫"</h5>';
        else:
            lines[132] = f'<h5><i>"{weekDays()}"</i></h5>\n';

    with open('README.md', 'w', encoding='utf-8') as file:
        file.writelines(lines);



now_date: datetime.datetime = datetime.datetime.now();
random_number: int = 1000405800;
random_date: datetime.datetime = datetime.datetime.fromtimestamp(random_number);
# delta_time = relativedelta.relativedelta(now_date, my_date)

generateMarkdown();
