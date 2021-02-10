import subprocess
import json

import os
from dotenv import load_dotenv

from web3 import Web3
from web3.middleware import geth_poa_middleware 
from eth_account import Account

from constants import *

load_dotenv()
mnemonic = os.getenv("MNEMONIC")


command = './derive -g --mnemonic="INSERT HERE" --cols=path,address,privkey,pubkey --format=json'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
p_status = p.wait()

keys = json.loads(output)
print(keys)
