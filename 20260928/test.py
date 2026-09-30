from util import util_time
from member import config as member_config
import os
import json
import session

class Memberservice:
    def __init__(self):
        self.members = {}
        self.init_database()

        def sign_up(self):

            mld = input('input your new ID:')

            if mld in self.members:
                print('이미 사용중인 ID입니다.')
                return
            
            mPw = input('input new member PW')
            mMail = input('input new member mMail')
            mPhone = input('input new member mPhone')

            newMember = {
                'mld': mld,
                'mPw': mPw,
                'mMail': mMail, 
                'mPhone': mPhone,
                'mRegDate' : util_time.getCurrentDateTime(),
            }

