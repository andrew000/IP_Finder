import socket
import re
import sys
import struct


def find_ip(file):
    with open(file, "r") as file:

        text = [x for x in [re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", x) for x in file.readlines()]]
        ip_list = []
        for i in text:
            for _ in i:
                ip_list.append(_)

        return sorted(list(set(ip_list)), key=lambda ip: struct.unpack("!L", socket.inet_aton(ip))[0])


def validate_ip(ip_list):
    true_ip = []

    for ip in ip_list:
        if socket.inet_pton(socket.AF_INET, ip):
            true_ip.append(ip)
        else:
            pass
    return true_ip


def write_ip(true_ip):
    with open("results.txt", "w") as file:
        file.write("\n".join(true_ip))


def main():
    if len(sys.argv) != 2:
        exit("I need file with ip, to find ip\nExample: python3 ips.txt")

    ip_list = find_ip(sys.argv[1])
    true_ip = validate_ip(ip_list)
    write_ip(true_ip)


if __name__ == '__main__':
    main()
