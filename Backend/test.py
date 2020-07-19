# def test(func):
#     def warpper(*args, **kw):
#         i = 1
#         func(i,*args, **kw)
#         print("finish")
#     return warpper
#
# @test
# def test_warpper(i):
#     print(i)
#
# if __name__ == '__main__':
#     test_warpper()

from captcha.image import ImageCaptcha
import random
import string

image = ImageCaptcha(100,40)    # 图片宽 160 高 60
characters = string.digits        #验证码组成，数字
char_num = 4 #验证码字符个数

captcha_str = ''.join(random.sample(characters, char_num))
img = image.generate_image(captcha_str)
img.save(captcha_str + '.jpg')
