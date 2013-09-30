#!/usr/bin/python
# coding=utf-8

HOST = '0.0.0.0'
DEBUG_HOST = '127.0.0.1'
PORT = 80
DEBUG_PORT = 5000

if __name__ == '__main__':
    import sys, main
    if sys.argv[1] == '-debug':
        main.app.run(port=DEBUG_PORT, debug=True, host=DEBUG_HOST)
    else:
        main.app.run(port=PORT, debug=False, host=HOST)
