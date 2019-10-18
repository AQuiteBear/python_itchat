# coding=utf8
import itchat
from itchat.content import *
from getResponse import get_response
from getParams import get_params

config = get_params()
userDic = {}

msgTypeDic = {'1': '文字信息',
              '3': '图片信息',
              '34': '语音信息',
              '43': '视屏信息',
              '47': '表情包图片',
              "49": "文件",
              '10000': '红包',
              '10002': '撤回信息'}

# 暂未开通
if config['receiveGroup'] == 1:
    # 回复群聊
    @itchat.msg_register([TEXT, PICTURE, MAP, CARD, NOTE, SHARING, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
    def reply_GroupChat(msg):
        '''
        MsgType 1:文字，系统自带表情，位置
                2：
                3：图片
                34：语音
                43：视屏
                47：表情包图片
                10000：红包
                10002：撤回信息提示
        :param msg:
        :return:
        '''
        # 判断是否需要保存群组信息
        if config['saveGroup'] == 1:
            print('应该保存信息')
        # 判断是否需要回应群组信息
        if config['replayGroup'] == 1:
            print("应该回复信息")
        # # 图片
        # if msg['MsgType'] == 3:
        #     print('接收到图片')
        #     msg.download(msg.fileName)
        #     sys.stdout.flush()
        #     # with open(msg.fileName, 'wb') as f:
        #     #     f.write(msg.download(msg.fileName))
        #
        # # 文字，系统自带表情
        # elif msg['MsgType'] == 1:
        #     print(msg['Text'])
        #     # print('FromUserName', msg['FromUserName'])
        #     # print('ActualNickName', msg['ActualNickName'])
        #     # print('Text', msg['Text'])
        #     # print('content', msg['Content'])

        return 0

if config['receivePerson'] == 1:
    # 回复个人
    @itchat.msg_register([TEXT, PICTURE, MAP, CARD, NOTE, SHARING, RECORDING, ATTACHMENT, VIDEO])
    def reply_person(msg):
        '''
           MsgType 1:文字，系统自带表情，位置
                   2：
                   3：图片
                   34：语音
                   43：视屏
                   47：表情包图片
                   49: 文件
                   10000：红包
                   10002：撤回信息提示
       '''

        print("收到来自{}的{}：{}".format(userDic[msg['FromUserName']],
                                    msgTypeDic[str(msg['MsgType'])], msg['Text']))
        if config['replayPerson'] == 1 or userDic[msg['FromUserName']] in config['replayPerson']:
            defaultReply = get_response(msg['Text'])
            itchat.send_msg(defaultReply, msg['FromUserName'])

if __name__ == '__main__':
    itchat.auto_login(hotReload=True)  # 热启动，不需要多次扫码登录
    myUserName = itchat.get_friends(update=True)
    print("您共有{}位微信好友".format(len(myUserName)))
    for temp in myUserName:
        userDic[temp['UserName']] = temp['NickName']
    itchat.run()
