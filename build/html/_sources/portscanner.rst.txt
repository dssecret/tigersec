###########
portscanner
###########

.. py:function:: scan_port(ip, port)
    
    Scans specified port on inputted IP address to check if open

    :param str ip: IP address
    :param int port: port number
    :return: port number if active; 0 if not active
    :rtype: int
    :raises Exception: if the port is not open


.. py:function:: scan_ip(ip)

    Scans range of ports from 1 to 65535 using scan_port

    :param str ip: IP address
    :return: None
    :rtype: None