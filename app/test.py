
import os


basedir = os.path.abspath(os.path.dirname(__file__))  # 获取当前文件所在目录


UPLOAD_FOLDER = basedir + '/static/file/img'
print(UPLOAD_FOLDER)