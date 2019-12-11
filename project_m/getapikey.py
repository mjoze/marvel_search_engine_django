import hashlib  
import time   
import json   
import requests 


m = hashlib.md5()  
private_key = b"78c030f7b3ddf4dbc5037f69a91bca1e3d2b4a2a"
public_key = b"6015ebfe6c6849dd6d84f80fca211911"
api_key = "6015ebfe6c6849dd6d84f80fca211911"
ts = str(time.time())   
ts_byte = bytes(ts, 'utf-8')  
m.update(ts_byte)  
m.update(private_key) 
m.update(public_key) 
  
hasht = m.hexdigest()    

base_url = "https://gateway.marvel.com"  
query = "/v1/public/characters" +"?"  
query_url = base_url + query +"ts=" + ts + "&apikey=" + api_key + "&hash=" + hasht
print(query_url) 

data = requests.get(query_url).json()


