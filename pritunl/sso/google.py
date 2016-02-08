from pritunl import settings

def verify_google(user_email):
    user, user_domain = user_email.split('@')
    if user_domain in settings.app.sso_match and user == 'foo':
      r_value = True
    else:
      r_value = False
    return r_value, None
