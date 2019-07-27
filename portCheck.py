def portInfo(currentPort):
    if currentPort == 20:
        return 'FTP'
    elif currentPort == 21:
        return 'FTP'
    elif currentPort == 22:
        return 'SSH'
    elif currentPort == 23:
        return 'Telnet'
    elif currentPort == 53:
        return 'DNS'
    elif currentPort == 69:
        return 'TFTP'
    elif currentPort == 80:
        return 'HTTP'
    elif currentPort == 110:
        return 'POP3'
    elif currentPort == 123:
        return 'NTP'
    elif currentPort == 143:
        return 'IMAP'
    elif currentPort == 161:
        return 'SNMP'
    elif currentPort == 389:
        return 'LDAP'
    elif currentPort == 443:
        return 'HTTPS'
    elif currentPort == 1443:
        return 'SQL Server'
    elif currentPort == 1521:
        return 'Oracle'
    elif currentPort == 1720:
        return 'H.323'
    elif currentPort == 1723:
        return 'PPTP'
    elif currentPort == 3389:
        return 'RDP'
