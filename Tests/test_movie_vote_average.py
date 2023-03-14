import pytest
import requests



class Test_MovieVoteAverage():

    compair_average = float(5.5)
    movie_id = 522444
    api_key = "289278144021ecbb82d2eb430fae5722"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"

    def test_getmoviedetails(self):

        movie_average_details_responce = requests.get(self.url)

        status_code = movie_average_details_responce.status_code
        assert status_code == 200

        movie_average_json = movie_average_details_responce.json()
        Actual_vote_average = float(movie_average_json['vote_average'])

        assert Actual_vote_average > self.compair_average , "movie vote average is less then given average value"

