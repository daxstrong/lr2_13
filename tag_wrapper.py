def wrap_in_tag(tag):
    def wrap_string(s):
        return f"<{tag}>{s}</{tag}>"

    return wrap_string
