from sys import stdout
from datetime import date


def instructions():
    TODAY = date.today()

    stdout.write('【蝦皮入賬明細工具】\n')
    stdout.write('『使用承諾』\n')
    stdout.write(f'請將今日下載的「網購訂單出貨明細.xlsx」重新命名為「網購訂單出貨明細_{TODAY}.xlsx」\n')
    stdout.write(r'「明細報表」默認資料夾在：N:\EComm\LENA-EC各平台交接\每日蝦皮明細報表' + '\n')
    stdout.write(r'「訂單報表」默認資料夾在：N:\EComm\LENA-EC各平台交接\每日蝦皮訂單報表' + '\n')
    stdout.write(r'處理完的「入賬明細」默認資料夾在：N:\EComm\LENA-EC各平台交接\每日蝦皮入帳明細' + '\n')
    stdout.write('----------\n')
    stdout.write(f'你需要先選擇「明細報表」，例如：「網購訂單出貨明細_{TODAY}.xlsx」\n')
    stdout.write('再來選擇「訂單報表」，例如：「Order.all.20221009_20221108.xlsx」\n')
    input('按下 ENTER鍵 繼續')
    stdout.flush()
