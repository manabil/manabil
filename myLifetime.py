import datetime
# from dateutil import relativedelta

def getDays(date) -> str:
    return date.strftime('%a')

def isIndependenceDay():
    id_independences = datetime.date(1945, 8, 17)
    if(id_independences.day == now_date.day and id_independences.month == now_date.month):
        return True
    return False

def isKartiniDay():
    kartiniDays = datetime.date(1879, 4, 21)
    if(kartiniDays.day == now_date.day and kartiniDays.month == now_date.month):
        return True
    return False

def isYouthPledge():
    YouthPledgeDays = datetime.date(1928, 10, 28)
    if(YouthPledgeDays.day == now_date.day and YouthPledgeDays.month == now_date.month):
        return True
    return False

def isThirtiethSept():
    ThirtiethSeptDays = datetime.date(1965, 9, 30)
    if(ThirtiethSeptDays.day == now_date.day and ThirtiethSeptDays.month == now_date.month):
        return True
    return False

def isBirthday():
    if(my_date.day == now_date.day and my_date.month == now_date.month):
        return True
    return False

def generateMarkdown():
    lines = []

    with open('README.md', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        lines[17] = f"- ⏳ I've been alive for {(now_date - my_date).days} days\n"
        if isBirthday():
            lines[132] = f'<h5><i>"It is my birthday ? Ah i forgot it 🙂"</i></h5>'
        elif isIndependenceDay():
            lines[132] = f'<h5><i>"Happy Independece Indonesia 🇮🇩🔥"</i></h5>'
        elif isKartiniDay():
            lines[132] = f'<h5><i>"Happy Kartini Day 🇮🇩👵"</i></h5>'
        elif isYouthPledge():
            lines[132] = f'<h5><i>"Happy Youth Pledge Day 🇮🇩✊👊"</i></h5>'
        elif isThirtiethSept():
            lines[132] = f'<h5>"Happy Independece Day 🇮🇩🛡🔫"</h5>'
        else:
            lines[132] = f'<h5><i>"{weekDays()}"</i></h5>\n'
            

    with open('README.md', 'w', encoding='utf-8') as file:
        file.writelines(lines)

def weekDays():
    if(getDays(now_date) == 'Mon'):
        return "Why's monday so far from friday ? 👀"
    elif(getDays(now_date) == 'Tue'):
        return "It's just a second monday 😪"
    elif(getDays(now_date) == 'Wed'):
        return "Halfway through the week 🙃"
    elif(getDays(now_date) == 'Thu'):
        return "Yeay tomorrow is friday 😬"
    elif(getDays(now_date) == 'Fri'):
        return "We made it, It's finally friday 🥳"
    elif(getDays(now_date) == 'Sat'):
        return "Ahh, It's the weekend 😎"
    elif(getDays(now_date) == 'Sun'):
        return "Tomorrow is monday again 😌"

now_date = datetime.datetime.now()
my_unixtime_stamp = 1000405800
my_date = datetime.datetime.fromtimestamp(my_unixtime_stamp)
# delta_time = relativedelta.relativedelta(now_date, my_date)

generateMarkdown()
