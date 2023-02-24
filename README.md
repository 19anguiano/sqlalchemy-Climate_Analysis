# sqlalchemy-Climate_Analysis

![images](https://user-images.githubusercontent.com/119361768/221124331-93435fc8-6897-4c63-b9d3-b68f4a64cb1f.jpg)

# Prompt
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.


# Part 1: Analyze and Explore the Climate Data
In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib.

## Precipitation Analysis
1. Find the most recent date in the dataset.
2. Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
3. Select only the "date" and "prcp" values.
4. Load the query results into a Pandas DataFrame, and set the index to the "date" column.
5. Sort the DataFrame values by "date".
6. Plot the results by using the DataFrame plot method
![download](https://user-images.githubusercontent.com/119361768/221122400-118c9750-ca6e-42e3-9373-622cfdddbb11.png)

7. Use Pandas to print the summary statistics for the precipitation data.

![summary-stats](https://user-images.githubusercontent.com/119361768/221122770-4ca745fc-b985-4346-8627-14717a6ac15d.png)

## Station Analysis
1. Design a query to calculate the total number of stations in the dataset.
2. Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:
  - List the stations and observation counts in descending order.
  - Answer the following question: which station id has the greatest number of observations?
3. Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
4. Design a query to get the previous 12 months of temperature observation (TOBS) data. 

![download](https://user-images.githubusercontent.com/119361768/221123153-33c8ff93-947f-4040-89d6-be8eaa1d3165.png)


# Part 2: Design Your Climate App
![app](https://user-images.githubusercontent.com/119361768/221123699-93560856-259e-42ef-a823-fa2854f6f2a8.png)
