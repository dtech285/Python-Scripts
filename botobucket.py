#!/usr/bin/env python3

import boto
s3 = boto.connect_s3('AKIAJMIXQITCRZAWVPKA', 'Lk2HvTJX6uDLAmSYvrHotapQ7/onkZ47f60uAjTf')
bucket = s3.create_bucket('285testbucket')
key = bucket.new_key('examples/first_file.csv')
key.set_contents_from_filename('c:/users/david/first_file.csv')
key.set_acl('public-read')

