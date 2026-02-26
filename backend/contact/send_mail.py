import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    from_email = "23ik069si@esisalama.org"
    password = "gdzd rrou srdw fbpn"

    # Créer le message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attacher le corps du message
    msg.attach(MIMEText(body, 'plain'))

    server = None
    try:
        # Connexion au serveur SMTP
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(from_email, password)
        server.send_message(msg)
        print("Email envoyé avec succès à", to_email)
    except Exception as e:
        print("Échec de l'envoi de l'email. Erreur:", str(e))
    finally:
        if server:
            server.quit()
