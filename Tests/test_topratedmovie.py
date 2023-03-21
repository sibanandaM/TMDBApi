import pytest
import requests


class TestTopRatedMovie:
    api_key = "289278144021ecbb82d2eb430fae5722"
    url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=en-US&page=1"

    def test_topratedmovie(self):

        top_rated_movie_response = requests.get(self.url)

        status_code = top_rated_movie_response.status_code
        assert status_code == 200

        top_rated_movie_json = top_rated_movie_response.json()

        top_rated_movie_list = []
        for i in range(0, len(top_rated_movie_json['results'])):
            l = []
            l.append(top_rated_movie_json['results'][i]['title'])
            l.append(top_rated_movie_json['results'][i]['vote_average'])
            l.append(top_rated_movie_json['results'][i]['release_date'])
            top_rated_movie_list.append(l)

        for i in range(0, len(top_rated_movie_list)):
            for j in range(i + 1, len(top_rated_movie_list)):
                if top_rated_movie_list[j][2] < top_rated_movie_list[i][2]:
                    top_rated_movie_list[j], top_rated_movie_list[i] = top_rated_movie_list[i], top_rated_movie_list[j]

        for movie in top_rated_movie_list:
            print(movie)
