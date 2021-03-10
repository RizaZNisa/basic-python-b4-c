# mengubah terlebih dahulu fitur keamanan baru GMAIL “less secure apps” 
# dari OFF ke ON atau AKTIFKAN pada akun gmail yang digunakan untuk mengizinkan aplikasi Python mengakses email tersebut.
# link = https://www.google.com/settings/security/lesssecureapps
# source = https://www.pythonindo.com/cara-mengirim-email-menggunakan-python/

# DENGAN INPUT ALAMAT EMAIL (hanya 1 email)

import getpass, smtplib, email                                     # import the packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#input email penerima atau receivers

emailbaru = input ("Masukkan email : ")                 # Input Email baru  

data = open ("receiver_list.txt", "a")                  # Save email ke file
data.write(emailbaru + "\n")
data.close() 

#setup sender and receiver(s)
sender = "test.email.riza@gmail.com"
password = getpass.getpass(prompt="Password : ", stream=None)   # supaya password tidak terlihat
receiver = emailbaru

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver

#messages
msg['Subject'] = "Test Python"                      # email subject
 
body = "Hello, Selamat pagi menjelang siang!"       # emali body or messages
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)        # create server
server.starttls()
server.login(sender, password)                     # login to sender's email
text = msg.as_string()
server.sendmail(sender, receiver, text)             # send the messages or email
server.quit()