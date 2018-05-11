#!/bin/python

import smtplib

#envio de emial GMAIL em python.

smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)

smtp.login('beltrano@gmail.com', 'passwd')

de = 'beltrano@gmail.com'
para = ['fulano@gmail.com']
msg = """From: %s
To: %s
Subject: Enviando Email Python

Email de teste VIA PYTHON.""" % (de, ', '.join(para))

smtp.sendmail(de, para, msg)

smtp.quit()
