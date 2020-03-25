from __future__ import print_function
import pickle
import os.path
import rsa
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
import os
from apiclient import errors
import math
import random 
import email_otp
import txn_1
from PyQt5 import QtCore, QtGui, QtWidgets

nid_db = {'2':{'email' : 'nikhilmuralidharan98@gmail.com' , 'wallet':'0x667'}, '12345':{'email':'sanmeeraj@gmail.com','wallet':'0x62a3F16Aed1B029A76768b262E9ED1c2A2952FC0'}}


class Ui_MainWindow(object):
    
    def __init__(self):
        self.otp = ''
        self.public_key = ''
        self.private_key = ''
        self.wallet_id = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.NID = QtWidgets.QLabel(self.centralwidget)
        self.NID.setGeometry(QtCore.QRect(80, 150, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NID.setFont(font)
        self.NID.setObjectName("NID")

        self.nid_ip = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.nid_ip.setGeometry(QtCore.QRect(260, 160, 241, 31))
        self.nid_ip.setObjectName("nid_ip")

        self.email_ip = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.email_ip.setGeometry(QtCore.QRect(260, 210, 241, 31))
        self.email_ip.setObjectName("email_ip")

        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(180, 60, 431, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(20)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")

        self.email_label = QtWidgets.QLabel(self.centralwidget)
        self.email_label.setGeometry(QtCore.QRect(30, 200, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.email_label.setFont(font)
        self.email_label.setObjectName("email_label")

        self.otp_button = QtWidgets.QPushButton(self.centralwidget)
        self.otp_button.setGeometry(QtCore.QRect(540, 190, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.otp_button.setFont(font)
        self.otp_button.setObjectName("otp_button")

        self.otp_label = QtWidgets.QLabel(self.centralwidget)
        self.otp_label.setGeometry(QtCore.QRect(60, 310, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.otp_label.setFont(font)
        self.otp_label.setObjectName("otp_label")

        self.verify_ip = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.verify_ip.setGeometry(QtCore.QRect(260, 310, 241, 31))
        self.verify_ip.setObjectName("verify_ip")

        self.verify_button = QtWidgets.QPushButton(self.centralwidget)
        self.verify_button.setGeometry(QtCore.QRect(540, 280, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.verify_button.setFont(font)
        self.verify_button.setObjectName("verify_button")

        self.res_label = QtWidgets.QLabel(self.centralwidget)
        self.res_label.setGeometry(QtCore.QRect(300, 440, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.res_label.setFont(font)
        self.res_label.setObjectName("res_label")

        self.wallet_label = QtWidgets.QLabel(self.centralwidget)
        self.wallet_label.setGeometry(QtCore.QRect(100, 260, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wallet_label.setFont(font)
        self.wallet_label.setObjectName("wallet_label")

        self.wallet_id_ip = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.wallet_id_ip.setGeometry(QtCore.QRect(260, 260, 241, 31))
        self.wallet_id_ip.setObjectName("wallet_id_ip")

        self.public_key_label = QtWidgets.QLabel(self.centralwidget)
        self.public_key_label.setGeometry(QtCore.QRect(60, 360, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.public_key_label.setFont(font)
        self.public_key_label.setObjectName("public_key_label")

        self.public_key_op = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.public_key_op.setGeometry(QtCore.QRect(260, 360, 241, 31))
        self.public_key_op.setObjectName("public_key_op")

        self.generate_button = QtWidgets.QPushButton(self.centralwidget)
        self.generate_button.setGeometry(QtCore.QRect(540, 360, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.generate_button.setFont(font)
        self.generate_button.setObjectName("generate_button")

        self.private_key_label = QtWidgets.QLabel(self.centralwidget)
        self.private_key_label.setGeometry(QtCore.QRect(60, 410, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.private_key_label.setFont(font)
        self.private_key_label.setObjectName("private_key_label")

        self.private_key_op = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.private_key_op.setGeometry(QtCore.QRect(260, 410, 241, 31))
        self.private_key_op.setObjectName("private_key_op")

        self.publish_button = QtWidgets.QPushButton(self.centralwidget)
        self.publish_button.setGeometry(QtCore.QRect(540, 410, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.publish_button.setFont(font)
        self.publish_button.setObjectName("publish_button")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #clicks
        self.verify_button.clicked.connect(self.clicked_register)
        self.otp_button.clicked.connect(self.clicked_generate_otp)
        self.generate_button.clicked.connect(self.clicked_generate_pk)
        self.publish_button.clicked.connect(self.clicked_publish)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_label.setText(_translate("MainWindow", "Certificate Registration Tool"))
        self.email_label.setText(_translate("MainWindow", "Enter E-mail ID To Verify:"))
        self.otp_button.setText(_translate("MainWindow", "GENERATE OTP"))
        self.otp_label.setText(_translate("MainWindow", "Enter Received OTP : "))
        self.verify_button.setText(_translate("MainWindow", "REGISTER"))
        self.res_label.setText(_translate("MainWindow", "waiting for user input"))
        self.NID.setText(_translate("MainWindow", "Enter NID Number : "))
        self.wallet_label.setText(_translate("MainWindow", "Enter Wallet ID : "))
        self.public_key_label.setText(_translate("MainWindow","Generated Public Key : "))
        self.private_key_label.setText(_translate("MainWindow","Generated Private Key : "))
        self.generate_button.setText(_translate("MainWindow","GENERATE PUBLIC PRIVATE KEY"))
        self.publish_button.setText(_translate("MainWindow","PUBLISH PUBLIC KEY"))

    def clicked_generate_otp(self):
        value1 = self.nid_ip.toPlainText()
        value1 = value1.strip()
        value2 = self.email_ip.toPlainText()
        value2 = value2.strip()
        self.wallet_id = self.wallet_id_ip.toPlainText()
        self.wallet_id = self.wallet_id.strip()
        if value1 in nid_db:
            email = nid_db[value1]['email']
            walletid = nid_db[value1]['wallet']
            if email == value2 and walletid ==self.wallet_id:
                self.otp = email_otp.otp_gen()
                creds = None
                if os.path.exists('token.pickle'):
                    with open('token.pickle', 'rb') as token:
                        creds = pickle.load(token)
                # If there are no (valid) credentials available, let the user log in.
                if not creds or not creds.valid:
                    if creds and creds.expired and creds.refresh_token:
                        creds.refresh(Request())
                    else:
                        flow = InstalledAppFlow.from_client_secrets_file(
                            'credentials.json', email_otp.SCOPES)
                        creds = flow.run_local_server(port=0)
                        # Save the credentials for the next run
                    with open('token.pickle', 'wb') as token:
                        pickle.dump(creds, token)
                #print(otp)
                otp_message = 'Please Enter The One Time Password(OTP) On The Registartion Tool.\n'+'Your OTP is : '+self.otp
                service = build('gmail', 'v1', credentials=creds)
                message = email_otp.create_msg('sanmeeraj@gmail.com',email,'DPKI One Time Password (OTP)',otp_message)
                x = email_otp.send_msg(service,message)
                self.res_label.setText("OTP Sent Successfully Please Verify")   
                self.res_label.adjustSize()
            else:
                self.res_label.setText("Entered Email Or Wallet ID mismatch")   
                self.res_label.adjustSize()
        else:
            self.res_label.setText("NID not in AADHAR Database")    
            self.res_label.adjustSize()    

    def clicked_register(self):
        #print('clicked')
        #email_ip
        entered_otp = self.verify_ip.toPlainText()
        print('Entered OTP: ',entered_otp)
        print('otp_gen: ',self.otp)
        if entered_otp == self.otp and self.otp:
            value = txn_1.check_whether_address_is_approved(self.wallet_id)
            print(value)
            if value:
                self.res_label.setText("Wallet ID already registered")
                self.res_label.adjustSize()
            else:
                txn_1.approve_publisher(self.wallet_id)
                self.res_label.setText("Wallet ID registeration complete")
                self.res_label.adjustSize()
        else:
            self.res_label.setText("OTP Incorrect")
            self.res_label.adjustSize()
        #self.label.adjustSize()    
    
    def clicked_generate_pk(self):
        (self.public_key, self.private_key) = rsa.newkeys(1024)
        self.res_label.setText("Public and Private key pair generated")
        self.res_label.adjustSize()
        #print("Public Key : ",self.public_key)
        self.public_key_op.setPlainText(str(self.public_key))
        #print("Private Key : ",self.private_key)
        self.private_key_op.setPlainText(str(self.private_key))

    def clicked_publish(self):
        if self.public_key:
            if txn_1.check_whether_address_is_approved(self.wallet_id):
                value = txn_1.publish_public_key(str(self.public_key),self.wallet_id)
                print(value)
                if value:
                    self.res_label.setText("Public Key published")
                    self.res_label.adjustSize()
                else:
                    self.res_label.setText("Something went wrong, wallet ID may not be approved")
                    self.res_label.adjustSize()
            else:
                self.res_label.setText("Wallet ID not approved, please complete registeration")
                self.res_label.adjustSize()
        else:
            self.res_label.setText("Please Generate Public and Private Key first")
            self.res_label.adjustSize()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())