# VAHackathon
TwitterBot

This is a simplified TwitterBot that serves two purposes.

The first goal is detection using a given individuals tweets and providing information for invididuals to seek help, it also has the ability to query the twitter api for friends of the user and suggest they reach out to that individual[Due to privacy concerns, this may not be the best approach unless we have more data on users to know that the users actually know each other. Graph centrality would be useful here, but obviously due to the limitaions of data this currently cannot be implemented effectively]. 

The second goal is to promote awareness and outreach. The bot is currently responsive to two commands (help and volunteer). The ultimate goal is to provide more general information where individuals could seek help/information from local communities customized to their geographic location.

*The current implmenetaion of the streaming process will look through large streams of tweets and so the false positive rate is very high. The bot will tweet at people if certain poritions of code are commented out. Otherwise the bot will just collect the tweets in json format in "tweets.json" for future analysis.

**Currently due to the limitations of twitter, it is not possible to direct message people if the individuals are not mutually following them. However, the current implementation of the bot will automatically follow any individual that talks to it, ideally individuals who are interested in private information should seek to follow the bot and eventually we will try to direct message the individual.

