import urllib.request
from bs4 import BeautifulSoup


def get_horses(track, date):
    url = "https://www.racenet.com.au/form-guide/horse-racing/" + track + '-' + date +"/all-races"
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
    req = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(req)
    page_html = response.read()
    response.close()

    html_soup = BeautifulSoup(page_html, 'html.parser')
    return html_soup.find_all('div', class_='event-selection-row-container')

def get_names(horses):
    names = []
    for horse in horses:
        name = horse.find('span', class_='horseracing-selection-details-name').text
        names.append(name[12:-12])

    return names


def get_rating(horses):
    ratings = []
    for horse in horses:
        rating = horse.find('div', class_='event-selection-row-right__column--rating').text
        ratings.append(int(rating[15:-14]))

    return ratings


def get_win_rates(horses):
    win_rates = []
    for horse in horses:
        career = horse.find('div', class_='event-selection-row-right__column--career').text
        win_rate = calc_win_rate(career[15:-14])
        win_rates.append(win_rate)
    return win_rates

def calc_win_rate(career):
    #print(career)
    win_rate = 0
    if career == '-':
        win_rate = 0.0
    else:
        races = career[0]
        wins = career[3]
        places = career[5]
        
        win_rate = float(places)/float(races)
    return win_rate

def create_array(horses):
    horse_names = get_names(horses)
    ratings = get_rating(horses)
    win_rate = get_win_rates(horses)
    arr = []
    for i in range(len(horse_names)):
        horse_data = [horse_names[i], ratings[i], win_rate[i]]
        arr.append(horse_data)
    return arr


def main():
    filename = 'out.csv'
    f = open(filename, 'w')
    headers = "Horse, Rating, Win rate \n"
    f.write(headers)

    track = 'ascot'
    date = '20211110'
    horses = get_horses('ascot', '20211110')

    array = create_array(horses)

    for horse in array:
        line = ""
        for element in horse:
            line += (str(element) + ',')
        f.write(line[:-1] + '\n')
        print(line)

main()