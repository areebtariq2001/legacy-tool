import sys
def log(message):
    print >> sys.stderr, "LOG:", message

log("Application started")
log("Processing data")
