import smtplib
import imapclient
import pyzmail

conn = smtplib.SMTP('smtp.gmail.com',  587)
conn.ehlo()
conn.starttls()
conn.login('your_email', 'your_password')
conn.sendmail('your_mail', 'receiver_mail', 'Subject: your_subject\n\nyour_message\n\nsignature')
conn.quit()

# to read mails
conn = imapclient.IMAPClient('imap.gmail.com',ssl=True)
conn.login('your_email', 'your_password')

conn.select_folder('INBOX', readonly=True)

emails = conn.search(['SINCE 20-Aug-2020'])
print(emails)
rawMessage = conn.fetch([],['BODY[]','FLAGS'])