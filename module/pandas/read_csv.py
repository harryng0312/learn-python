import pandas as pd
import numpy as np
from module.util.logger_conf import logger
from module.conf import PROJECT_DIR
from datetime import datetime as dt


DATA_FILE = "".join([PROJECT_DIR, "/data/csv/FACT_InternetSales.csv"])


def load_csv() -> pd.DataFrame:
    frm_data = pd.read_csv(filepath_or_buffer=DATA_FILE)
    return frm_data


def select_data(data_frm: pd.DataFrame) -> None:
    data_frm['OrderDateKey'] = pd.to_datetime(arg=data_frm['OrderDateKey'], format=r"%Y%m%d")
    data_frm['DueDateKey'] = pd.to_datetime(arg=data_frm['DueDateKey'], format=r"%Y%m%d")
    data_frm['ShipDateKey'] = pd.to_datetime(arg=data_frm['ShipDateKey'], format=r"%Y%m%d")
    date_comp: dt = dt.strptime("2022/06/01", r"%Y/%m/%d")
    data_frm.query("ProductKey > 600 & OrderDateKey >= @date_comp", inplace=True)
    data_frm.sort_values(by=["ProductKey", "OrderDateKey"], ascending=[True, False], inplace=True)
    logger.info(f"\n{data_frm}")
    # filter_result: pd.DataFrame = data_frm[(data_frm['ProductKey'] > 600) & (data_frm['OrderDateKey'] > dt.strptime("2022/06/01", r"%Y/%m/%d"))]
    # filter_result.sort_values("ProductKey", ascending=True, inplace=True)
    # logger.info(f"{type(filter_result)}")
    # logger.info(f"\n{filter_result}")
    return


if __name__ == "__main__":
    # show_dataframe()
    # show_dataseries()
    frm_data = load_csv()
    select_data(frm_data)
    pass
