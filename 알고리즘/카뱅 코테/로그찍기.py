import datetime

def solution(logs):
	ret = [0] * 24
	datetime_obj = datetime.datetime.strptime(logs, '%Y/%m/%d %H:%M:%S')
	datetime_obj = datetime_obj + datetime.timedelta(hours=9)
	ret[datetime_obj.hour] += 1
	return ret
	
logs = ["2019/05/01 00:59:19", "2019/05/01 00:59:19", ]

print(solution(logs))