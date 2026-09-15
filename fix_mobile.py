import glob, os

directories = [
    r'D:\website projects\interior website 1',
    r'd:\website tesing and projects\interior-app'
]

header_target = '<span class="material-symbols-outlined text-on-primary text-[18px]">person</span></div></div></div></header>'

header_replacement = '''<span class="material-symbols-outlined text-on-primary text-[18px]">person</span></div>
<button class="lg:hidden w-10 h-10 flex items-center justify-center text-on-surface" onclick="toggleMobileMenu()"><span class="material-symbols-outlined text-[28px]">menu</span></button>
</div></div>
<div id="mobileMenu" class="fixed inset-0 z-[60] bg-surface flex flex-col pt-6 px-margin-mobile gap-8 translate-x-full transition-transform duration-300 lg:hidden shadow-2xl overflow-hidden">
  <div class="flex items-center justify-between">
    <span class="font-headline-sm text-headline-sm text-on-surface">Home Decor</span>
    <button class="w-10 h-10 flex items-center justify-center text-on-surface" onclick="toggleMobileMenu()">
      <span class="material-symbols-outlined text-[28px]">close</span>
    </button>
  </div>
  <nav class="flex flex-col gap-8 mt-8">
    <a class="font-label-lg text-2xl uppercase tracking-wider text-on-surface-variant hover:text-primary transition-colors" href="index.html">Home</a>
    <a class="font-label-lg text-2xl uppercase tracking-wider text-on-surface-variant hover:text-primary transition-colors" href="about.html">About Us</a>
    <a class="font-label-lg text-2xl uppercase tracking-wider text-on-surface-variant hover:text-primary transition-colors" href="services.html">Services</a>
    <a class="font-label-lg text-2xl uppercase tracking-wider text-on-surface-variant hover:text-primary transition-colors" href="portfolio.html">Portfolio</a>
  </nav>
</div>
</header>'''

body_target = '</body>'
body_replacement = '''<script>
function toggleMobileMenu() {
  const menu = document.getElementById('mobileMenu');
  if (menu.classList.contains('translate-x-full')) {
    menu.classList.remove('translate-x-full');
    menu.classList.add('translate-x-0');
  } else {
    menu.classList.remove('translate-x-0');
    menu.classList.add('translate-x-full');
  }
}
</script></body>'''

for d in directories:
    for filepath in glob.glob(os.path.join(d, '*.html')):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check if already added
        if 'toggleMobileMenu()' not in content:
            content = content.replace(header_target, header_replacement)
            content = content.replace(body_target, body_replacement)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        
print("Mobile menu added successfully!")
