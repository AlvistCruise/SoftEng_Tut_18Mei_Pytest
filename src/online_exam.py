def compute_online_exam(exam_max_duration, accomodation_status, dc_duration, login_time, is_public_holiday):
    
    # Rule 1: Max duration limits
    if exam_max_duration > 120:
        return "Error"
        
    # Rule 2: Public holidays cancel the exam
    if dc_duration > 5:
        return "autosubmit"
        
    # Rule 3: Late logins are rejected
    if login_time > 30:
        return "Rejected"
        
    # Rule 4: Long disconnects trigger auto-submit
    
    if is_public_holiday:
        return "Cancel"
    
        
    # If no special conditions are triggered, the exam submits normally
    else: 
        return "Submit"