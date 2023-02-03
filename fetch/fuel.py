from libraries.fetch_data import FetchData

class Fuel:
    def __init__(self, country: str):
        self.country =  country

    def fetch_fuel(self):
        url = f'https://www.globalpetrolprices.com/{self.country}/gasoline_prices/'
        FetchData(url=url, file_name=f'{self.country.lower()}_fuel_price').run()

if __name__=="__main__":
    Fuel('Nigeria').fetch_fuel()
    Fuel('Kenya').fetch_fuel()