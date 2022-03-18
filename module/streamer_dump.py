import requests

def streamer_dump():
    file = open('list.txt', 'w')
    records=0
    for i in range(3):
        url='https://sullygnome.com/api/tables/channeltables/getchannels/7/230/1/3/desc/' + str(records) + '/100'
        x = requests.get(url, headers={'User-Agent': 'Custom'}).json()
        for line in x['data']:
            file.write(line['displayname'] + "\n")
        records = records + 100
    file.close()