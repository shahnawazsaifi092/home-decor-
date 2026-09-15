import glob

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Increase logo size
    content = content.replace('class="h-8 w-auto object-contain"', 'class="h-16 w-auto object-contain"')
    
    # Replace business name
    content = content.replace('Atelier Terre', 'Home Decor')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated successfully!')
