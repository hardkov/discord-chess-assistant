global client

# lichess functions
def get_top(game_type, count):
    try:
        top = client.users.get_leaderboard(game_type, count)
        top_parsed = [(user['username'], user['perfs']['rapid']['rating']) for user in top]
        return top_parsed
    except:
        return None
        
def get_own_rating(game_type):
    try:
        account = client.account.get()
        rating = account['perfs'][game_type]['rating']
        return rating
    except:
        return None

def get_all_games(game_type):
    try:
        account = client.account.get()
        games_amount = account['perfs'][game_type]['games']
        return games_amount
    except:
        return None

def challenge_player(username, clock_limit, clock_increment):
    try:
        result = client.challenges.create(username, False, clock_limit=clock_limit, clock_increment=clock_increment)
        dest_user = result['challenge']['destUser']
        
        return dest_user
    except:
        return None

def create_tournament(clock_time, clock_increment, minutes):
    try:
        return client.tournaments.create(clock_time, clock_increment, minutes)
    except: 
        return None
    
def join_team(team_id):
    try:
        return client.teams.join(team_id)
    except:
        return None
        