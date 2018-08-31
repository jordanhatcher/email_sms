"""
sms_email

Contains the SMSNode class
"""

import logging
import smtplib
from pubsub import pub
from ....node import Node

LOGGER = logging.getLogger(__name__)

NODE_CLASS_NAME = 'SMSNode'

class SMSNode(Node):
    """
    SMSNode

    Provides an interface to send text messages by sending
    emails to an SMS gateway
    """

    def __init__(self, label, state, config=None):
        """
        Constuctor
        """

        Node.__init__(self, label, state, config)

        try:
            self.username = config['username']
            self.password = config['password']
            self.recipient_sms_gateway_map = config['recipient_sms_gateway_map']
        except KeyError as e:
            LOGGER.error('Missing key from email SMS node config')
            LOGGER.exception(e)

        pub.subscribe(self.send, f'{self.label}.send')

    def send(self, msg):
        """
        Handler for sending SMS messages
        """

        recipient = msg['recipient']
        message = msg['message']
        recipient_email = self.recipient_sms_gateway_map[recipient]

        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(self.username, self.password)
            server.sendmail(self.username, recipient_email, message)
            server.quit()
        except Exception as exception:
            LOGGER.error('Error sending SMS')
            LOGGER.exception(exception)
