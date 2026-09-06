#!/usr/bin/env python3
"""Site integrity: broken internal links + cross-page text similarity.
Run after every build. Exit 1 if any content pair exceeds 15% or any link is broken."""
import os, re, itertools, sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def bt(fp):
    h=open(fp,encoding='utf-8').read()
    h=re.sub(r'(?s)<script.*?</script>|<nav.*?</nav>|<footer.*?</footer>|<section class="related".*?</section>',' ',h)
    m=re.search(r'(?s)<div class="prose">.*?</div></div>',h)
    return re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',m.group(0) if m else h)).lower()
def sh(t,n=6):
    w=re.findall(r'[a-z]+',t); return {tuple(w[i:i+n]) for i in range(len(w)-n+1)}
pages={}; bad=0
for root,_,fs in os.walk(ROOT):
    if '/.git' in root or '/_build' in root: continue
    for f in fs:
        if f not in ('index.html','404.html'): continue
        fp=os.path.join(root,f); h=open(fp,encoding='utf-8').read()
        for href in set(re.findall(r'href="(/[^"#?]*)"',h)):
            if href.startswith(('/img/','/assets/','/video/')): continue
            t=os.path.join(ROOT,href.strip('/'))
            if href.strip('/') and not (os.path.exists(t) or os.path.exists(os.path.join(t,'index.html'))):
                print("BROKEN",href,"in",os.path.relpath(fp,ROOT)); bad+=1
        if f=='index.html':
            t=bt(fp)
            if len(t.split())>250: pages[os.path.relpath(root,ROOT)]=sh(t)
w=[]
for a,b in itertools.combinations(sorted(pages),2):
    A,B=pages[a],pages[b]
    if A and B: w.append((len(A&B)/min(len(A),len(B)),a,b))
w.sort(reverse=True)
EXEMPT={('.','guides'),('sms-privacy-policy','sms-terms')}
# Content depth floor: hand-written prose + FAQ per content page. Reported every build;
# becomes a hard FAIL once the backlog is cleared (set DEPTH_FAIL=True).
DEPTH_FLOOR=1200; DEPTH_FAIL=False
SKIP_DEPTH={'.','terms','sms-terms','sms-privacy-policy','contact','booking','gallery','testimonials','pricing','about',
            'services','guides','auto-detailing','makes','vehicles','situations','commercial'}
def depth(fp):
    h=open(fp,encoding='utf-8').read()
    if '<div class="page-head">' not in h: return None
    st=h.index('<div class="page-head">'); en=h.index('<section class="related">') if '<section class="related">' in h else len(h)
    seg=re.sub(r'(?s)<script.*?</script>','',h[st:en]); return len(re.sub(r'<[^>]+>',' ',seg).split())
thin=[]
for rel in pages:
    if rel in SKIP_DEPTH: continue
    d=depth(os.path.join(ROOT,rel,'index.html'))
    if d is not None and d<DEPTH_FLOOR: thin.append((d,rel))
thin.sort()
flag=[x for x in w if x[0]>0.15 and (x[1],x[2]) not in EXEMPT]
print(f"pages {len(pages)} | pairs {len(w)} | >10% {len([x for x in w if x[0]>0.10])} | >5% {len([x for x in w if x[0]>0.05])} | broken links {bad}")
print(f"depth: {len(thin)} content pages under {DEPTH_FLOOR} words (shortest {thin[0][0] if thin else '-'})")
for j,a,b in w[:5]: print(f"  {j*100:5.1f}%  {a} <-> {b}")
if flag or bad or (DEPTH_FAIL and thin):
    print("FAIL"); sys.exit(1)
print("PASS")
