import argparse
import logging
import socket


def scan_port(ip, port):
    """
    Scan port on certain IP address to check if open.
    :param ip: IP address
    :param port: port number
    :return:
    """
    connection = socket.socket()
    try:
        connection.connect((ip, port))
        logger.info("Connection successful on port %s" % port)
        return port
    except socket.error as e:
        logger.info("Connection failed on port %s: %s" % (port, e))
        return "Failed"
    finally:
        connection.close()


def scan_ip(ip):
    """
    Scan range of ports from 1 to 65535 using scan_port.
    :param ip: IP address
    :return:
    """
    for port in range(1, 65535):
        result = scan_port(ip, port)
        if result != "Failed":
            valid_ports.append(int(result))

    print("Open Ports: " + str(valid_ports))
    logger.info("Open Ports: " + str(valid_ports))


if __name__ == "__main__":
    logging.basicConfig(filename="portscanner.log", format="%(asctime)s %(message)s", filemode="a")
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--address", dest="address", default='localhost', help="ADDRESS for server")
    args = parser.parse_args()

    ip = args.address
    logger.info("Scanning " + ip)

    valid_ports = []

    for port in range(1, 65535):
        result = scan_port(ip, port)
        if result != "Failed":
            valid_ports.append(int(result))

    print("Open Ports: " + str(valid_ports))
    logger.info("Open Ports: " + str(valid_ports))
