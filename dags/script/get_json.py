import requests
import json
from datetime import datetime

data_req = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data_json = json.loads(data_req.text)

kolom = ['disclaimer', 'chart_name', 'time_updated',
'time_updated_iso', 'bpi_usd_code', 'bpi_usd_rate_float',
'bpi_usd_description', 'bpi_gdp_code', 'bpi_gdp_rate_float',
'bpi_gdp_description', 'bpi_eur_code', 'bpi_eur_rate_float',
'bpi_eur_description']

data = []

disclaimer = data_json['disclaimer']
chart_name = data_json['chartName']
time_updated = data_json['time']['updated']
time_updated_iso = data_json['time']['updatedISO']
bpi_usd_code = data_json['bpi']['USD']['code']
bpi_usd_rate_float = data_json['bpi']['USD']['rate_float']
bpi_usd_description = data_json['bpi']['USD']['description']
bpi_gdp_code = data_json['bpi']['GBP']['code']
bpi_gdp_rate_float = data_json['bpi']['GBP']['rate_float']
bpi_gdp_description = data_json['bpi']['GBP']['description']
bpi_eur_code = data_json['bpi']['EUR']['code']
bpi_eur_rate_float = data_json['bpi']['EUR']['rate_float']
bpi_eur_description = data_json['bpi']['EUR']['description']
bpi_idr_rate_float = bpi_usd_rate_float * 15000

format_time_updated =  datetime.strptime(time_updated, "%b %d, %Y %H:%M:%S UTC")
time_updated =  format_time_updated.strftime('%Y-%m-%d %H:%M:%S')
time_updated = str(time_updated)

format_time_updated_iso =  datetime.fromisoformat(time_updated_iso)
time_updated_iso =  format_time_updated_iso.strftime('%Y-%m-%d %H:%M:%S')
time_updated_iso = str(time_updated_iso)


last_updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


data_final = ( disclaimer, chart_name, time_updated,
time_updated_iso, bpi_usd_code, bpi_usd_rate_float,
bpi_usd_description, bpi_gdp_code, bpi_gdp_rate_float,
bpi_gdp_description, bpi_eur_code, bpi_eur_rate_float,
bpi_eur_description,bpi_idr_rate_float, last_updated)


