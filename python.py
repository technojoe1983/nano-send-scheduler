'''Program to schedule regular nano transactions,  decentralized Patreon'''
import datetime
import json
#from nano.rpc import Client

#rpc = Client('http://localhost:7076')
#rpc.version()


class NanoSchedule:
    def __init__(self, scheduleName, recipientAddress,  nanoAmount, startDate, timeInterval,
             sendCount):
        self.scheduleName = {'scheduleName': scheduleName}
        self.recipientAddress = {'recipientAddress': recipientAddress}
        self.nanoAmount = {'nanoAmount': nanoAmount}
        self.startDate = {'startDate': startDate}
        self.timeInterval = {'timeInterval': timeInterval}
        self.sendCount = {'sendCount': sendCount}

    @staticmethod
    def newSchedule(self):
        '''build json file'''
        with open('schedule.json', 'w') as fw:
            json.dumps(self, fw.write, indent=2)


class WalletConfig:
    def __init__(self, publicAddress, privateKey, walletAddress):
        self.publicAddress = publicAddress
        self.privateKey = privateKey
        self.walletAddress = walletAddress


def showCurrentSchedules(jsonFile):
    '''read json file'''
    
    with open('schedule.json', 'r') as fr:
        data = fr.read()
        for schedule in data:
            print(schedule)


def deleteSchedule(scheduleName):
    '''find schedule in json and remove'''


def scheduleReady(scheduleName):
    '''read json and compare current time to schedule to see if any new transactions
are ready to be sent'''

    today = datetime.date.today()
    timeDelta = datetime.timedelta(1,0,0,0)
    diffTime = today - datetime.date(2018, 1, 21)
    intervalsSinceStart = diffTime/timeDelta

    print(today)
    print(timeDelta)
    print(diffTime)
    print(intervalsSinceStart)

def sendTransactiom(scheduleName):
    '''Send RPC call with data for send'''
    print ("sending")
