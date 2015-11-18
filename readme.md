TigreData
==============
Using D3 to visualize graphs of Princeton students. Currently work-in-progress

Self-notes: 
* python makestudenttree.py -- uses princetonstudentfacebook.html to make studenttree.json
* python sort_dormstudents.py -- uses studenttree.json to make sort_dormstudents.json
* python makedatadump.py -- uses sort_dormstudents.json to make datadump.json
* python manage.py loaddata datadump.json -- loads database with contents of datadump.json
