class Solution:
    def validIPAddress(self, IP: str) -> str:
        if IP.count('.') == 3:
            for token in IP.split('.'):
                if len(token) == 0 or len(token) > 3: return 'Neither'
                if token[0] == '0' and len(token) != 1: return 'Neither'
                if not token.isdigit() or int(token) > 255: return 'Neither'
            return 'IPv4'
        if IP.count(':') == 7:
            for token in IP.split(':'):
                if len(token) == 0 or len(token) > 4: return 'Neither'
                for c in token:
                    if not(c>='0' and c<='9' or c>='a' and c <='f' or c>='A' and c<='F'):
                        return 'Neither'
            return 'IPv6'
        return 'Neither'
