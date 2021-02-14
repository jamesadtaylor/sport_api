#!/usr/bin/env python
"""test class"""
import unittest
import mock
import requests
from flask import json
from requests import Response
from requests.exceptions import HTTPError
from sports.config import URL_LAST_FIVE_RESULTS
from sports.main import transform_response


def internet_query(query: str) -> Response:
    """creates test http response"""
    url = URL_LAST_FIVE_RESULTS
    params = {'id': query}
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp


class TestRequestsCall(unittest.TestCase):
    """
    example text that mocks requests.get and
    returns a mock Response object
    """

    def _mock_response(
            self,
            status=200,
            content="CONTENT",
            json_data=None,
            raise_for_status=None):

        mock_resp = mock.Mock()
        # mock raise_for_status call w/optional error
        mock_resp.raise_for_status = mock.Mock()
        if raise_for_status:
            mock_resp.raise_for_status.side_effect = raise_for_status
        # set status code and content
        mock_resp.status_code = status
        mock_resp.content = content
        # add json data if provided
        if json_data:
            mock_resp.json = mock.Mock(
                return_value=json_data
            )
        return mock_resp

    @mock.patch('requests.get')
    def test_internet_query(self, mock_get):
        """test query method """

        _json = '{"results":[{"dateEvent":"2021-02-08","dateEventLocal":"2021-02-08",' \
                '"idAPIfootball":"592364","idAwayTeam":"133632","idEvent":"1032915",' \
                '"idHomeTeam":"133635",' \
                '"idLeague":"4328","idSoccerXML":null,"intAwayScore":"0",' \
                '"intAwayShots":null,' \
                '"intHomeScore":"2","intHomeShots":null,"intRound":"23",' \
                '"intSpectators":null,' \
                '"strAwayFormation":null,"strAwayGoalDetails":"","strAwayLineupDefense":null,' \
                '"strAwayLineupForward":null,"strAwayLineupGoalkeeper":null,' \
                '"strAwayLineupMidfield":null,' \
                '"strAwayLineupSubstitutes":null,"strAwayRedCards":null,' \
                '"strAwayTeam":"Crystal Palace",' \
                '"strAwayYellowCards":null,"strBanner":null,"strCity":"",' \
                '"strCountry":"England",' \
                '"strDate":null,"strDescriptionEN":"","strEvent":"Leeds vs Crystal Palace",' \
                '"strEventAlternate":"Crystal Palace @ Leeds","strFanart":null,' \
                '"strFilename":"English ' \
                'Premier League 2021-02-08 Leeds vs Crystal Palace","strHomeFormation":null,' \
                '"strHomeGoalDetails":"","strHomeLineupDefense":null,' \
                '"strHomeLineupForward":null,' \
                '"strHomeLineupGoalkeeper":null,"strHomeLineupMidfield":null,' \
                '"strHomeLineupSubstitutes":null,"strHomeRedCards":null,"strHomeTeam":"Leeds",' \
                '"strHomeYellowCards":null,"strLeague":"English Premier League",' \
                '"strLocked":"unlocked",' \
                '"strMap":null,"strOfficial":"","strPoster":null,"strPostponed":"no",' \
                '"strResult":"",' \
                '"strSeason":"2020-2021","strSport":"Soccer","strSquare":null,' \
                '"strStatus":"Match Finished",' \
                '"strTVStation":null,' \
                '"strThumb":"https://www.thesportsdb.com/images/media/event/thumb' \
                '/cojimx1603530635.jpg",' \
                '"strTime":"20:00:00","strTimeLocal":"20:00:00",' \
                '"strTimestamp":"2021-02-08T20:00:00+00:00",' \
                '"strTweet1":"","strTweet2":"","strTweet3":"","strVenue":"Elland Road",' \
                '"strVideo":"https://www.youtube.com/watch?v=ACWdreL1TWI"},' \
                '{"dateEvent":"2021-02-03",' \
                '"dateEventLocal":"2021-02-03","idAPIfootball":"592354","idAwayTeam":"133615",' \
                '"idEvent":"1032905","idHomeTeam":"133635","idLeague":"4328",' \
                '"idSoccerXML":null,' \
                '"intAwayScore":"2","intAwayShots":null,"intHomeScore":"1","intHomeShots":null,' \
                '"intRound":"22","intSpectators":null,"strAwayFormation":null,' \
                '"strAwayGoalDetails":"",' \
                '"strAwayLineupDefense":null,"strAwayLineupForward":null,' \
                '"strAwayLineupGoalkeeper":null,' \
                '"strAwayLineupMidfield":null,"strAwayLineupSubstitutes":null,' \
                '"strAwayRedCards":null,' \
                '"strAwayTeam":"Everton","strAwayYellowCards":null,"strBanner":null,' \
                '"strCity":"",' \
                '"strCountry":"England","strDate":null,"strDescriptionEN":"",' \
                '"strEvent":"Leeds vs Everton",' \
                '"strEventAlternate":"Everton @ Leeds","strFanart":null,' \
                '"strFilename":"English Premier ' \
                'League 2021-02-03 Leeds vs Everton","strHomeFormation":null,' \
                '"strHomeGoalDetails":"",' \
                '"strHomeLineupDefense":null,"strHomeLineupForward":null,' \
                '"strHomeLineupGoalkeeper":null,' \
                '"strHomeLineupMidfield":null,"strHomeLineupSubstitutes":null,' \
                '"strHomeRedCards":null,' \
                '"strHomeTeam":"Leeds","strHomeYellowCards":null,"strLeague":"English Premier ' \
                'League",' \
                '"strLocked":"unlocked","strMap":null,"strOfficial":"","strPoster":null,' \
                '"strPostponed":"no","strResult":"","strSeason":"2020-2021",' \
                '"strSport":"Soccer",' \
                '"strSquare":null,"strStatus":"Match Finished","strTVStation":null,' \
                '"strThumb":"https://www.thesportsdb.com/images/media/event/thumb' \
                '/co3h2r1603530630.jpg",' \
                '"strTime":"19:30:00","strTimeLocal":"19:30:00",' \
                '"strTimestamp":"2021-02-03T19:30:00+00:00",' \
                '"strTweet1":"","strTweet2":"","strTweet3":"","strVenue":"Elland Road",' \
                '"strVideo":"https://www.youtube.com/watch?v=MY6j6iT4xGY"},' \
                '{"dateEvent":"2021-01-16",' \
                '"dateEventLocal":"2021-01-16","idAPIfootball":"592324","idAwayTeam":"133619",' \
                '"idEvent":"1032875","idHomeTeam":"133635","idLeague":"4328",' \
                '"idSoccerXML":null,' \
                '"intAwayScore":"1","intAwayShots":null,"intHomeScore":"0","intHomeShots":null,' \
                '"intRound":"19","intSpectators":null,"strAwayFormation":null,' \
                '"strAwayGoalDetails":"",' \
                '"strAwayLineupDefense":null,"strAwayLineupForward":null,' \
                '"strAwayLineupGoalkeeper":null,' \
                '"strAwayLineupMidfield":null,"strAwayLineupSubstitutes":null,' \
                '"strAwayRedCards":null,' \
                '"strAwayTeam":"Brighton","strAwayYellowCards":null,"strBanner":null,' \
                '"strCity":"",' \
                '"strCountry":"England","strDate":null,"strDescriptionEN":"",' \
                '"strEvent":"Leeds vs ' \
                'Brighton","strEventAlternate":"Brighton @ Leeds","strFanart":null,' \
                '"strFilename":"English ' \
                'Premier League 2021-01-16 Leeds vs Brighton","strHomeFormation":null,' \
                '"strHomeGoalDetails":"","strHomeLineupDefense":null,' \
                '"strHomeLineupForward":null,' \
                '"strHomeLineupGoalkeeper":null,"strHomeLineupMidfield":null,' \
                '"strHomeLineupSubstitutes":null,"strHomeRedCards":null,"strHomeTeam":"Leeds",' \
                '"strHomeYellowCards":null,"strLeague":"English Premier League",' \
                '"strLocked":"unlocked",' \
                '"strMap":null,"strOfficial":"","strPoster":null,"strPostponed":"no",' \
                '"strResult":"",' \
                '"strSeason":"2020-2021","strSport":"Soccer","strSquare":null,' \
                '"strStatus":"Match Finished",' \
                '"strTVStation":null,' \
                '"strThumb":"https://www.thesportsdb.com/images/media/event/thumb' \
                '/qqplax1603530616.jpg",' \
                '"strTime":"15:00:00","strTimeLocal":"15:00:00",' \
                '"strTimestamp":"2021-01-16T15:00:00+00:00",' \
                '"strTweet1":"","strTweet2":"","strTweet3":"","strVenue":"Elland Road",' \
                '"strVideo":"https://www.youtube.com/watch?v=cuIBM0puu8U"},' \
                '{"dateEvent":"2020-12-27",' \
                '"dateEventLocal":"2020-12-27","idAPIfootball":"592284","idAwayTeam":"133623",' \
                '"idEvent":"1032835","idHomeTeam":"133635","idLeague":"4328",' \
                '"idSoccerXML":null,' \
                '"intAwayScore":"0","intAwayShots":null,"intHomeScore":"1","intHomeShots":null,' \
                '"intRound":"15","intSpectators":null,"strAwayFormation":null,' \
                '"strAwayGoalDetails":"",' \
                '"strAwayLineupDefense":null,"strAwayLineupForward":null,' \
                '"strAwayLineupGoalkeeper":null,' \
                '"strAwayLineupMidfield":null,"strAwayLineupSubstitutes":null,' \
                '"strAwayRedCards":null,' \
                '"strAwayTeam":"Burnley","strAwayYellowCards":null,"strBanner":null,' \
                '"strCity":"",' \
                '"strCountry":"England","strDate":null,"strDescriptionEN":"",' \
                '"strEvent":"Leeds vs Burnley",' \
                '"strEventAlternate":"Burnley @ Leeds","strFanart":null,' \
                '"strFilename":"English Premier ' \
                'League 2020-12-27 Leeds vs Burnley","strHomeFormation":null,' \
                '"strHomeGoalDetails":"",' \
                '"strHomeLineupDefense":null,"strHomeLineupForward":null,' \
                '"strHomeLineupGoalkeeper":null,' \
                '"strHomeLineupMidfield":null,"strHomeLineupSubstitutes":null,' \
                '"strHomeRedCards":null,' \
                '"strHomeTeam":"Leeds","strHomeYellowCards":null,"strLeague":"English Premier ' \
                'League",' \
                '"strLocked":"unlocked","strMap":null,"strOfficial":"","strPoster":null,' \
                '"strPostponed":"no","strResult":"","strSeason":"2020-2021",' \
                '"strSport":"Soccer",' \
                '"strSquare":null,"strStatus":"Match Finished","strTVStation":null,' \
                '"strThumb":"https://www.thesportsdb.com/images/media/event/thumb' \
                '/61739z1603530597.jpg",' \
                '"strTime":"12:00:00","strTimeLocal":"12:00:00",' \
                '"strTimestamp":"2020-12-27T12:00:00+00:00",' \
                '"strTweet1":"","strTweet2":"","strTweet3":"","strVenue":"Elland Road",' \
                '"strVideo":"https://www.youtube.com/watch?v=zzEblS1lEvU"},' \
                '{"dateEvent":"2020-12-16",' \
                '"dateEventLocal":"2020-12-16","idAPIfootball":"592264","idAwayTeam":"134777",' \
                '"idEvent":"1032815","idHomeTeam":"133635","idLeague":"4328",' \
                '"idSoccerXML":null,' \
                '"intAwayScore":"2","intAwayShots":null,"intHomeScore":"5","intHomeShots":null,' \
                '"intRound":"13","intSpectators":null,"strAwayFormation":null,' \
                '"strAwayGoalDetails":"",' \
                '"strAwayLineupDefense":null,"strAwayLineupForward":null,' \
                '"strAwayLineupGoalkeeper":null,' \
                '"strAwayLineupMidfield":null,"strAwayLineupSubstitutes":null,' \
                '"strAwayRedCards":null,' \
                '"strAwayTeam":"Newcastle","strAwayYellowCards":null,"strBanner":null,' \
                '"strCity":"",' \
                '"strCountry":"England","strDate":null,"strDescriptionEN":"",' \
                '"strEvent":"Leeds vs ' \
                'Newcastle","strEventAlternate":"Newcastle @ Leeds","strFanart":null,' \
                '"strFilename":"English ' \
                'Premier League 2020-12-16 Leeds vs Newcastle","strHomeFormation":null,' \
                '"strHomeGoalDetails":"","strHomeLineupDefense":null,' \
                '"strHomeLineupForward":null,' \
                '"strHomeLineupGoalkeeper":null,"strHomeLineupMidfield":null,' \
                '"strHomeLineupSubstitutes":null,"strHomeRedCards":null,"strHomeTeam":"Leeds",' \
                '"strHomeYellowCards":null,"strLeague":"English Premier League",' \
                '"strLocked":"unlocked",' \
                '"strMap":null,"strOfficial":"","strPoster":null,"strPostponed":"no",' \
                '"strResult":"",' \
                '"strSeason":"2020-2021","strSport":"Soccer","strSquare":null,' \
                '"strStatus":"Match Finished",' \
                '"strTVStation":null,' \
                '"strThumb":"https://www.thesportsdb.com/images/media/event/thumb' \
                '/7rm9941603530587.jpg",' \
                '"strTime":"18:00:00","strTimeLocal":"18:00:00",' \
                '"strTimestamp":"2020-12-16T18:00:00+00:00",' \
                '"strTweet1":"","strTweet2":"","strTweet3":"","strVenue":"Elland Road",' \
                '"strVideo":"https://www.youtube.com/watch?v=sNrkB-0fFBk"}]} '

        mock_resp = self._mock_response(json_data=_json)
        mock_get.return_value = mock_resp

        transormed_json = transform_response(json.loads(internet_query('12345').json()))
        self.assertTrue(mock_resp.raise_for_status.called)
        self.assertTrue(transormed_json is not None)

    @mock.patch('requests.get')
    def test_failed_query(self, mock_get):
        """test case where sport db is down"""
        mock_resp = self._mock_response(status=500, raise_for_status=HTTPError("site is down"))
        mock_get.return_value = mock_resp
        self.assertRaises(HTTPError, internet_query, '12345')


if __name__ == '__main__':
    unittest.main()
