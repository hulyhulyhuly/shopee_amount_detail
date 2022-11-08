''' Merge DataFrame '''
from sys import stdout, exit
from time import sleep
from datetime import date

import tkinter as tk
from tkinter import filedialog
import numpy as np

from utils.amount_detail import get_amount_detail_df
from utils.orders_detail import get_orders_df
from utils.check import check_path, check_amount_file_name


def handle_df():
    root = tk.Tk()
    root.withdraw()

    AMOUNT_FILE_PATH = filedialog.askopenfilename(initialdir=r'N:\EComm\LENA-EC各平台交接\每日蝦皮明細報表', title='請選擇明細報表')
    check_amount_file_name(AMOUNT_FILE_PATH)

    ORDERS_FILE_PATH = filedialog.askopenfilename(initialdir=r'N:\EComm\LENA-EC各平台交接\每日蝦皮訂單報表', title='請選擇訂單報表')
    check_path(ORDERS_FILE_PATH, '訂單報表')

    amount_df, amount_num_arr = get_amount_detail_df(AMOUNT_FILE_PATH)

    orders_df = get_orders_df(ORDERS_FILE_PATH, amount_num_arr)

    full_df = amount_df.merge(orders_df, on="訂單編號")

    full_df.loc[full_df.duplicated('訂單編號'), ['訂單編號', '賣場優惠券', '買家支付運費', '買家總支付金額_總和', '蝦皮促銷組合折扣:促銷組合標籤']] = np.NaN

    FULL_DETAIL_FILE_PATH = r'N:\EComm\LENA-EC各平台交接\每日蝦皮入帳明細\入賬明細_蝦皮_{0}.xlsx'.format(date.today())

    full_df.to_excel(FULL_DETAIL_FILE_PATH, index=None)

    stdout.write('Merge Complete!\n')
    stdout.write(f'入賬明細在：{FULL_DETAIL_FILE_PATH}\n')
    stdout.write('3秒後，將自動關閉')
    stdout.flush()
    sleep(5)
    exit()
