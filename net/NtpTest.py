import ntplib

def print_time():
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request('ntp2.zhidaozhixing.com')
    print(response.ref_time)
    print(response.orig_time)
    print(response.recv_time)
    print(response.tx_time)

if __name__ == '__main__':
    print_time()