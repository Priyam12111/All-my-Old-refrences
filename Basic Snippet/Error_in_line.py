import sys
e = 'error'
print('[Long method error - {}]: '.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)

