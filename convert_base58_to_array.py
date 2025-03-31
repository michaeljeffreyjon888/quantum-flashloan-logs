import base58

def convert_base58_to_array(base58_key):
    decoded = base58.b58decode(base58_key)
    return list(decoded)

if __name__ == "__main__":
    key = input("Paste your Phantom base58 private key here:\n> ").strip()
    try:
        result = convert_base58_to_array(key)
        print("\n✅ Converted Private Key Array:")
        print(result)
    except Exception as e:
        print(f"❌ Error: {e}")
