import file, url

def is_file():
    return this is a file

def is_url():


def analyze(param):
    if is_file(param):
        return file.analyze(param)
    elif is_url(param):
        return url.analyze(param)
    else:
        return "Not valid or url"