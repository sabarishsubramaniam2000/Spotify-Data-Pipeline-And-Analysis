# Spotify Data Pipeline and Analysis

<img width="854" alt="Data Pipeline" src="https://github.com/sabarishsubramaniam2000/Spotify-Data-Pipeline-And-Analysis/assets/84472301/2ece16cb-c403-470d-85ad-890cf1032414">

The Spotify Data Pipeline and Analysis project is an end-to-end implementation that demonstrates the integration of various AWS services to store, transform, and analyze data, resulting in the creation of an insightful dashboard using Tableau. This project follows a systematic workflow, leveraging AWS's powerful data management and analytical tools to process and visualize Spotify data.

## Main Steps

1. **Data Storage**: The raw Spotify dataset is initially stored in an Amazon S3 bucket, serving as the staging area for the data.

2. **Data Transformation**: AWS Glue ETL is employed to perform necessary data transformations. This involves cleaning, enriching, and structuring the data to make it suitable for analysis. The transformed data is then stored in another S3 bucket, which acts as the data warehouse.

3. **Data Cataloging**: An AWS Glue Crawler is used to scan the transformed data in the S3 data warehouse. This process creates a database and populates a table in the AWS Glue Data Catalog, making the data easily accessible for querying.

4. **Data Querying**: AWS Athena is utilized to query the data table created by the Glue Crawler. Athena allows for efficient SQL queries directly on the data stored in S3, enabling flexible and powerful data exploration.

5. **Data Visualization**: Finally, the data queried through AWS Athena is connected to Tableau. Tableau is then used to create detailed and interactive visualizations, helping to derive insights and trends from the Spotify data.

## Tableau Dashboard

<img width="880" alt="Spotify Tableau Dashboard" src="https://github.com/sabarishsubramaniam2000/Spotify-Data-Pipeline-And-Analysis/assets/84472301/2b3ba5db-8ec5-48e9-8144-12b3b5bad222">

The dashboard presents a concise overview of Spotify data insights, encompassing key aspects of artist popularity and music genre trends. It features the top 10 artists, showcasing their popularity metrics and followers. Additionally, it ranks the top 15 genres by their popularity on Spotify, providing insight into listener preferences. The dashboard also compares the prevalence of explicit and non-explicit songs and explores the relationship between artist popularity and follower count. Lastly, it highlights the top 10 genres with the highest number of songs available, offering a glimpse into the breadth of musical content within each genre. Overall, the dashboard provides a comprehensive snapshot of music consumption patterns and trends on Spotify.

## Dataset

The dataset used for this project can be found on Kaggle: [Spotify Dataset 2023](https://www.kaggle.com/datasets/tonygordonjr/spotify-dataset-2023).
