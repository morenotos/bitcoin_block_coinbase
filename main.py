import requests
import json
from time import sleep

base_url = "https://blockstream.info/api"
block_height = 630000

block_hash_url = base_url + '/block-height/' + str(block_height)
#print(block_hash_url)
block_hash = requests.get(block_hash_url).text
#print('The hash of block ' + str(block_height) + ' is ' + str(block_hash))

block_coinbase_url = base_url + '/block/' + block_hash + '/txs/0'
#print(block_coinbase_url)
block_coinbase = requests.get(block_coinbase_url).text
#print(block_coinbase)

'''
#Coinbase transaction
coinbase_txid_url = base_url + '/block/' + str(block_hash) + '/txid/0'
coinbase_txid = requests.get(coinbase_txid_url).text
#print(coinbase_txid)
coinbase_tx = base_url + '/tx/' + str(coinbase_txid)
parsed_coinbase_tx = json.loads(coinbase_tx)
json_coinbase_tx = json.dumps(parsed_coinbase_tx, indent = 4)
print(json_coinbase_tx)
'''
#0000000000000000000000000000000000000000000000000000000000000000'

print('Checking block subsidy for block ' + str(block_height) + '...')
sleep(5)

try:
  parsed_block_coinbase = json.loads(block_coinbase)
  json_block_coinbase = json.dumps(parsed_block_coinbase, indent=4)
  #print(json_block_coinbase)
  #print(type(json_block_coinbase))

  block_subsidy = parsed_block_coinbase[0]['vout'][0]['value']
  #print(type(block_subsidy))
  print('The block subsidy of this block was: ' + str(block_subsidy) + ' satoshis')
  print('Block hash is: ' + str(block_hash))
except json.decoder.JSONDecodeError:
  print('We have not gotten to the block ' + str(block_height) +  ' yet.')
  print('------------------------------------------')
  print('Click the run button to check again.')
