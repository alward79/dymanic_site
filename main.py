'''
Angelena Ward
5/28/2015
Design Patterns for Web Programming
Dynamic Site
'''

import webapp2
from pages import Content #imports from pages.py the Content() class
from data import Data #import from data.py the Data() class

#MainHandler() receives and handles request
class MainHandler(webapp2.RequestHandler):
    def get(self):
        #refencing the subclasses from pages.py and data.py
        page = Content()
        data = Data()

        #get method will display team depending on link clicked
        if self.request.GET:
            team = self.request.GET['team']#request data.
            print team
            #sending objects to setter
            if team == "atlanta":#button to request data
                print data.eteam_array[0]#print data from class Data on the 1st position of the array.
                page.results = data.eteam_array[0]#sending objects to setter of 1st array to team link
            elif team == "cleveland":#button to request data
                print data.eteam_array[1]#print data from class Data on the 2nd position of the array.
                page.results = data.eteam_array[1]#sending objects to setter of 2nd array to team link
            elif team == "chicago":#button to request data
                print data.eteam_array[2]#print data from class Data on the 3rd position of the array.
                page.results = data.eteam_array[2]#sending objects to setter of 3rd array to team link
            elif team == "toronto":#button to request data
                print data.eteam_array[3]#print data from class Data on the 4th position of the array.
                page.results = data.eteam_array[3]#sending objects to setter of 4th array to team link
            elif team == "washington":#button to request data
                print data.eteam_array[4]#print data from class Data on the 5th position of the array.
                page.results = data.eteam_array[4]#sending objects to setter of 5th array to team link
            elif team == "golden_state":#button to request data
                print data.wteam_array[0]#print data from class Data on the 1st position of the array.
                page.results = data.wteam_array[0]#sending objects to setter of 1st array to team link
            elif team == "houston":#button to request data
                print data.wteam_array[1]#print data from class Data on the 2nd position of the array.
                page.results = data.wteam_array[1]#sending objects to setter of 2nd array to team link
            elif team == "clippers":#button to request data
                print data.wteam_array[2]#print data from class Data on the 3rd position of the array.
                page.results = data.wteam_array[2]#sending objects to setter of 3rd array to team link
            elif team == "portland":#button to request data
                print data.wteam_array[3]#print data from class Data on the 4th position of the array.
                page.results = data.wteam_array[3]#sending objects to setter of 4th array to team link
            elif team == "memphis":#button to request data
                print data.wteam_array[4]#print data from class Data on the 5th position of the array.
                page.results = data.wteam_array[4]#sending objects to setter of 5th array to team link
            #html written to browser
            self.response.write(page.print_out_result())

        else:
            #html written to browser before link is clicked
            self.response.write(page.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
