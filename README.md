# Problem Set 6
### Group 9 Members:
    - Steve Bischoff
    - Andrew Yee
    - Suwat Chritamara
    - Vy Vu
    - Jack Mentch

## **Exploratory Data Analysis:** 
#### <i>all EDA is located in **eda.ipynb**</i>
- [x] neighborhoods
- [x] reviews 
- [x] listings 
- [x] calendar

<br>

## **How To Generate Database (airbnb.db):** 

#### 1. cd into the project directory
```console
cd JHUDataScienceGroup9
``` 

#### 2. generate the database schema
```console
sqlite3 airbnb.db
sqlite> .read airbnb.sql
``` 
#### 3. populate the database
```console
datawarehouse.py
``` 

<br>

## **airbnb.db** 
###### Database that contains **4 Tables**: Neighbourhoods, Calendar, Reviews, and  Listings

---


### **Neighbourhoods Table:** 
###### source data: **neightbourhoods.csv**
| id  | name |
| --- | ---- |
| 1  | Capitol Hill, Lincoln Park  |
| 2  | Douglas, Shipley Terrace  |
| 3  | Historic Anacostia  |
| ...  | ...  |

### **Calendar Table:** 
###### source data: **calendar.csv**
| id  | listing_id | date | available | price | adjusted_price | minimum_nights | maximum_nights |
| --- | ---------- | ---- | --------- | ----- | -------------- | -------------- | -------------- |
| 1  | 3686 | 3/19/2023  | t | $67.00 | $67.00 | 31 | 365 |
| 2  | 4325533 | 3/19/2023  | f | $145.00 | $145.00 | 3 | 1125 |
| 3  | 4343926 | 3/20/2023  | f | $120.00 | $120.00 | 28 | 365 |
| ...| ...  | ... | ... | ... | ... | ... | ... |

### **Reviews Table:** 
###### source data: **reviews.csv**
| id  | listing_id | date | reviewer_name | reviewer_id | comments | 
| --- | ---------- | ---- | ------------- | ----------- | -------- |
| 1  | 3686 | 3/19/2023  | Adam | 324502 | This home is beautiful, modern and spotless!  |
| 2  | 3943 | 3/20/2023  | Robert | 413351 | Great host! Very welcoming and organised. |
| 3  | 3948 | 3/21/2023  | Nelson | 628405 | Loved the neighborhood and the decoration |
| ...| ...  | ... | ... | ... | ... | ... | ... |

### **Listings Table:** </u> 
###### source data: **listings.csv**
| id  | listing_id | scrape_url | last_scraped | * | reviews_per_month | 
| --- | ---------- | ---- | --------- | ----- | -------------- | 
| 1  | 22229408 | https://www.airbnb.com/rooms/22229408  | 3/19/2023 | ... | 0.32 |  
| 2  | 46951758 | https://www.airbnb.com/rooms/46951758  | 3/23/2023 | ... | 1.87 |
| 3  | 40341225 | https://www.airbnb.com/rooms/40341225  | 3/28/2023 | ... | 1.20 | 
| ...| ...  | ... | ... | ... | ... |

<br>

---

## **Secondary Dataset:** 
#### Secondary datasets contain data related to recommended attractions, and their respective latitude longitude distances.

#### <u>Websites: </u>

- #### https://travel.usnews.com/Washington_DC/Things_To_Do/
- #### https://www.hotels.com/go/usa/things-to-do-washington-dc
- #### https://www.google.com/maps

<br>

---

## **Peer Evaluations:** 
### Author: Jack Mentch
| team member  | score | comments | 
| ------------ | ----- | -------- | 
| Steve Bischoff  | 5/5 | Steve was extremely attentive throughout the lifetime of the project. He served as the leader of the team and made major contributions to the final project. The contributions he made demonstrated a strong working knowledge of the material this class covered |
| Andrew Yee  | 5/5 | Andrew collaborated effectively with others and incorporate different perspectives into our work. He was also a huge asset, as it helped us to produce a more well-rounded and comprehensive final product. The contributions he made demonstrated a strong working knowledge of the material this class covered |  
| Suwat Chritamara  | 5/5 | Suwat helped the team with numerous contributions. He was incredibly attentive and helpful with addressing questions and problems in the team group chat. His work on this project has demonstrated a strong working knowledge of the material this class covered |  
| Vy Vu  | 5/5 | Vy was instrumental in guiding the team through each step of the project. She helped keep the team organized and made major contributions at each point along the way. Her work has demonstrated a strong understanding of the core data science fundamentals |

### Author: Steve Bischoff
| team member  | score | comments | 
| ------------ | ----- | -------- | 
| Jack Mentch  | /5 |  |
| Andrew Yee  | /5 |  |  
| Suwat Chritamara  | /5 |  |  
| Vy Vu  | /5 |  |

### Author: Andrew Yee
| team member  | score | comments | 
| ------------ | ----- | -------- | 
| Jack Mentch  | /5 |  |
| Steve Bischoff  | /5 |  |  
| Suwat Chritamara  | /5 |  |  
| Vy Vu  | /5 |  |

### Author: Suwat Chritamara
| team member  | score | comments | 
| ------------ | ----- | -------- | 
| Jack Mentch  | /5 |  |
| Steve Bischoff  | /5 |  |  
| Andrew Yee  | /5 |  |  
| Vy Vu  | /5 |  |

### Author: Vy Vu
| team member  | score | comments | 
| ------------ | ----- | -------- | 
| Jack Mentch  | /5 |  |
| Steve Bischoff  | /5 |  |  
| Andrew Yee  | /5 |  |  
| Suwat Chritamara  | /5 |  |