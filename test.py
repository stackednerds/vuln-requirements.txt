import requests

# TRIGGER: We are using the specific feature (Auth + Redirect) 
# that makes this version of 'requests' vulnerable.
# Vulnerability: This auth header gets leaked to 'attacker.com'
def trigger_vulnerability():
    target_url = "http://example.com/redirect-to-attacker"
    
    # usage of 'auth' param with default allow_redirects=True 
    # is the specific signature for CVE-2018-18074
    response = requests.get(target_url, auth=('admin', 'secret_password'))
    
    return response.status_code

if __name__ == "__main__":
    trigger_vulnerability()
