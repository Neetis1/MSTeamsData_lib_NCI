import unittest
from  MSTeamsdataretrieval import TeamsDataRetrival

class Test(unittest.TestCase):
    """
    The basic class that inherits unittest.TestCase
    """
    test_data = "Meeting Summary \nTotal Number of Participants	2\nMeeting Title	Devops project \nMeeting Start Time	12/10/2021, 7:37:51 PM\nMeeting End Time	12/10/2021, 8:07:14 PM\nMeeting Id	453adbad-3672-4bde-92d0-6be3049eb379\nNeeti Sharma	12/10/2021, 7:37:51 PM	12/10/2021, 8:07:14 PM	29m 22s	x20242778@student.ncirl.ie	Organiser	x20242778@student.ncirl.ie"
    teamsData = TeamsDataRetrival.MSTeamsAttendanceProcessor(test_data)  # instantiate the Person Class

    def test_0_get_time_in_minutes(self):
        print("Start get_time_in_minutes test case\n")
        timeInMin = self.teamsData.getTimeInMinutes("2h 30m 1 s")
        self.assertEqual(timeInMin,150)
        print("\nFinish get_time_in_minutes test\n")

    def test_1_get_Attendees_Details_As_List(self):
        print("\nStart get_Attendees_Details_As_List test\n")
        attendees = self.teamsData.getAttendeesDetailsAsList()
        self.assertListEqual(attendees,['Neeti Sharma', '12/10/2021, 7:37:51 PM', '12/10/2021, 8:07:14 PM', 29, 'x20242778@student.ncirl.ie', 'Organiser', 'Devops project ',
'453adbad-3672-4bde-92d0-6be3049eb379', 'Neeti Sharma']) 
        print("\nFinish get_Attendees_Details_As_List test\n")

    def test_2_get_Attendees_Details_As_Dict(self):
        print("\nStart get_Attendees_Details_As_Dict test\n")
        attendees = self.teamsData.getAttendeesDetailsAsDict()
        expected= {'x20242778@student.ncirl.ie': ['Neeti Sharma', '12/10/2021, 7:37:51 PM', '12/10/2021, 8:07:14 PM', 29, 'x20242778@student.ncirl.ie', 'Organiser', 'Devops project ', '453adbad-3672-4bde-92d0-6be3049eb379', 'Neeti Sharma']}
        self.assertDictEqual(attendees,expected)
        print("\nFinish get_Attendees_Details_As_Dict test\n")

#to execute the test case use :
#python -m unittest tests.test_Teamsdataretrieval
if __name__ == "__main__":
    unittest.main()

