#With this script we will scrape data from SofaScore.com and save it in a csv file
#We will data from seasons 2011-2021 of the top 4 European leagues (Premier League, La Liga, Serie A, Bundesliga)
#This script requires the soccerdata package to be installed. You can install it by running the following command:
#pip install soccerdata

#Here we import the necessary libraries
import soccerdata as sd
import pandas as pd
import time

#Here we define some auxiliary functions
def points_home(row: pd.Series) -> int:
    """
    This function returns the points obtained by a Home Team in a Football Match.

    Args:
    row (pd.Series): A row of a pandas DataFrame.

    Returns:
    int: The points obtained by the Home Team in the match.
    """
    #If the Home Team won the match, it gets 3 points
    if row["home_score"] > row["away_score"]:
        return 3
    #If the match ended in a draw, both teams get 1 point
    elif row["home_score"] == row["away_score"]:
        return 1
    #If the Home Team lost the match, it gets 0 points
    else:
        return 0
    
def goal_difference_home(row: pd.Series) -> int:
    """
    This function returns the goal difference of the Home Team in a Football Match.

    Args:
    row (pd.Series): A row of a pandas DataFrame.

    Returns:
    int: The goal difference of the Home Team in the match.
    """
    #The goal difference is the difference between the goals scored by the Home Team and the goals scored by the Away Team
    return row["home_score"] - row["away_score"]

#Now we run the main code
if __name__ == "__main__":

    #First we need to define the leagues and seasons we want to scrape
    leagues = ['ESP-La Liga', 'ENG-Premier League', 'ITA-Serie A', 'GER-Bundesliga']
    seasons = ['2011/2012','2012/2013','2013/2014','2014/2015','2015/2016','2016/2017','2017/2018','2018/2019','2019/2020','2020/2021']

    #Now we create an instance of the SofaScore class with the leagues and seasons we defined
    sofascore = sd.Sofascore(leagues, seasons)

    #We can now scrape the data and will obtain a pandas DataFrame with the data
    print("Scraping data from SofaScore.com...")
    start_time = time.time()
    leagues_results = sofascore.read_schedule()
    end_time = time.time()
    print(f"Data scraped in {end_time - start_time} seconds.")

    #Now we can clean the dataset and save it in a csv file
    #First we will reset the index to avoid problems with the csv file
    leagues_results = leagues_results.reset_index()
    #Now we will drop unnecessary columns
    columns_to_drop = ["game", "round", "week", "date", "game_id"]
    leagues_results = leagues_results.drop(columns=columns_to_drop)
    
    #Here we create two new columns with the points and the goal difference of the home team
    leagues_results["points_home"] = leagues_results.apply(points_home, axis=1)
    leagues_results["goal_difference_home"] = leagues_results.apply(goal_difference_home, axis=1)

    #Finally we save the dataset in a csv file
    leagues_results.to_csv("leagues_results.csv", index=False)
