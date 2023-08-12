from rest_framework.throttling import UserRateThrottle

class define_throttle(UserRateThrottle):
    scope='ayush'