import random
from modules.lichess import *
from datetime import datetime

conversation_in_progress = False
last_message = None

def GREET_handler(message):
    global last_message
    result = {}
    result["finished_talking"] = True

    result["message"] = "Hello"

    last_message = result['message']
    return result

def GOODBYE_handler(message):
    global last_message
    result = {}
    result["finished_talking"] = True

    result["message"] = "See you!"
    last_message = result['message']
    return result

def REPEAT_handler(message):
    global last_message
    result = {}
    result["finished_talking"] = True
    
    if last_message:
        result["message"] = last_message
    else:
        result["message"] = "I didn't say anything"
    
    return result

def TIME_handler(message):
    global last_message
    result = {}
    result["finished_talking"] = True

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    result['message'] = current_time
    last_message = result['message']
    return result

def CURIOSITY_handler(message):
    global last_message
    result = {}
    result["finished_talking"] = True

    curiosities = ["Initially, the Queen could only move one square at a time, diagonally.",
                   "The number of possibilities of a Knight's tour is over 122 million.",
                   'The word "Checkmate" in Chess comes from the Persian phrase "Shah Mat," which means"the King is dead.',
                   'The longest chess game theoretically possible is 5,949 moves.', 
                   "A computer called DeepThought became the first computer to beat an international grandmaster in November 1988, Long Beach, California."]

    result['message'] = curiosities[random.randrange(0, len(curiosities))]
    last_message = result['message']
    return result

def CHAMPION_handler(message):
    global last_message
    result = {}
    result["finished_talking"] = True
    result["message"] = "Magnus Carlsen!"
    last_message = result['message']
    return result

def TOP_PLAYERS_handler(message):
    global last_message
    result = {}
    result["finished_talking"] = True
    
    top10 = get_top("rapid", 10)
    message = "\n".join([f"{player[0]}, {player[1]}" for player in top10])
    result["message"] = message 
    last_message = result['message']
    return result

def MY_RATING_handler(message):
    global last_message
    result = {}
    result["finished_talking"] = True
    
    rating = get_own_rating("rapid")
    result["message"] = f"You have {rating} elo" 
    last_message = result['message']
    return result

def PLAYED_GAMES_handler(message):
    global last_message
    result = {}
    result["finished_talking"] = True
    
    games_amount = get_all_games("rapid")
    result["message"] = f"You have played {games_amount} games" 
    last_message = result['message']
    return result

def CHALLENGE_handler(message):
    global last_message
    global conversation_in_progress
    
    result = {}

    if conversation_in_progress:
        username = message.content.lower()
        conversation_in_progress = False
        result['finished_talking'] = True
        
        if challenge_player(username, 600, 0):
            result["message"] = "You have challenged " + username
        else:
            result["message"] = "Something went wrong :("
    else:
        conversation_in_progress = True
        result['finished_talking'] = False
        result["message"] = "Who is your enemy?";
    last_message = result['message']
    return result

def TOURNAMENT_handler(message):
    global last_message
    global conversation_in_progress
    
    result = {}

    if conversation_in_progress:
        duration = message.content.lower()
        conversation_in_progress = False
        result['finished_talking'] = True

        if create_tournament(10, 0, int(duration)):
            result["message"] = "You have created tournament"
        else:
            result["message"] = "Something went wrong :("
    else:
        conversation_in_progress = True
        result['finished_talking'] = False
        result["message"] = "How long should tournament last?";
    last_message = result['message']
    return result

def JOIN_TEAM_handler(message):
    global last_message
    global conversation_in_progress
    
    result = {}

    if conversation_in_progress:
        team_id = message.content.lower()
        conversation_in_progress = False
        result['finished_talking'] = True

        if join_team(team_id):
            result["message"] = "You have joined team with team_id " + team_id
        else:
            result["message"] = "Something went wrong :("
    else:
        conversation_in_progress = True
        result['finished_talking'] = False
        result["message"] = "Tell me team id";
    last_message = result['message']
    return result

def DEFAULT_handler(message):
    result = {}

    result["finished_talking"] = True
    result["message"] = ""

    return result