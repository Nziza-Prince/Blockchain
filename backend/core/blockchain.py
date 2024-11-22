import sys
sys.path.append("/home/nziza/Documents/code")
from Blockchain.backend.core.block import Block
from Blockchain.backend.core.blockHeader import BlockHeader
from Blockchain.backend.util.util import twoLayerhash256
import time
import json

ZERO_HASH = '0' * 64
VERSION = 1

class BlockChain:
    def __init__(self):
        self.chain = []
        self.GenesisBlock()
        
    def GenesisBlock(self):
        BlockHeight = 0
        prevBlockHash = ZERO_HASH
        self.addBlock(BlockHeight, prevBlockHash)
        
    def addBlock(self, BlockHeight, prevBlockHash):
        timestamp = int(time.time())
        Transaction = f"Alert miners sent {BlockHeight} bitcoins to Nziza"
        merkelRoot = twoLayerhash256(Transaction.encode()).hex()
        bits = "ffff001f"
        blockheader = BlockHeader(VERSION, prevBlockHash, merkelRoot, timestamp, bits)
        blockheader.mine()
        self.chain.append(Block(BlockHeight, 1, blockheader.__dict__, Transaction).__dict__)
        print(self.chain)
        print(json.dumps(self.chain, indent=4))
        
    def main(self):
        while True:
            lastBlock = self.chain[::-1]  # Access the last block
            BlockHeight = lastBlock[0]['Height'] + 1
            prevBlockHash = lastBlock[0]['TxCount']['blockHash']  # Access blockHash
            self.addBlock(BlockHeight, prevBlockHash)

if __name__ == "__main__":
    blockchain = BlockChain()
    blockchain.main()
