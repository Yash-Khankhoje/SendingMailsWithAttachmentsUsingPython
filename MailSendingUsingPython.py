#User Interactice Mail Sending...
import imghdr
import smtplib
import os
import sys
from email.message import EmailMessage
from email.mime.text import MIMEText

sender_email = str(input("From: "))
password = str(input("Please enter your password.: "))
rec_email = []
ReciverChoice = str(input("Do you want to send the mail to all addresses of the text file?[yes/no]"))
if ReciverChoice.lower() == "yes":
    contacts = []
    filepath = str(input("Enter the text file including the file paths.: "))
    with open(filepath) as fp:
        line = fp.readlines()
        for l in line:
            contacts.append(l)
    Recivers = []
    for i in contacts:
        j = i.replace('\n', '')
        Recivers.append(j)
    Recivers.remove(Recivers[-1])
    for i in Recivers:
        Reciver = i
        print(Reciver)
        rec_email.append(Reciver)
elif ReciverChoice.lower() =="no":
    ReciverCount = int(input("To how many people do you want to send this.?: "))
    for i in range(0,ReciverCount):
        Reciver = str(input("To: "))
        print(Reciver)
        rec_email.append(Reciver)
#rec_email = str(input("To: "))


msg = EmailMessage()
subject = str(input("Subject: "))
choice = str(input("Do you want to get the text from text file ?[yes/no]: "))
if choice.lower() == "no":
    text = str(input("Text: "))
elif choice.lower() == "yes":
    FileToRead = str(input("Please enter the file which you want to read : "))
    F = open(FileToRead, 'r')
    text = F.read()
    F.close()
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = rec_email
msg.set_content(text)

def SendNormalMail():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, password)
        print("Login success")
        smtp.send_message(msg)
        print("Email has been sent to ", rec_email)

def AttachmentCount():
    AttachmentQuant = int(input("Please enter how many attachments do you want to attach.: "))
    Files = []
    for i in range(0,AttachmentQuant):
        Attachments = str(input("File Name: "))
        Files.append(Attachments)
    AttachmentInsertion(Files)

def AttachmentInsertion(Files):
    for File in Files:
        if File[-1] == "g":
            with open(File, 'rb') as f:
                file_data = f.read()
                file_type = imghdr.what(f.name)
                file_name = f.name
            #print(file_type)
            msg.add_attachment(file_data, maintype = 'image', subtype = file_type, filename = file_name)
        elif File[-1] == "f":
            with open(File, 'rb') as f:
                file_data = f.read()
                file_name = f.name
                # print(file_type)
            msg.add_attachment(file_data, maintype='application', subtype='octet-tream', filename=file_name)
        elif File[-1] == "t":
            file_name = File
            msg.add_attachment(open(file_name, "r").read(), filename=file_name)

while(True):
   Task = str(input("Do you want to attach any file? [yes/no]: "))
   if Task.lower() == "yes":
       AttachmentCount()
       SendNormalMail()
       sys.exit()
   else:
       print("Sending message.")
       SendNormalMail()
       sys.exit()




