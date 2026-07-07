import MySQLdb
import urllib2
import requests
import boto
import redis

def connect_db():
    db = MySQLdb.connect("localhost", "user", "pass")
    return db

def fetch_api(url):
    response = urllib2.urlopen(url)
    return response.read()

def upload_s3(data):
    conn = boto.connect_s3()
    return conn