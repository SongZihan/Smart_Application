from flask import jsonify, make_response


def return_JSON(code,msg,data={}):
    """
        返回信息 "code":200（正常）或401（登录失败）或400（未获授权）或402（token过期）或501（内部错误）
    """
    return jsonify({"code":code,"msg":msg,"data":data})

def return_jpeg(jpeg_file):
    response = make_response(jpeg_file)
    response.headers['Content-Type'] = 'image/jpeg'
    return response

