import csv
import sqlite3

connection = sqlite3.connect('airbnb.db')
cursor = connection.cursor()


# Load neighborhoods file
with open('datasets/neighbourhoods.csv', 'r', encoding='utf-8') as file:
    csvfile = csv.reader(file)
    for row in csvfile:
        name = row[1]
        cursor.execute('INSERT INTO neighborhoods (name) VALUES (?)', (name,))
file.close()


# Load reviews in Mar 2023
with open('datasets/reviews_3_2023.csv', 'r', encoding='utf-8') as file:
    csvfile = csv.reader(file)
    header = next(csvfile)
    for row in csvfile:
        cursor.execute('INSERT INTO reviews VALUES(:source_name, :listing_id, :id, :date, :reviewer_id, :reviewer_name, :comments)',\
                        {'source_name': 'reviews_3_2023', 'listing_id': row[0], 'id': row[1], 'date': row[2], 'reviewer_id': row[3], 'reviewer_name': row[4], 'comments': row[5]})
file.close()


# Load reviews in Dec 2022
with open('datasets/reviews_12_2022.csv', 'r', encoding='utf-8') as file:
    csvfile = csv.reader(file)
    header = next(csvfile)
    for row in csvfile:
        cursor.execute('INSERT INTO reviews VALUES(:source_name, :listing_id, :id, :date, :reviewer_id, :reviewer_name, :comments)',\
                        {'source_name': 'reviews_12_2022', 'listing_id': row[0], 'id': row[1], 'date': row[2], 'reviewer_id': row[3], 'reviewer_name': row[4], 'comments': row[5]})
file.close()


# Load reviews in Sep 2022
with open('datasets/reviews_9_2022.csv', 'r', encoding='utf-8') as file:
    csvfile = csv.reader(file)
    header = next(csvfile)
    for row in csvfile:
        cursor.execute('INSERT INTO reviews VALUES(:source_name, :listing_id, :id, :date, :reviewer_id, :reviewer_name, :comments)',\
                        {'source_name': 'reviews_9_2022', 'listing_id': row[0], 'id': row[1], 'date': row[2], 'reviewer_id': row[3], 'reviewer_name': row[4], 'comments': row[5]})
file.close()


# Load reviews in Jun 2022
with open('datasets/reviews_6_2022.csv', 'r', encoding='utf-8') as file:
    csvfile = csv.reader(file)
    header = next(csvfile)
    for row in csvfile:
        cursor.execute('INSERT INTO reviews VALUES(:source_name, :listing_id, :id, :date, :reviewer_id, :reviewer_name, :comments)',\
                        {'source_name': 'reviews_6_2022', 'listing_id': row[0], 'id': row[1], 'date': row[2], 'reviewer_id': row[3], 'reviewer_name': row[4], 'comments': row[5]})
file.close()


# # Load calendar in Mar 2023
with open('datasets/calendar_3_2023.csv', 'r', encoding='utf-8') as file:
    csvfile = csv.reader(file)
    header = next(csvfile)
    for row in csvfile:
        cursor.execute('INSERT INTO calendar VALUES(:source_name, :listing_id, :date, :available, :price, :adjusted_price, :minimum_nights, :maximum_nights)',\
                        {'source_name': 'calendar_3_2023', 'listing_id': row[0], 'date': row[1], 'available': row[2], 'price': row[3], \
                         'adjusted_price': row[4], 'minimum_nights': row[5], 'maximum_nights': row[6]})
file.close()


# Load calendar in Dec 2022
with open('datasets/calendar_12_2022.csv', 'r', encoding='utf-8') as file:
    csvfile = csv.reader(file)
    header = next(csvfile)
    for row in csvfile:
        cursor.execute('INSERT INTO calendar VALUES(:source_name, :listing_id, :date, :available, :price, :adjusted_price, :minimum_nights, :maximum_nights)',\
                        {'source_name': 'calendar_12_2022', 'listing_id': row[0], 'date': row[1], 'available': row[2], 'price': row[3], \
                         'adjusted_price': row[4], 'minimum_nights': row[5], 'maximum_nights': row[6]})
