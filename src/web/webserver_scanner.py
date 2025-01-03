import requests
import socket

def foot_printing(url):
    request = requests.get(url)
    header_list = [
        'Server', 'Date', 'Via', 'X-Powered-By', 'X-Country-Code', 'Connection','Content - Length']
    for header in header_list:
        try:
            result = request.headers[header]
            print('%s: %s' % (header, result))
        except Exception as err:
            print('%s: No Details Found' % header)

def testing_availability_of_http(url):
    method_list = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'TRACE', 'TEST']
    for method in method_list:
        req = requests.request(method, url)
        print(method, req.status_code, req.reason)
        if method == 'TRACE' and 'TRACE / HTTP/1.1' in req.text:
            print('Cross Site Tracing(XST) is possible')

def scan():
    with open("websites.txt", "r") as urls:
        for url in urls:
            url = url.strip()
            req = requests.get(url)
            print(url, 'report:')

            try:
                protection_xss = req.headers['X-XSS-Protection']
                if protection_xss != '1; mode = block':
                    print('X-XSS-Protection not set properly, it may be possible:', protection_xss)
            except:
                print('X-XSS-Protection not set, it may be possible')

            try:
                options_content_type = req.headers['X-Content-Type-Options']
                if options_content_type != 'nosniff':
                    print('X-Content-Type-Options not set properly:', options_content_type)
            except:
                print('X-Content-Type-Options not set')

            try:
                transport_security = req.headers['Strict-Transport-Security']
            except:
                print('HSTS header not set properly, Man in the middle attacks is possible')

            try:
                content_security = req.headers['Content-Security-Policy']
                print('Content-Security-Policy set:', content_security)
            except:
                print('Content-Security-Policy missing')



def garb(url):

    try:
       s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.htons(0x0800))
       s.connect((url, 80))
       s.send('GET HTTP/1.1 \r\n')
       ret = s.recv(1024)
       print ('[+]' + str(ret))
       return
    except Exception as error:
       print (" Not information grabbed:" + str(error))
       return


if __name__ == '__main__':
  testing_availability_of_http('http://192.168.0.20/cgi-bin/')
  foot_printing('http://192.168.0.20/cgi-bin/')
  garb('http://192.168.0.20/cgi-bin/')
  scan()
