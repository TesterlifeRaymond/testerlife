"""
# @Author: liujinjia
# @File Name:/home/ray/git/testerlife/app/apis/resource/login.py 
# @Create by:   Ray
# @Create time: 2017年3月21日 上午7:01:41  
"""

from flask_restful import reqparse, fields
from ...util.result.result import BaseResource
from ...model import db, User
from werkzeug import responder


RESULT = {
    'result': fields.String,
    'message': fields.String,
    'response': fields.Nested(fields.String)
}


class Login(BaseResource):
    """ Login apis class model """

    def __init__(self):
        """ init class model """
        super(Login, self).__init__()
        self.parse = reqparse.RequestParser()
        self.date_base = db.session
        self.parse.add_argument('username', type=str, required=True, help='请输入用户名')
        self.parse.add_argument('password', type=str, required=True, help='请输入登录密码')

    def post(self):
        """用户登录"""
        args = self.parse.parse_args()
#         user = self.date_base.query(User).filter_by(username=args.get('username')).first()
        user = args.get('username')
        if user and args.get('password') == 'qwer1234':
#         if user and user.confirm_password(args.get('password')) is True:
#             self.base_res.set_res("用户登录失败"，"failed", "")
#             return self.base_res
            self.base_res.set_res(dict(message='用户登录成功',result='success',response=''))
            return self.base_res
