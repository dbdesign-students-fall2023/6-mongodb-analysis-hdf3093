# AirBnB MongoDB Analysis

I chose to analyze the AirBnB listings of Buenos Aires, Argentina, where I'm from. I actually stayed in an AirBnB in Villa Urquiza, Buenos Aires, this June-July, so it's interesting to see the database side of this. 

This dataset is from [Inside AirBnB](http://insideairbnb.com/get-the-data.html). It's located as CSV in my [data directory](data/listings_clean.csv).

Here are the first few rows.


| id | listing_url | scrape_id | last_scraped | source | name | description | neighborhood_overview | picture_url | host_id | host_url | host_name | host_since | host_location | host_about | host_response_time | host_response_rate | host_acceptance_rate | host_is_superhost | host_thumbnail_url | host_picture_url | host_neighbourhood | host_listings_count | host_total_listings_count | host_verifications | host_has_profile_pic | host_identity_verified | neighbourhood | neighbourhood_cleansed | neighbourhood_group_cleansed | latitude | longitude | property_type | room_type | accommodates | bathrooms | bathrooms_text | bedrooms | beds | amenities | price | minimum_nights | maximum_nights | minimum_minimum_nights | maximum_minimum_nights | minimum_maximum_nights | maximum_maximum_nights | minimum_nights_avg_ntm | maximum_nights_avg_ntm | calendar_updated | has_availability | availability_30 | availability_60 | availability_90 | availability_365 | calendar_last_scraped | number_of_reviews | number_of_reviews_ltm | number_of_reviews_l30d | first_review | last_review | review_scores_rating | review_scores_accuracy | review_scores_cleanliness | review_scores_checkin | review_scores_communication | review_scores_location | review_scores_value | license | instant_bookable | calculated_host_listings_count | calculated_host_listings_count_entire_homes | calculated_host_listings_count_private_rooms | calculated_host_listings_count_shared_rooms | reviews_per_month |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 11508 | https://www.airbnb.com/rooms/11508 | 20230922223302 | 2023-09-23 | city scrape | Condo in Buenos Aires · ★4.81 · 1 bedroom · 1 bed · 1 bath | LUXURIOUS 1 BDRM APT- POOL/ GYM/ SPA/ 24-HR SECURITY in Palermo Soho<br /><br /><b>The space</b><br />LUXURIOUS APT: 1 BDRM- POOL/ GYM/ SPA/ 24-HR SECURITY<br /><br />Palermo Soho, Buenos Aires<br /><br />BUILDING DETAILS<br /><br />Luxury building in the heart of the trendy Palermo Soho<br />24-hour security <br />Outdoor pool (opened from November 15th to April 15th)<br />Gym and Spa in building (top floor with panoramic view)<br />Laundry in building <br />Optional house keeping <br /><br />AREA: PALERMO SOHO<br /><br />Minutes walking distance from most popular bars, restaurants and boutiques<br />Buenos Aires Eco-Park within walking distance<br />Botanical Garden and magnificent park with lake (“Bosques de Palermo”) within walking distance<br />One block from Santa Fe Avenue and “D Line” subway <br />All major bus lines within walking distance<br /><br />APARTMENT DETAILS<br /><br />Fully Furnished 1 bedroom apartment <br />Wifi and Cable TV<br />Air conditioner/ heat<br />Balcony | AREA: PALERMO SOHO<br /><br />Minutes walking distance from most popular bars, restaurants and boutiques<br />Buenos Aires Eco-Park within walking distance<br />Botanical Garden and magnificent park with lake (“Bosques de Palermo”) within walking distance<br />One block from Santa Fe Avenue and “D Line” subway <br />All major bus lines within walking distance | https://a0.muscache.com/pictures/19357696/b1de16cb_original.jpg | 42762 | https://www.airbnb.com/users/show/42762 | Candela | 2009-10-01 | New York, NY | - | within an hour | 100% | 91% | t | https://a0.muscache.com/im/users/42762/profile_pic/1332809447/original.jpg?aki_policy=profile_small | https://a0.muscache.com/im/users/42762/profile_pic/1332809447/original.jpg?aki_policy=profile_x_medium | Palermo | 1 | 2 | ['email', 'phone'] | t | t | Buenos Aires, Capital Federal, Argentina | Palermo |  | -34.58184 | -58.42415 | Entire condo | Entire home/apt | 2 |  | 1 bath | 1 | 1 | ["Dining table", "Kitchen", "Freezer", "Safe", "Extra pillows and blankets", "Shared hot tub - open specific hours", "Air conditioning", "Bidet", "Bed linens", "Paid street parking off premises", "Coffee maker", "Paid washer \u2013 In building", "Shared backyard \u2013 Fully fenced", "Hair dryer", "Cooking basics", "Body soap", "Elevator", "Drying rack for clothing", "Bathtub", "Dishes and silverware", "Shared pool", "Laundromat nearby", "Stove", "Wine glasses", "Room-darkening shades", "Long term stays allowed", "Hot water", "TV with standard cable", "Paid dryer \u2013 In building", "Shared sauna", "Microwave", "Cleaning products", "Private entrance", "Gym", "Private patio or balcony", "Essentials", "Clothing storage: closet and dresser", "Host greets you", "Outdoor furniture", "Refrigerator", "Heating", "Hangers", "Oven", "Toaster", "Wifi", "Single level home", "Iron", "Books and reading material"] | $23,753.00 | 3 | 1125 | 3 | 3 | 1125 | 1125 | 3.0 | 1125.0 |  | t | 5 | 17 | 21 | 240 | 2023-09-23 | 36 | 6 | 0 | 2012-07-02 | 2023-05-13 | 4.81 | 4.94 | 4.89 | 4.91 | 4.97 | 4.94 | 4.89 |  | f | 1 | 1 | 0 | 0 | 0.26 |
| 107259 | https://www.airbnb.com/rooms/107259 | 20230922223302 | 2023-09-23 | city scrape | Rental unit in Buenos Aires · ★4.58 · 6 bedrooms · 9 beds · 5 baths | We have 7 bedrooms and 5 bathrooms,gourmet kitchen,great living room and bar.<br />Also three small balconies and one bigger.<br /><br /><b>The space</b><br />In an old and charming building on Corrientes Avenue, built over a hundred years ago when Tango was born.We offer this beautiful and centrally located apartment (walking distances to Teatro Colon ,Obelisco. Congreso, Main theaters of the city, restaurantes,milongas,bookstores, etc.<br />And the subway is right at the corner(Callao Station ,Line "C")<br /><br />Tango keep evolved, and that's what makes it immortal... the possibility of growth and change.<br /><br />It is called Paradise because we would like to provide for all your tango needs(including the apple, but not the snake HO!HO!).<br />Of course if You are not evolved with Tango, you can be anyway,very comfortable here, .(We have had several groups of people assisting to Congress or famous Musicians bands that were playing in Buenos Aires or just groups of family living  |  | https://a0.muscache.com/pictures/822490/5bc2ab07_original.jpg | 555693 | https://www.airbnb.com/users/show/555693 | Vittoria | 2011-05-03 | Montevideo, Uruguay | Soy Vittoria, ofrezco para alquiler este hermoso departamento.
Me encanta viajar y conocer nuevos paises,a demás recibir personas de todo el mundo.
 | within a day | 90% | 78% | f | https://a0.muscache.com/im/users/555693/profile_pic/1332180142/original.jpg?aki_policy=profile_small | https://a0.muscache.com/im/users/555693/profile_pic/1332180142/original.jpg?aki_policy=profile_x_medium | Balvanera | 2 | 2 | ['email', 'phone'] | t | t |  | Balvanera |  | -34.60514 | -58.3957 | Entire rental unit | Entire home/apt | 12 |  | 5 baths | 6 | 9 | ["Dining table", "Kitchen", "Freezer", "Private hot tub", "Fire extinguisher", "Indoor fireplace", "Extra pillows and blankets", "Air conditioning", "Bidet", "Bed linens", "Dishwasher", "Coffee maker", "Hair dryer", "Cooking basics", "First aid kit", "Body soap", "Elevator", "Bathtub", "Dishes and silverware", "Laundromat nearby", "Washer", "Stove", "Wine glasses", "Paid parking off premises", "Pocket wifi", "Hot water", "TV with standard cable", "Microwave", "Hot water kettle", "Private patio or balcony", "Blender", "Dryer", "Essentials", "Host greets you", "Refrigerator", "Heating", "Hangers", "Pets allowed", "Oven", "Luggage dropoff allowed", "Toaster", "Wifi", "Iron", "Crib"] | $157,512.00 | 1 | 15 | 1 | 1 | 15 | 15 | 1.0 | 15.0 |  | t | 0 | 0 | 0 | 219 | 2023-09-23 | 38 | 6 | 0 | 2012-06-18 | 2023-07-23 | 4.58 | 4.41 | 4.24 | 4.79 | 4.71 | 4.63 | 4.53 |  | f | 2 | 2 | 0 | 0 | 0.28 |







## Data scrubbing

```python

#removing unnecessary / blank columns
drop_columns = [ 'neighborhood_overview', 'host_about', 'host_response_time', 'host_response_rate', 'host_acceptance_rate',  'neighbourhood_group_cleansed','license', 'calendar_updated']

cleaned_rows = []
for row in rows:
    cleaned_row = {}
    for key, value in row.items():
        if key not in drop_columns and value is not None:
            cleaned_row[key] = value
    if len(cleaned_row) == len(row) - len(drop_columns):
        cleaned_rows.append(cleaned_row)


```

While looking through the CSV, I noticed some unneeded information (in my opinion) that I decided to remove, like host_about, neighborhood_overview, varying ratings about the host, as well as columns with null values, like license and neighbourhood_group_cleansed. The cleaned data was written to data/listings_clean.csv.



## MongoDB Queries

### 1. Show exactly two documents from the listings collection in any order.

```bash
db.listings.find().limit(2)
```
Using find and limit here. I'm not sure if this was supposed to happen, but the results were formatted well already, so they seem to be formatted the same as they would using pretty() function... To my knowledge, this should have resulted in a large, dense chunk of text rather than with line breaks. I'm not sure if this has to do with using the MongoSH shell within MongoDB compass?

Results:

```bash
{
  "_id": {
    "$oid": "65538a627ca98f88f68ed479"
  },
  "id": 11508,
  "listing_url": "https://www.airbnb.com/rooms/11508",
  "scrape_id": {
    "$numberLong": "20230922223302"
  },
  "last_scraped": {
    "$date": "2023-09-23T00:00:00.000Z"
  },
  "source": "city scrape",
  "name": "Condo in Buenos Aires · ★4.81 · 1 bedroom · 1 bed · 1 bath",
  "description": "LUXURIOUS 1 BDRM APT- POOL/ GYM/ SPA/ 24-HR SECURITY in Palermo Soho<br /><br /><b>The space</b><br />LUXURIOUS APT: 1 BDRM- POOL/ GYM/ SPA/ 24-HR SECURITY<br /><br />Palermo Soho, Buenos Aires<br /><br />BUILDING DETAILS<br /><br />Luxury building in the heart of the trendy Palermo Soho<br />24-hour security <br />Outdoor pool (opened from November 15th to April 15th)<br />Gym and Spa in building (top floor with panoramic view)<br />Laundry in building <br />Optional house keeping <br /><br />AREA: PALERMO SOHO<br /><br />Minutes walking distance from most popular bars, restaurants and boutiques<br />Buenos Aires Eco-Park within walking distance<br />Botanical Garden and magnificent park with lake (“Bosques de Palermo”) within walking distance<br />One block from Santa Fe Avenue and “D Line” subway <br />All major bus lines within walking distance<br /><br />APARTMENT DETAILS<br /><br />Fully Furnished 1 bedroom apartment <br />Wifi and Cable TV<br />Air conditioner/ heat<br />Balcony",
  "picture_url": "https://a0.muscache.com/pictures/19357696/b1de16cb_original.jpg",
  "host_id": 42762,
  "host_url": "https://www.airbnb.com/users/show/42762",
  "host_name": "Candela",
  "host_since": {
    "$date": "2009-10-01T00:00:00.000Z"
  },
  "host_location": "New York, NY",
  "host_is_superhost": true,
  "host_thumbnail_url": "https://a0.muscache.com/im/users/42762/profile_pic/1332809447/original.jpg?aki_policy=profile_small",
  "host_picture_url": "https://a0.muscache.com/im/users/42762/profile_pic/1332809447/original.jpg?aki_policy=profile_x_medium",
  "host_neighbourhood": "Palermo",
  "host_listings_count": 1,
  "host_total_listings_count": 2,
  "host_verifications": "['email', 'phone']",
  "host_has_profile_pic": true,
  "host_identity_verified": true,
  "neighbourhood": "Buenos Aires, Capital Federal, Argentina",
  "neighbourhood_cleansed": "Palermo",
  "latitude": -34.58184,
  "longitude": -58.42415,
  "property_type": "Entire condo",
  "room_type": "Entire home/apt",
  "accommodates": 2,
  "bathrooms_text": "1 bath",
  "bedrooms": 1,
  "beds": 1,
  "amenities": [
    "Dining table",
    "Kitchen",
    "Freezer",
    "Safe",
    "Extra pillows and blankets",
    "Shared hot tub - open specific hours",
    "Air conditioning",
    "Bidet",
    "Bed linens",
    "Paid street parking off premises",
    "Coffee maker",
    "Paid washer – In building",
    "Shared backyard – Fully fenced",
    "Hair dryer",
    "Cooking basics",
    "Body soap",
    "Elevator",
    "Drying rack for clothing",
    "Bathtub",
    "Dishes and silverware",
    "Shared pool",
    "Laundromat nearby",
    "Stove",
    "Wine glasses",
    "Room-darkening shades",
    "Long term stays allowed",
    "Hot water",
    "TV with standard cable",
    "Paid dryer – In building",
    "Shared sauna",
    "Microwave",
    "Cleaning products",
    "Private entrance",
    "Gym",
    "Private patio or balcony",
    "Essentials",
    "Clothing storage: closet and dresser",
    "Host greets you",
    "Outdoor furniture",
    "Refrigerator",
    "Heating",
    "Hangers",
    "Oven",
    "Toaster",
    "Wifi",
    "Single level home",
    "Iron",
    "Books and reading material"
  ],
  "price": "$23,753.00",
  "minimum_nights": 3,
  "maximum_nights": 1125,
  "minimum_minimum_nights": 3,
  "maximum_minimum_nights": 3,
  "minimum_maximum_nights": 1125,
  "maximum_maximum_nights": 1125,
  "minimum_nights_avg_ntm": 3,
  "maximum_nights_avg_ntm": 1125,
  "has_availability": true,
  "availability_30": 5,
  "availability_60": 17,
  "availability_90": 21,
  "availability_365": 240,
  "calendar_last_scraped": {
    "$date": "2023-09-23T00:00:00.000Z"
  },
  "number_of_reviews": 36,
  "number_of_reviews_ltm": 6,
  "number_of_reviews_l30d": 0,
  "first_review": {
    "$date": "2012-07-02T00:00:00.000Z"
  },
  "last_review": {
    "$date": "2023-05-13T00:00:00.000Z"
  },
  "review_scores_rating": 4.81,
  "review_scores_accuracy": 4.94,
  "review_scores_cleanliness": 4.89,
  "review_scores_checkin": 4.91,
  "review_scores_communication": 4.97,
  "review_scores_location": 4.94,
  "review_scores_value": 4.89,
  "instant_bookable": false,
  "calculated_host_listings_count": 1,
  "calculated_host_listings_count_entire_homes": 1,
  "calculated_host_listings_count_private_rooms": 0,
  "calculated_host_listings_count_shared_rooms": 0,
  "reviews_per_month": 0.26
}


{
  "_id": {
    "$oid": "65538a627ca98f88f68ed47a"
  },
  "id": 107259,
  "listing_url": "https://www.airbnb.com/rooms/107259",
  "scrape_id": {
    "$numberLong": "20230922223302"
  },
  "last_scraped": {
    "$date": "2023-09-23T00:00:00.000Z"
  },
  "source": "city scrape",
  "name": "Rental unit in Buenos Aires · ★4.58 · 6 bedrooms · 9 beds · 5 baths",
  "description": "We have 7 bedrooms and 5 bathrooms,gourmet kitchen,great living room and bar.<br />Also three small balconies and one bigger.<br /><br /><b>The space</b><br />In an old and charming building on Corrientes Avenue, built over a hundred years ago when Tango was born.We offer this beautiful and centrally located apartment (walking distances to Teatro Colon ,Obelisco. Congreso, Main theaters of the city, restaurantes,milongas,bookstores, etc.<br />And the subway is right at the corner(Callao Station ,Line \"C\")<br /><br />Tango keep evolved, and that's what makes it immortal... the possibility of growth and change.<br /><br />It is called Paradise because we would like to provide for all your tango needs(including the apple, but not the snake HO!HO!).<br />Of course if You are not evolved with Tango, you can be anyway,very comfortable here, .(We have had several groups of people assisting to Congress or famous Musicians bands that were playing in Buenos Aires or just groups of family living ",
  "picture_url": "https://a0.muscache.com/pictures/822490/5bc2ab07_original.jpg",
  "host_id": 555693,
  "host_url": "https://www.airbnb.com/users/show/555693",
  "host_name": "Vittoria",
  "host_since": {
    "$date": "2011-05-03T00:00:00.000Z"
  },
  "host_location": "Montevideo, Uruguay",
  "host_is_superhost": false,
  "host_thumbnail_url": "https://a0.muscache.com/im/users/555693/profile_pic/1332180142/original.jpg?aki_policy=profile_small",
  "host_picture_url": "https://a0.muscache.com/im/users/555693/profile_pic/1332180142/original.jpg?aki_policy=profile_x_medium",
  "host_neighbourhood": "Balvanera",
  "host_listings_count": 2,
  "host_total_listings_count": 2,
  "host_verifications": "['email', 'phone']",
  "host_has_profile_pic": true,
  "host_identity_verified": true,
  "neighbourhood_cleansed": "Balvanera",
  "latitude": -34.60514,
  "longitude": -58.3957,
  "property_type": "Entire rental unit",
  "room_type": "Entire home/apt",
  "accommodates": 12,
  "bathrooms_text": "5 baths",
  "bedrooms": 6,
  "beds": 9,
  "amenities": [
    "Dining table",
    "Kitchen",
    "Freezer",
    "Private hot tub",
    "Fire extinguisher",
    "Indoor fireplace",
    "Extra pillows and blankets",
    "Air conditioning",
    "Bidet",
    "Bed linens",
    "Dishwasher",
    "Coffee maker",
    "Hair dryer",
    "Cooking basics",
    "First aid kit",
    "Body soap",
    "Elevator",
    "Bathtub",
    "Dishes and silverware",
    "Laundromat nearby",
    "Washer",
    "Stove",
    "Wine glasses",
    "Paid parking off premises",
    "Pocket wifi",
    "Hot water",
    "TV with standard cable",
    "Microwave",
    "Hot water kettle",
    "Private patio or balcony",
    "Blender",
    "Dryer",
    "Essentials",
    "Host greets you",
    "Refrigerator",
    "Heating",
    "Hangers",
    "Pets allowed",
    "Oven",
    "Luggage dropoff allowed",
    "Toaster",
    "Wifi",
    "Iron",
    "Crib"
  ],
  "price": "$157,512.00",
  "minimum_nights": 1,
  "maximum_nights": 15,
  "minimum_minimum_nights": 1,
  "maximum_minimum_nights": 1,
  "minimum_maximum_nights": 15,
  "maximum_maximum_nights": 15,
  "minimum_nights_avg_ntm": 1,
  "maximum_nights_avg_ntm": 15,
  "has_availability": true,
  "availability_30": 0,
  "availability_60": 0,
  "availability_90": 0,
  "availability_365": 219,
  "calendar_last_scraped": {
    "$date": "2023-09-23T00:00:00.000Z"
  },
  "number_of_reviews": 38,
  "number_of_reviews_ltm": 6,
  "number_of_reviews_l30d": 0,
  "first_review": {
    "$date": "2012-06-18T00:00:00.000Z"
  },
  "last_review": {
    "$date": "2023-07-23T00:00:00.000Z"
  },
  "review_scores_rating": 4.58,
  "review_scores_accuracy": 4.41,
  "review_scores_cleanliness": 4.24,
  "review_scores_checkin": 4.79,
  "review_scores_communication": 4.71,
  "review_scores_location": 4.63,
  "review_scores_value": 4.53,
  "instant_bookable": false,
  "calculated_host_listings_count": 2,
  "calculated_host_listings_count_entire_homes": 2,
  "calculated_host_listings_count_private_rooms": 0,
  "calculated_host_listings_count_shared_rooms": 0,
  "reviews_per_month": 0.28
}

```

Snippets of the 2 results. 








### 2. Show exactly 10 documents in any order, but "prettyprint" in easier to read format, using the `pretty()` function.

```bash
db.listings.find().limit(10).pretty()
```
I used limit 10 and the pretty() function for this. 

First three results:

```bash
{
  _id: ObjectId("65538a627ca98f88f68ed479"),
  id: 11508,
  listing_url: 'https://www.airbnb.com/rooms/11508',
  scrape_id: 20230922223302,
  last_scraped: 2023-09-23T00:00:00.000Z,
  source: 'city scrape',
  name: 'Condo in Buenos Aires · ★4.81 · 1 bedroom · 1 bed · 1 bath',
  description: 'LUXURIOUS 1 BDRM APT- POOL/ GYM/ SPA/ 24-HR SECURITY in Palermo Soho<br /><br /><b>The space</b><br />LUXURIOUS APT: 1 BDRM- POOL/ GYM/ SPA/ 24-HR SECURITY<br /><br />Palermo Soho, Buenos Aires<br /><br />BUILDING DETAILS<br /><br />Luxury building in the heart of the trendy Palermo Soho<br />24-hour security <br />Outdoor pool (opened from November 15th to April 15th)<br />Gym and Spa in building (top floor with panoramic view)<br />Laundry in building <br />Optional house keeping <br /><br />AREA: PALERMO SOHO<br /><br />Minutes walking distance from most popular bars, restaurants and boutiques<br />Buenos Aires Eco-Park within walking distance<br />Botanical Garden and magnificent park with lake (“Bosques de Palermo”) within walking distance<br />One block from Santa Fe Avenue and “D Line” subway <br />All major bus lines within walking distance<br /><br />APARTMENT DETAILS<br /><br />Fully Furnished 1 bedroom apartment <br />Wifi and Cable TV<br />Air conditioner/ heat<br />Balcony',
  picture_url: 'https://a0.muscache.com/pictures/19357696/b1de16cb_original.jpg',
  host_id: 42762,
  host_url: 'https://www.airbnb.com/users/show/42762',
  host_name: 'Candela',
  host_since: 2009-10-01T00:00:00.000Z,
  host_location: 'New York, NY',
  host_is_superhost: true,
  host_thumbnail_url: 'https://a0.muscache.com/im/users/42762/profile_pic/1332809447/original.jpg?aki_policy=profile_small',
  host_picture_url: 'https://a0.muscache.com/im/users/42762/profile_pic/1332809447/original.jpg?aki_policy=profile_x_medium',
  host_neighbourhood: 'Palermo',
  host_listings_count: 1,
  host_total_listings_count: 2,
  host_verifications: "['email', 'phone']",
  host_has_profile_pic: true,
  host_identity_verified: true,
  neighbourhood: 'Buenos Aires, Capital Federal, Argentina',
  neighbourhood_cleansed: 'Palermo',
  latitude: -34.58184,
  longitude: -58.42415,
  property_type: 'Entire condo',
  room_type: 'Entire home/apt',
  accommodates: 2,
  bathrooms_text: '1 bath',
  bedrooms: 1,
  beds: 1,
  amenities: [
    'Dining table',
    'Kitchen',
    'Freezer',
    'Safe',
    'Extra pillows and blankets',
    'Shared hot tub - open specific hours',
    'Air conditioning',
    'Bidet',
    'Bed linens',
    'Paid street parking off premises',
    'Coffee maker',
    'Paid washer – In building',
    'Shared backyard – Fully fenced',
    'Hair dryer',
    'Cooking basics',
    'Body soap',
    'Elevator',
    'Drying rack for clothing',
    'Bathtub',
    'Dishes and silverware',
    'Shared pool',
    'Laundromat nearby',
    'Stove',
    'Wine glasses',
    'Room-darkening shades',
    'Long term stays allowed',
    'Hot water',
    'TV with standard cable',
    'Paid dryer – In building',
    'Shared sauna',
    'Microwave',
    'Cleaning products',
    'Private entrance',
    'Gym',
    'Private patio or balcony',
    'Essentials',
    'Clothing storage: closet and dresser',
    'Host greets you',
    'Outdoor furniture',
    'Refrigerator',
    'Heating',
    'Hangers',
    'Oven',
    'Toaster',
    'Wifi',
    'Single level home',
    'Iron',
    'Books and reading material'
  ],
  price: '$23,753.00',
  minimum_nights: 3,
  maximum_nights: 1125,
  minimum_minimum_nights: 3,
  maximum_minimum_nights: 3,
  minimum_maximum_nights: 1125,
  maximum_maximum_nights: 1125,
  minimum_nights_avg_ntm: 3,
  maximum_nights_avg_ntm: 1125,
  has_availability: true,
  availability_30: 5,
  availability_60: 17,
  availability_90: 21,
  availability_365: 240,
  calendar_last_scraped: 2023-09-23T00:00:00.000Z,
  number_of_reviews: 36,
  number_of_reviews_ltm: 6,
  number_of_reviews_l30d: 0,
  first_review: 2012-07-02T00:00:00.000Z,
  last_review: 2023-05-13T00:00:00.000Z,
  review_scores_rating: 4.81,
  review_scores_accuracy: 4.94,
  review_scores_cleanliness: 4.89,
  review_scores_checkin: 4.91,
  review_scores_communication: 4.97,
  review_scores_location: 4.94,
  review_scores_value: 4.89,
  instant_bookable: false,
  calculated_host_listings_count: 1,
  calculated_host_listings_count_entire_homes: 1,
  calculated_host_listings_count_private_rooms: 0,
  calculated_host_listings_count_shared_rooms: 0,
  reviews_per_month: 0.26
}


{
  _id: ObjectId("65538a627ca98f88f68ed47a"),
  id: 107259,
  listing_url: 'https://www.airbnb.com/rooms/107259',
  scrape_id: 20230922223302,
  last_scraped: 2023-09-23T00:00:00.000Z,
  source: 'city scrape',
  name: 'Rental unit in Buenos Aires · ★4.58 · 6 bedrooms · 9 beds · 5 baths',
  description: `We have 7 bedrooms and 5 bathrooms,gourmet kitchen,great living room and bar.<br />Also three small balconies and one bigger.<br /><br /><b>The space</b><br />In an old and charming building on Corrientes Avenue, built over a hundred years ago when Tango was born.We offer this beautiful and centrally located apartment (walking distances to Teatro Colon ,Obelisco. Congreso, Main theaters of the city, restaurantes,milongas,bookstores, etc.<br />And the subway is right at the corner(Callao Station ,Line "C")<br /><br />Tango keep evolved, and that's what makes it immortal... the possibility of growth and change.<br /><br />It is called Paradise because we would like to provide for all your tango needs(including the apple, but not the snake HO!HO!).<br />Of course if You are not evolved with Tango, you can be anyway,very comfortable here, .(We have had several groups of people assisting to Congress or famous Musicians bands that were playing in Buenos Aires or just groups of family living `,
  picture_url: 'https://a0.muscache.com/pictures/822490/5bc2ab07_original.jpg',
  host_id: 555693,
  host_url: 'https://www.airbnb.com/users/show/555693',
  host_name: 'Vittoria',
  host_since: 2011-05-03T00:00:00.000Z,
  host_location: 'Montevideo, Uruguay',
  host_is_superhost: false,
  host_thumbnail_url: 'https://a0.muscache.com/im/users/555693/profile_pic/1332180142/original.jpg?aki_policy=profile_small',
  host_picture_url: 'https://a0.muscache.com/im/users/555693/profile_pic/1332180142/original.jpg?aki_policy=profile_x_medium',
  host_neighbourhood: 'Balvanera',
  host_listings_count: 2,
  host_total_listings_count: 2,
  host_verifications: "['email', 'phone']",
  host_has_profile_pic: true,
  host_identity_verified: true,
  neighbourhood_cleansed: 'Balvanera',
  latitude: -34.60514,
  longitude: -58.3957,
  property_type: 'Entire rental unit',
  room_type: 'Entire home/apt',
  accommodates: 12,
  bathrooms_text: '5 baths',
  bedrooms: 6,
  beds: 9,
  amenities: [
    'Dining table',
    'Kitchen',
    'Freezer',
    'Private hot tub',
    'Fire extinguisher',
    'Indoor fireplace',
    'Extra pillows and blankets',
    'Air conditioning',
    'Bidet',
    'Bed linens',
    'Dishwasher',
    'Coffee maker',
    'Hair dryer',
    'Cooking basics',
    'First aid kit',
    'Body soap',
    'Elevator',
    'Bathtub',
    'Dishes and silverware',
    'Laundromat nearby',
    'Washer',
    'Stove',
    'Wine glasses',
    'Paid parking off premises',
    'Pocket wifi',
    'Hot water',
    'TV with standard cable',
    'Microwave',
    'Hot water kettle',
    'Private patio or balcony',
    'Blender',
    'Dryer',
    'Essentials',
    'Host greets you',
    'Refrigerator',
    'Heating',
    'Hangers',
    'Pets allowed',
    'Oven',
    'Luggage dropoff allowed',
    'Toaster',
    'Wifi',
    'Iron',
    'Crib'
  ],
  price: '$157,512.00',
  minimum_nights: 1,
  maximum_nights: 15,
  minimum_minimum_nights: 1,
  maximum_minimum_nights: 1,
  minimum_maximum_nights: 15,
  maximum_maximum_nights: 15,
  minimum_nights_avg_ntm: 1,
  maximum_nights_avg_ntm: 15,
  has_availability: true,
  availability_30: 0,
  availability_60: 0,
  availability_90: 0,
  availability_365: 219,
  calendar_last_scraped: 2023-09-23T00:00:00.000Z,
  number_of_reviews: 38,
  number_of_reviews_ltm: 6,
  number_of_reviews_l30d: 0,
  first_review: 2012-06-18T00:00:00.000Z,
  last_review: 2023-07-23T00:00:00.000Z,
  review_scores_rating: 4.58,
  review_scores_accuracy: 4.41,
  review_scores_cleanliness: 4.24,
  review_scores_checkin: 4.79,
  review_scores_communication: 4.71,
  review_scores_location: 4.63,
  review_scores_value: 4.53,
  instant_bookable: false,
  calculated_host_listings_count: 2,
  calculated_host_listings_count_entire_homes: 2,
  calculated_host_listings_count_private_rooms: 0,
  calculated_host_listings_count_shared_rooms: 0,
  reviews_per_month: 0.28
}

{
  _id: ObjectId("65538a627ca98f88f68ed47b"),
  id: 14222,
  listing_url: 'https://www.airbnb.com/rooms/14222',
  scrape_id: 20230922223302,
  last_scraped: 2023-09-23T00:00:00.000Z,
  source: 'city scrape',
  name: 'Rental unit in Palermo/Buenos Aires · ★4.79 · 1 bedroom · 1 bed · 1 bath',
  description: 'Beautiful cozy apartment in excellent location in Palermo.1 lovely bedroom for 2 people.1 functional bathroom w/running hot water.Spacious living room facing a small patio w/plants.Fully-equipped kitchen. One extra space with a single bed (no door not a proper room just a space). Lovely and comfy! :)<br /><br /><b>The space</b><br />ONE BIG BEDROOM <br />One lovely bedroom with a balcony facing the street that accommodates 2 people comfortably. Functional bathroom with running hot water. Spacious living room facing a nice small yard with plants. Fully equipped kitchen. <br />An extra space (no door & no wardrobe) that accommodates an extra person. Ideal for a child.<br /><br />2° FLOOR BY STAIRS IN PALERMO NEIGHBORHOOD<br />You just have to climb two flight of stairs and reach home!<br /><br /><b>Guest access</b><br />LINEN, TOWELS, COFFEE, TEA & SUGAR: We provide clean towels, soap, toilet paper, linen and blankets. We also leave some coffee, sugar, tea and ingredients for you to use.',
  picture_url: 'https://a0.muscache.com/pictures/4695637/bbae8e87_original.jpg',
  host_id: 87710233,
  host_url: 'https://www.airbnb.com/users/show/87710233',
  host_name: 'María',
  host_since: 2016-08-03T00:00:00.000Z,
  host_location: 'Buenos Aires, Argentina',
  host_is_superhost: true,
  host_thumbnail_url: 'https://a0.muscache.com/im/pictures/user/dc9d9f11-1085-42b6-8125-ab00504a68b2.jpg?aki_policy=profile_small',
  host_picture_url: 'https://a0.muscache.com/im/pictures/user/dc9d9f11-1085-42b6-8125-ab00504a68b2.jpg?aki_policy=profile_x_medium',
  host_listings_count: 10,
  host_total_listings_count: 13,
  host_verifications: "['email', 'phone']",
  host_has_profile_pic: true,
  host_identity_verified: true,
  neighbourhood: 'Palermo/Buenos Aires, Autonomous City of Buenos Aires, Argentina',
  neighbourhood_cleansed: 'Palermo',
  latitude: -34.58617,
  longitude: -58.41036,
  property_type: 'Entire rental unit',
  room_type: 'Entire home/apt',
  accommodates: 2,
  bathrooms_text: '1 bath',
  bedrooms: 1,
  beds: 1,
  amenities: [
    'Kitchen',
    'Air conditioning',
    'TV',
    'Coffee maker',
    'Cooking basics',
    'Dedicated workspace',
    'Bathtub',
    'Dishes and silverware',
    'Washer',
    'Stove',
    'Paid parking off premises',
    'Room-darkening shades',
    'Long term stays allowed',
    'Hot water',
    'Microwave',
    'Private patio or balcony',
    'Essentials',
    'Host greets you',
    'Refrigerator',
    'Heating',
    'Hangers',
    'Oven',
    'Wifi',
    'Iron'
  ],
  price: '$11,928.00',
  minimum_nights: 7,
  maximum_nights: 100,
  minimum_minimum_nights: 7,
  maximum_minimum_nights: 7,
  minimum_maximum_nights: 1125,
  maximum_maximum_nights: 1125,
  minimum_nights_avg_ntm: 7,
  maximum_nights_avg_ntm: 1125,
  has_availability: true,
  availability_30: 12,
  availability_60: 42,
  availability_90: 72,
  availability_365: 162,
  calendar_last_scraped: 2023-09-23T00:00:00.000Z,
  number_of_reviews: 110,
  number_of_reviews_ltm: 12,
  number_of_reviews_l30d: 0,
  first_review: 2012-07-10T00:00:00.000Z,
  last_review: 2023-08-10T00:00:00.000Z,
  review_scores_rating: 4.79,
  review_scores_accuracy: 4.75,
  review_scores_cleanliness: 4.77,
  review_scores_checkin: 4.81,
  review_scores_communication: 4.9,
  review_scores_location: 4.89,
  review_scores_value: 4.75,
  instant_bookable: false,
  calculated_host_listings_count: 7,
  calculated_host_listings_count_entire_homes: 7,
  calculated_host_listings_count_private_rooms: 0,
  calculated_host_listings_count_shared_rooms: 0,
  reviews_per_month: 0.81
}
```





### 3. Choose two hosts (by reffering to their `host_id` values) who are superhosts (available in the `host_is_superhost` field), and show all of the listings offered by both of the two hosts.

```bash
db.listings.find(
    {$or: [
        {'host_id':75891},
        {'host_id':570921}
    ] },
    { 
        'name': 1,
        'price': 1,
        'neighborhood': 1,
        'host_name': 1,
        'host_is_superhost': 1
    }
)
```
To choose 2 hosts, I use $or and selected two random host IDs. With this parameter, the name, price, neighbourhood, host_name, and host_is_superhost results are output.

First three results:
```bash
{
  _id: ObjectId("65538a627ca98f88f68ed47f"),
  name: 'Rental unit in Buenos Aires · ★4.93 · 2 bedrooms · 2 beds · 1.5 baths',
  host_name: 'Sergio Damian',
  host_is_superhost: true,
  price: '$35,654.00'
}

{
  _id: ObjectId("65538a627ca98f88f68ed480"),
  name: 'Rental unit in Buenos Aires · ★4.78 · Studio · 1 bed · 1 bath',
  host_name: 'Emilce',
  host_is_superhost: true,
  price: '$15,401.00'
}

{
  _id: ObjectId("65538a627ca98f88f68ed482"),
  name: 'Rental unit in Buenos Aires · ★4.75 · Studio · 1 bed · 1 bath',
  host_name: 'Emilce',
  host_is_superhost: true,
  price: '$13,301.00'
}
```


4. Find all the unique host_name values.

```
db.listings.distinct('host_name')
```

 Using distinct here. Thank you distinct!

First three results:
```bash
'725 Continental Hotel',
  '7Team',
  'A.',
```

5. Find all of the places that have more than 2 beds in a neighborhood of your choice, ordered by review_scores_rating descending.

```
db.listings.find(
    {$and: [
        {'beds': {
            $gt: 2
        }},
        {'neighbourhood_cleansed': 'Recoleta'}
    ] },
    { 
        'name': 1,
        'beds': 1,
        'review_scores_rating': 1,
        'price': 1
    }
    ).sort(
        {'review_scores_rating': -1}
    )

```
I can find both parameters of Recoleta and having more than 2 beds with $and. Then, I only show the name, beds, review_scores_rating, and price. I sort the review_scores_rating in descending order for the highest rated results first.


First three results:

```bash
{
  _id: ObjectId("65538a627ca98f88f68ed51d"),
  name: 'Rental unit in Buenos Aires · 2 bedrooms · 3 beds · 1 bath',
  beds: 3,
  price: '$28,002.00',
  review_scores_rating: 5
}

 _id: ObjectId("65538a627ca98f88f68ed586"),
  name: 'Rental unit in Buenos Aires · ★5.0 · 2 bedrooms · 3 beds · 2.5 baths',
  beds: 3,
  price: '$70,005.00',
  review_scores_rating: 5

  {
  _id: ObjectId("65538a647ca98f88f68ed8cc"),
  name: 'Condo in Buenos Aires · 2 bedrooms · 3 beds · 2 baths',
  beds: 3,
  price: '$14,701.00',
  review_scores_rating: 5
}
```




6. Show the number of listings per host.

```
db.listings.aggregate(
    {$group: {
         _id: '$host_id', 
         listingCount: {$sum: 1}
        }
    }
)
```

Here I use aggregrate and $group- within each group, the sum of the number of documents is calculated, counting the number of listings for each host_id. The aggregation pipeline...

First three results:

```bash
{
  _id: 1722104,
  listingCount: 1
}
{
  _id: 49069906,
  listingCount: 13
}
{
  _id: 475361901,
  listingCount: 1
}
```


7. Find the average review_scores_rating per neighbourhood, and only show the ones above a 95, sorted in descending order of rating.

```
db.listings.aggregate(
    [
        {$match: {number_of_reviews: {$gt:95}}},
        {$group: {_id: '$neighbourhood_cleansed', avgRating: {$avg: '$review_scores_rating'}}},
        {$sort: {avgRating: -1}}
    ]
)
```
Results:

```bash
{
  _id: 'Coghlan',
  avgRating: 4.95
}

{
  _id: 'Parque Chas',
  avgRating: 4.95
}

{
  _id: 'Boedo',
  avgRating: 4.92
}
```


I use aggregate again here along with $match to fulfill the parameter of number_of_reviews over 95. I use $group to group by neighborhood. $avg gets us the average rating, which I then sort descendingly.