file.close()


# Load calendar in Sep 2022
with open('datasets/calendar_9_2022.csv', 'r', encoding='utf-8') as file:
    csvfile = csv.reader(file)
    header = next(csvfile)
    for row in csvfile:
        cursor.execute('INSERT INTO calendar VALUES(:source_name, :listing_id, :date, :available, :price, :adjusted_price, :minimum_nights, :maximum_nights)',\
                        {'source_name': 'calendar_9_2022', 'listing_id': row[0], 'date': row[1], 'available': row[2], 'price': row[3], \
                         'adjusted_price': row[4], 'minimum_nights': row[5], 'maximum_nights': row[6]})
file.close()


# Load calendar in Jun 2022
with open('datasets/calendar_6_2022.csv', 'r', encoding='utf-8') as file:
    csvfile = csv.reader(file)
    header = next(csvfile)
    for row in csvfile:
        cursor.execute('INSERT INTO calendar VALUES(:source_name, :listing_id, :date, :available, :price, :adjusted_price, :minimum_nights, :maximum_nights)',\
                        {'source_name': 'calendar_6_2022', 'listing_id': row[0], 'date': row[1], 'available': row[2], 'price': row[3], \
                         'adjusted_price': row[4], 'minimum_nights': row[5], 'maximum_nights': row[6]})
file.close()


# Load listings in Mar 2023
with open('datasets/listings_3_2023.csv', 'r', encoding='utf-8') as file:
    csvfile = csv.reader(file)
    header = next(csvfile)
    for row in csvfile:
        cursor.execute('INSERT INTO listings VALUES(:source_name, :id, :listing_url, :scrape_id, :last_scraped, :source, :name, :description, :neighborhood_overview, \
                       :picture_url, :host_id, :host_url, :host_name, :host_since, :host_location, :host_about, :host_response_time, :host_response_rate, \
                       :host_acceptance_rate, :host_is_superhost, :host_thumbnail_url, :host_picture_url, :host_neighbourhood, :host_listings_count,\
                       :host_total_listings_count, :host_verifications, :host_has_profile_pic, :host_identity_verified, :neighbourhood, :neighbourhood_cleansed, \
                       :neighbourhood_group_cleansed, :latitude, :longitude, :property_type, :room_type, :accommodates,	:bathrooms, :bathrooms_text, :bedrooms, \
                       :beds, :amenities, :price, :minimum_nights, :maximum_nights, :minimum_minimum_nights, :maximum_minimum_nights, :minimum_maximum_nights, \
                       :maximum_maximum_nights, :minimum_nights_avg_ntm, :maximum_nights_avg_nt, :calendar_updated, :has_availability, :availability_30, \
                       :availability_60, :availability_90, :availability_365, :calendar_last_scraped, :number_of_reviews, :number_of_reviews_ltm, :number_of_reviews_l30d, \
                       :first_review, :last_review, :review_scores_rating, :review_scores_accuracy, :review_scores_cleanliness, :review_scores_checkin, \
                       :review_scores_communication, :review_scores_location, :review_scores_value, :license, :instant_bookable, :calculated_host_listings_count, \
                       :calculated_host_listings_count_entire_homes, :calculated_host_listings_count_private_rooms, :calculated_host_listings_count_shared_rooms, \
                       :reviews_per_month)',\
                        {'source_name': 'listings_3_2023', 'id': row[0], 'listing_url': row[1], 'scrape_id': row[2], 'last_scraped': row[3], 'source': row[4], 'name': row[5], \
                        'description': row[6], 'neighborhood_overview': row[7], 'picture_url': row[8], 'host_id': row[9], 'host_url': row[10], 'host_name': row[11], \
                        'host_since': row[12], 'host_location': row[13], 'host_about': row[14], 'host_response_time': row[15], 'host_response_rate': row[16], \
                        'host_acceptance_rate': row[17], 'host_is_superhost': row[18], 'host_thumbnail_url': row[19], 'host_picture_url': row[20], 'host_neighbourhood': row[21], \
                        'host_listings_count': row[22], 'host_total_listings_count': row[23], 'host_verifications': row[24], 'host_has_profile_pic': row[25], \
                        'host_identity_verified': row[26], 'neighbourhood': row[27], 'neighbourhood_cleansed': row[28], 'neighbourhood_group_cleansed': row[29], \
                        'latitude': row[30], 'longitude': row[31], 'property_type': row[32], 'room_type': row[33], 'accommodates': row[34], 'bathrooms': row[35], \
                        'bathrooms_text': row[36], 'bedrooms': row[37], 'beds': row[38], 'amenities': row[39], 'price': row[40], 'minimum_nights': row[41], \
                        'maximum_nights': row[42], 'minimum_minimum_nights': row[43], 'maximum_minimum_nights': row[44], 'minimum_maximum_nights': row[45], \
                        'maximum_maximum_nights': row[46], 'minimum_nights_avg_ntm': row[47], 'maximum_nights_avg_nt': row[48], 'calendar_updated': row[49], \
                        'has_availability': row[50], 'availability_30': row[51], 'availability_60': row[52], 'availability_90': row[53], 'availability_365': row[54], \
                        'calendar_last_scraped': row[55], 'number_of_reviews': row[56], 'number_of_reviews_ltm': row[57], 'number_of_reviews_l30d': row[58], \
                        'first_review': row[59], 'last_review': row[60], 'review_scores_rating': row[61], 'review_scores_accuracy': row[62], 'review_scores_cleanliness': row[63], \
                        'review_scores_checkin': row[64], 'review_scores_communication': row[65], 'review_scores_location': row[66], 'review_scores_value': row[67], \
                        'license': row[68], 'instant_bookable': row[69], 'calculated_host_listings_count': row[70], 'calculated_host_listings_count_entire_homes': row[71], \
                        'calculated_host_listings_count_private_rooms': row[72], 'calculated_host_listings_count_shared_rooms': row[73], 'reviews_per_month': row[74]})
