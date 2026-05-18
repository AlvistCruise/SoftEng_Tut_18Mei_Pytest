def compute_online_exam(exam_max_duration, accomodation_status, dc_duration, login_time, is_public_holiday):
    if login_time < 1:
        return "Rejected"
    if exam_max_duration > 1:
        return "Error"
        
    
    if is_public_holiday:
        return "Cancel"
    
    if dc_duration > 5:
        return "autosubmit"
    else: 
        return "Submit"