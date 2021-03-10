# mengubah terlebih dahulu fitur keamanan baru GMAIL “less secure apps” 
# dari OFF ke ON atau AKTIFKAN pada akun gmail yang digunakan untuk mengizinkan aplikasi Python mengakses email tersebut.
# link = https://www.google.com/settings/security/lesssecureapps
# source = https://www.pythonindo.com/cara-mengirim-email-menggunakan-python/

# TANPA INPUT ALAMAT EMAIL (2 email)

import getpass, smtplib                                     # import the packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#setup sender and receiver(s)
sender = "test.email.riza@gmail.com"
password = getpass.getpass(prompt="Password : ", stream=None)   # supaya password tidak terlihat
receivers = "zahrotunnisariza@gmail.com,rizaznisa93@gmail.com"

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receivers

#messages
msg['Subject'] = "Test Python"                      # email subject
 
body = "Hello, Selamat pagi menjelang siang!"       # emali body or messages
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)        # create server
server.starttls()
server.login(sender, password)                     # login to sender's email
text = msg.as_string()
server.sendmail(sender, receivers, text)             # send the messages or email
server.quit()