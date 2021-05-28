#!/usr/bin/python3
import sys, getopt, os
from USBNinjaModule import Transmitter
from USBNinjaModule import Scriptconverter

def help():
    print("┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐")
    print("│ Usage:                                                                                                           │")
    print("│    ./USBNinja.py -m <mode> [options]                                                                             │")
    print("│                                                                                                                  │")
    print("│ Modes:                                                                                                           │")
    print("│    r                                                   Remote:       Mimics the USB ninja Remote                 │")
    print("│    c                                                   Converter:    Converts ducky.txt payloads into USBNinja.c │")
    print("│                                                                                                                  │")
    print("│ Remote:                                                                                                          │")
    print("│    ./USBNinja.py -m r -d <BDADDR>                                                                                │")
    print("│                                                                                                                  │")
    print("│ Commands of Interactive mode:                                                                                    │")
    print("│    I or Info                                           Prints device info                                        │")
    print("│    A or Button A                                       Triggers payload A                                        │")
    print("│    B or Button B                                       Triggers payload B                                        │")
    print("│    Q or Quit                                           Leaves interactive mode                                   │")
    print("│                                                                                                                  │")
    print("│ Converter:                                                                                                       │")
    print("│    ./USBNinja.py -m c -i <input file> -j <input file 2> -o <output file> -l <keyboard language> -t <triggermode> │")
    print("└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘")

def main(argv):
    BTADDR = ""
    MODE   = ""
    IFILE  = ""
    OFILE  = ""
    LAMG   = ""

    try:
        opts, args = getopt.getopt(argv,"hm:i:d:o:l:s:",["help", "mode=", "device=", "ifile=", "ofile=", "language=", "scriptmode="])
    except getopt.GetoptError:
        help()
        sys.exit(2)

    for opt, arg in opts:
        if opt == ('-h', "--help"):
            help()
            sys.exit()
        elif opt in ("-d", "--device"):
           BTADDR = arg 
        elif opt in ("-m", "--mode"):
           MODE = arg
        elif opt in ("-i", "--ifile"):
           IFILE = arg 
        elif opt in ("-o", "--ofile"):
           OFILE = arg 
        elif opt in ("-l", "--language"):
           LAMG = arg
        elif opt in ("-s", "--scriptmode"):
           LAMG = arg
        else:
            help()
            sys.exit()           

    if(MODE.lower() == 'r' and BTADDR != '' and len(str(BTADDR)) == 17):
        TX = Transmitter.TX(BTADDR)

        if(TX.Initialconnection() != False):
            inputstring = ""
            Conection = True
            while(Conection == True):
                print("\033[94m[" + BTADDR + "]\033[97m[LE]>", end = '')

                inputstring = input()
                
                if(   inputstring.lower() == "button a" or inputstring.lower() == "a"):
                    print("Pressed Button A")
                    Conection = TX.Button(True)

                elif (inputstring.lower() == "button b" or inputstring.lower() == "b"):
                    print("Pressed Button B")
                    Conection = TX.Button(False)

                elif (inputstring.lower() == "help"     or inputstring.lower() == "h"):
                    help()
                elif (inputstring.lower() == "info"     or inputstring.lower() == "i"):   
                    Conection = TX.deviceinforamtion()

                elif (inputstring.lower() == "quit"     or inputstring.lower() == "q" ):
                    sys.exit()
                elif(inputstring.lower() == ""):
                    continue
                else:              
                    print("Invalid Input")

    elif(MODE.lower() == 'c' and IFILE != '' and OFILE != ''):
        if(os.path.isfile(IFILE)):
            Scriptconverter.Converter(IFILE, OFILE)
        else:
            print("Inputfile does not exist")
            sys.exit(2)
    else:
        help()
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])