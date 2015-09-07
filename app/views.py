"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

YOUR_INFO = {
    'name' : 'Nick Pereira',
    'bio' : "I'm a junior developer for Interline Vacations and a senior studying CS at UT",
    'email' : '', # Leave blank if you'd prefer not to share your email with other conference attendees
    # 'twitter_username' : '', # No @ symbol, just the handle.
    'github_username' : "PresidentNick", 
    'headshot_url' : 'https://avatars1.githubusercontent.com/u/8160053?v=3&s=460', # Link to your GitHub, Twitter, or Gravatar profile image.
}
    
def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/base.html',
        context_instance = RequestContext(request,
            {
                'attendee' : YOUR_INFO,    
                'year': datetime.now().year,
            })
    )