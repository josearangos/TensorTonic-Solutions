def tokenize(text: str) -> list:
    """
    Returns a list of token strings.
    """
    result = []
    world = ""
    for t in text:
        if t.isalnum() or t == "_":
            world = world + t
        else:
            if world !="":
                result.append(world)
                world = ""
            if  t.isspace() == False and t!="":
                result.append(t)
    if world !="":
        result.append(world)
    result
    return result