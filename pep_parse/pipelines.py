import datetime as dt
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_sum = {}

    def process_item(self, item, spider):
        status = item['status']
        self.status_sum[status] = self.status_sum.get(status, 0) + 1
        return item

    def close_spider(self, spider):
        total = 0
        now = dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = BASE_DIR / 'results' / f'status_summary_{now}.csv'
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for key, value in self.status_sum.items():
                f.write(f'{key}, {value}\n')
                total += int(value)
            f.write(f'Total,{total}\n')
