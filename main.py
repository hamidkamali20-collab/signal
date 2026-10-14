import asyncio
import aiohttp
from config import API_KEY, API_BASE_URL
from orderflow_strategy import TsetmcOrderFlowEngine

async def fetch_and_analyze(session, engine, symbol):
    # In a real scenario, you would make an API call here using API_KEY
    # For now, we simulate the API response
    print(f"Monitoring {symbol}...")
    await asyncio.sleep(1)
    
    # Mock data passing to the engine
    mock_data = {
        "symbol": symbol,
        "last_price": 5000,
        "close_price": 4900,
        "volume": 50000000,
        "month_avg_volume": 15000000,
        "real_buy_vol": 80000,
        "real_buy_count": 200,
        "real_sell_vol": 30000,
        "real_sell_count": 500
    }
    
    result = engine.analyze(mock_data)
    if result['signal']:
        print(f"🚨 Smart Money Alert for {symbol}! Score: {result['score']}/35 | Buyer Power: {result['ratio']}x")

async def main():
    print("Starting Bourse Bot Engine...")
    engine = TsetmcOrderFlowEngine()
    
    # Symbols to monitor
    symbols_to_track = ["FAMELI", "FOOLAD"]
    
    async with aiohttp.ClientSession() as session:
        while True:
            tasks = [fetch_and_analyze(session, engine, sym) for sym in symbols_to_track]
            await asyncio.gather(*tasks)
            print("--- Waiting for next API cycle ---")
            await asyncio.sleep(5)

if __name__ == '__main__':
    asyncio.run(main())
