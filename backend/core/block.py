class Block:
    """
    Block is a storage container that stores transactions
    """
    def __init__(self,Height,Blocksize,TxCount,Txs):
        self.Height = Height
        self.Blocksize = Blocksize
        self.TxCount = TxCount
        self.Txs = Txs