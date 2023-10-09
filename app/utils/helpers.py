import datetime
from masonite.environment import env
from urllib.parse import urlparse
from country_list import countries_for_language

def get_country_list():
	return countries_for_language('en') 

def get_year_range(start_year=1900, end_year=None):
	year_list = list()
	today = datetime.date.today()
	start_from = start_year
	end_at = end_year or today.year+1
	for year in range(start_from, end_at):
		year_list.append(year)

	year_list.sort(reverse=True)

	return year_list

def format_duration(duration):
    d = str(round(int(duration), 1))
    durationMinute = round(float(d), 0)
    result = str(datetime.timedelta(seconds=durationMinute))
    return result

def format_filesize(size_bytes):
    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']

    index = 0
    while size_bytes >= 1024 and index < len(units) - 1:
        size_bytes /= 1024
        index += 1
    return f"{size_bytes:.2f} {units[index]}"

def format_bitrate(bitrate):
    if bitrate < 512:
        return int(round(bitrate)) + "Bps"
    else:
        return int(round(bitrate / 1000)) + "Bps"
    
def get_file_url(file_path):
    app_url = env("PUBLIC_URL")
    return app_url + "/" + file_path
	
def get_rel_path(url):
    parsed_url = urlparse(url)
    return parsed_url.path
