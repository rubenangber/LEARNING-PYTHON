import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configura las credenciales y el servidor SMTP de Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # Puerto TLS de Gmail
smtp_user = 'tu_correo@gmail.com'
smtp_password = 'tu_contraseña_o_contraseña_de_aplicación'

# Crea el objeto SMTP
smtp = smtplib.SMTP(smtp_server, smtp_port)
smtp.starttls()  # Habilita TLS

# Inicia sesión en tu cuenta de Gmail
smtp.login(smtp_user, smtp_password)

# Crea el mensaje
subject = 'Asunto del correo'
from_email = 'tu_correo@gmail.com'
to_email = 'destinatario@gmail.com'
message = 'Contenido del correo'

msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# Envía el correo
smtp.sendmail(from_email, to_email, msg.as_string())

# Cierra la conexión SMTP
smtp.quit()