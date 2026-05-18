def compute_online_exam(exam_max_duration, accomodation_status, dc_duration, login_time, is_public_holiday):
    if login_time < 1:
        return "Rejected"
    # Rule 1: Max duration limits
    if exam_max_duration > 1:
        return "Error"
        
    # Rule 2: Public holidays cancel the exam
    
        
    # Rule 3: Late logins are rejected
    
        
    # Rule 4: Long disconnects trigger auto-submit
    
    if is_public_holiday:
        return "Cancel"
    
    if dc_duration > 5:
        return "autosubmit"
        
    # If no special conditions are triggered, the exam submits normally
    else: 
        return "Submit"