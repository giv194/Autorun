import urllib2, urllib, json
import calendar
baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = "select * from weather.forecast where woeid=2427936"
yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
result = urllib2.urlopen(yql_url).read()
data = json.loads(result)
for day in data['query']['results']['channel']['item']['forecast']:
	date = day['date'].split(' ');

	first_line = str(list(calendar.month_abbr).index(date[1])) + "/" + date[0]
	for i in range(len(first_line), 12):
		first_line += " "
	first_line = first_line + "H:" + day['high'] + "'"

	second_line = ""
	if "Partly Cloudy" != day['text'] and "Sunny" != day['text']:
		if int(day['low']) < 32:
			second_line = "Snowy"
		else:
			second_line = "Rainy"
	for i in range(len(second_line), 12):
		second_line += " "	
	second_line = second_line + "L:" + day['low'] + "'"
	print first_line
	print second_line