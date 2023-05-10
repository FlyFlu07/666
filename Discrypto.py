
from eth_account import Account
import secrets
from mnemonic import Mnemonic
import time
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("// Всего Найдено [0 ETH ≈ 0$]") #Всего Найдено [0.22 ETH ≈ 389$]")
i = 0
while i < 10**8:
    i += 1
    my_mnemonic = Mnemonic("english")
    words = my_mnemonic.generate(128) 
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    acct = Account.from_key(private_key)
    print('address: ', acct.address, '  balance: None | Mnemonic phrase: ', words, "key:", private_key[:50])
    time.sleep(0.1)





