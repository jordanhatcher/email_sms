"""
sms_conditions

Contains the SMSConditions class
"""

import logging
import re
from pubsub import pub
from ....condition import Condition

LOGGER = logging.getLogger(__name__)

CONDITION_CLASS_NAME = 'SMSConditions'

class SMSConditions(Condition):
    """
    SMSConditions

    Conditions for parsing strings into SMS messages
    """

    def __init__(self, scheduler, schedule=None):
        """
        Constructor
        """

        Condition.__init__(self, scheduler, schedule=None)
        pub.subscribe(self.evaluate, 'messages.pipe_node')
        LOGGER.debug('Initialized')

    def evaluate(self, msg):
        """
        Handler to transform an incomming message to the format
        that the SMS node expects
        """

        LOGGER.info('Evaluating')
        LOGGER.debug(msg['content'])

        # "^send <mesage> to <recipient>$"
        match = re.search('^send\s(.*)\sto\s(\w+)$', msg['content'])
        if match is not None:
            message =  match.group(1)
            recipient = match.group(2)

        LOGGER.info(f'Sending SMS message to {recipient}: {message}')
        pub.sendMessage('sms_node.send', msg={
            'recipient': recipient,
            'message': message
        })
