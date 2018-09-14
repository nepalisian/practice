import httplib
from timer import Timer

with Timer() as t:
    conn = httplib.HTTPConnection('google.com')
    conn.request('GET', '/')

print('Request took %0.03f sec' % t.interval)