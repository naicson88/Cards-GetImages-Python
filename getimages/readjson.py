from pdb import line_prefix
import requests
import re
import json
import time

api_url = 'https://db.ygoprodeck.com/api/v7/cardinfo.php?name='
cards_url = 'http://localhost:8080/yugiohAPI'

def do_login_and_get_token(url):
    full_path = url+'/auth/login'
    # print('Inset UserName')  
    # user_name = input()
    # print('Inset Password')  
    # password = input()
    login = {'username':'alannaicson','password':'91628319'}
    resp = requests.post(full_path, json=login)
    data = resp.json();
    token = data['accessToken']
    return 'Bearer '+token      

def send_card_images(url, auth):
    full_path = url+'/cards/update-images'
    card_images = {'cardName': obj['name'], 'images': array_numbers} 
    response_cards_api = requests.post(full_path, headers={"Authorization": auth}, json=card_images)
    print(response_cards_api.json())
        
token = do_login_and_get_token(cards_url)
array_numbers = [];

with open('allcards.json','r') as cards:
    data = json.load(cards)
    
    for line in data:
     response = requests.get(api_url+line['nome'].strip())
     json_response = response.json();
     
     if response.status_code == 200:
         time.sleep(1)
         print('Consulting...' , line['nome'])
         obj = json_response['data'][0]
         array_images = obj['card_images']
        
         for image in array_images:
            url = image['image_url']
            number = re.search('cards/(.*).jpg', url).group(1)
            array_numbers.append(number)
            if(len(array_numbers) > 1):  
              send_card_images(cards_url, token)
         array_numbers = []
         
     else:
        print('Error when trying consulting Card: ', line)
        
    print('FINISHED!!!')



        
# response = requests.get(api_url)
# json_response = response.json();
# status = response.status_code

# obj = json_response['data'][0]
# array_images = obj['card_images']

# array_numbers = [];

# for image in array_images:
#    url = image['image_url']
#    number = re.search('cards/(.*).jpg', url).group(1)
#    array_numbers.append(number)


    

