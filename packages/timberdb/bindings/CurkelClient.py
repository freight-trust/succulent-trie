import grpc
import cztrie_pb2_grpc
import cztrie_pb2
import json
import time

#Encryption/Decryption TODO


def start(address, port):
    channel = grpc.insecure_channel(address + ":" + port)
    return cztrie_pb2_grpc.CztrieServiceStub(channel)

def create(cztrie, name):
    return cztrie.Create(cztrie_pb2.DatasetRequest(name= name))

def get(cztrie, name, key, enc = False, sk = ""):
    GetResponse = cztrie.Get(cztrie_pb2.GetRequest(name= name, key=key))
    if enc:
        GetRequest.value = decrypt(sk, value)
    return GetResponse

def put(cztrie, name, key, value, enc = False, sk = ""):
    if enc:
        value = encrypt(sk, value)
    return cztrie.Put(cztrie_pb2.PutRequest(name=name, key=key, value=value))

def delete(cztrie, name, key):
    return cztrie.Del(cztrie_pb2.DeleteRequest(name= name, key=key))

def encrypt(sk, val):
    return val

def decrypt(sk, val):
    return val

def main():
    address = '0.0.0.0'
    external ='35.235.101.177'
    port = '50051'
    cztrie = start(external, port)
    print("Starting client .....")
    db_name = "Python_DB"
    key = bytes(str.ljust("Binance", 32))
    value = bytes('{"contractAddress": "0xB8c77482e45F1F44dE1745F52C74426C631bDD52", "name": "BNB", "totalSupply": "189175490242498551714388965"}')
    #st = time.time()
    #create(cztrie, db_name)
    #end = time.time()
    #print(end - st)
    ##print(put(cztrie, db_name, key, value))
    ##for ()
    #st = time.time()
    #response = get(cztrie, db_name, key)
    #end = time.time()
    print(response)
    #print(end - st)
    # 20-60 ms from AWS
    binance = json.loads(response.value.decode(encoding="utf-8"))
    
    
    print("NAME: " + binance["name"])


main()
