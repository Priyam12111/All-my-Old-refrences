import win32print

def var_print():
    print('Press Ctrl-C to quit.')
    try:
        while True:
            ##Define the terms here, not after the function
            con = win32print.OpenPrinter("Canon G2000 series Printer")
            x = win32print.EnumJobs(con,0,1)[0]["PagesPrinted"]
            positionStr = 'X: ' + str(x).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
            con.close()
    except KeyboardInterrupt:
        print('\n')
        
var_print()