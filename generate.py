import collections
import re

from jinja2 import Environment, FileSystemLoader


lines = [
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
]
regex = re.compile(r"['.-\\*-\\!]")
lines_dict = collections.OrderedDict()
for line in lines:
    filename = regex.sub('', line.lower()).replace(' ', '-')
    lines_dict[filename] = line

env = Environment(loader=FileSystemLoader('templates'))

# make line files
line_template = env.get_template('line.html')
for filename, line in lines_dict.items():
    with open('output/{}.html'.format(filename), 'w') as f:
        f.write(line_template.render(line=line))

# gimme some index
index_template = env.get_template('index.html')
with open('output/index.html', 'w') as f:
    f.write(index_template.render(lines=lines_dict))
