import requests, json, random, os, re, time
from colorama import Back, Fore, Style
#------------------------ALL FUNCTIONS----------------------
def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
def updates():
    pass
#-----------------------------------------------------------
while True:
    try:
        clear()
        if os.name == 'posix':
            otv = input('Вставьте путь до текстового файла пример:\n/sdcard/Downloads/аккаунты от вк.txt\n# ')
        else:
            otv = input('Вставьте путь до текстового файла пример:\nC:\\...\\аккаунты от вк.txt\n# ')
        
        with open(otv) as vk_log:
            cont = vk_log.read()
            vk_log.close()
        login = re.findall('(\w+):', cont)
        password = re.findall(':(\w+)', cont)
        break
    except:
        pass

gift = str(input('ID подарка: '))
user_id = str(input('''Ссылка на пользователя, которому нужно отправить подарок
(Пример: vk.com/XXXXXX - вместо иксов ник или цифры без ID): '''))
r = requests.post('http://regvk.com/id/', data={'link':'vk.com/'+user_id, 'button':'Определить+ID'})
user_id = re.findall('ID пользователя: (\w+)', r.text)[0]
message = str(input('Сообщение: '))
private = str(input('Анонимно отправить? (1-да?/0-нет) '))
ckok_raz = int(input('Сколько подарков отправить с каждого аккаунта? '))
token = []
clear()

for i in range(len(login)):
    try:
        r = requests.get('https://oauth.vk.com/token?grant_type=password&client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH&username='+login[i]+'&password='+password[i])
        token1 = json.loads(r.text)
        token.append(token1['access_token'])
    except:
        token.append(' ')
        print(Fore.RED+token1['error_description']+Style.RESET_ALL)


for i1 in range(len(token)):
    for i in range(ckok_raz):
        rnd = random.randint(1, 99999)
        rnd1 = random.randint(1, 20)
        if token == ' ':
            break
        try:
            r = requests.get('https://api.vk.com/method/gifts.send?user_ids='+user_id+'&privacy='+private+'&message='+message+'&gift_id='+gift+'&guid='+str(rnd)+'&access_token='+str(token[i1])+'&v=5.52')
            txt = json.loads(r.text)
            error = re.findall('{"(\w+)":{', r.text)
            
            if error[0] == 'response':
                print(Fore.GREEN+'Отправлено!'+Style.RESET_ALL)
            elif txt['error']['error_code'] == 14:
                print('Решите капчу: '+txt['error']['captcha_img'])
                captcha_sid = txt['error']['captcha_sid']
                captcha_key = input('# ')
                r = requests.get('https://api.vk.com/method/gifts.send?user_ids='+user_id+'&privacy='+private+'&message='+message+'&gift_id='+gift+'&guid='+str(rnd)+'&access_token='+str(token[i1])+'&v=5.52&captcha_sid='+str(captcha_sid)+'&captcha_key='+str(captcha_key))
            else:
                print(Fore.RED+'ERROR: '+str(json.loads(r.text)['error']['error_msg'])+Style.RESET_ALL)
        except IndexError:
            print('Системная ошибка!')
