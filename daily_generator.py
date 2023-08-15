from random import randint;
from argparse import ArgumentParser, Namespace;
from datetime import datetime, date, timedelta;


def is_independence_day(date_now: datetime) -> tuple:
    id_independences: date = date(1945, 8, 17);
    if(id_independences.day == date_now.day
       and id_independences.month == date_now.month):
        return True, date_now.year - id_independences.year;
    return False, None;

def is_kartini_day(date_now: datetime) -> bool:
    kartini_days: date = date(1879, 4, 21);
    if(kartini_days.day == date_now.day
       and kartini_days.month == date_now.month):
        return True;
    return False;

def is_youth_pledge(date_now: datetime) -> bool:
    youth_pledge_days: date = date(1928, 10, 28);
    if(youth_pledge_days.day == date_now.day
       and youth_pledge_days.month == date_now.month):
        return True;
    return False;

def is_thirty_sept(date_now: datetime) -> bool:
    thirty_sept_days: date = date(1965, 9, 30);
    if(thirty_sept_days.day == date_now.day
       and thirty_sept_days.month == date_now.month):
        return True;
    return False;

def get_weekdays(date_now: datetime) -> str:
    if(date_now.strftime("%a") == 'Mon'):
        return "Why's monday so far from friday ? 👀";
    elif(date_now.strftime("%a") == 'Tue'):
        return "It's just a second monday 😪";
    elif(date_now.strftime("%a") == 'Wed'):
        return "Halfway through the week 🙃";
    elif(date_now.strftime("%a") == 'Thu'):
        return "Yeay tomorrow is friday 😬";
    elif(date_now.strftime("%a") == 'Fri'):
        return "We made it, It's finally friday 🥳";
    elif(date_now.strftime("%a") == 'Sat'):
        return "Ahh, It's the weekend 😎";
    else:
        return "Tomorrow is monday again 😌";

def generate_markdown(date_now: datetime,
                      specific_date: datetime,
                      min_sleep: int,
                      max_sleep: int,
                      month: int) -> None:
    lines: list = [];
    delta_days: int = (date_now - specific_date).days;
    sleep: int = randint(a=min_sleep, b=max_sleep);

    with open('README.md', 'r', encoding='utf-8') as file:
        lines = file.readlines();
        lines[17] = f"- 🛌 I've spent {((delta_days * sleep) // 24) // month} months of my life asleep\n"

        if is_independence_day(date_now=date_now)[0]:
            id_age: int = is_independence_day(date_now=date_now)[1];
            lines[132] = f'<h5><i>"Happy Independence Day {id_age} Indonesia 🇮🇩🔥"</i></h5>\n';
        elif is_kartini_day(date_now=date_now):
            lines[132] = '<h5><i>"Happy Kartini Day 🇮🇩👵"</i></h5>\n';
        elif is_youth_pledge(date_now=date_now):
            lines[132] = '<h5><i>"Happy Youth Pledge Day 🇮🇩✊👊"</i></h5>\n';
        elif is_thirty_sept(date_now=date_now):
            lines[132] = '<h5>"Happy Independence Day 🇮🇩🛡🔫"</h5>\n';
        else:
            lines[132] = f'<h5><i>"{get_weekdays(date_now=date_now)}"</i></h5>\n';

    with open('README.md', 'w', encoding='utf-8') as file:
        file.writelines(lines);

def get_variable() -> tuple:
    parser: ArgumentParser = ArgumentParser(
        description="Generate markdown with specific events"
    );
    parser.add_argument("a", type=int, help="Min value of sleep time")
    parser.add_argument("b", type=int, help="Max value of sleep time")
    parser.add_argument("m", type=int, help="Total days in a month")
    parser.add_argument(
        "-u",
        "--unixtime",
        type=int,
        help="The unixtime of your birthday",
        required=True
    );
    args: Namespace = parser.parse_args()
    return args.a, args.b, args.m, args.unixtime;


if __name__ == "__main__":
    a: int;
    b: int;
    month: int;
    unixtime: int;
    min, max, month, unixtime = get_variable();
    today: datetime = datetime.now();
    unix_date: datetime= datetime.fromtimestamp(unixtime);
    
    generate_markdown(
        date_now=today,
        specific_date=unix_date,
        min_sleep=min,
        max_sleep=max,
        month=month
    );
