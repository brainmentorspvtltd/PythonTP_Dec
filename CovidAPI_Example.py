import json
import urllib.request as url

path = "https://data.covid19india.org/states_daily.json"
response = url.urlopen(path)
data = json.load(response)
states = data["states_daily"]

for i in range(len(states)):
    for key in states[i]:
        if key == "status" or key == "date" or key == "dateymd":
            continue
        else:
            states[i][key] = int(states[i][key])

confirmed = []
recovered = []
deceased = []

for i in range(len(states)):
    if states[i]['status'] == 'Confirmed':
        confirmed.append(states[i])
    elif states[i]['status'] == 'Recovered':
        recovered.append(states[i])
    else:
        deceased.append(states[i])

index = 410
state = 'mh'
print("Date :",confirmed[index]['date'])
print("Confirmed :",confirmed[index][state])
print("Recovered :",recovered[index][state])
print("Deceased :",deceased[index][state])

sum = 0
for i in range(len(confirmed)):
    sum += confirmed[i][state]

print("="*30)
print("Overall Total Cases :",sum)
