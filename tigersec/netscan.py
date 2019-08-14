import argparse
import logging
import multiprocessing
import os
import socket
import subprocess


def get_my_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


def pinger(job_q, results_q):
    DEVNULL = open(os.devnull, 'w')
    while True:
        ip = job_q.get()

        if ip is None:
            break

        try:
            subprocess.check_call(['ping', '-c1', ip], stdout=DEVNULL)
            results_q.put(ip)
        except:
            pass


def map_network(pool_size=255):
    ip_list = list()

    ip_parts = get_my_ip().split('.')
    base_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'

    jobs = multiprocessing.Queue()
    results = multiprocessing.Queue()

    pool = [multiprocessing.Process(target=pinger, args=(jobs, results)) for i in range(pool_size)]

    for p in pool:
        p.start()

    for i in range(1, 255):
        jobs.put(base_ip + '{0}'.format(i))

    for p in pool:
        jobs.put(None)

    for p in pool:
        p.join()

    while not results.empty():
        ip = results.get()
        ip_list.append(ip)

    return ip_list


if __name__ == "__main__":
    logging.basicConfig(filename="netscan.log", format="%(asctime)s %(message)s", filemode="a")
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--user", dest="user", nargs="?", const=True, default=False, help="Get User IP")
    parser.add_argument("-n", "--network", dest="net", nargs="?", const=True, default=False, help="Scan Network")
    # parser.add_argument("-p", "--pool-size", dest="pool", type=int, default=255, help="Pool Size to Map Network")
    args = parser.parse_args()

    user_ip = args.user
    scan_net = args.net

    if user_ip and scan_net:
        logger.error("Can't set param -u and -n at same time")
        logger.info("")
        raise Exception("Can't set parameters -u and -n at the same time")

    if user_ip:
        logger.info("User IP enabled")
        myip = get_my_ip()
        logger.info("User IP: " + myip)
        print("Your IP is " + myip + ".")
    elif scan_net:
        logger.info("Scan Network enabled")
    else:
        logger.info("")
        raise Exception("Logic Error: Run Debugger and Check Log")