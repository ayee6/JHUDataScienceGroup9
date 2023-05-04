import sqlite3

connection = sqlite3.connect('airbnb.db')
cursor = connection.cursor()

# We will create 2 views.
# The first view is the most_recent_calendar including all records with distinct listing_id and most recent date
# The second view is the most_recent_listings including all records with distinct id and most recent last scraped date

# drop_most_recent_calendar = """DROP VIEW most_recent_calendar"""
# cursor.execute(drop_most_recent_calendar)
# drop_most_recent_listings = """DROP VIEW most_recent_listings"""
# cursor.execute(drop_most_recent_listings)
# drop_airbnb_view = """DROP VIEW airbnb_view"""
# cursor.execute(drop_airbnb_view)

cursor.execute(''' CREATE VIEW most_recent_calendar AS
                SELECT DISTINCT listing_id, MAX(date), available, price, adjusted_price, minimum_nights, maximum_nights, source_name
                FROM calendar
                GROUP BY listing_id ''')


cursor.execute(''' CREATE VIEW most_recent_listings AS
                SELECT DISTINCT id, MAX(last_scraped), source_name, scrape_id, source, name, description, neighborhood_overview, \
                host_id, host_name, host_since, host_location, host_about, host_response_time, host_response_rate, \
                host_acceptance_rate, host_is_superhost, host_neighbourhood, host_listings_count, \
                host_total_listings_count, host_verifications, host_has_profile_pic, host_identity_verified, neighbourhood, \
                neighbourhood_cleansed, latitude, longitude, property_type, room_type, accommodates, \
                bathrooms, bathrooms_text, bedrooms, beds, amenities, minimum_minimum_nights, maximum_minimum_nights, \
                minimum_maximum_nights, maximum_maximum_nights, minimum_nights_avg_ntm, maximum_nights_avg_ntm, \
                has_availability, availability_30, availability_60, availability_90, availability_365, \
                calendar_last_scraped, number_of_reviews, number_of_reviews_ltm, number_of_reviews_l30d, first_review, \
                last_review, review_scores_rating, review_scores_accuracy, review_scores_cleanliness, review_scores_checkin, \
                review_scores_communication, review_scores_location, review_scores_value, license, instant_bookable, \
                calculated_host_listings_count, calculated_host_listings_count_entire_homes, \
                calculated_host_listings_count_private_rooms, calculated_host_listings_count_shared_rooms, \
                reviews_per_month, price
                FROM listings
                GROUP BY id
                ''')

connection.commit()
connection.close()

