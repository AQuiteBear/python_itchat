import requests

#涉及到青云客智能聊天机器人API，如有侵权，请联系删除
def get_response(msg):
    params = {"key": "free",
              "appid": 0,
              'msg': msg}
    api_url = 'http://api.qingyunke.com/api.php'
    replys = requests.get(api_url, params=params).json()
    return replys['content']
