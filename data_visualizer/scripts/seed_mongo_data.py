import csv
from data_visualizer.models import CountryData, YearlyData


def run():
    with open('data_visualizer/scripts/data/seed_country_data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line = 0
        for row in csv_reader:
            if line > 0:
                if line % 10 == 0:
                    print(f"Processing Line {line}")

                new_cd = CountryData(
                    series_name=row[0],
                    series_code=row[1],
                    country_name=row[2],
                    country_code=row[3],
                )

                new_cd.yearly_data = []
                for i, data in enumerate(row[4:]):
                    try:
                        data = float(data)
                    except ValueError:
                        data = None
                    year = 2000 + i
                    new_cd.yearly_data.append(YearlyData(year=year, data=data))
                new_cd.save()
            line += 1
        print(f"Completed seed with {line} lines")
