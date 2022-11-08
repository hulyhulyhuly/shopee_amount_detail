''' Shopee Amount Detail '''
import pandas as pd


def get_amount_detail_df(filepath):

    amount_detail_df = pd.read_excel(filepath, '蝦皮')

    amount_detail_header = amount_detail_df.columns

    AMOUNT_DETAIL_TARGET_COLUMNS = [
        amount_detail_header[0],  # 訂單編號
        amount_detail_header[1],  # 姓名
        amount_detail_header[3],  # 訂單全部出完
        amount_detail_header[5],  # 入帳日
        amount_detail_header[9],  # SKN
        amount_detail_header[10],  # 數量
    ]

    # Choose columns what we WANT
    amount_detail_df = amount_detail_df[AMOUNT_DETAIL_TARGET_COLUMNS]

    # Filter Condition
    DATE_NULL = amount_detail_df['入帳日'].isnull()
    ORDER_END = amount_detail_df['訂單全部出完'] == 'v'

    # Filter and Drop useless Columns
    amount_detail_df = (amount_detail_df[DATE_NULL & ORDER_END].drop('訂單全部出完', axis=1).drop('入帳日', axis=1))

    amount_detail_df = amount_detail_df.fillna(method="ffill")

    # Provide Number which we need to Orders DataFrame
    amount_detail_num_arr = amount_detail_df[amount_detail_df['訂單編號'].notnull()]['訂單編號'].values

    return amount_detail_df, amount_detail_num_arr
