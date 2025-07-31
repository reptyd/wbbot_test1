import os
import time
import logging
import requests
import pandas as pd

WB_TOKEN = os.getenv("WB_TOKEN")

URL = "https://advert-api.wildberries.ru/adv/v1/promotion/count"
HEADERS = {"Authorization": WB_TOKEN}

logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(levelname)s  %(message)s", datefmt="%H:%M:%S")

def fetch_promotion_count():
    logging.info("Запрос к WB…")
    r = requests.get(URL, headers=HEADERS, timeout=30)
    r.raise_for_status()
    data = r.json()
    logging.info("Ответ WB: %s", data)
    return data

def save_to_xlsx(data, out_path="wb_promotion_count.xlsx"):
    pd.DataFrame([data]).to_excel(out_path, index=False)
    logging.info("Сохранено: %s", out_path)

def main():
    start = time.perf_counter()
    if not WB_TOKEN:
        logging.error("Не задан WB_TOKEN")
        return
    data = fetch_promotion_count()
    save_to_xlsx(data)
    logging.info("Готово за %.2f сек.", time.perf_counter() - start)

if __name__ == "__main__":
    main()
