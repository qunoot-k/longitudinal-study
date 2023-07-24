import email.utils
import sys
from urllib.parse import urlsplit

for l in sys.stdin:
 try:
  uri, dateTime = l.split('\t', 1)
  epoch = email.utils.parsedate_to_datetime(dateTime).timestamp()
  parts = urlsplit(uri)
  print(uri, len(uri), len(parts.netloc), len(parts.path), len(parts.query), epoch, sep='\t')
 except Exception as e:
  print(uri,e,sep='\t')
