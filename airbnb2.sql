DROP TABLE IF EXISTS listings;
CREATE TABLE listings (
    source_name STRING,
    id INTEGER,
    listing_url STRING,
    scrape_id STRING,
    last_scraped STRING,
    source STRING,
    name STRING,
    description STRING,
    neighborhood_overview STRING,
    picture_url STRING,
    host_id INTEGER,
    host_url STRING,
    host_name STRING,
    host_since STRING,
    host_location STRING,
    host_about STRING,
    host_response_time STRING,
    host_response_rate STRING,
    host_acceptance_rate STRING,
    host_is_superhost STRING,
    host_thumbnail_url STRING,
    host_picture_url STRING,
    host_neighbourhood STRING,
    host_listings_count NUMERIC,
    host_total_listings_count NUMERIC,
    host_verifications STRING,
    host_has_profile_pic STRING,
    host_identity_verified STRING,
    neighbourhood STRING,
    neighbourhood_cleansed STRING,
    neighbourhood_group_cleansed STRING,
    latitude NUMERIC,
    longitude NUMERIC,
    property_type STRING,
    room_type STRING,
    accommodates NUMERIC,
    bathrooms NUMERIC,
    bathrooms_text STRING,
    bedrooms NUMERIC,
    beds NUMERIC,
    amenities STRING,
    price STRING,
    minimum_nights NUMERIC,
    maximum_nights NUMERIC,
    minimum_minimum_nights NUMERIC,
    maximum_minimum_nights NUMERIC,
    minimum_maximum_nights NUMERIC,
    maximum_maximum_nights NUMERIC,
    minimum_nights_avg_ntm NUMERIC,
    maximum_nights_avg_ntm NUMERIC,
    calendar_updated STRING,
    has_availability STRING,
    availability_30 NUMERIC,
    availability_60 NUMERIC,
    availability_90 NUMERIC,
    availability_365 NUMERIC,
    calendar_last_scraped STRING,
    number_of_reviews NUMERIC,
    number_of_reviews_ltm NUMERIC,
    number_of_reviews_l30d NUMERIC,
    first_review STRING,
    last_review STRING,
    review_scores_rating NUMERIC,
    review_scores_accuracy NUMERIC,
    review_scores_cleanliness NUMERIC,
    review_scores_checkin NUMERIC,
    review_scores_communication NUMERIC,
    review_scores_location NUMERIC,
    review_scores_value NUMERIC,
    license STRING,
    instant_bookable STRING,
    calculated_host_listings_count NUMERIC,
    calculated_host_listings_count_entire_homes NUMERIC,
    calculated_host_listings_count_private_rooms NUMERIC,
    calculated_host_listings_count_shared_rooms NUMERIC,
    reviews_per_month NUMERIC
);

DROP TABLE IF EXISTS host;
CREATE TABLE host (
    id INTEGER PRIMARY KEY,
    host_name STRING
);

DROP TABLE IF EXISTS reviews;
CREATE TABLE reviews (
    source_name STRING,
    id INTEGER,
    reviewer_name STRING,
    reviewer_id STRING,
    date STRING,
    comments STRING,
    listing_id INTEGER
);

DROP TABLE IF EXISTS neighborhoods;
CREATE TABLE neighborhoods (
    id INTEGER PRIMARY KEY,
    name STRING
);

DROP TABLE IF EXISTS calendar;
CREATE TABLE calendar (
    source_name STRING,
    listing_id STRING,
    date STRING,
    available STRING,
    price STRING,
    adjusted_price STRING,
    minimum_nights INTEGER,
    maximum_nights INTEGER
);