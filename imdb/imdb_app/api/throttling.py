from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class ReviewCreateThrottle(UserRateThrottle):
    scope = 'review-create'
    
    
    
class ReviweListThrottle(UserRateThrottle):
    scope = 'review-list'