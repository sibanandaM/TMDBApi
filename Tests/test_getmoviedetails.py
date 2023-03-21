import pytest
import requests


class TestGetMovieDetails():
    movie_id = 522444
    api_key = "289278144021ecbb82d2eb430fae5722"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"

    def test_getmoviedetails(self):
        movie_details_response = requests.get(self.url)

        status_code = movie_details_response.status_code
        assert status_code == 200

        get_json = movie_details_response.json()

        movie_title = get_json['title']
        movie_tag = get_json['tagline']
        release_status = get_json['status']
        vote_average = get_json['vote_average']
        vote_count = get_json['vote_count']
        release_date = get_json['release_date']
        movie_language = get_json['spoken_languages'][0]['english_name']

        print("movie title name is :", movie_title)
        print("movie tag name is :", movie_tag)
        print("movie release status is :", release_status)
        print("movie vote average is :", vote_average)
        print("movie vote count is :", vote_count)
        print("movie release date is :", release_date)
        print("movie language is :", movie_language)
