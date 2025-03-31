from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.keypair import Keypair
from solana.rpc.commitment import Confirmed

def send_transaction(tx: Transaction, private_key):
    client = Client("https://api.mainnet-beta.solana.com")
    kp = Keypair.from_secret_key(bytes(private_key))
    tx.recent_blockhash = client.get_recent_blockhash()["result"]["value"]["blockhash"]
    tx.sign(kp)
    response = client.send_transaction(tx, kp, opts={"skip_preflight": True, "preflight_commitment": Confirmed})
    return response["result"]
