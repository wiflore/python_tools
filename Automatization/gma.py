import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
(type(conn))
((conn))
conn.starttls()
conn.login('williamflorezmaestre@gmail.com', 'toshi2014.')

conn.sendmail('williamflorezmaestre@gmail.com', 'williamflorezmaestre@gmail.com', 'Subject: Solong...\n\nTest, \nbbdddbb bbbf f  fff.\n\n Sincerely, will')

conn.quit()