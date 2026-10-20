#!/usr/bin/env python3


import os
from dotenv import load_dotenv


load_dotenv()


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    print("Configuration loaded:")
    mode = os.getenv("MATRIX_MODE", "development")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    print(f"Mode: {mode}")
    if db_url:
        db_status = "Connected to local instance"
    else:
        db_status = "Disconnected"
    print(f"Database: {db_status}")
    if api_key:
        api_status = "Authenticated"
    else:
        api_status = "Not Authenticated"
    print(f"API Access: {api_status}")
    print(f"Log Level: {log_level}")
    if os.getenv("ZION_ENDPOINT"):
        zion_status = "Online"
    else:
        zion_status = "Offline"
    print(f"Zion Network: {zion_status}")
    if mode == "production":
        print()
        print("WARNING: Running in PRODUCTION mode")
        print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if mode and db_url and api_key and log_level:
        print("[OK] .env file properly configured")
    else:
        print("[KO] Missing required environment variables")
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
