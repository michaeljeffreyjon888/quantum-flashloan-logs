import os, json, asyncio
from solana.rpc.async_api import AsyncClient
from solana.publickey import PublicKey
from solana.transaction import Transaction
from price_fetcher import get_price_diff
from rpc_executor import send_transaction
from datetime import datetime

PRIVATE_KEY = json.loads(os.getenv("PRIVATE_KEY"))
AUTO_COMPOUND = os.getenv("AUTO_COMPOUND", "false").lower() == "true"
GITHUB_REPO = os.getenv("GITHUB_REPO")
LOG_TO_GITHUB = os.getenv("LOG_TO_GITHUB", "false").lower() == "true"
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")

async def run_arbitrage():
    tokens = ["SOL", "BONK", "PEPE"]
    for token in tokens:
        try:
            price_info = get_price_diff(token)
            if isinstance(price_info, dict) and price_info.get("diff", 0) >= 1.0:
                print(f"[💹 PROFIT] Opportunity found on {token}: {price_info['diff']}%")
                
                tx = Transaction()
                tx.add(...)  # Add real arbitrage instruction here
                
                result = send_transaction(tx, PRIVATE_KEY)
                log_to_file(token, price_info["diff"], result)

                if AUTO_COMPOUND:
                    print("[♻️] Auto-compound enabled: reinvesting profits...")

                break  # Prioritize one trade at a time (Flashloan > Memecoin > Arb)
        except Exception as e:
            print(f"[⚠️ ERROR] {token} → {e}")
            continue

def log_to_file(token, diff, tx_hash):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"{now} | Token: {token} | Profit: {diff}% | TX: {tx_hash}\n"
    with open("trade_log.txt", "a") as f:
        f.write(log_line)
    print(f"[📄 LOGGED] {log_line.strip()}")

    if LOG_TO_GITHUB:
        os.system("git add trade_log.txt && git commit -m 'Auto log' && git push origin main")

if __name__ == "__main__":
    asyncio.run(run_arbitrage())
