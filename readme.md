# Discord chess assistant
### Requirements:
Discord bot - generate bot with your discord account and acquire a token  
Lichess account - sign up on lichess and acquire a API token
### Installation
Create a file "config.js" in settings directory and paste there name of the file with intents, discord and lichess tokens. it should look like this:  
<div style="text-align:center"><img src="readme_imgs/install.png" /></div>
Add your bot to your discord server. Run bot.py file. It will install necessary data from nltk (If it is not already installed).

### Intents
* <a href="#1">Welcoming messages</a>
* <a href="#2">Goodbye messages</a>
* <a href="#3">Repeadting a message</a>
* <a href="#4">Asking about current time </a>
* <a href="#5">Telling a interesting chess fact</a>
* <a href="#6">Asking about world chess champion</a>
* <a href="#7">Asking about top chess players on lichess.com</a>
* <a href="#8">Telling player's rating</a>
* <a href="#9">Telling how many games have been played on this account</a>
* <a href="#10">Challenging a player</a>
* <a href="#11">Creating a tournament</a>
* <a href="#12">Joining a team </a>

<div id="#1">

#### Welcoming messages
<div style="text-align:center"><img src="readme_imgs/welcome.png" /></div>

</div>
<div id="#2">

#### Goodbye messages
<div style="text-align:center"><img src="readme_imgs/goodbye.png" /></div>

</div>
<div id="#3">

#### Repeating a message
<div style="text-align:center"><img src="readme_imgs/repeat.png" /></div>

</div>
<div id="#4">

#### Asking about current time 
<div style="text-align:center"><img src="readme_imgs/time.png" /></div>

</div>
<div id="#5">

#### Telling a interesting chess fact
Facts are hard-coded and picked randomly.
<div style="text-align:center"><img src="readme_imgs/fact.png" /></div>

</div>
<div id="#6">

#### Asking about world chess champion
<div style="text-align:center"><img src="readme_imgs/champ.png" /></div>

</div>
<div id="#7">

#### Asking about top chess players on lichess.com
Fetch top 10 rapid players from lichess api.
<div style="text-align:center"><img src="readme_imgs/top.png" /></div>

</div>
<div id="#8">

#### Telling player's rating
Fetch own rating from lichess api.
<div style="text-align:center"><img src="readme_imgs/elo.png" /></div>

</div>
<div id="#9">

#### Telling how many games have been played on this account
Fetch rapid games amount from lichess api.
<div style="text-align:center"><img src="readme_imgs/games.png" /></div>

</div>
<div id="#10">

#### Challenging a player
Create a challenge using lichess api.
<div style="text-align:center"><img src="readme_imgs/challenge.png" /></div>  
Challenge created:  
<div style="text-align:center"><img src="readme_imgs/challenge_ex.png" /></div>

</div>
<div id="#11">

#### Creating a tournament
Create a tournament using lichess api.
<div style="text-align:center"><img src="readme_imgs/contest.png" /></div>
Tournament created:  
<div style="text-align:center"><img src="readme_imgs/contest_ex.png" /></div>

</div>
<div id="#12">

#### Joining a team 
Join a team using lichess api.
<div style="text-align:center"><img src="readme_imgs/team.png" /></div>
Joined a team:  
<div style="text-align:center"><img src="readme_imgs/team_ex.png" /></div>

</div>
