import random
import re

def replace_bbcode(text):
    bbcode = [
        r"\[b](.*?)\[/b]",
        r"\[i](.*?)\[/i]",
        r"\[u](.*?)\[/u]",
        r"\[s](.*?)\[/s]",
        r"\[\*](.*)",
        r"\[list](.*?)\[/list]",
        r"\[ul](.*?)\[/ul]",
        r"\[ol\](.*?)\[\/ol\]",
    ]
    replacement = [
        r"<strong>\g<1></strong>",
        r"<em>\g<1></em>",
        r"<span style='text-decoration: underline'>\g<1></span>",
        r"<span style='text-decoration: strikethrough'>\g<1></span>",
        r"<li>\g<1></li>",
        r"<ul>\g<1></ul>",
        r"<ul>\g<1></ul>",
        r"<ol>\g<1></ol>",
    ]
    for i in range(len(bbcode)):
        if i > 4:
            text = re.sub(bbcode[i], replacement[i], text, flags=re.DOTALL)
        else:
            text = re.sub(bbcode[i], replacement[i], text)
    text = text.replace("\n", "<br>")
    return text