
def content_selection (player2):
    import random
    food = ['milk', 'meat', 'apple', 'banana','avocado', 'blackberry', 'grapes']
    jobs = ['teacher', 'engineer', 'doctor', 'waiter', 'actor', 'musician']
    sports = ['football', 'swimming', 'tennis', 'basketball', 'boxing']
    
    
    if player1 == 'food':
        player2 = random.choice(food).casefold
        
    elif player1 == 'jobs':
        player2 = random.choice(jobs).casefold

    elif player1 == 'sports':
        player2 = random.choice(sports).casefold
    
    return player2
    
run = 0
while run < 10:
    run += 1
    
    print('please choose a content to begin playing. \n Available contents are: food, jobs and sports')
    player1 = input('please type your choice here : \n ').casefold()

    content_selection (player1)
    
  