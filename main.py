import os
import time
import json
import random
import requests
import threading
import skidbilly as pystyle

from colorama import Fore
from itertools import cycle


with open('data/config.json') as f:
    config = json.load(f)

    debug       = config['Aio']['Debug']
    use_proxies = config['Generator']['Use Proxies']
    captcha_key = config['Generator']['captcha_key']





class captchaio:
    def __init__(self, ) -> None:
        pass
        self.session = requests.Session()
        self.api_key = captcha_key

    def createTask(self, blob):
        try:
            headers = {'Content-Type': 'application/json'}
            json = {
                "clientKey": self.api_key,
                "task":
                    {
                        "type":"FunCaptchaTaskProxyless",
                        "websiteURL":"https://www.roblox.com/",
                        "websitePublicKey":"A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F",
                        "funcaptchaApiJSSubdomain":"https://roblox-api.arkoselabs.com/",
                        "data": f"{{\"blob\":\"{blob}\"}}",
                        "userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
                    }
            }
            r = self.session.post('https://api.captchaai.io/createTask', json=json, headers=headers)
            return r.json()['taskId']
        except:
            pass

    def getResult(self, blob):
        json = {
            'clientKey': self.api_key,
            'taskId'   : captchaio().createTask(blob)
            }
        headers = {'Host': 'api.captchaai.io','Content-Type': 'application/json'}
        while True:
            time.sleep(1)
            r = self.session.post('https://api.captchaai.io/getTaskResult', json=json, headers=headers)
            if r.json()['status'] == "ready":
                return r.json()['solution']['token']




class stat():
    created = 0
    err     = 0


class Misc:
    def __init__(self):
        pass

    def get_cookie():
        with open('data/cookies.txt', 'r') as f:
            cookies = [line.strip('\n') for line in f]
        return cookies
     
    cookie = get_cookie()
    ilit_cookies = cycle(cookie)


class aio:
    def __init__(self) -> None:
        self.session = requests.Session()

    def csrf(self):
        try:
            csrf_token = self.session.post('https://auth.roblox.com/v2/signup').headers['x-csrf-token']
            return csrf_token
        except Exception as e:
            if debug == True:
                print(e)
            else:
                None

    def csrfFriend(cookie):
        r = requests.post('https://auth.roblox.com/v2/logout', headers={'cookie': f'.ROBLOSECURITY={cookie}','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'})
        return r.headers.get('x-csrf-token')


    def GetUser(self, username):
        r = self.session.get(f'https://api.roblox.com/users/get-by-username?username={username}')
        return r.json()['Id']


    def CheckUser(self, username):
        try:
            headers = {'authority': 'auth.roblox.com','accept': 'application/json, text/plain, */*','accept-language': 'en-GB,en;q=0.9','content-type': 'application/json;charset=UTF-8','origin': 'https://www.roblox.com','referer': 'https://www.roblox.com/','sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36','x-csrf-token': aio().csrf(),}
            json = {'username': username,'context': 'Signup','birthday': '2000-05-07T23:00:00.000Z',}
            response = self.session.post('https://auth.roblox.com/v1/usernames/validate', headers=headers, json=json)
            if response.json()['code'] == 0:
                return username
            else:
                return username + ''.join(random.choices('poiuytrewqlkjhgfdsamnbvcxz0123456789', k=3))
        except Exception as e:
            if debug == True:
                print(e)
            else:
                None

    def get_data(self):
        try:
            json = {'username': 'randoffmuser837735','password': 'oujdwadiaw985'}
            headers = {'x-csrf-token': aio().csrf()}
            signup = self.session.post('https://auth.roblox.com/v2/signup', json=json, headers=headers, proxies=None, timeout=5).json()
            infoJson = str(signup).split("fieldData': '")[1].split("'}]")[0].split(',')
            dxBlob = infoJson[1]
            captchaId = infoJson[0]
            res = {'captcha_id': captchaId, 'blob': dxBlob}
            return res
        except Exception as e:
            if debug == True:
                print(e)
            else:
                None

    def Generate(self):
        try:
            proxy = random.choice(open('data/proxies.txt', 'r').read().splitlines())
            proxies = {
                'http': f'http://{proxy}', 'https': f'http://{proxy}'
            }
            username   = aio().CheckUser(random.choice(open('data/usernames.txt', 'r').read().splitlines()))
            password   = ''.join(random.choices('QWERTYUIOPASDFGHJKLZXCVBNMpoiuytrewqlkjhgfdsamnbvcxz0123456789', k=13))
            gender     = random.randint(1,2)
            data       = aio().get_data()
            captcha_id = data['captcha_id']
            blob       = data['blob']
            cp_token   = captchaio().getResult(blob)

            headers = {'authority': 'auth.roblox.com','accept': 'application/json, text/plain, */*','accept-language': 'en-GB,en;q=0.9','content-type': 'application/json;charset=UTF-8','dnt': '1','origin': 'https://www.roblox.com','referer': 'https://www.roblox.com/','sec-ch-ua': '"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36','x-csrf-token': aio().csrf(),}
            json = {
                'username': username,
                'password': password,
                'birthday': '2000-02-09T23:00:00.000Z',
                'gender': gender,
                'isTosAgreementBoxChecked': True,
                'captchaId': captcha_id,
                'captchaToken': cp_token,
                'agreementIds': [
                    '54d8a8f0-d9c8-4cf3-bd26-0cbf8af0bba3',
                    '848d8d8f-0e33-4176-bcd9-aa4e22ae7905',
                ],
            }
            if use_proxies == True:
                response = self.session.post('https://auth.roblox.com/v2/signup', headers=headers, json=json, proxies=proxies)
            else:
                response = self.session.post('https://auth.roblox.com/v2/signup', headers=headers, json=json)
            if "userId" in response.text:
                stat.created += 1
                userID = response.json()['userId']
                cookie = response.cookies['.ROBLOSECURITY']
                print(f"{Fore.BLUE}[ {Fore.GREEN}+ {Fore.BLUE}]{Fore.RESET} Created Account ({stat.created})")
                print(cookie[0:200])
                open('results/accounts.txt', 'a').write(f'{username}:{password}:{userID}:{cookie}\n')
                open('results/account.txt', 'a').write(f'{username}:{password}\n')
                open('results/withproxy.txt', 'a').write(f'{cookie}:{proxy}\n')
                open('results/cookies.txt', 'a').write(f'{cookie}\n')
        except Exception as e:
            if debug == True:
                print(e)
            else:
                None

    def friend(self, userId):
        try:
            cookie = next(Misc.ilit_cookies)
            headers = {'authority': 'friends.roblox.com','accept': 'application/json, text/plain, */*','accept-language': 'en-GB,en;q=0.9','content-type': 'application/json;charset=utf-8','cookie': f'.ROBLOSECURITY={cookie}','origin': 'https://web.roblox.com','referer': 'https://web.roblox.com/','sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36','x-csrf-token': aio.csrfFriend(cookie),}
            response = self.session.post(f'https://friends.roblox.com/v1/users/{userId}/request-friendship', headers=headers)
            try:
                if response.json()['success'] == True:
                    print(f"{Fore.BLUE}[ {Fore.GREEN}+ {Fore.BLUE}]{Fore.RESET} Successfully Followed")
            except:
                pass
            try:
                if response.json()['errors'][0]['code'] == 5:
                    print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Request already sent")
            except:
                pass
        except Exception as e:
            if debug == True:
                print(e)
            else:
                pass



