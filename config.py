#!/usr/bin/env python
# -*- coding: utf-8 -*-

#bigmap_contact="pdorange@mac.com"
bigmap_contact="cyrille@giquello.fr"

# default value (if no parameters), default location is Cognac, France (where i live)
default_loc0=(45.69424,-0.33369)		# (latitude, longitude)
default_loc1=default_loc0
default_zoom=17
default_server="mapnik"
default_tile_size=256

test_loc0=(49.42313,0.23366)
test_loc1=test_loc0

# I add a sleep() each n tiles
max_tiles=100000
sleep_n_tiles=50

# constants
k_multi_thread=False
k_chrono=True
k_cache_folder="cache"
k_cache_delay=24.0*3600.0		#cache age : 24h (in seconds)
k_cache_max_size=500*1024*1024	#cache max size : 500 MB

