# encoding=utf-8
import getopt
import sys
def main(argv):
    try:

        options, args = getopt.getopt(argv, "hp:i:", ["help", "ip=", "port="])

    except getopt.GetoptError:

        sys.exit()

    for option, value in options:

        if option in ("-h", "--help"):
            print("help")

        if option in ("-i", "--ip"):
            print("ip is: {0}".format(value))

        if option in ("-p", "--port"):
            print("port is: {0}".format(value))

    print("error args: {0}".format(args))


if __name__ == '__main__':
    main(sys.argv[1:])