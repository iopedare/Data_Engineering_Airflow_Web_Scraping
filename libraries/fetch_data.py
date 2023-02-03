import requests
import os
os.environ['no_proxy']='*'

class FetchData:
    def __init__(self, url: str, file_name):
        self.web_link = url
        self.file_name = file_name

        if not url:
            raise Exception("You have not provided a url to fetch data")

        if not isinstance(url, str):
            msg = f"The type of the url should be a string but you parsed url of type {type(url)}"
            raise ValueError(msg)

    def fetch(self):
        html_data = requests.get(self.web_link).content
        return html_data

    def run(self):
        data = self.fetch()
        with open(f'tmp/{self.file_name}.html', 'wb') as file:
            file.write(data)
            file.close()

if __name__=="__main__":
    fetch_obj = FetchData('https://www.globalpetrolprices.com/Nigeria/gasoline_prices/', 'test_file').run()