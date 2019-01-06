from IPython.core.display import display, Markdown, Image

display(Markdown("# Absolute Value"))

display(Markdown("$$ \\mid n \\mid = \\text{n's distance from 0} $$"))

def abs_dif(n):
    return abs(n - 21)

def abs_dif(n):
    if n > 21:
        result = 2*abs(n - 21)
    else:
        result = abs(n-21)
    return result
