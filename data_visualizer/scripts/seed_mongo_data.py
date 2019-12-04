import csv
from data_visualizer.models import Country, Series, DataPoint


def run():
    with open('data_visualizer/scripts/data/seed_country_data.csv') as csv_file:
        countries_dict = {}
        series_dict = {}
        line = 0
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if line > 0:
                if line % 10 == 0:
                    print(f"Processing Line {line}")

                if row[1] not in series_dict:
                    series = Series(
                        series_name=row[0],
                        series_code=row[1],
                    )
                    series.save()
                    series_dict[row[1]] = series
                else:
                    series = series_dict[row[1]]

                if row[3] not in countries_dict:
                    country = Country(
                        country_name=row[2],
                        country_code=row[3],
                    )
                    country.save()
                    countries_dict[row[3]] = country
                else:
                    country = countries_dict[row[3]]

                for i, data in enumerate(row[4:]):
                    try:
                        data = float(data)
                    except ValueError:
                        data = None
                    year = 2000 + i

                    new_yd = DataPoint(year=year, data=data, country=country, series=series)
                    new_yd.save()
            line += 1
        print(f"Completed seed with {line} lines")
