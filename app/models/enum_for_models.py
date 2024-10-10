"""
All enum to be used through out the application.
"""

from enum import Enum

class UserRole(Enum):
    GUEST: str = "Not a member of discord server or not a verified account"
    USER: str = "Member of discord server and verified account"
    ADMIN: str = "Member with Admin privileges for admission"

class RequestStatus(Enum):
    PENDING: str = "Request is pending review or action"
    COMPLETED: str = "Request has been completed successfully"
    REJECTED: str = "Request has been rejected"

class Projects(Enum):
    OPENLOGO: str = "Openlogo is your API solutions for efficient retrieval of 500+ logos"
    RSVP: str = "Create, Share, and Sell Event Tickets Easily"
    FEEDBACKPULSE: str = "Join Team.shiksha projects, request and provide reviews"
