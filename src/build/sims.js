/* 회계 팩 실험 모듈 — 설명용 예시값. 하나의 범용 계산 실험(calc)을 칸마다 설정으로 다르게 씁니다. */
function sum(a){return a.reduce(function(s,v){return s+v},0)}
function cum(a){var s=0;return a.map(function(v){s+=v;return s})}
function seq(n,f){var o=[];for(var i=0;i<n;i++)o.push(f?f(i):i);return o}
var FMT={won:function(v){return nf(Math.round(v))+'만 원'},n:function(v){return nf(Math.round(v))},n1:function(v){return nf(v,1)},n2:function(v){return nf(v,2)},pct:function(v){return (+v).toFixed(1)+'%'},pct0:function(v){return Math.round(v)+'%'},x:function(v){return isFinite(v)?(+v).toFixed(1)+'회':'계산 불가(0으로 나눔)'},wk:function(v){return (+v).toFixed(1)+'주'},d:function(v){return nf(Math.round(v))+'일'},raw:function(v){return String(v)},ea:function(v){return nf(Math.round(v))+'개'},w:function(v){return nf(Math.round(v))+'원'},usd:function(v){return '$'+nf(Math.round(v))},eok:function(v){return nf(v,1)+'억'},yr:function(v){return v+'년'},mo:function(v){return v+'개월'},cnt:function(v){return v+'건'},sgn:function(v){return (v>0?'+':'')+nf(Math.round(v))}};
function fm(k){return FMT[k]||FMT.n}
function ev(expr,p){try{return (new Function('p','sum','cum','seq','with(p){return ('+expr+')}'))(p,sum,cum,seq)}catch(e){console.error(expr,e);return NaN}}
function tpl(s,p){return s.replace(/\{\{([^}|]+)(?:\|(\w+))?\}\}/g,function(_,x,f){return fm(f||'n')(ev(x,p))})}
function cc(c){return COL[c]||c||COL.s}
function sbars(c,items,fmtf,title,H){var W=fit(c,H),ctx=c.getContext('2d');ctx.clearRect(0,0,W,H);grid(ctx,W,H);var L=16,R=16,T=34,B=52,pw=W-L-R,ph=H-T-B;if(title)txt(ctx,title,L,20,COL.text,13,'left',true);
  var mx=Math.max.apply(null,items.map(function(i){return Math.max(0,i.v)}).concat([1e-9])),mn=Math.min.apply(null,items.map(function(i){return Math.min(0,i.v)}).concat([0])),span=(mx-mn)||1,y0=T+ph*mx/span,bw=pw/items.length;
  ctx.strokeStyle=COL.rule;ctx.beginPath();ctx.moveTo(L,y0+.5);ctx.lineTo(L+pw,y0+.5);ctx.stroke();
  items.forEach(function(it,i){var bh=Math.abs(it.v)/span*ph,w=Math.min(bw*.64,110),x=L+i*bw+(bw-w)/2,y=it.v>=0?y0-bh:y0;ctx.fillStyle=cc(it.c);ctx.fillRect(x,y,w,Math.max(bh,1));
    txt(ctx,fmtf(it.v),x+w/2,it.v>=0?y-6:Math.min(y+bh+14,H-28),COL.text,bw<70?10:12,'center',true);txt(ctx,it.l,x+w/2,H-10,COL.muted,bw<70?10:11,'center')});stamp(ctx,W,'예시값')}
SIMS.calc=function(el,cfg){var p={},H=cfg.h||230,c=null,tw=null;
  if(cfg.bars||cfg.lines)c=mkCanvas(el,H,cfg.aria||'계산 결과 그림',cfg.wide);
  if(cfg.table){tw=h('div',{class:'tw'});el.appendChild(tw)}
  var row=ctrlRow(el),K=cfg.kp?kpis(el,Math.min(4,cfg.kp.length)):null,E=cfg.eq?eqline(el):null,I=cfg.notes?insight(el):null;
  (cfg.params||[]).forEach(function(q){if(q[2]==='opt'){p[q[0]]=q[4];buttons(row,q[1],q[3],q[4],function(v){p[q[0]]=v;draw()})}else{p[q[0]]=q[5];slider(row,q[1],q[2],q[3],q[4],q[5],fm(q[6]),function(v){p[q[0]]=v;draw()})}});
  function draw(){
    if(cfg.bars){sbars(c,cfg.bars.items.map(function(b){return {l:tpl(b[0],p),v:+ev(b[1],p)||0,c:b[2]}}),fm(cfg.bars.fmt),cfg.bars.title?tpl(cfg.bars.title,p):'',H)}
    if(cfg.lines){var Ln=cfg.lines,f=fm(Ln.fy);dChart(c,{title:tpl(Ln.title||'',p)+' · 예시값',xs:ev(Ln.xs,p),ys:Ln.ys.map(function(s){return {n:s[0],d:ev(s[1],p),c:cc(s[2]),dash:s[3]?[5,4]:null}}),fy:f,fx:fm(Ln.fx||'raw'),ymin:Ln.ymin,xl:Ln.xl,mark:Ln.mark?{x:ev(Ln.mark,p),l:Ln.markl||''}:null},H)}
    if(cfg.table){var rows=ev(cfg.table.rows,p)||[];tw.innerHTML='<table class="tb"><tr>'+cfg.table.head.map(function(x){return '<th>'+x+'</th>'}).join('')+'</tr>'+rows.map(function(r){return '<tr'+(r.hl?' style="background:rgba(183,120,0,.10);font-weight:700"':'')+'>'+r.map(function(x){return '<td>'+(typeof x==='number'?nf(x):x)+'</td>'}).join('')+'</tr>'}).join('')+'</table>'}
    if(K)K(cfg.kp.map(function(k){return [fm(k[3])(ev(k[0],p)),tpl(k[1],p),k[2]]}));
    if(E)E(tpl(cfg.eq,p));
    if(I)I(cfg.notes.filter(function(n){return ev(n[0],p)}).map(function(n){return [n[1],tpl(n[2],p)]}))}
  if(c)addMod(c,function(dt){if(!dt)draw()});draw()};
/* 대결: 값은 빌드 때 검산해 넣은 고정값 */
DUELS.fixed=function(cfg){return {fly:cfg.fly,robo:cfg.robo,say:cfg.say,cond:cfg.cond,condA:cfg.condA,condB:cfg.condB}};
