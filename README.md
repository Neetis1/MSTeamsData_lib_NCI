## Library Decription

Python Library To retrieve data from a MS teams CSV attendance report in the form of List and Dictionary which can be used for processing this data for creating data models and visualization.

## Installation
Run the following to install the library 
```
pip install pip install MSTeamsdataretrieval-neeti-sharma1

```
## Usage

```
from MSTeamsdataretrieval import TeamsDataRetrival

 teamsData = TeamsDataRetrival.MSTeamsAttendanceProcessor(test_data)
 dict = teamsData.getAttendeesDetailsAsDict()

```