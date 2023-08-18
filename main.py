import uuid
import tls_client
import threading
import colorama
import os
import requests
import time
import requests
import capmonster_python
import random
from colorama import Fore
import emoji as ej
import user_agent
from colorama import Fore
from timeit import default_timer as timer
from pystyle import Center, Colorate, Colors
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW(f"Leaked by .gg/opiumtools Proxy and Tweety on top")

colorama.init()

os.system('cls')

class Start:
    def __init__(self):
        self.session = tls_client.Session(
            client_identifier = "okhttp4_android_7", 
            ja3_string="771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-16-5-13-18-51-45-43-27-17513,29-23-24,0",
            h2_settings = {
                "HEADER_TABLE_SIZE": 65536,
                "MAX_CONCURRENT_STREAMS": 1000,
                "INITIAL_WINDOW_SIZE": 6291456,
                "MAX_HEADER_LIST_SIZE": 262144
            }, h2_settings_order = ["HEADER_TABLE_SIZE","MAX_CONCURRENT_STREAMS","INITIAL_WINDOW_SIZE","MAX_HEADER_LIST_SIZE"],
            supported_signature_algorithms = ["ECDSAWithP256AndSHA256", "PSSWithSHA256", "PKCS1WithSHA256", "ECDSAWithP384AndSHA384", "PSSWithSHA384", "PKCS1WithSHA384", "PSSWithSHA512", "PKCS1WithSHA512",],
            supported_versions = ["GREASE", "1.3", "1.2"],
            key_share_curves = ["GREASE", "X25519"],
            cert_compression_algo = "brotli",
            pseudo_header_order = [":method", ":authority", ":scheme", ":path"],
            connection_flow = 15663105,
            header_order = ["accept", "user-agent", "accept-encoding", "accept-language"]
          )
        
        def cookies(self):
                
            r = self.session.get(f'https://discord.com/api/v9//login/')
            self.cookie1 = r.headers['Set-Cookie'][0],
            self.cookie2 = r.headers['Set-Cookie'][1],
            self.cookie3 = r.headers['Set-Cookie'][2],

        
        def join(self):

            cookies(self)

            tokens = open('input/tokens.txt', 'r').read().splitlines()
            token = random.choice(tokens)
            headers = {
                    'Accept': '*/*',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Authorization': token,
                    #'Content-Length': 2,
                    'Content-Type': 'application/json',
                    'Origin': f'https://api/v9/invites/',
                    'Referer': f'https:///api/v9/invites/invites/{self.invite}',
                    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE3MzYyNywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
                    'User-Agent': user_agent.generate_user_agent(),
                    'Cookie': f'{self.cookie1}; {self.cookie2}; {self.cookie3};'
            }
            json_data = {"session_id" : uuid.uuid4().hex}
            response = self.session.post(f'https://discord.com/api/v9/invites/{self.invite}', 
                                    headers=headers, 
                                    json=json_data,
                                    )

            print(f'[{Fore.RED}/{Fore.RESET}]> {Fore.YELLOW}Tying To join with [{token[:19]}*****]- discord.gg/{self.invite} {Fore.RESET}')
            print(f'[{Fore.BLUE}+{Fore.RESET}] {Fore.GREEN}Joined with {token[:19]}*****]- discord.gg/{self.invite} {Fore.RESET}')         
    
        def singledm(self):

            try:
                cookies(self)

                tokens = open('input/tokens.txt', 'r').read().splitlines()
                token = random.choice(tokens)

                headers = {
                    'authority': 'discord.com',
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9',
                    'authorization': token,
                    'content-type': 'application/json',
                    'origin': 'https://discord.com',
                    'referer': 'https://discord.com/channels/@me',
                    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43',
                    'x-context-properties': 'eyJsb2NhdGlvbiI6IlF1aWNrc3dpdGNoZXIifQ==',
                    'x-debug-options': 'bugReporterEnabled',
                    'x-discord-locale': 'en-US',
                    'x-discord-timezone': 'America/New_York',
                    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTQuMC4xODIzLjQzIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE0LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5iaW5nLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluIjoid3d3LmJpbmcuY29tIiwic2VhcmNoX2VuZ2luZSI6ImJpbmciLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjA2NDQ2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
                }

                json_data = {
                    'recipients': [
                        self.userid,
                    ],
                }
                responsee = self.session.post('https://discord.com/api/v9/users/@me/channels', headers=headers, json=json_data)
                r = (responsee.json()['id'])
                headers = {
                    'Accept': '*/*',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Authorization': token,
                    'Content-Type': 'application/json',
                    'origin': 'https://discord.com',
                    'referer': f'https://discord.com/channels/@me/{r}',
                    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE3MzYyNywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
                    'User-Agent': user_agent.generate_user_agent(),
                    'Cookie': f'{self.cookie1}; {self.cookie2}; {self.cookie3};'
                }   
                json_data = {
                    'content': self.message,
                    'nonce': str(random.randint(999999999, 999999999999999999)),
                    'tts': False,
                    'flags': 0,
                }
                response = self.session.post(
                f'https://discord.com/api/v9/channels/{r}/messages',
                    headers=headers,
                    json=json_data,
                
                )

                print(f'[{Fore.RED}Pulse{Fore.RESET}]> Sent the message from [{Fore.RED}{token[:19]}*****{Fore.RESET}] [{Fore.RED}{self.message}{Fore.RESET}] [{Fore.RED}{str(random.randint(999999999, 999999999999999999))}{Fore.RESET}] {response.status_code}')
            except:
                print(f'[{Fore.RED}Pulse{Fore.RESET}]> Unkown Error      [{Fore.RED}{token[:19]}*****{Fore.RESET}] [{Fore.RED}{self.message}{Fore.RESET}] [{Fore.RED}{str(random.randint(999999999, 999999999999999999))}{Fore.RESET}]')
    
        def massdm(self):
            try:
                cookies(self)

                tokens = open('input/tokens.txt', 'r').read().splitlines()
                token = random.choice(tokens)
                ids = open('input/ids.txt', 'r').read().splitlines()
                idd = random.choice(ids)

                headers = {
                    'authority': 'discord.com',
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9',
                    'authorization': token,
                    'content-type': 'application/json',
                    'origin': 'https://discord.com',
                    'referer': 'https://discord.com/channels/@me',
                    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43',
                    'x-context-properties': 'eyJsb2NhdGlvbiI6IlF1aWNrc3dpdGNoZXIifQ==',
                    'x-debug-options': 'bugReporterEnabled',
                    'x-discord-locale': 'en-US',
                    'x-discord-timezone': 'America/New_York',
                    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTQuMC4xODIzLjQzIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE0LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5iaW5nLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluIjoid3d3LmJpbmcuY29tIiwic2VhcmNoX2VuZ2luZSI6ImJpbmciLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjA2NDQ2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
               }

                json_data = {
                   'recipients': [
                        idd,
                    ],
                }
    
                responsee = self.session.post('https://discord.com/api/v9/users/@me/channels', headers=headers, json=json_data)
                r = (responsee.json()['id'])

                headers = {
                    'Accept': '*/*',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Authorization': token,
                    'Content-Type': 'application/json',
                    'origin': 'https://discord.com',
                    'referer': f'https://discord.com/channels/@me/{r}',
                    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE3MzYyNywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
                    'User-Agent': user_agent.generate_user_agent(),
                    'Cookie': f'{self.cookie1}; {self.cookie2}; {self.cookie3};',
                }
                json_data = {
                    'content': self.message,
                    'nonce': str(random.randint(999999999, 999999999999999999)),
                    'tts': False,
                    'flags': 0,
                }
                responsee = self.session.post(
                    f'https://discord.com/api/v9/channels/{r}/messages',
                        headers=headers,
                        json=json_data,
                )

                print(f'[{Fore.BLUE}/{Fore.RESET}]> {Fore.YELLOW} Sending Message From: [{Fore.BLUE}{token[:19]}*****{Fore.RESET}] [{Fore.BLUE}{self.message}{Fore.RESET}] [{Fore.RED}{str(random.randint(999999999, 999999999999999999))}{Fore.RESET}]')
                print(f'[{Fore.BLUE}+{Fore.RESET}]{Fore.GREEN}  Message Sent!')

                with open('input/ids.txt', 'r+') as f:
                    lines = f.readlines()
                    f.seek(0)
                    for line in lines:
                        if line.strip() != idd:
                            f.write(line)
                    f.truncate()
            except:
                print(f'[{Fore.RED}!{Fore.RESET}]> Unkown Error      [{Fore.RED}{token[:19]}*****{Fore.RESET}] [{Fore.RED}{self.message}{Fore.RESET}] [{Fore.RED}{str(random.randint(999999999, 999999999999999999))}{Fore.RESET}]')

        def displaychange(self):

            cookies(self)

            tokens = open('tokens.txt', 'r').read().splitlines()
            token = random.choice(tokens)

            headers = {
               'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9',
                'Authorization': token,
                'Content-Type': 'application/json',
                'origin': 'https://discord.com',
                'referer': 'https://discord.com/channels/@me',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE3MzYyNywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
                'User-Agent': user_agent.generate_user_agent(),
                'Cookie': f'{self.cookie1}; {self.cookie2}; {self.cookie3};',
            }

            json_data = {
                'global_name': self.name,
            }

            response = self.session.patch('https://discord.com/api/v9/users/@me', headers=headers, json=json_data)
            print(f'   [{Fore.RED}Pulse{Fore.RESET}]> Attempted Name Change [{Fore.RED}{token[:19]}*****{Fore.RESET}] [{Fore.RED}{self.name}{Fore.RESET}] [{Fore.RED}{str(random.randint(999999999, 999999999999999999))}{Fore.RESET}] {response.status_code}')

        def biochange(self):

            cookies(self)

            tokens = open('input/tokens.txt', 'r').read().splitlines()
            token = random.choice(tokens)

            headers = {
                'authority': 'discord.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'authorization': token,
                'content-type': 'application/json',
                'origin': 'https://discord.com',
                'referer': 'https://discord.com/channels/@me',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43',
                'x-debug-options': 'bugReporterEnabled',
                'x-discord-locale': 'en-US',
                'x-discord-timezone': 'America/New_York',
                'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTQuMC4xODIzLjQzIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE0LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5iaW5nLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluIjoid3d3LmJpbmcuY29tIiwic2VhcmNoX2VuZ2luZSI6ImJpbmciLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjA2NDQ2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
                'Cookie': f'{self.cookie1}; {self.cookie2}; {self.cookie3};'
            }
            json_data = {
                'bio': self.bio,
            }
            response = self.session.patch('https://discord.com/api/v9/users/%40me/profile', headers=headers, json=json_data)
            print(f'   [{Fore.RED}Pulse{Fore.RESET}]> Changed Bio from [{Fore.RED}{token[:19]}*****{Fore.RESET}] to - [{Fore.RED}{self.bio}{Fore.RESET}] [{Fore.RED}{str(random.randint(999999999, 999999999999999999))}{Fore.RESET}] {response.status_code}')

        def check(self):
            tokens = open('input/tokens.txt', 'r').read().splitlines()
            token = random.choice(tokens)

            response = requests.get('https://discord.com/api/v9/users/@me/library', headers={"accept": "*/*","accept-encoding": "gzip, deflate, br","accept-language": "en-US,en;q=0.9","authorization": token,"cookie": "__dcfduid=88221810e37411ecb92c839028f4e498; __sdcfduid=88221811e37411ecb92c839028f4e498dc108345b16a69b7966e1b3d33d2182268b3ffd2ef5dfb497aef45ea330267cf; locale=en-US; OptanonConsent=isIABGlobal=false&datestamp=Fri+Jun+03+2022+15%3A36%3A59+GMT-0400+(Eastern+Daylight+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __stripe_mid=3a915c95-4cf7-4d27-9d85-cfea03f7ce829a88e5; __stripe_sid=b699111a-a911-402d-a08a-c8801eb0f2e8baf912; __cf_bm=nEUsFi1av6PiX4cHH1PEcKFKot6_MslL4UbUxraeXb4-1654285264-0-AU8vy1OnS/uTMTGu2TbqIGYWUreX3IAEpMo++NJZgaaFRNAikwxeV/gxPixQ/DWlUyXaSpKSNP6XweSVG5Mzhn/QPdHU3EmR/pQ5K42/mYQaiRRl6osEVJWMMtli3L5iIA==","referer": "https://discord.com/channels/967617613960187974/981260247807168532","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","sec-gpc": "1","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36","x-discord-locale": "en-US","x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuNjEgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMi4wLjUwMDUuNjEiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwNDEwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="}, timeout=5)
            if response.status_code == 200: 
                print(f"   {Fore.RESET}({Fore.GREEN}+{Fore.RESET}) Valid   [{Fore.GREEN}{token[:19]}*****{Fore.RESET}]")
            else:
                print(f"   {Fore.RESET}({Fore.RED}!{Fore.RESET}) Invalid [{Fore.RED}{token[:19]}*****{Fore.RESET}]")

                with open('input/tokens.txt', 'r+') as f:
                    lines = f.readlines()
                    f.seek(0)
                    for line in lines:
                        if line.strip() != token:
                            f.write(line)
                    f.truncate()

        def verifier(self):

            cookies(self)

            tokens = open('input/tokens.txt', 'r').read().splitlines()
            token = random.choice(tokens)
            headers = {
                'Content-Type': 'application/json',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US',
                'DNT': '1',
                'origin': 'https://discord.com',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                'TE': 'Trailers',
                'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                'authorization': token,
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
                'Cookie': f'{self.cookie1}; {self.cookie2}; {self.cookie3};'
            }

            emojiee = ej.emojize(self.emojiee)
            r = requests.put(
                f"https://discordapp.com/api/v9/channels/{self.channelid}/messages/{self.messageid}/reactions/{emojiee}/@me",
                headers=headers)
            
            print(f'   [{Fore.RED}Pulse{Fore.RESET}]> Attempted Verify [{Fore.RED}{token[:19]}*****{Fore.RESET}] [{Fore.RED}{emojiee}{Fore.RESET}] [{Fore.RED}{str(random.randint(999999999, 999999999999999999))}{Fore.RESET}] {r.status_code}')


        def ui(self):  
            print(Center.XCenter(Colorate.Vertical(Colors.green_to_cyan, f"""
                               _____                           ____        _     __         
                              / ___/____  ____  ____  ___     / __ \____ _(_)___/ /__  _____
                              \__ \/_  / / __ \/ __ \/ _ \   / /_/ / __ `/ / __  / _ \/ ___/
                             ___/ / / /_/ /_/ / / / /  __/  / _, _/ /_/ / / /_/ /  __/ /    
                            /____/ /___/\____/_/ /_/\___/  /_/ |_|\__,_/_/\__,_/\___/_/     
                                         Leaked By discord.gg/opiumtools                                                     
                                        cr1sty.w get fucked by opiumtools                                           
                                           
                                  [1] > Server Joiner           [5] > Bio Changer                                          
                                  [2] > Single Mass DM          [6] > Token Checker
                                  [3] > Server Mass DM          [7] > Verifier 
                                  [4] > Name Changer            [8] > ID Scraper
                                          discord.gg/opiumtools on top
     """, 1)))
            choice = input('                                  [Option]->')
            tokenamount = len(open('input/tokens.txt', 'r').readlines())
            idamount = len(open('input/ids.txt', 'r').readlines())

            if choice == '1':
                self.invite = input(f'     Invite {Fore.RED}>{Fore.RESET} ')
                self.delay = input('    Delay: ')
                for i in range(int(tokenamount)):
                    time.sleep(int(self.delay))
                    threading.Thread(target = join,args = [self]).start()

            if choice == '2':
                self.userid = input(f'     ID {Fore.RED}>{Fore.RESET} ')
                self.message = input(f'     Message {Fore.RED}>{Fore.RESET} ')
                self.delay = input('    Delay: ')
                self.amount = input(F'     Amount {Fore.RED}> {Fore.RESET} ')
                for i in range(int(self.amount)):
                    time.sleep(int(self.delay))
                    threading.Thread(target = singledm,args = [self]).start()


            if choice == '3':
                self.message = input(f'     Message {Fore.RED}>{Fore.RESET} ')
                self.delay = input('    Delay: ')
                for i in range(int(idamount)):
                    time.sleep(float(self.delay))
                    threading.Thread(target = massdm,args = [self]).start()


            if choice == '4':
                self.name = input(f'     Name {Fore.RED}>{Fore.RESET} ')
                self.delay = input('    Delay: ')
                for i in range(int(tokenamount)):
                    time.sleep(float(self.delay))
                    threading.Thread(target = displaychange,args = [self]).start()


            if choice == '5':
                self.bio = input(f'     Bio {Fore.RED}>{Fore.RESET} ')
                self.delay = input('    Delay: ')
                for i in range(int(tokenamount)):
                    time.sleep(float(self.delay))
                    threading.Thread(target = biochange,args = [self]).start()


            if choice == '6':
                self.delay = input('    Delay: ')
                for i in range(int(tokenamount)):
                    time.sleep(float(self.delay))
                    threading.Thread(target = check,args = [self]).start()

            if choice == '7':
                self.channelid = input(f'     Channel ID {Fore.RED}>{Fore.RESET} ')
                self.messageid = input(f'     Message ID {Fore.RED}>{Fore.RESET} ')
                self.emojiee = input(f'     Emoji(Example: :skull:) {Fore.RED}>{Fore.RESET} ')
                self.delay = input('    Delay: ')
                for i in range(int(tokenamount)):
                    time.sleep(float(self.delay))
                    threading.Thread(target = verifier,args = [self]).start()

            if choice == '8':
                from scrape import scraper
                self.serverid = input(f'     Server ID {Fore.RED}>{Fore.RESET} ')
                self.channelid = input(f'     Channel ID {Fore.RED}>{Fore.RESET} ')

                if __name__ == "__main__":
                    try:
                        scraper(f"{self.serverid}", f"{self.channelid}")
                    except Exception as e:
                        print(e)
                        os.abort()


        
        ui(self)


Start()
