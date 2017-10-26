#superClass
class Page(object):
    def __init__(self):
        #html elements
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>NBA Top Teams</title>
        <link href="css/style.css" rel="stylesheet" type="text/css" >
    </head>
    <body>'''
        self._body = ''
        self._close = '''
    </body>
</html>'''
        def print_out(self):
            return self._head + self._body + self._close

#subclass
class Content(Page):
    def __init__(self):
        #init subclass of superClass Page
        super(Content, self).__init__()

        #this will link the teams to buttons to return info
        self._links = '''
        <div id="container">
            <div id="team_links">
                <p>Eastern Conference</p>
                <a href="?team=atlanta">Atlanta Hawks</a>
                <a href="?team=cleveland">Cleveland Cavaliers</a>
                <a href="?team=chicago">Chicago Bulls</a>
                <a href="?team=toronto">Toronto Raptors</a>
                <a href="?team=washington">Washington Wizards</a>
            </div>

            <div id="team_links">
                <p>Western Conference</p>
                <a href="?team=golden_state">Golden State Warriors</a>
                <a href="?team=houston">Houston Rockets</a>
                <a href="?team=clippers">Los Angeles Clippers</a>
                <a href="?team=portland">Portland Trail Blazers</a>
                <a href="?team=memphis">Memphis Grizzlies</a>
            </div>
        </div>
        '''
        #static elements that will show before a team is clicked on
        self._info = '''
            <div id="info">
                <h1>NBA TOP TEAMS</h1>
            </div>
        '''
        #will contain html from the getter
        self._results = ''
        self._close_results = '''</div>
        '''

    @property
    def results(self):
        pass

    #calculate teams Percent
    def __calc_pct(self, perc):
        pct = float(perc.wins) / float(perc.wins + perc.losses)#divide wins by wins+losses(total games)
        win_percentage = round(pct, 3)#round results 3 places
        return win_percentage#returns value of ptc to printed

    #setter to set self._results to html elements
    @results.setter
    def results(self, info):
        win_percentage = self.__calc_pct(info)#pass obj to self.__calc_ptc(obj)

        self._results += '''    <div id="team_info">\n  '''#open div to hold data for team info
        self._results += '''<h2 id="name">''' + info.team_name + '''</h2>\n           '''#attribute to receive data for team name
        self._results += '''    <img src="''' + info.img + '''" alt="team_img">\n           '''#attribute to receive data for team img
        self._results += '''</div>\n        '''#closs team info dive
        self._results += '''    <div id="team_stats">\n             '''#open div to hold data for team stats
        self._results += '<h2><strong>Wins: </strong> ' + str(info.wins) + '</h2>\n             '''#attribute to receive data for team wins (bold print)
        self._results += '<h2 class="odd"><strong>Losses: </strong> ' + str(info.losses) + '</h2>\n             '''#attribute to receive data for team losses(bold print)
        self._results += '<h2><strong>Home Record: </strong> ' + str(info.home_game) + '</h2>\n             '''#attribute to receive data for team home game record
        self._results += '<h2 class="odd"><strong>Road Record: </strong> ' + str(info.road_game) + '</h2>\n             '''#attribute to receive data for team away game record
        self._results += '<h2><strong>Win Percentage: </strong> ' + str(win_percentage) + '</h2>\n          '''#attribute to receive data for team ptc from function __calc_ptc
        self._results += '''</div>\n        '''#close stats div

    def print_out(self):#prints to browser
        return self._head + self._info + self._links + self._close_results + self._close

    #returns html elements to be written to browser
    def print_out_result(self):
        return self._head + self._info + self._links + self._results + self._close_results + self._close
