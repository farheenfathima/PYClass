import re

f = open("log1.log")

regex = r"(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}) port (?P<port>\d{2,4})"

while True:
	s = f.readline()
	if not s:
		break

	result = regexp.search(s)
	if result:
		ip = result.group("ip")
		print(ip)