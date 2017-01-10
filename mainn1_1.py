
import imapclient, backports, imaplib, sys, os

#def nullout(one1, two2, three3):
#    pass

#sys.excepthook = nullout

# class my1_imapclient(imapclient.IMAPClient):
#     def _create_IMAP4(self):
#         if self.stream:
#             return imaplib.IMAP4_stream(self.host)

#         if self.ssl:
#             return imaplib.IMAP4_SSL(self.host, self.port, 
#                                      self.ssl_context, self._timeout)
    


# Общие данные. Пока статика. Имена переменных не имеют значения.
HOST = "imap.yandex.ru"
USER = "FrikiTiki"
PASSWD = "RikiFrikiTikiTavi000"
LOCAL_DIR = "/home/dimasik/mboxes/" + USER + "/"

FIRST_RUN = 1

# Это для поддержки шифрования SSL. 
# (!!!) Чтобы это работало в системе должна быть библиотека OpenSSL. А в Python должна стоять pyopenssl(обвязка для OpenSSL).
# (!!!) В Windows OpenSSL нужно поставить руками.
my1_context = imapclient.create_default_context()
my1_context.check_hostname = False
my1_context.verify_mode = backports.ssl.CERT_NONE

# Коннестимся.
my2_server = imapclient.IMAPClient(HOST, use_uid=True, ssl=True, ssl_context=my1_context)
try:
    login_status = my2_server.login(USER, PASSWD)
   # print(login_status, '\n') # Проверяем что успешно вошли. Чисто для дебага.
except:
    print("Login Failed!", '\n\n') 

# Запрашиваем у сервера список каталогов и еще какую-то неведомую фигню.
directory_list = my2_server.list_folders(directory=u"", pattern=u"*")

# Выводим список каталогов по одному за раз и добавляем их в список. 
# Спасибо разработчику этой замечательной библиотеки (imapclient), 
# за то что написал процедуру парсинга ответа и преобразования из UTF-7 в UTF-8.
parsed_mail_dir = [one_dir[2] for one_dir in directory_list]
# А это предыдущий вариант только что увиденного включения.
#   for one_unit in directory_list:
#       print(one_unit[2], '\n')

print(parsed_mail_dir, '\n')

##########################################################################################################
##################################___Тут больше нечего ловить___##########################################
##########################################################################################################

local_dirs = os.listdir(LOCAL_DIR)
print(local_dirs)

#is_file = os.path.exists('')




class synchrophasotron():
    def tolocal(self, list_server_dir):
        pass
    
    def toserver(self, list_local_dir):
        pass



# Пробегаем несколько раз с таймаутом
my_step = 0
#while True:
#for my_step in range(1,100,1):
    #time.sleep(1)
# В этом цикле пробегаем по всем найденным папкам и ищем в них письма,
# апосля выводим результат и его длинну.
# Длинна тоже чисто для дебага.
search_result = []
for current_dir in parsed_mail_dir:
    my2_server.select_folder(current_dir)
    search_result.append(my2_server.search())
i = 0
while True:
    try:
        print(search_result[i], '--->', len(search_result[i]))
        i += 1
    except IndexError:
        print('\n', '===', my_step, '===')
        my_step += 1
        break


# Переходим в с_каталог
my2_server.select_folder('INBOX|My111')


# Получаем с сервера заданное (search_result[3][1]) сообщение, получаем в виде:
#
# >>> type(fetch_response)
# <class 'collections.defaultdict'>
#
# Короче это сообщение-словарь-в-словаре. {2: {b'RFC822' : ' b'Сообщение'} . 
#fetch_response = my2_server.fetch(search_result[3][1], ['RFC822'])
fetch_response = my2_server.fetch(search_result[1], ['RFC822'])
#fetch_response = my2_server.fetch(search_result[3][1], ['INTERNALDATE', 'RFC822']) - это тоже работает
print(fetch_response)
# Получить, из ообщение-словарь-в-словаре, словарь по ключу '2'
fetch_response_dictionary = fetch_response[2]

# На всяк случай получим все ключи, а вдруг потом понадобятся??? o_o
fetch_response2_keys = fetch_response_dictionary.keys()

# Наконец получим само сообщение по ключу b'RFC822'
target_message_body = fetch_response_dictionary[b'RFC822']

# Буковка 'b' перед ключем ( [b'RFC822'] ) значит что объект типа 'bytes'.
# Преобразуем его в строку методом 'decode'.
target_message_body = target_message_body.decode('utf-8')

#print('\n\n', fetch_response2_keys)
#print('\n\n', fetch_response_dictionary)
print('\n\n', target_message_body)

