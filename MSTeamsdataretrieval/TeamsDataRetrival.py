class MSTeamsAttendanceProcessor:

    def __init__(self, fileCsvDetails):
        self.fileCsv = fileCsvDetails

    #splits the stream of string by newlines
    def splitFilesByNewline(self):
        fileCsvlines = self.fileCsv.splitlines()
        return fileCsvlines
    
    #records the meeting details common for all the meeting attendees
    def setMeetingDetails(self):
        fileCsvlines = self.splitFilesByNewline()
        for fileData in fileCsvlines:
            if 'Meeting Title' in fileData:
                self.meetingTitle = fileData.split('\t')[1]
            if 'Meeting Id' in fileData:
                self.meetingId = fileData.split('\t')[1]
            if 'Organiser' in fileData:
                self.organiser = fileData.split('\t')[0]
            if 'Total Number of Participants' in fileData:
                self.totalAttendees = fileData.split('\t')[1]
                

    #get time as input in the format 00h 00m 00s(string) and returns the minutes (int)        
    def getTimeInMinutes(self,timeData):
        timeList = timeData.split()
        time = 0
        if len(timeList) > 2:
            time = int(timeList[0][0:-1]) * 60
            time = time + int(timeList[1][0:-1])
        else:
            time = int(timeList[0][0:-1])
        return time

    #returns the details of the attendees as dictionary with key as the email and values as the list with details
    #organises the data which will later be used for calculations and displaying data in the dashboard
    def getAttendeesDetailsAsDict(self):
        Msdict = {}
        MsList = []
        MsListData = []
        val = ""
        key = ""
        fileCsvlines = self.splitFilesByNewline()
        self.setMeetingDetails()
        for fileData in fileCsvlines: 
            MsList = []
            if len(fileData.split('\t')) == 7 and 'Full Name' not in fileData:
                for i in range(0,6):
                    #converting time to minutes
                    if i == 3:
                        timeMin = self.getTimeInMinutes(fileData.split('\t')[3])
                        MsList.append(timeMin)
                    else:
                        MsList.append(fileData.split('\t')[i])
                MsList.append(self.meetingTitle)
                MsList.append(self.meetingId)
                MsList.append(self.organiser)
                key = fileData.split('\t')[4]
                Msdict[key] = MsList
        return Msdict
    #returns the details of the attendees as a list with  details of the attendees
    #organises the data which will later be used for calculations and displaying data in the dashboard
    def getAttendeesDetailsAsList(self):
        MsListData = []
        fileCsvlines = self.splitFilesByNewline()
        self.setMeetingDetails()
        for fileData in fileCsvlines: 
            MsList = []
            if len(fileData.split('\t')) == 7 and 'Full Name' not in fileData:
                for i in range(0,6):
                    #converting time to minutes
                    if i ==3:
                        timeMin = self.getTimeInMinutes(fileData.split('\t')[3])
                        MsList.append(timeMin)
                    else:
                        MsList.append(fileData.split('\t')[i])
                MsList.append(self.meetingTitle)
                MsList.append(self.meetingId)
                MsList.append(self.organiser)
                MsListData.append(MsList)
        return MsListData

    #returns a list of data for master data model
    def getAttendeesforMasterData(self):
        MsList = []
        self.setMeetingDetails()
        MsList.append(self.meetingTitle)
        MsList.append(self.meetingId)
        MsList.append(self.organiser)
        MsList.append(self.totalAttendees)
        return MsList


someString = "Meeting Summary \nTotal Number of Participants	2\nMeeting Title	Devops project \nMeeting Start Time	12/10/2021, 7:37:51 PM\nMeeting End Time	12/10/2021, 8:07:14 PM\nMeeting Id	453adbad-3672-4bde-92d0-6be3049eb379\nNeeti Sharma	12/10/2021, 7:37:51 PM	12/10/2021, 8:07:14 PM	29m 22s	x20242778@student.ncirl.ie	Organiser	x20242778@student.ncirl.ie \n Parag Sharad Salunkhe	12/10/2021, 7:38:13 PM	12/10/2021, 8:07:12 PM	28m 58s	x20224699@student.ncirl.ie	Presenter	x20224699@student.ncirl.ie"

TeamsProc = MSTeamsAttendanceProcessor(someString) 
#print(TeamsProc.splitFilesByNewline())
output = TeamsProc.getAttendeesDetailsAsDict()
print(output)
print(type(TeamsProc.splitFilesByNewline()))