class menu:
    def __init__(self):
        pass

    def main(self):
        os.system('cls')
        os.system(f'title Roblox Aio ^| Twiddle Menu')
        pystyle.Write.Print("""
                                            ╦═╗┌─┐┌┐ ┬  ┌─┐─┐ ┬  ┌─┐┬┌─┐
                                            ╠╦╝│ │├┴┐│  │ │┌┴┬┘  ├─┤││ │
                                            ╩╚═└─┘└─┘┴─┘└─┘┴ └─  ┴ ┴┴└─┘""", pystyle.Colors.purple_to_blue, interval=0)
        
        print("\n\n")

        print(f'                                              {Fore.RED}[{Fore.RESET} {Fore.BLUE}1{Fore.RESET} {Fore.RED}]{Fore.RESET} Account Creator')
        print(f'                                              {Fore.RED}[{Fore.RESET} {Fore.BLUE}2{Fore.RESET} {Fore.RED}]{Fore.RESET} Friend User')


        print("\n\n\n")
        choice = int(input(f"{Fore.GREEN} [ {Fore.CYAN}?{Fore.GREEN} ] Enter Choice {Fore.GREEN}> {Fore.WHITE}"))  


        if choice == 1:
            os.system('cls')
            pystyle.Write.Print("""
                                            ╔═╗┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┌─┐┬─┐
                                            ║ ╦├┤ │││├┤ ├┬┘├─┤ │ │ │├┬┘
                                            ╚═╝└─┘┘└┘└─┘┴└─┴ ┴ ┴ └─┘┴└─""", pystyle.Colors.purple_to_blue, interval=0)
            print("")
            threads = input(f"{Fore.GREEN}[{Fore.CYAN} ? {Fore.GREEN}] Accounts To Create {Fore.CYAN}> {Fore.WHITE}")

            for i in range(int(threads)):
                x = threading.Thread(target=aio().Generate)
                x.start()

            for i in range(int(threads)):
                x.join()
            time.sleep(2.2)
            input(f"{Fore.RED}[{Fore.RESET}{Fore.BLUE}Cookie Creator{Fore.RESET}{Fore.RED}]{Fore.RESET} Completed tasks! Press Enter To Return To The Menu {Fore.YELLOW}>{Fore.RESET} ")
            menu().main()

        if choice == 2:
            os.system('cls')
            pystyle.Write.Print("""
                                            ╔═╗┬─┐┬┌─┐┌┐┌┌┬┐
                                            ╠╣ ├┬┘│├┤ │││ ││
                                            ╚  ┴└─┴└─┘┘└┘─┴┘""", pystyle.Colors.purple_to_blue, interval=0)
            print("")
            username = input(f"{Fore.GREEN}[{Fore.CYAN} ? {Fore.GREEN}] Username {Fore.CYAN}> {Fore.WHITE}")
            threads = input(f"{Fore.GREEN}[{Fore.CYAN} ? {Fore.GREEN}] Requests to send {Fore.CYAN}> {Fore.WHITE}")

            userID = aio().GetUser(username)

            for i in range(int(threads)):
                x = threading.Thread(target=aio().friend, args=(userID,))
                x.start()

            for i in range(int(threads)):
                x.join()
            time.sleep(2.2)
            input(f"{Fore.RED}[{Fore.RESET}{Fore.BLUE}Friend User{Fore.RESET}{Fore.RED}]{Fore.RESET} Completed tasks! Press Enter To Return To The Menu {Fore.YELLOW}>{Fore.RESET} ")
            menu().main()



menu().main()
