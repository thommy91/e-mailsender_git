import smtplib, ssl
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.application import MIMEApplication

smtp_server = 'smtp.gmail.com'
smtp_port = 587
#Replace with your own gmail account
gmail = 'thomas91code@gmail.com'
password = '???????????'

message = MIMEMultipart('mixed')
message['From'] = 'Contact <{sender}>'.format(sender = gmail)
message['To'] = 'contact@company.com'
message['CC'] = 'contact@company.com'
message['Subject'] = 'Hello'

msg_content = '<h4>Hi There,<br> This is a testing message.</h4>\n'
body = MIMEText(msg_content, 'html')
message.attach(body)

attachmentPath = r"C:\Users\thoma\OneDrive\Dokumenter\100daysofcode\e-mailsender_git\test.txt"
try:
	with open(attachmentPath, "rb") as attachment:
		p = MIMEApplication(attachment.read(),_subtype="pdf")	
		p.add_header('Content-Disposition', "attachment; filename= %s" % attachmentPath.split("\\")[-1]) 
		message.attach(p)
except Exception as e:
	print(str(e))

msg_full = message.as_string()
context = ssl.create_default_context()

with smtplib.SMTP(smtp_server, smtp_port) as server:
	server.ehlo()  
	server.starttls(context=context)
	server.ehlo()
	server.login(gmail, password)
	server.sendmail(gmail, 
				#to.split(";") + (cc.split(";") if cc else []),
                "thomas_aj_9@hotmail.com",
				msg_full)
	server.quit()

print("email sent out successfully")