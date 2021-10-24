from urllib.request import urlretrieve as retrieve


def get_data(url_data, dir):
    for t in url_data.keys():
        print(f"Downloading {t}... ", end="")
        retrieve(url_data[t], f"{dir}/{t}.csv")
        print(f"Success")


imdb_urls = {
    "name_basics": "https://datasets.imdbws.com/name.basics.tsv.gz",
    "title_akas": "https://datasets.imdbws.com/title.akas.tsv.gz",
    "title_basics": "https://datasets.imdbws.com/title.basics.tsv.gz",
    "title_crew": "https://datasets.imdbws.com/title.crew.tsv.gz",
    "title_episode": "https://datasets.imdbws.com/title.episode.tsv.gz",
    "title_principals": "https://datasets.imdbws.com/title.principals.tsv.gz",
    "title_ratings": "https://datasets.imdbws.com/title.ratings.tsv.gz"
}
data_dir = "./data"


if __name__ == "__main__":
    get_data(imdb_urls, data_dir)
