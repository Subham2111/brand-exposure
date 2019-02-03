

def decision(detected, total, validation):
    sum = detected/total
    sum = sum*100
    if sum >= int(validation):
        message = 'worth it'
    else:
        message = 'loss'
    return sum, message