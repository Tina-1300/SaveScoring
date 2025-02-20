# n'est plus utiliser pour le moment

from bs4 import BeautifulSoup
import requests
import sys
import os


# https://docs.python.org/fr/3.13/library/time.html
class BaseCrawler:

    def __init__(
        self,
        stdin=sys.stdin.reconfigure(encoding="utf-8"),
        stdout=sys.stdout.reconfigure(encoding="utf-8"),
    ):
        self.stdin = stdin
        self.stdout = stdout

    # allows you to save a file
    def save_file(self, file_name: str, writing_value) -> None:
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(writing_value)

    # allows you to read a file
    def read_file(self, file_name: str) -> str:
        with open(file_name, encoding="utf-8") as r:
            data = r.read()
        return data

    def download_page(self, file_name_page: str, url: str) -> None:
        page_scrore = requests.get(url)
        self.save_file(file_name_page, page_scrore.text)

    # the function returns true if the file exists and false if the file does not exist
    def check_file(self, file_name: str) -> bool:
        return True if os.path.exists(file_name) else False


# no errors
class CrawlerRootMe(BaseCrawler):
    def __init__(self):
        BaseCrawler.__init__(self)

    # automatically read the file, no need to return the contents of the file and this function returns the score
    def find_score(self, file_name_html: str) -> str:
        soup = BeautifulSoup(self.read_file(file_name_html), "html.parser")
        search = soup.find_all(
            "div", {"class": "small-6 medium-3 columns text-center"}
        )[1]
        score = search.find("h3").text
        return score


# à faire je n'est pas encore devlopper cela
class CrawlerNewbieContest(BaseCrawler):

    def __init__(self):
        BaseCrawler.__init__(self)

    # automatically read the file, no need to return the contents of the file and this function returns the score
    def find_score(self, file_name_html: str) -> str: ...


# ------------------------------------------------------------------------------------------
# crawler_root_me = CrawlerRootMe()

# url_root_me = "https://www.root-me.org/Tina-853821"

# file_name_html_root_me = "Root.html"

# if crawler_root_me.check_file(file_name_html_root_me) == True:
#     resultat_scan_score = crawler_root_me.find_score(file_name_html_root_me)
#     # Add exception checks to confirm that the file was read successfully
#     print("No error ✅ : the file was read successfully")
# else:
#     # Download the page containing root me scores
#     crawler_root_me.download_page(file_name_html_root_me, url_root_me)

#     if crawler_root_me.check_file(file_name_html_root_me) == False:
#         print("Error ⛔ : the file was not downloaded")
#     else:
#         resultat_scan_score = crawler_root_me.find_score(file_name_html_root_me)
#         print("No error ✅ : the file was downloaded successfully")
#         print("No error ✅ : the file was read successfully")

# print(resultat_scan_score) # Score display

# ------------------------------------------------------------------------------------------
