def bob_response(hey_bob):
    # Strip leading and trailing whitespace
    statement = hey_bob.strip()
    
    # Check if the statement is empty or contains only whitespace
    if not statement:
        return "Fine. Be that way!"
    
    # Check if the statement is in all caps (yelling)
    is_yelling = statement.isupper()
    
    # Check if the statement is a question
    is_question = statement.endswith('?')
    
    # Check if it's a yelled question
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    
    # Check if it's a question (but not yelled)
    if is_question:
        return "Sure."
    
    # Check if it's yelling (but not a question)
    if is_yelling:
        return "Whoa, chill out!"
    
    # Default response
    return "Whatever."