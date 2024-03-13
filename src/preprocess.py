import pandas as pd
import geopy


i = 0


def get_zipcode(df, geolocator, lat_field, lon_field):
    global i
    print(str(round(i / df.shape[0], 2)) + '%')
    i += 1

    location = geolocator.reverse((df[lat_field], df[lon_field]))
    if 'address' in location.raw and 'postcode' in location.raw['address']:
        return location.raw['address']['postcode']
    else:
        return None


def preprocess():
    df = pd.read_csv('./data/listings_original.csv')
    geolocator = geopy.Nominatim(user_agent='airbnb')
    df['zipcode'] = df.apply(get_zipcode, axis=1, geolocator=geolocator, lat_field='latitude', lon_field='longitude')
    df.to_csv('./data/listings.csv')


if __name__ == '__main__':
    preprocess()