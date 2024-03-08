#import smtplib, ssl
#from email.message import EmailMessage 

#smtp_server = "smtp.gmail.com"
#port = 587
#sender_email = "bogdan.viblyy@gmail.com"
#password = input("Type your password and press enter: ")

##Create a secure SSL context
#context = ssl.create_default_context()
#msg=EmailMessage()
#msg.set_content("Tere tulemast!")
#msg['Subject']="Kirja teema"
#msg['From']="bogdan.viblyy@gmail.com"
#msg['To']="marina.oleinik@tthk.ee"


## Try to log in to server and send email
#try:
#    server = smtplib.SMTP(smtp_server,port)
#    server.ehlo() #Can be omitted
#    server.starttls(context=context)
#    server.ehlo() #Can be omitted
#    server.login(sender_email,password)
#    server.sendmail(sender_email,sender_email,msg)
#    # TODO: Send email here
#except Exception as e:
#    # Print any error messages to stdout
#    print(e)
#finally:
#    server.quet()

