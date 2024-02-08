# pylint: disable=line-too-long
# flake8: noqa
"""
Python program to configure prefect Flow to extract, load and transform
data (Science and management) from Signals ELN Notebook
"""

# import aiohttp
# import asyncio
import os
from datetime import datetime
# import json
# from dotenv import load_dotenv
# import pandas as pd
from prefect import flow, task, context
# from prefect_snowflake.database import SnowflakeConnector
# from snowflake.connector.pandas_tools import write_pandas
# import requests
# from prefect.blocks.system import Secret


# load_dotenv()

DEPLOYMENT_NAME = 'testdeployment"'
# ELN_API_KEY_SECRET = os.environ["ELN_API_KEY_SECRET"]
# ELN_ENDPOINT_ORIGEN = os.environ["ELN_ENDPOINT_ORIGEN"]
# ELN_API_KEY="7Na1mSjk15yOO91YFqOgpEn5MPeMO/kfipxChgTZSnPdc7bJLLIL0ZcmjahzLqPRQBbxkw=="
# ELN_ENDPOINT_ORIGEN="https://sinapze.signalsnotebook.perkinelmercloud.eu/api/rest/v1.0/" 
# eln_api_headers = {"accept": "application/octet-stream", "x-api-key": ELN_API_KEY}

# response = requests.get(url = 'https://sinapze.signalsnotebook.perkinelmercloud.eu/api/rest/v1.0/entities/text%3A276abaac-5514-4c70-a09e-85bcd8682eab/export',
#                         headers=eln_api_headers,
#                         )
# print(response.text)

@flow(log_prints=True)
def buy():
    """ Test function """
    print(DEPLOYMENT_NAME + ' worked!')
    # ent_exp_hist_endpoint = f"{ELN_ENDPOINT_ORIGEN}entities/experiment:96382744-335d-4802-8bc4-e80960926c26/history?depth=-1&action=Changed%20Status&page%5Boffset%5D=0&page%5Blimit%5D=100"

    # response = requests.get(
    #     url=ent_exp_hist_endpoint,
    #     headers=eln_api_headers,
    #     timeout=3600,
    # )
    # print(response.status_code)

    flow_id = context.get_run_context().flow_run.id
    start_time = context.get_run_context().flow_run.start_time.strftime("%Y-%m-%d %H:%M:%S")
    print(f'flow id is {flow_id} and start_time is {start_time}')
if __name__ == "__main__":
    buy.serve(name=DEPLOYMENT_NAME)
