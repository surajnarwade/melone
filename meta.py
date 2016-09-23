#!/usr/bin/python
# -*- coding: utf-8 -*-
import melone

# initialize class
pomodori = melone.pomodori('http://cherry.prezzemolo.ga/')

# retrive globalip
try:
    meta = pomodori.serverMeta()
except melone.error.HTTPError as e:
    print("HTTPError: %d %s" % (e.code, e.reason))
    exit(1)
except melone.error.URLError as e:
    print("URLError: %s" % (e.reason))
    exit(1)
except melone.error.JSONDecodeError as e:
    print("JSONDecodeError: %s" % (e.msg))
    exit(1)

# show result
print("Server Version: %s" % (meta['version']))