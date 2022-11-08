from sys import stdout, stderr, exit
from datetime import date
from time import sleep


def check_path(path, name):
    if path == '':
        stderr.write(f"你沒有選擇「{name}」，工具將在5秒後自動退出")
        stderr.flush()
        sleep(5)
        exit()
    stdout.write(f"{name}在：{path}\n")


def check_amount_file_name(filename):
    AMOUNT_FILE_NAME = filename.split('/')[-1]
    TODAY = date.today()

    if AMOUNT_FILE_NAME != f'網購訂單出貨明細_{TODAY}.xlsx':
        stderr.write('明細報表名稱有誤\n')
        stderr.write(f'今日明細報表名稱=>網購訂單出貨明細_{TODAY}.xlsx\n')
        stderr.write('工具將在5秒後自動退出')
        stderr.flush()
        sleep(5)
        exit()

    check_path(filename, '明細報表')
