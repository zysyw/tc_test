

def testRedMail():
    from redmail import outlook
    from redbox import EmailBox
    from redbox.query import SEEN, FROM, HEADER

    outlook.username = 'liufan18279580792@outlook.com'
    outlook.password = 'liufan123456789'

    # And then you can send emails
    outlook.send(
        receivers=["zysyw@163.com"],
        subject="An example",
        text="Hi, this is an example."
    )

    box = EmailBox(
        host='outlook.office365.com',
        port='993',
        username='liufan18279580792@outlook.com',
        password='liufan123456789'
    )

    inbox = box.inbox
    msgs = inbox.search(FROM('warn@dtuip.cn'))
    #msgs = inbox.search(unseen=False)

    # Get one message
    msg = msgs[0]
    # Get some header information
    print(msg.from_)
    print(msg.to)
    print(msg.subject)
    #print(msg.date)

    # Get text body of the email
    #print(msg.text_body)

    # Get HTML body of the email
    #print(msg.html_body)

def testSmtp():
    SERVER = "smtp.office365.com"
    FROM = "liufan18279580792@outlook.com"
    TO = ["zysyw@163.com"] # must be a list

    SUBJECT = "Hello!"
    TEXT = "This is a test of emailing through smtp of example.com."

    # Prepare actual message
    message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

    %s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    # Send the mail
    import smtplib
    server = smtplib.SMTP(SERVER)
    server.login("liufan18279580792", "liufan123456789")
    server.sendmail(FROM, TO, message)
    server.quit()

def testSmtp3():
    import smtplib, ssl

    smtp_server = "outlook.office365.com"
    port = 993  # For starttls
    sender_email = "liufan18279580792@outlook.com"
    password = "liufan123456789"#input("Type your password and press enter: ")
    receiver_email = "zysyw1970@gmail.com"
    message = """\
    Subject: Hi there

    This message is sent from Python."""

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

def sendEmail():
    import smtplib, ssl
    from email.message import EmailMessage

    smtp_server = "smtp-mail.outlook.com"
    port = 587  # For starttls
    sender_email = "liufan18279580792@outlook.com"
    password = "liufan123456789"#input("Type your password and press enter: ")
    receiver_email = "zysyw1970@gmail.com"
    message = """\
    Subject: Hi there

    This message is sent from Python."""
    msg = EmailMessage()
    msg.set_content("This message is sent from Python.")
    msg['Subject'] = "Hi there"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        server.send_message(msg,sender_email, receiver_email)
        # TODO: Send email here
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()  # TODO: Send email here
def recieveEmail():
    import imaplib
    import pprint

    imap_server = "outlook.office365.com"
    mailbox_user = "liufan18279580792@outlook.com"
    mailbox_password = "liufan123456789"

    # connect to host using SSL
    imap = imaplib.IMAP4_SSL(imap_server)

    ## login to server
    imap.login(mailbox_user, mailbox_password)

    imap.select('Inbox')

    tmp, data = imap.search(None, 'ALL')
    for num in data[0].split():
        tmp, data = imap.fetch(num, '(RFC822)')
        print('Message: {0}\n'.format(num))
        pprint.pprint(data[0][1])
        break
    imap.close()

def download_TC_Email_EmbededFile():
    import win32com.client
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)
    # for sub folder, add <.folder("your folder name")>
    inbox = outlook.GetDefaultFolder(6).folders("屋顶光伏电站")
    # Access to the email in the inbox
    messages = inbox.Items
    # get the first email
    message = messages.GetFirst()
    # get the last email
    #message = messages.GetLast()
    # to loop thru the email in the inbox 
    while True:
        try:
            print(message.subject) # get the subject of the email
            downloadEmbededFile(message)
            #downloadAttachment(message)
            # if you use messages.GetFirst() earlier
            message = messages.GetNext() 
            # if you use messages.GetPrevious() earlier 
            #message = messages.GetPrevious()
        except:
            # if you use messages.GetFirst() earlier
            message = messages.GetNext() 
            # if you use messages.GetPrevious() earlier 
            #message = messages.GetPrevious()

def downloadAttachment(message):
    from  pathlib import Path 
    #Let's assume we want to save the email attachment to the below directory
    #outputDir = r"C:\attachment"
    try:
        try:
            s = message.sender
            for attachment in message.Attachments:
                attachment.SaveASFile(Path.cwd() / attachment.FileName)
                print(f"attachment {attachment.FileName} from {s} saved")
        except Exception as e:
            print("error when saving the attachment:" + str(e))
    except Exception as e:
        print("error when processing emails messages:" + str(e))

def downloadEmbededFile(message):
    from pathlib import Path
    from bs4 import BeautifulSoup
    import urllib.request
    import ssl
    import re

    ssl._create_default_https_context = ssl._create_unverified_context #取消全局证书验证

    soup = BeautifulSoup(message.HTMLBody, "html.parser")
    for link in soup.findAll('a', attrs={'href': re.compile("\.xlsx$")}):
        try:
            url=link.get('href')
            urllib.request.urlretrieve(url, Path.cwd() / "temp.xlsx")
        except Exception as e:
            print("error when saving the embeded file:" + str(e))

#sendEmail()
#recieveEmail()
download_TC_Email_EmbededFile()