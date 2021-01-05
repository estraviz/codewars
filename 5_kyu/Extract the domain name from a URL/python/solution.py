"""Extract the domain name from a URL"""


def domain_name(url):
    s = (url if "://" not in url else url.split("://")[1]).split(".")
    return s[1] if s[0] == "www" else s[0]
