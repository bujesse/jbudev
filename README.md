# jbudev

DEVELOPMENT:
1. Create conda env from yml:
conda env create -f environment.yml

2. Set up Db and pgAdmin (postgres and postgres gui):
docker-compose up -d

3. Run migrations
python manage.py migrate

4. Create superuser for yourself:
python manage.py createsuperuser

Some good big data sources:
https://www.forbes.com/sites/bernardmarr/2018/02/26/big-data-and-ai-30-amazing-and-free-public-data-sources-for-2018/#5469d9835f8a
https://databank.worldbank.org/home.aspx
https://microdata.worldbank.org/api-documentation/catalog/index.html
