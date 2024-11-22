from Blockchain.backend.util.util import twoLayerhash256
class BlockHeader:
    def __init__(self,version,prevBlockHash,merkelRoot,timestamp,bits):
        self.version = version
        self.previousBlockHash = prevBlockHash
        self.merkelRoot = merkelRoot
        self.timestamp = timestamp
        self.bits = bits
        self.nonce = 0
        self.blockHash = ''
        
    def mine(self):
        while (self.blockHash[0:4] != '0000'):
            self.blockHash = twoLayerhash256((str(self.version)+str(self.previousBlockHash)+str(self.merkelRoot)+str(self.bits)+str(self.nonce)).encode()).hex()
            self.nonce +=1
            print(f"Mining started {self.nonce}",end = "\r")
        
        