
def compute_online_exam(
        exam_max_duration,
        accomodation_status,
        dc_duration,
        login_time,
        is_public_holiday
):
        if exam_max_duration < 120:
                pass
        elif exam_max_duration > 120:
                return "Error"
        
        if dc_duration < 5:
                pass
        elif dc_duration > 5:
                return "autosubmit"
        
        if(login_time < 30):
                pass
        elif login_time > 30:
                return "Rejected"
        
        if( not is_public_holiday):
                pass
        elif is_public_holiday:
                return "Cancel"
        
        return "Submit"
        