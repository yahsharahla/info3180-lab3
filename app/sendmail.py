import smtplib

#message information
fromaddr = ''
toaddrs = ''
message = """From: {} <{}>
To: {} <{}>
Subject: {}
{}
"""
fromname = ''
toname = ''
subject = ''
msg = """"""

# Credentials (if needed)
username = 'artnellebanks@gmail.com'
password = 'zszgysigcwoqzoqv'
 
def mailit(fromname,fromaddr,toname,toaddrs,subject,msg):
  fromname = fromname
  fromaddr = fromaddr
  toname = toname
  toaddrs = toaddrs
  subject = msg
  #messagetosend = ""
  messagetosend = message.format(fromname,fromaddr,toname,toaddrs,subject,msg)
  
# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, messagetosend)
server.quit()