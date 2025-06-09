print("""👋
       Hello! I’m CryptoBuddy — your AI-powered crypto advisor! 🌟""")
print("Ask me about trends, sustainability, security or what’s hot in the crypto world!")
print("I can help you with:")
print("1️⃣ Latest trends in cryptocurrency")
print("2️⃣ Sustainable crypto practices") 
print("3️⃣ Hot topics in the crypto space")
print("4️⃣ General crypto advice")    
print("5️⃣ Crypto market analysis")
print("6️⃣ Crypto security tips")

crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    }  
}

user_query = input("🤖 What would you like to know about crypto? ").lower()

if "sustainable" in user_query:
    recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
    print(f"🌱 Invest in {recommend}! It’s eco-friendly and has long-term potential.")

elif "growth" in user_query or "profitable" in user_query:
    for coin, data in crypto_db.items():
        if data["price_trend"] == "rising" and data["market_cap"] == "high":
            print(f"🚀 {coin} is rising and has a strong market cap — a solid growth choice!")

elif "trending" in user_query or "up" in user_query:
    rising = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
    print(f"📈 These coins are trending up: {', '.join(rising)}")

elif "security" in user_query:
    print("🔒 Always use secure wallets and keep your private keys safe!")

elif "analysis" in user_query:
    for coin, data in crypto_db.items():
        print(f"{coin}: Price Trend: {data['price_trend']}, Market Cap: {data['market_cap']}, Energy Use: {data['energy_use']}, Sustainability Score: {data['sustainability_score']*10}/10")

elif "hot" in user_query or "news" in user_query:
    print("🔥 Stay updated with the latest crypto news on platforms like CoinDesk, CoinTelegraph, and Twitter!")
else:
    print("🤔 I’m not sure about that. Can you ask something else related to crypto trends, sustainability, or security?")
print("Thank you for using CryptoBuddy! Happy investing! 💰")
print("\n⚠️ Crypto is risky—always do your own research before investing!")





