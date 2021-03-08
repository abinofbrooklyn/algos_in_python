class Solution():
    def validateIP(self, ip):
        """
        @param ip: str
        @return: bool
        """
        ip_array = ip.split(".")
        if len(ip_array) != 4:
          return False
        for ip in ip_array:
            if not check(ip):
                return False
        return True

    def check(self, ip):
        if len(ip) == 0:
            return False

        for i in range(len(ip)):
            if ip[i] < '0' or ip[i] > '9':
                return False

        if 0 <= int(ip) and int(ip) <= 255:
            return True
