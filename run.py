#!/usr/bin/python
# coding=utf-8

if __name__ == '__main__':
    import sys, main
    from config import DEBUG_PORT, DEBUG_HOST, HOST, PORT
    if '-debug' in sys.argv:
        main.app.config['SERVER_NAME'] = None
        main.app.run(port=DEBUG_PORT, debug=True, host=DEBUG_HOST)
    else:
        main.app.run(port=PORT, debug=False, host=HOST)
