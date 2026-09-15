import glob, os

target_dir = r'D:\website projects\interior website 1'
old_phone = '+33 (0)1 44 28 90 10'
new_phone = '8172155443'

for filepath in glob.glob(os.path.join(target_dir, '*.html')):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_phone in content:
        content = content.replace(old_phone, new_phone)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
print("Phone number updated successfully!")
