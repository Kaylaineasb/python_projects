import smtplib
import email.message

def enviar_email():
    corpo_email = """
    <p>Só testando<\p>
    """
    msg= email.message.Message()
    msg['Subject']= "teste"
    msg['From']='kaylaineasb9@gmail.com'
    msg['To']='kaylaineasb9@gmail.com'
    password='tdusnrcyjzifsktf'
    msg.add_header('content-type','text/html')
    msg.set_payload(corpo_email)

    s=smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()

    s.login(msg['From'],password)
    s.sendmail(msg['From'],[msg['To']],msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()