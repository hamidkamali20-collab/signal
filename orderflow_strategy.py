class TsetmcOrderFlowEngine:
    def __init__(self):
        self.pass_score = 20

    def analyze(self, data):
        score = 0
        symbol = data.get('symbol', 'Unknown')
        last_price = data.get('last_price', 0)
        close_price = data.get('close_price', 0)
        volume = data.get('volume', 0)
        avg_vol = data.get('month_avg_volume', float('inf'))
        
        # 1. Suspicious Volume Check
        if volume > (avg_vol * 2.5):
            score += 15

        # 2. Real Buyer Power Check
        real_buy_count = data.get('real_buy_count', 0)
        real_sell_count = data.get('real_sell_count', 0)
        buyer_power_ratio = 0
        
        if real_buy_count > 0 and real_sell_count > 0:
            buy_per_capita = (data.get('real_buy_vol', 0) * last_price) / real_buy_count
            sell_per_capita = (data.get('real_sell_vol', 0) * last_price) / real_sell_count
            buyer_power_ratio = buy_per_capita / sell_per_capita
            
            if buyer_power_ratio > 1.5:
                score += 10

        # 3. Price Tick Check (Ranging Positive)
        if last_price > close_price:
            score += 10

        # Final Decision
        if score >= self.pass_score:
            return {
                "signal": True, 
                "symbol": symbol, 
                "score": score, 
                "ratio": round(buyer_power_ratio, 2),
                "volume": volume
            }
        return {"signal": False}
