#sending mail using python


import smtplib
try:
	s=smtplib.SMTP('smtp.gmail.com','587')
	s.starttls()
	sender='pritamchaurasiya11@gmail.com'
	receiver='kingcofcrew@gmail.com'
	msg="hi"
	s.login(sender,'Type your email password')
	s.sendmail(sender,receiver,msg)
except:
	print("some error occured")
else:
	print("msg sent successfully")
	s.quit()