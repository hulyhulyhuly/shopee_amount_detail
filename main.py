''' Handle Shopee Amount Detail '''
from datetime import date

import pandas as pd

from utils import amount_detail, orders_detail

amount_df, amount_num_arr = amount_detail.get_amount_detail_df()

orders_df = orders_detail.get_orders_df(amount_num_arr)

final_df = pd.concat([amount_df, orders_df], axis=1, join='inner')

final_df.to_excel(f'入賬明細_蝦皮_{date.today()}.xlsx', index=None)
