import pytest
from src.online_exam import compute_online_exam

# Full test suite mapped from the requirements table
# Format: (exam_max_duration, accomodation_status, dc_duration, login_time, is_public_holiday, expected)
test_data = [
    # Row 1: Edge case (over max duration)
    (130, False, 0, 0, False, "Error"),
    
    # Rows 2-9: Max duration 120, With Accommodations
    (120, True, 3, 25, False, "Submit"),       # Row 2
    (120, True, 4, 23, True, "Cancel"),        # Row 3
    (120, True, 5, 54, False, "Rejected"),     # Row 4
    (120, True, 6, 21, False, "autosubmit"),   # Row 6
    (120, True, 7, 22, True, "autosubmit"),    # Row 7
    (120, True, 9, 57, False, "autosubmit"),   # Row 8
    (120, True, 10, 38, True, "autosubmit"),   # Row 9
    
    # Rows 10-17: Max duration 120, No Accommodations
    (120, False, 2, 15, False, "Submit"),      # Row 10
    (120, False, 1, 18, True, "Cancel"),       # Row 11
    (120, False, 4, 43, False, "Rejected"),    # Row 12
    (120, False, 7, 13, False, "autosubmit"),  # Row 14
    (120, False, 20, 11, True, "autosubmit"),  # Row 15
    (120, False, 32, 46, False, "autosubmit"), # Row 16
    (120, False, 21, 56, True, "autosubmit"),  # Row 17
    
    # Rows 18-25: Variable durations, With Accommodations
    (90, True, 2, 11, False, "Submit"),        # Row 18
    (80, True, 4, 24, True, "Cancel"),         # Row 19
    (67, True, 5, 23, True, "Rejected"),       # Row 21
    (50, True, 9, 24, False, "autosubmit"),    # Row 22
    (56, True, 23, 32, True, "autosubmit"),    # Row 23
    (32, True, 12, 45, False, "autosubmit"),   # Row 24
    (12, True, 34, 55, True, "autosubmit"),    # Row 25
    
    # Rows 26-33: Variable durations, No Accommodations
    (42, False, 5, 16, False, "Submit"),       # Row 26
    (23, False, 4, 19, True, "Cancel"),        # Row 27
    (12, False, 2, 46, False, "Rejected"),     # Row 28
    (98, False, 24, 10, False, "autosubmit"),  # Row 30
    (19, False, 32, 11, True, "autosubmit"),   # Row 31
    (34, False, 11, 49, False, "autosubmit"),  # Row 32
    (21, False, 33, 58, True, "autosubmit"),   # Row 33
]

@pytest.mark.parametrize(
    "exam_max_duration, accomodation_status, dc_duration, login_time, is_public_holiday, expected",
    test_data
)
def test_compute_online_exam(exam_max_duration, accomodation_status, dc_duration, login_time, is_public_holiday, expected):
    # Call the function from your source code
    result = compute_online_exam(
        exam_max_duration,
        accomodation_status,
        dc_duration,
        login_time,
        is_public_holiday
    )
    
    # Verify the logic matches the expected output table
    assert result == expected