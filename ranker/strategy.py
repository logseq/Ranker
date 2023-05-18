def issue_rank_score(issue):
    """
        Calculate the issue rank score with the algorithm:\n
        (<num-of-comments> * 2 + <num-of-emoji>) * <last-response-decay>\n
        where last-response-decay is 10 if the last response was within 30 days,\n
        linearly decaying to 1 if the last response was 360 days ago.  
    """
    num_of_comments = len(issue.comments)
    # TODO: Implement emoji parsing
    num_of_emoji = 0
    # TODO: Implement last response decay
    last_response_decay =  10
    ir_score = (num_of_comments * 2 + num_of_emoji) * last_response_decay
    # Comment string for logging how the score was calculated
    ir_comment = "comment number: {}".format(num_of_comments)
    return ir_score, ir_comment
