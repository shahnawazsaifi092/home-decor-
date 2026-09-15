import glob, re

extra_classes = " duration-300 transform hover:scale-105 active:scale-95 hover:-translate-y-1 "

def add_classes(match):
    # match.group(0) is the entire class="... bg-primary text-on-primary ..."
    class_str = match.group(0)
    
    # If it already has some of our extra classes, don't add them again
    if 'hover:scale-105' not in class_str:
        # Insert just before the closing quote
        return class_str[:-1] + extra_classes + '"'
    return class_str

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find class="..." containing 'bg-primary text-on-primary'
    # We use a regex that matches class=" followed by anything, then our target string, then anything until "
    pattern = r'class="[^"]*bg-primary text-on-primary[^"]*"'
    
    new_content = re.sub(pattern, add_classes, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

print('Animated buttons successfully!')