file.close()


# Load listings in Dec 2022
with open('datasets/listings_12_2022.csv', 'r', encoding='utf-8') as file:
    csvfile = csv.reader(file)
    header = next(csvfile)
    for row in csvfile:
        cursor.execute('INSERT INTO listings VALUES(:source_name, :id, :listing_url, :scrape_id, :last_scraped, :source, :name, :description, :neighborhood_overview, \
                       :picture_url, :host_id, :host_url, :host_name, :host_since, :host_location, :host_about, :host_response_time, :host_response_rate, \
                       :host_acceptance_rate, :host_is_superhost, :host_thumbnail_url, :host_picture_url, :host_neighbourhood, :host_listings_count,\
                       :host_total_listings_count, :host_verifications, :host_has_profile_pic, :host_identity_verified, :neighbourhood, :neighbourhood_cleansed, \
                       :neighbourhood_group_cleansed, :latitude, :longitude, :property_type, :room_type, :accommodates,	:bathrooms, :bathrooms_text, :bedrooms, \
                       :beds, :amenities, :price, :minimum_nights, :maximum_nights, :minimum_minimum_nights, :maximum_minimum_nights, :minimum_maximum_nights, \
                       :maximum_maximum_nights, :minimum_nights_avg_ntm, :maximum_nights_avg_nt, :calendar_updated, :has_availability, :availability_30, \
                       :availability_60, :availability_90, :availability_365, :calendar_last_scraped, :number_of_reviews, :number_of_reviews_ltm, :number_of_reviews_l30d, \
                       :first_review, :last_review, :review_scores_rating, :review_scores_accuracy, :review_scores_cleanliness, :review_scores_checkin, \
                       :review_scores_communication, :review_scores_location, :review_scores_value, :license, :instant_bookable, :calculated_host_listings_count, \
                       :calculated_host_listings_count_entire_homes, :calculated_host_listings_count_private_rooms, :calculated_host_listings_count_shared_rooms, \
                       :reviews_per_month)',\
                        {'source_name': 'listings_12_2022', 'id': row[0], 'listing_url': row[1], 'scrape_id': row[2], 'last_scraped': row[3], 'source': row[4], 'name': row[5], \
                        'description': row[6], 'neighborhood_overview': row[7], 'picture_url': row[8], 'host_id': row[9], 'host_url': row[10], 'host_name': row[11], \
                        'host_since': row[12], 'host_location': row[13], 'host_about': row[14], 'host_response_time': row[15], 'host_response_rate': row[16], \
                        'host_acceptance_rate': row[17], 'host_is_superhost': row[18], 'host_thumbnail_url': row[19], 'host_picture_url': row[20], 'host_neighbourhood': row[21], \
                        'host_listings_count': row[22], 'host_total_listings_count': row[23], 'host_verifications': row[24], 'host_has_profile_pic': row[25], \
                        'host_identity_verified': row[26], 'neighbourhood': row[27], 'neighbourhood_cleansed': row[28], 'neighbourhood_group_cleansed': row[29], \
                        'latitude': row[30], 'longitude': row[31], 'property_type': row[32], 'room_type': row[33], 'accommodates': row[34], 'bathrooms': row[35], \
                        'bathrooms_text': row[36], 'bedrooms': row[37], 'beds': row[38], 'amenities': row[39], 'price': row[40], 'minimum_nights': row[41], \
                        'maximum_nights': row[42], 'minimum_minimum_nights': row[43], 'maximum_minimum_nights': row[44], 'minimum_maximum_nights': row[45], \
                        'maximum_maximum_nights': row[46], 'minimum_nights_avg_ntm': row[47], 'maximum_nights_avg_nt': row[48], 'calendar_updated': row[49], \
                        'has_availability': row[50], 'availability_30': row[51], 'availability_60': row[52], 'availability_90': row[53], 'availability_365': row[54], \
                        'calendar_last_scraped': row[55], 'number_of_reviews': row[56], 'number_of_reviews_ltm': row[57], 'number_of_reviews_l30d': row[58], \
                        'first_review': row[59], 'last_review': row[60], 'review_scores_rating': row[61], 'review_scores_accuracy': row[62], 'review_scores_cleanliness': row[63], \
                        'review_scores_checkin': row[64], 'review_scores_communication': row[65], 'review_scores_location': row[66], 'review_scores_value': row[67], \
                        'license': row[68], 'instant_bookable': row[69], 'calculated_host_listings_count': row[70], 'calculated_host_listings_count_entire_homes': row[71], \
                        'calculated_host_listings_count_private_rooms': row[72], 'calculated_host_listings_count_shared_rooms': row[73], 'reviews_per_month': row[74]})
