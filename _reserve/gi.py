import math,random
random.seed(4)
def cr(pts,closed=False,t=.5):
    d=f"M {pts[0][0]:.1f} {pts[0][1]:.1f}"
    n=len(pts)
    for i in range(n-1):
        p0=pts[i-1] if i>0 else pts[i];p1=pts[i];p2=pts[i+1];p3=pts[i+2] if i+2<n else pts[i+1]
        c1=(p1[0]+(p2[0]-p0[0])*t/3*2*.5*1.0,p1[1]+(p2[1]-p0[1])*t/3*2*.5*1.0)
        c2=(p2[0]-(p3[0]-p1[0])*t/3*2*.5*1.0,p2[1]-(p3[1]-p1[1])*t/3*2*.5*1.0)
        d+=f" C {c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}"
    return d
# small intestine: serpentine rows
pts=[];rows=6;y0=296;dy=24;x0=134;x1=266
for r in range(rows):
    y=y0+r*dy
    xs=[x0+ (x1-x0)*k/4 for k in range(5)]
    if r%2: xs=xs[::-1]
    for k,x in enumerate(xs):
        pts.append((x+random.uniform(-2,2),y+(8 if k%2 else -8)+random.uniform(-2,2)))
    # turn
    ex=x1+10 if r%2==0 else x0-10
    pts.append((ex,y+dy/2))
SI=cr(pts)
COLON="M 100 424 L 100 268 A 24 24 0 0 1 124 244 Q 200 292 276 244 A 24 24 0 0 1 300 268 L 300 402 C 300 440 252 428 238 452 C 226 472 200 468 200 498"
STOMACH="M 196 96 C 168 98 148 128 158 164 C 168 204 214 226 252 216 C 280 208 274 178 248 174 C 228 170 222 148 226 124 C 229 106 214 94 196 96 Z"
ESO="M 196 14 L 196 72 C 196 86 200 90 204 98"
DUO="M 252 216 C 262 232 256 262 240 288"
LIVER="M 70 120 C 70 92 120 84 150 98 C 172 108 170 140 150 160 C 120 186 74 170 70 120 Z"
def svg(style):
    if style=='line':
        return f'''<svg viewBox="0 0 400 520" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Der menschliche Verdauungstrakt, gezeichnet in feinen Linien">
<g fill="none" stroke-linecap="round" stroke-linejoin="round">
<path d="{COLON}" stroke="#A9AFB6" stroke-width="30"/><path d="{COLON}" stroke="#FAF5EC" stroke-width="26"/>
<path d="{COLON}" stroke="#A9AFB6" stroke-width="18" stroke-dasharray="1 15" opacity=".9"/>
<path d="{SI}" stroke="#E3A15C" stroke-width="13"/><path d="{SI}" stroke="#FAF5EC" stroke-width="9"/>
<path d="{DUO}" stroke="#E3A15C" stroke-width="9"/><path d="{DUO}" stroke="#FAF5EC" stroke-width="5.4"/>
<path d="{STOMACH}" fill="#FAF5EC" stroke="#A9AFB6" stroke-width="2.6"/>
<path d="{STOMACH}" stroke="#E3A15C" stroke-width="1.4" transform="translate(5 5)" opacity=".8"/>
<path d="{ESO}" stroke="#A9AFB6" stroke-width="13"/><path d="{ESO}" stroke="#FAF5EC" stroke-width="9.6"/>
</g></svg>'''
    if style=='water':
        return f'''<svg viewBox="0 0 400 520" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Der menschliche Verdauungstrakt als weiche Aquarell-Illustration">
<defs><filter id="wf" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence type="fractalNoise" baseFrequency=".03" numOctaves="3" seed="5" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="5"/><feGaussianBlur stdDeviation=".7"/></filter>
<filter id="sb"><feGaussianBlur stdDeviation="7"/></filter>
<radialGradient id="gs" cx="40%" cy="35%"><stop offset="0" stop-color="#F6C9A0"/><stop offset="1" stop-color="#E3A15C"/></radialGradient></defs>
<g fill="none" stroke-linecap="round" stroke-linejoin="round">
<ellipse cx="200" cy="270" rx="150" ry="215" fill="#F6D3AA" opacity=".35" filter="url(#sb)"/>
<g filter="url(#wf)">
<path d="{LIVER}" fill="#C98A64" opacity=".5" stroke="none"/>
<path d="{COLON}" stroke="#8FA68A" stroke-width="30" opacity=".85"/>
<path d="{COLON}" stroke="#B9CBB2" stroke-width="20" stroke-dasharray="2 14" opacity=".9"/>
<path d="{SI}" stroke="#E3A15C" stroke-width="15" opacity=".92"/><path d="{SI}" stroke="#F6C9A0" stroke-width="6" opacity=".9"/>
<path d="{DUO}" stroke="#E3A15C" stroke-width="11"/>
<path d="{STOMACH}" fill="url(#gs)" stroke="#C98A64" stroke-width="2"/>
<path d="{ESO}" stroke="#D9A07E" stroke-width="13"/>
</g></g></svg>'''
    if style=='ring':
        # Jahresring-Optik: Konturen aus mehreren versetzten Linien
        out=[]
        def lines(path,w0,n,col,op):
            s=''
            for i in range(n):
                s+=f'<path d="{path}" stroke="{col}" stroke-width="{max(w0-i*(w0/n),.8):.1f}" opacity="{op}"/>'
            return s
        return f'''<svg viewBox="0 0 400 520" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Der menschliche Verdauungstrakt als Linienzeichnung">
<g fill="none" stroke-linecap="round" stroke-linejoin="round">
<path d="{COLON}" stroke="#A9AFB6" stroke-width="28" opacity=".55"/><path d="{COLON}" stroke="#FFFFFF" stroke-width="23" opacity=".9"/><path d="{COLON}" stroke="#A9AFB6" stroke-width="14" stroke-dasharray="1 13" opacity=".8"/>
<path d="{SI}" stroke="#E3A15C" stroke-width="12"/><path d="{SI}" stroke="#FFFFFF" stroke-width="8" opacity=".9"/>
<path d="{DUO}" stroke="#E3A15C" stroke-width="8.5"/><path d="{DUO}" stroke="#FFFFFF" stroke-width="5" opacity=".9"/>
<path d="{STOMACH}" fill="#FFFFFF" fill-opacity=".85" stroke="#A9AFB6" stroke-width="2.4"/>
<path d="{STOMACH}" stroke="#E3A15C" stroke-width="1.2" transform="translate(-5 -4) scale(1.04)" opacity=".6" transform-origin="200 160"/>
<path d="{ESO}" stroke="#A9AFB6" stroke-width="12"/><path d="{ESO}" stroke="#FFFFFF" stroke-width="8.6"/>
</g></svg>'''
if __name__=='__main__':
    for s in('line','water','ring'):
        open(f'gi_{s}.svg','w').write(svg(s))
