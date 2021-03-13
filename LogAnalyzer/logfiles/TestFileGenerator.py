from datetime import datetime
from random import randint, choice
import sys

dictionary = {'request': ['GET', 'POST', 'PUT', 'DELETE'], 'endpoint': ['/usr', '/usr/admin', '/usr/admin/developer', '/usr/login', '/usr/register'], 'statuscode': [
    '303', '404', '500', '403', '502', '304'], 'username': ['james', 'adam', 'eve', 'alex', 'smith', 'isabella', 'david', 'angela', 'donald', 'hilary']}
for j in range(1, len(sys.argv)):
    with open(f'./logFile{sys.argv[j]}.log', 'w+') as f:
        for i in range(int(sys.argv[j])):
            uname = choice(dictionary['username'])
            f.write(
                f'''{datetime.now()},{randint(0, 1000)} ERROR (default task-95) IP-Address=192.168.{randint(0, 10)}.{randint(0, 255)}#,!User-Agent=Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0;  . / ;  . : / IEMobile/9.0)#,!X-Request-From=UIX#,!Request-Type={choice(dictionary['request'])}#,!API={choice(dictionary['endpoint'])}#,!User-Login={uname}@demo.com#,!User-Name={uname}#,!EnterpriseId={randint(1, 10000)}#,!EnterpriseName=Enterprise-{randint(1, 10000)}#,!Auth-Status=#,!Status-Code={choice(dictionary['statuscode'])}#,!Response-Time={randint(4, 2000)}#,!Request-Body=\n''')