file.close()


# Load listings in Sep 2022
with open('datasets/listings_9_2022.csv', 'r', encoding='utf-8') as file:
    csvfile = csv.reader(file)
    header = next(csvfile)
    for row in csvfile:
        cursor.execute('INSERT INTO listings VALUES(:source_name, :id, :listing_url, :scrape_id, :last_scraped, :source, :name, :description, :neighborhood_overview, \
                       :picture_url, :host_id, :host_url, :host_name, :host_since, :host_location, :host_about, :host_response_time, :host_response_rate, \
                       :host_acceptance_rate, :host_is_superhost, :host_thumbnail_url, :host_picture_url, :host_neighbourhood, :host_listings_count,\
                       :host_total_listings_count, :host_verifications, :host_has_profile_pic, :host_identity_verified, :neighbourhood, :neighbourhood_cleansed, \
                       :neighbourhood_group_cleansed, :latitude, :longitude, :property_type, :room_type, :accommodates,	:bathrooms, :bathrooms_text, :bedrooms, \
                       :beds, :amenities, :price, :minimum_nights, :maximum_nights, :minimum_minimum_nights, :maximum_minimum_nights, :minimum_maximum_nights, \
                       :maximum_maximum_nights, :minimum_nights_avg_ntm, :maximum_nights_avg_nt, :calendar_updated, :has_availability, :availability_30, \
                       :availability_60, :availability_90, :availability_365, :calendar_last_scraped, :number_of_reviews, :number_of_reviews_ltm, :number_of_reviews_l30d, \
                       :first_review, :last_review, :review_scores_rating, :review_scores_accuracy, :review_scores_cleanliness, :review_scores_checkin, \
                       :review_scores_communication, :review_scores_location, :review_scores_value, :license, :instant_bookable, :calculated_host_listings_count, \
                       :calculated_host_listings_count_entire_homes, :calculated_host_listings_count_private_rooms, :calculated_host_listings_count_shared_rooms, \
                       :reviews_per_month)',\
                        {'source_name': 'listings_9_2022', 'id': row[0], 'listing_url': row[1], 'scrape_id': row[2], 'last_scraped': row[3], 'source': row[4], 'name': row[5], \
                        'description': row[6], 'neighborhood_overview': row[7], 'picture_url': row[8], 'host_id': row[9], 'host_url': row[10], 'host_name': row[11], \
                        'host_since': row[12], 'host_location': row[13], 'host_about': row[14], 'host_response_time': row[15], 'host_response_rate': row[16], \
                        'host_acceptance_rate': row[17], 'host_is_superhost': row[18], 'host_thumbnail_url': row[19], 'host_picture_url': row[20], 'host_neighbourhood': row[21], \
                        'host_listings_count': row[22], 'host_total_listings_count': row[23], 'host_verifications': row[24], 'host_has_profile_pic': row[25], \
                        'host_identity_verified': row[26], 'neighbourhood': row[27], 'neighbourhood_cleansed': row[28], 'neighbourhood_group_cleansed': row[29], \
                        'latitude': row[30], 'longitude': row[31], 'property_type': row[32], 'room_type': row[33], 'accommodates': row[34], 'bathrooms': row[35], \
                        'bathrooms_text': row[36], 'bedrooms': row[37], 'beds': row[38], 'amenities': row[39], 'price': row[40], 'minimum_nights': row[41], \
                        'maximum_nights': row[42], 'minimum_minimum_nights': row[43], 'maximum_minimum_nights': row[44], 'minimum_maximum_nights': row[45], \
                        'maximum_maximum_nights': row[46], 'minimum_nights_avg_ntm': row[47], 'maximum_nights_avg_nt': row[48], 'calendar_updated': row[49], \
                        'has_availability': row[50], 'availability_30': row[51], 'availability_60': row[52], 'availability_90': row[53], 'availability_365': row[54], \
                        'calendar_last_scraped': row[55], 'number_of_reviews': row[56], 'number_of_reviews_ltm': row[57], 'number_of_reviews_l30d': row[58], \
                        'first_review': row[59], 'last_review': row[60], 'review_scores_rating': row[61], 'review_scores_accuracy': row[62], 'review_scores_cleanliness': row[63], \
                        'review_scores_checkin': row[64], 'review_scores_communication': row[65], 'review_scores_location': row[66], 'review_scores_value': row[67], \
                        'license': row[68], 'instant_bookable': row[69], 'calculated_host_listings_count': row[70], 'calculated_host_listings_count_entire_homes': row[71], \
                        'calculated_host_listings_count_private_rooms': row[72], 'calculated_host_listings_count_shared_rooms': row[73], 'reviews_per_month': row[74]})
