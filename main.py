"""
Importing necessary libraries:
"""

import pandas as pd 
import matplotlib.pyplot as plt


def linebreak():
    print("\n\n")
    
    
    def linebreak_single():
        print()



# Setting labels for y-axis of scatter plots

values = []

for i in range(0, 290 + 1, 10):
    values.append(i)
    
    y_scale = values
    
    linebreak_single()   
    
    
    # Task 1 #
    """Netflix! What started in 1997 as a DVD rental service has since exploded into the largest entertainment/media company
by market capitalization, boasting over 200 million subscribers as of January 2021. Given the large number of movies and
series available on the platform, it is a perfect opportunity to flex our data manipulation skills and dive into the
entertainment industry. Our friend has also been brushing up on their Python skills and has taken a first crack at a CSV
file containing Netflix data. For their first order of business, they have been performing some analyses, and they 
believe that the average duration of movies has been declining. As evidence of this, they have provided us with the 
following information:

For the years from 2011 to 2020, the average movie durations are 103, 101, 99, 100, 100, 95, 95,
96, 93, and 90, respectively. If we're going to be working with this data, we know a good place to start would be to 
probably start working with pandas. But first we'll need to create a dictionary from scratch and convert it to a
Pandas DataFrame!"""

# Years: 
years = list(range(2011,2021))
print("Years:",years)

# dictionary:
movie_dict = {"years": years,
              "durations": durations}
print("Movies:", movie_dict)

linebreak()


# Task 2 # 
"""
To convert our dictionary movie_dict to a pandas DataFrame, we will first need to import the library under its usual 
alias. We'll also want to inspect our DataFrame to ensure it was created correctly.
"""

durations_df = pd.DataFrame(movie_dict)
print("Durations DataFrame: \n")
print(durations_df)

linebreak()

# Task 3 #
"""
Alright, we now have a pandas DataFrame, the most common way to work with tabular data in Python. Now back to the task
at hand. We want to follow up on our friend's assertion that movie lengths have been decreasing over time. A great place
to start will be a visualization of the data. Given that the data is continuous, a line plot would be a good choice,
with the dates represented along the x-axis and the average length in minutes along the y-axis. This will allow us to
easily spot any trends in movie durations. There are many ways to visualize data in Python, but matplotlib.pyplot is one
 of the most common packages to do so.

Note: In order for us to correctly test your plot, you will need to initialize a matplotlib.pyplot Figure object. 
You can continue to create your plot as you have learned in Intermediate Python.
"""

fig = plt.figure(figsize=(10, 10))

line_plot = fig.add_subplot(111)

line_plot.plot(years, durations, label="movie length")
line_plot.scatter(years, durations)
line_plot.grid(True)
line_plot.set_title("Line Plot")
line_plot.set_xlabel("Release Years")
line_plot.set_ylabel("Durations")
line_plot.legend()

plt.title("Netflix Movie Durations 2011-2020")
plt.show()

linebreak()


# Task 4 #
"""
Well, it looks like there is something to the idea that movie lengths have decreased over the past ten years! But
equipped only with our friend's aggregations, we're limited in the further explorations we can perform. There are a few
questions about this trend that we are currently unable to answer, including:

    1. What does this trend look like over a longer period of time?
    2. Is this explainable by something like the genre of entertainment?

Upon asking our friend for the original CSV they used to perform their analyses, they gladly oblige and send it. We now 
have access to the CSV file, available at the path "datasets/netflix_data.csv". Let's create another DataFrame, this 
time with all of the data. Given the length of our friend's data, printing the whole DataFrame is probably not a good 
idea, so we will inspect it by printing only the first five rows.
"""

netflix_df = pd.read_csv("netflix_data.csv")
netflix_df = pd.DataFrame(netflix_df)
print(netflix_df.iloc[0:5])

linebreak()

# Task 5 # 
"""
Okay, we have our data! Now we can dive in and start looking at movie lengths.

Or can we? Looking at the first five rows of our new DataFrame, we notice a column type. Scanning the column, it's clear
 there are also TV shows in the dataset! Moreover, the duration column we planned to use seems to represent different 
 values depending on whether the row is a movie or a show (perhaps the number of minutes versus the number of seasons)?

Fortunately, a DataFrame allows us to filter data quickly, and we can select rows where type is Movie. While we're at 
it, we don't need information from all of the columns, so let's create a new DataFrame netflix_movies containing only 
title, country, genre, release_year, and duration.

Let's put our data subsetting skills to work!
"""
netflix_df_movies_only = netflix_df[netflix_df["type"] == "Movie"]
print(netflix_df_movies_only)

linebreak_single()

netflix_movies_col_subset = netflix_df_movies_only[["title","country","genre","release_year","duration"]]
print(netflix_movies_col_subset.iloc[0:5])

linebreak()
