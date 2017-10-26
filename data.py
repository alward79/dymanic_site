#class with attributes for the teams info
class TopTeams(object):
    def __init__(self):
        self.__team_name = ''
        self.__img = ''
        self.__wins = 0
        self.__losses = 0
        self.__home_game = 0
        self.__road_game = 0

#class with instances of objects
class Data(object):
    def __init__(self):
        #eastern team instance
        atlanta = TopTeams() #attribute that will store values of atlanta
        atlanta.team_name = 'Atlanta Hawks'
        atlanta.img = 'http://i0.wp.com/stuffled.com/wp-content/uploads/2014/04/Atlanta-Hawks-Logo-Vector-Image.png?resize=1020%2C680'
        atlanta.wins = 60
        atlanta.losses = 22
        atlanta.home_game = 35 - 6
        atlanta.road_game = 25 -16

        cleveland = TopTeams() #attribute to store values for cleveland
        cleveland.team_name = 'Cleveland Cavaliers'
        cleveland.img = 'http://www.hdicon.com/wp-content/uploads/2011/04/Cleveland_Cavaliers_2010.png'
        cleveland.wins = 53
        cleveland.losses = 29
        cleveland.home_game = 31 - 10
        cleveland.road_game = 25 - 19

        chicago = TopTeams() #attribute to store values for chicago
        chicago.team_name = 'Chicago Bulls'
        chicago.img = 'http://www.learnitanytime.com/wp-content/uploads/2013/06/chicago_bulls_logo.png'
        chicago.wins = 50
        chicago.losses = 32
        chicago.home_game = 27 - 14
        chicago.road_game = 23 - 18

        toronto = TopTeams() #attribute to store values for toronto
        toronto.team_name = 'Toronto Raptors'
        toronto.img = 'http://upload.wikimedia.org/wikipedia/en/thumb/5/54/Toronto_Raptors_alternate_logo.svg/1024px-Toronto_Raptors_alternate_logo.svg.png'
        toronto.wins = 49
        toronto.losses = 33
        toronto.home_game = 27 - 14
        toronto.road_game = 23 -18

        washington = TopTeams() #attribute to store values for washington
        washington.team_name = 'Washington Wizards'
        washington.img = 'http://upload.wikimedia.org/wikipedia/en/thumb/b/bd/Washington_Wizards_Logo.svg/1111px-Washington_Wizards_Logo.svg.png'
        washington.wins = 46
        washington.losses = 36
        washington.home_game = 29 - 12
        washington.road_game = 17 - 24

        #western team instance
        golden_state = TopTeams()#attribute to store values for golden state
        golden_state.team_name = 'Golden State Warriors'
        golden_state.img = 'http://clippertalk.com/sites/default/files/logos/Warriors.png'
        golden_state.wins = 67
        golden_state.losses = 15
        golden_state.home_game = 39 - 2
        golden_state.road_game = 28 -13

        houston = TopTeams() #attribute to store values for houston
        houston.team_name = 'Houston Rockets'
        houston.img = 'http://upload.wikimedia.org/wikipedia/de/thumb/2/28/Houston_Rockets.svg/2000px-Houston_Rockets.svg.png'
        houston.wins = 56
        houston.losses = 26
        houston.home_game = 30 -11
        houston.road_game = 26 -15

        clippers = TopTeams() #attribute to store values for LA clippers
        clippers.team_name = 'Los Angeles Clippers'
        clippers.img = 'http://www.nightmovesonline.com/wp-content/uploads/2014/04/Los-Angeles-Clippers-Logo-Medium.png'
        clippers.wins = 56
        clippers.losses = 26
        clippers.home_game = 30 - 11
        clippers.road_game = 26 - 15

        portland = TopTeams() #attribute to store values for portland
        portland.team_name = 'Portland Trail Blazers'
        portland.img = 'http://img1.wikia.nocookie.net/__cb20101026151711/nba/images/b/b7/Portland_Trail_Blazers_alternate_logo.png'
        portland.wins = 51
        portland.losses = 31
        portland.home_game = 32 - 9
        portland.road_game = 19 - 22

        memphis = TopTeams() #attribute to store values for memphis
        memphis.team_name = 'Memphis Grizzlies'
        memphis.img = 'http://upload.wikimedia.org/wikipedia/fr/6/6f/Memphis_Grizzlies_logo.png'
        memphis.wins = 55
        memphis.losses = 27
        memphis.home_game = 31 - 10
        memphis.road_game = 24 - 17

        #array containing team instances
        self.eteam_array = [atlanta, cleveland, chicago, toronto, washington]

        #array containing team instances
        self.wteam_array = [golden_state, houston, clippers, portland, memphis]