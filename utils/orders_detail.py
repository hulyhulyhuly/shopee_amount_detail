''' Shopee All Orders Detail'''
import pandas as pd
import numpy as np

def get_orders_df(amount_num_arr):
    ORDERS_PATH = r'PATH'

    orders_df = pd.read_excel(ORDERS_PATH)
    orders_header = orders_df.columns

    ORDERS_TARGET_COLUMNS = [
        orders_header[0],  # 訂單編號
        orders_header[1],  # 訂單狀態
        orders_header[15],  # 賣場優惠券
        orders_header[7],  # 買家支付運費
        orders_header[10],  # 買家總支付金額
        orders_header[12],  # 🦐幣折抵
        orders_header[13],  # 銀行信用卡活動折抵
        orders_header[17],  # 優惠券
        orders_header[31],  # 蝦皮促銷組合折扣:促銷組合標籤
    ]

    # Choose columns what we WANT
    orders_df = orders_df[ORDERS_TARGET_COLUMNS]

    # Filter Condition
    ORD_STAT_VALID = orders_df['訂單狀態'] != '不成立'
    ORD_STAT_PAID = orders_df['訂單狀態'] != '尚未付款'

    orders_df = orders_df[ORD_STAT_VALID & ORD_STAT_PAID].drop('訂單狀態', axis=1)

    orders_df['買家總支付金額_總和'] = orders_df['買家總支付金額'] + orders_df['蝦幣折抵'] + orders_df['銀行信用卡活動折抵'] + orders_df['優惠券']

    orders_df = orders_df[orders_df['訂單編號'].apply(lambda n: n in amount_num_arr)].reset_index(drop=True)

    orders_df = orders_df.reindex(columns=['訂單編號', '賣場優惠券', '買家支付運費', '買家總支付金額_總和', '蝦皮促銷組合折扣:促銷組合標籤']).reset_index(drop=True)

    orders_df.loc[orders_df.duplicated('訂單編號'), ['訂單編號', '賣場優惠券', '買家支付運費', '買家總支付金額_總和', '蝦皮促銷組合折扣:促銷組合標籤']] = np.NaN

    orders_df = orders_df.drop('訂單編號', axis=1)

    return orders_df
