#!/usr/bin/python
#based on https://gist.github.com/gwenshap/11390102
import time
import datetime
import random
timestr = time.strftime("%Y%m%d-%H%M%S")

f = open('/tmp/access_log','a+')

ips=["200.203.11.41","200.210.110.1","200.202.109.11","189.172.16.244","189.176.53.134","127.0.0.1","200.182.1.223","144.157.45.12","81.73.150.239","237.43.24.118"]
referers=["-","http://www.testsite.com","http://dummydata.com/partners","http://foo.net","http://helloworld.com"]
resources=["/elasticsearch","/kibana","/logstash","/interdevops","/test","/","/hello","/world","/foo","/bar","/registration","/myaccount?id="]
useragents=["Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36","Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1","Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25","Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201","Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0","Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))"]
methods=["GET","POST"]
statuses=["200","404","400","403","500"]

otime = datetime.datetime.now();
itime = otime
itime -= datetime.timedelta(seconds=500)

while itime <= otime:
	increment = datetime.timedelta(seconds=random.randint(0,1))
	itime += increment
	uri = random.choice(resources)
	if uri.find("myaccount")>0:
		uri += `random.randint(1000,1500)`
	ip = random.choice(ips)
	useragent = random.choice(useragents)
	referer = random.choice(referers)
	method = random.choice(methods)
        status = random.choice(statuses)
	f.write('%s - - [%s] "%s %s HTTP/1.1" %s %s "%s" "%s"\n' % (random.choice(ips),itime.strftime('%d/%b/%Y:%H:%M:%S -0300'),method,uri,status,random.randint(2000,5000),referer,useragent))