file.close()


# Load listings in Jun 2022
with open('datasets/listings_6_2022.csv', 'r', encoding='utf-8') as file:
    csvfile = csv.reader(file)
    header = next(csvfile)
    for row in csvfile:
        cursor.execute('INSERT INTO listings VALUES(:source_name, :id, :listing_url, :scrape_id, :last_scraped, :source, :name, :description, :neighborhood_overview, \
                       :picture_url, :host_id, :host_url, :host_name, :host_since, :host_location, :host_about, :host_response_time, :host_response_rate, \
                       :host_acceptance_rate, :host_is_superhost, :host_thumbnail_url, :host_picture_url, :host_neighbourhood, :host_listings_count,\
                       :host_total_listings_count, :host_verifications, :host_has_profile_pic, :host_identity_verified, :neighbourhood, :neighbourhood_cleansed, \
                       :neighbourhood_group_cleansed, :latitude, :longitude, :property_type, :room_type, :accommodates,	:bathrooms, :bathrooms_text, :bedrooms, \
                       :beds, :amenities, :price, :minimum_nights, :maximum_nights, :minimum_minimum_nights, :maximum_minimum_nights, :minimum_maximum_nights, \
                       :maximum_maximum_nights, :minimum_nights_avg_ntm, :maximum_nights_avg_nt, :calendar_updated, :has_availability, :availability_30, \
                       :availability_60, :availability_90, :availability_365, :calendar_last_scraped, :number_of_reviews, :number_of_reviews_ltm, :number_of_reviews_l30d, \
                       :first_review, :last_review, :review_scores_rating, :review_scores_accuracy, :review_scores_cleanliness, :review_scores_checkin, \
                       :review_scores_communication, :review_scores_location, :review_scores_value, :license, :instant_bookable, :calculated_host_listings_count, \
                       :calculated_host_listings_count_entire_homes, :calculated_host_listings_count_private_rooms, :calculated_host_listings_count_shared_rooms, \
                       :reviews_per_month)',\
                        {'source_name': 'listings_6_2022', 'id': row[0], 'listing_url': row[1], 'scrape_id': row[2], 'last_scraped': row[3], 'source': 'NA', 'name': row[4], \
                        'description': row[5], 'neighborhood_overview': row[6], 'picture_url': row[7], 'host_id': row[8], 'host_url': row[9], 'host_name': row[10], \
                        'host_since': row[11], 'host_location': row[12], 'host_about': row[13], 'host_response_time': row[14], 'host_response_rate': row[15], \
                        'host_acceptance_rate': row[16], 'host_is_superhost': row[17], 'host_thumbnail_url': row[18], 'host_picture_url': row[19], 'host_neighbourhood': row[20], \
                        'host_listings_count': row[21], 'host_total_listings_count': row[22], 'host_verifications': row[23], 'host_has_profile_pic': row[24], \
                        'host_identity_verified': row[25], 'neighbourhood': row[26], 'neighbourhood_cleansed': row[27], 'neighbourhood_group_cleansed': row[28], \
                        'latitude': row[29], 'longitude': row[30], 'property_type': row[31], 'room_type': row[32], 'accommodates': row[33], 'bathrooms': row[34], \
                        'bathrooms_text': row[35], 'bedrooms': row[36], 'beds': row[37], 'amenities': row[38], 'price': row[39], 'minimum_nights': row[40], \
                        'maximum_nights': row[41], 'minimum_minimum_nights': row[42], 'maximum_minimum_nights': row[43], 'minimum_maximum_nights': row[44], \
                        'maximum_maximum_nights': row[45], 'minimum_nights_avg_ntm': row[46], 'maximum_nights_avg_nt': row[47], 'calendar_updated': row[48], \
                        'has_availability': row[49], 'availability_30': row[50], 'availability_60': row[51], 'availability_90': row[52], 'availability_365': row[53], \
                        'calendar_last_scraped': row[54], 'number_of_reviews': row[55], 'number_of_reviews_ltm': row[56], 'number_of_reviews_l30d': row[57], \
                        'first_review': row[58], 'last_review': row[59], 'review_scores_rating': row[60], 'review_scores_accuracy': row[61], 'review_scores_cleanliness': row[62], \
                        'review_scores_checkin': row[63], 'review_scores_communication': row[64], 'review_scores_location': row[65], 'review_scores_value': row[66], \
                        'license': row[67], 'instant_bookable': row[69], 'calculated_host_listings_count': row[69], 'calculated_host_listings_count_entire_homes': row[70], \
                        'calculated_host_listings_count_private_rooms': row[71], 'calculated_host_listings_count_shared_rooms': row[72], 'reviews_per_month': row[73]})
file.close()

connection.commit()
connection.close()
