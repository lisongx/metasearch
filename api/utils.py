from langid import classify

def get_lang(us):
    return classify(us)[0]