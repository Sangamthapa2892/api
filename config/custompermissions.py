from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle

class CustomThrottle(AnonRateThrottle):
    rate = "3/min"
    
class NewCustomThrottle(AnonRateThrottle):
    rate = "10/day"
    
# progressive rate throttling 
# first count the view hits, if user hits wrong password more than three time, set user.is_active=False, and
# return response "Your account has locked. Please contact administrator" 

