import csv
import json
import requests

# Name of your roster csv file
ROSTER = "data.csv"

# Your access token. See README for details on how to obtain
ACCESS_TOKEN = ""

# Group Id. See README for details on how to obtain
GROUP_ID = ""

# Only update this if Groupme releases a new API
GROUPME_API_URL = "https://api.groupme.com/v3"


def csvToJson():
    with open(ROSTER, 'r') as csvfile:
        members = csv.reader(csvfile)
        members_data = []
        next(members, None)
        for member in members:
            if member[0] == "":
                break
            number = str(member[2])
            name = str(member[0] + " " + member[1])
            new_groupme_member = {"nickname": name, "phone_number": number}
            members_data.append(new_groupme_member)
        wrapper = {"members": members_data}
        json_members = json.dumps(wrapper)
        return json_members


def add_members():
    json_members = csvToJson()
    requests.post(GROUPME_API_URL + "/groups/" + GROUP_ID + "/members/add" +
                  "?token=" + ACCESS_TOKEN, data=json_members, timeout=30)


def main():
    add_members()

if __name__ == "__main__":
    main()
