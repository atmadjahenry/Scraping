from bs4 import BeautifulSoup
import requests
import json

query = input('Masukkan kata pencarian: ')
pagenya = int(input('Masukkan jumlah page yang ingin dicari: '))

print('================Hasilnya==================')

url = "https://www.detik.com/search/searchall?query={}&sortby=time&page=".format(query)



for page in range(1,pagenya+1):

    web = requests.get(url+str(page))
    soup = BeautifulSoup(web.text, 'html.parser')

    item = soup.findAll('article')
    
    dict = {}
    for i in item :

        judul = i.find('h2', 'title').text

        link = i.find('a')['href']


        date = i.find('span', 'date').text.replace('detikNews', '').replace('detikEdu', '').replace('detikOto', '')
    
        dict['title'] = judul
        dict['url'] = link
        dict['tanggal'] = date

        print(dict)

       
    # with open('testnih.json', 'w') as json_file:
    #     json.dump(dict, json_file)