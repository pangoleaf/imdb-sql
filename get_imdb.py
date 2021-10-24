from dataclasses import dataclass
import sqlalchemy as sqa
from pandas import read_table
from imdb_metadata import metadata
from db_details import details as d 


@dataclass
class ImdbLoader:
    datasets: dict
    engine: sqa.engine.Engine

    def import_to_database(self):
        print("Importing data from IMDb...")
        with self.engine.connect() as conn, conn.begin():
            for name, url in self.datasets.items():
                print(f"    Downloading & loading in {name}... ", end="")
                
                # TODO try small chunks for read_table to reduce memory usage? research
                read_table(url, compression="gzip", header=0, quoting=3, encoding="utf-8") \
                    .to_sql(name, engine, if_exists="replace", index=False, chunksize=1000)

                print(f"Success")
                # TODO expand metadata dict to include pks and fks then apply them, possibly with pandas
        print("Data successfully loaded!")


db_str = f"{d.dialect}+{d.driver}://{d.username}:{d.password}@{d.host}/{d.database}?charset={d.charset}"
engine = sqa.create_engine(db_str, pool_recycle=3600, future=True)

if __name__ == "__main__":
    app = ImdbLoader(metadata, engine)
    app.import_to_database()
