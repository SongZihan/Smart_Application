from datetime import datetime


def getCurrentTime(frm="%Y-%m-%d %H:%M:%S"):
    dt = datetime.now()
    return dt.strftime(frm)
