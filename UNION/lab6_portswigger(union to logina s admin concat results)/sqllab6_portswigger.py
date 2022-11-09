
import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.connectionpool.InsecureRequestWarning())

proxies = {'http': 'http://127.0.0.1:8080' , 'https': 'http://127.0.0.1:8080'}


def exploit_user_table(url):
    
    path =  


if __name__ == '__main__':
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print('[+] Usage: %s <url>' % sys.argv[0])
        print('[+] Example: %s www.example.com' % sys.argv[0])
        sys.exit(-1)

    print('[+] Dumping the list of username and passwords.....')

    if not exploit_user_table(url):
        print('[-] Did not find the list of any usernames and passwords.')