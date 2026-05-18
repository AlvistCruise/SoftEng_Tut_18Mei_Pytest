
def compute_online_exam(
        exam_max_duration,
        accomodation_status,
        dc_duration,
        login_time,
        is_public_holiday
):

        if exam_max_duration > 120:
                return "Error"
        
        if dc_duration > 5:
                return "autosubmit"
        
        if login_time > 30:
                return "Rejected"

        if is_public_holiday:
                return "Cancel"
        
        return "Submit"
        