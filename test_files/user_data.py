import urllib2
import cPickle

def fetch(url):
    response = urllib2.urlopen(url)
    return response.read()

def save(data, f):
    cPickle.dump(data, open(f, "w"))

users = {"a": 1, "b": 2}
for k in users.iterkeys():
    print k
