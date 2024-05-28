import requests
from bs4 import BeautifulSoup
import sys
from plyer import notification
from time import sleep

print("\nLive Cricket Matches:")
print("=====================")
url = "http://static.cricinfo.com/rss/livescores.xml"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")

i = 1
links = []
for item in soup.findAll("item"):
    print(str(i) + ". " + item.find("description").text)
    links.append(item.find("guid").text)
    i += 1

print("\n\nEnter match number or enter 0 to exit:")
while True:
    try:
        user_input = int(input())
        if user_input == 0:
            sys.exit()
        elif user_input < 0 or user_input > len(links):
            print("Invalid match number. Please try again!")
            continue
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number!")

print("\n\n")

previous_score_string = ""
previous_runs = -1
previous_wickets = -1
previous_batting_team = ""
previous_overs = -1  # Initialize to -1

while True:
    try:
        match_url = links[user_input - 1]
        r = requests.get(match_url)
        soup = BeautifulSoup(r.text, "lxml")
        score = soup.findAll("title")

        try:
            r.raise_for_status()
        except Exception as exc:
            print("Connection Failure. Try again!")
            continue

        current_score_string = str(score[0].text)
        if current_score_string != previous_score_string:
            print(current_score_string + "\n")
            previous_score_string = current_score_string

            score_split = current_score_string.split(" ")
            runs = -1
            wickets = -1
            batting_team = ""
            for string in score_split:
                if "/" in string:
                    runs = int(string.split("/")[0].strip())
                    wickets = int(string.split("/")[1].strip())
                    batting_team = str(score_split[score_split.index(string) - 1]).strip()
                    break

            detailed_scores = (current_score_string[current_score_string.find("(") + 1 : current_score_string.find(")")]).strip()
            detailed_scores_split = detailed_scores.split(",")
            overs = detailed_scores_split[0].split(" ")[0].strip()

            if previous_overs == -1:
                previous_overs = int(float(overs))  # Initialize to the current value of overs

            # Convert overs to float to handle cases like "10.2"
            current_overs = int(float(overs))

            if current_overs != previous_overs:
                if current_overs % 5 == 0:  # Notify after every 5 overs
                    notification.notify(
                        title="After " + str(current_overs) + " overs...",
                        message=current_score_string,
                        app_name="Live Cricket Score",
                        timeout=5
                    )
                previous_overs = current_overs

            # Rest of your code for handling notifications based on score updates...

    except requests.exceptions.ConnectionError:
        pass

    except requests.exceptions.TooManyRedirects:
        pass

    sleep(5)  # Wait for 5 seconds before polling again
