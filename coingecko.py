from pycoingecko import CoinGeckoAPI

def get_price(token):
    cg = CoinGeckoAPI()
    price = cg.get_price(ids=token, vs_currencies='usd').get(token).get('usd')
    print(price)
    return(price)