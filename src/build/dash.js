
/* 동적 대시보드: 주차마다 한 화면(조절기 · 숫자 카드 4개 · 그림 2개 · 해석), 목차에서는 탭으로 13개 */
var DASHES={};
function niceTicks(lo,hi,n){var span=hi-lo||1,step=Math.pow(10,Math.floor(Math.log10(span/n))),e=span/n/step;step*=e>=5?10:e>=2?5:e>=1?2:1;var t=[],s=Math.ceil(lo/step)*step;for(var v=s;v<=hi+step*1e-6;v+=step)t.push(+v.toFixed(10));return t}
function dChart(c,spec,H){var W=fit(c,H),ctx=c.getContext('2d');ctx.clearRect(0,0,W,H);
  var L=52,R=14,T=30,B=40,pw=W-L-R,ph=H-T-B;txt(ctx,spec.title,L,18,COL.text,13,'left',true);
  if(spec.t==='bar'){var n=spec.vals.length,mx=spec.ymax||Math.max.apply(null,spec.vals.concat([1e-9]))*1.18,bw=pw/n;ctx.strokeStyle=COL.rule;ctx.beginPath();ctx.moveTo(L,T+ph+.5);ctx.lineTo(L+pw,T+ph+.5);ctx.stroke();
    if(spec.hline!=null){var hy=T+ph-spec.hline/mx*ph;ctx.save();ctx.setLineDash([5,4]);ctx.strokeStyle=COL.a;ctx.beginPath();ctx.moveTo(L,hy);ctx.lineTo(L+pw,hy);ctx.stroke();ctx.restore();txt(ctx,spec.hlabel||'',L+2,hy-5,COL.a,11,'left',true)}
    spec.vals.forEach(function(v,i){var bh=Math.max(0,v)/mx*ph,x=L+i*bw+bw*.2;ctx.fillStyle=(spec.cols&&spec.cols[i])||COL.s;ctx.fillRect(x,T+ph-bh,bw*.6,bh);txt(ctx,(spec.fy||String)(v),x+bw*.3,T+ph-bh-6,COL.text,bw<44?10:12,'center',true);txt(ctx,spec.labels[i],x+(spec.pair?bw*.8:bw*.3),T+ph+16,COL.muted,11,'center')});return}
  if(spec.t==='hist'){var bins=spec.bins||30,cnt=new Array(bins).fill(0),lo=spec.lo,hi=spec.hi;spec.vals.forEach(function(v){var k=Math.floor((v-lo)/(hi-lo)*bins);if(k>=0&&k<bins)cnt[k]++});var m=Math.max.apply(null,cnt)||1;
    ctx.fillStyle=spec.c||'rgba(63,95,168,.55)';cnt.forEach(function(k,i){var bh=k/m*ph;ctx.fillRect(L+i*pw/bins+1,T+ph-bh,pw/bins-2,bh)});
    ctx.strokeStyle=COL.rule;ctx.beginPath();ctx.moveTo(L,T+ph+.5);ctx.lineTo(L+pw,T+ph+.5);ctx.stroke();niceTicks(lo,hi,5).forEach(function(t){var x=L+(t-lo)/(hi-lo)*pw;txt(ctx,(spec.fx||String)(t),x,T+ph+16,COL.muted,11,'center')});
    (spec.marks||[]).forEach(function(mk,i){var x=L+(mk.x-lo)/(hi-lo)*pw;if(x<L||x>L+pw)return;ctx.save();ctx.strokeStyle=mk.c||COL.r;ctx.setLineDash([4,3]);ctx.beginPath();ctx.moveTo(x,T);ctx.lineTo(x,T+ph);ctx.stroke();ctx.restore();txt(ctx,mk.l,x+(i%2?-4:4),T+10+(i%3)*13,mk.c||COL.r,11,i%2?'right':'left',true)});
    if(spec.xl)txt(ctx,spec.xl,L+pw,H-6,COL.muted,11,'right');return}
  /* line */
  var xs=spec.xs,x0=xs[0],x1=xs[xs.length-1],ylo=spec.ymin,yhi=spec.ymax;if(ylo==null||yhi==null){var all=[];spec.ys.forEach(function(s){s.d.forEach(function(v){if(isFinite(v))all.push(v)})});if(ylo==null)ylo=Math.min.apply(null,all);if(yhi==null)yhi=Math.max.apply(null,all);if(yhi===ylo)yhi=ylo+1;var pad=(yhi-ylo)*.08;if(spec.ymin==null)ylo-=pad;if(spec.ymax==null)yhi+=pad}
  function X(v){return spec.logx?L+(Math.log(v)-Math.log(x0))/(Math.log(x1)-Math.log(x0))*pw:L+(v-x0)/(x1-x0)*pw}function Y(v){return T+ph-(v-ylo)/(yhi-ylo)*ph}
  ctx.strokeStyle=COL.rule;ctx.lineWidth=1;niceTicks(ylo,yhi,4).forEach(function(t){var y=Y(t);ctx.beginPath();ctx.moveTo(L,y+.5);ctx.lineTo(L+pw,y+.5);ctx.stroke();txt(ctx,(spec.fy||String)(t),L-6,y+4,COL.muted,11,'right')});
  var xt=spec.logx?[1,3,10,30,100,300,1000,3000,10000,30000,100000].filter(function(v){return v>=x0&&v<=x1}):niceTicks(x0,x1,5);xt.forEach(function(t){txt(ctx,(spec.fx||String)(t),X(t),T+ph+16,COL.muted,11,'center')});
  if(spec.band){ctx.fillStyle='rgba(19,138,82,.08)';var b=spec.band,b0=clamp(X(b[0]),L,L+pw),b1=clamp(X(b[1]),L,L+pw);if(b1>b0)ctx.fillRect(b0,T,b1-b0,ph)}
  if(spec.hline!=null){ctx.save();ctx.setLineDash([5,4]);ctx.strokeStyle=COL.a;ctx.beginPath();ctx.moveTo(L,Y(spec.hline));ctx.lineTo(L+pw,Y(spec.hline));ctx.stroke();ctx.restore();txt(ctx,spec.hlabel||'',L+pw-2,Y(spec.hline)<T+16?Y(spec.hline)+14:Y(spec.hline)-5,COL.a,11,'right',true)}
  var lx=L+pw;spec.ys.forEach(function(s,si){ctx.save();ctx.strokeStyle=s.c;ctx.lineWidth=s.w||2.2;if(s.dash)ctx.setLineDash(s.dash);ctx.beginPath();var st=false;s.d.forEach(function(v,i){if(!isFinite(v)){st=false;return}var px=X(xs[i]),py=Y(clamp(v,ylo,yhi));if(!st){ctx.moveTo(px,py);st=true}else ctx.lineTo(px,py)});ctx.stroke();if(s.fill){ctx.lineTo(X(x1),Y(ylo));ctx.lineTo(X(x0),Y(ylo));ctx.closePath();ctx.globalAlpha=.12;ctx.fillStyle=s.c;ctx.fill()}ctx.restore();
    if(s.n&&spec.ys.length>1){ctx.save();ctx.font='700 11px "IBM Plex Sans KR",system-ui,sans-serif';var tw=ctx.measureText('● '+s.n).width;ctx.restore();lx-=tw+12;txt(ctx,'● '+s.n,lx+12,18,s.c,11,'left',true)}});
  if(spec.mark&&X(spec.mark.x)>=L-1&&X(spec.mark.x)<=L+pw+1){var mx_=X(spec.mark.x);ctx.save();ctx.strokeStyle=COL.r;ctx.setLineDash([4,3]);ctx.beginPath();ctx.moveTo(mx_,T);ctx.lineTo(mx_,T+ph);ctx.stroke();ctx.restore();if(spec.mark.y!=null){ctx.fillStyle=COL.r;ctx.beginPath();ctx.arc(mx_,Y(clamp(spec.mark.y,ylo,yhi)),5,0,7);ctx.fill()}if(spec.mark.l)txt(ctx,spec.mark.l,mx_+(mx_>L+pw*.7?-6:6),T+ph-8,COL.r,11,mx_>L+pw*.7?'right':'left',true)}
  if(spec.xl)txt(ctx,spec.xl,L+pw,H-4,COL.muted,11,'right');if(spec.yl)txt(ctx,spec.yl,4,T-10+0,COL.muted,11,'left')}

function Dash(el,key){var D=DASHES[key];if(!D){el.innerHTML='';return}el.innerHTML='';var p={},seed=1,ctl={},playing=false;
  var head=h('div',{class:'dhead'});head.innerHTML='<div><span class="eyebrow">동적 대시보드 · '+esc(D.tag||'')+'</span><h3>'+D.title+'</h3><p class="muted" style="font-size:14px">'+(D.sub||'')+'</p></div>';var hb=h('div',{class:'dbtns'});head.appendChild(hb);el.appendChild(head);
  var row=ctrlRow(el);var K=kpis(el,4);var g=h('div',{class:'dgrid'});el.appendChild(g);var c1=mkCanvas(g,240,D.title+' 그림 1'),c2=mkCanvas(g,240,D.title+' 그림 2');var I=insight(el);
  D.params.forEach(function(q){p[q[0]]=q[5];ctl[q[0]]=slider(row,q[1],q[2],q[3],q[4],q[5],q[6],function(v){p[q[0]]=v;draw()})});
  var pb=action(hb,'▶ 재생: '+(D.playLabel||'천천히 바꿔 보기'),function(){if(playing){playing=false;return}var q=D.params.filter(function(x){return x[0]===D.play})[0];if(!q)return;if(reduce){ctl[q[0]].set(q[3]);return}playing=true;pb.textContent='■ 멈춤';var t0=null,from=q[2],to=q[3];function step(ts){if(!playing){pb.textContent='▶ 재생: '+(D.playLabel||'천천히 바꿔 보기');return}if(!t0)t0=ts;var u=Math.min(1,(ts-t0)/4500),v=from+(to-from)*(D.playLog?(Math.pow(to/from,u)*from-from)/(to-from):u);v=Math.round(v/q[4])*q[4];ctl[q[0]].set(+v.toFixed(6));if(u<1)requestAnimationFrame(step);else{playing=false;pb.textContent='▶ 재생: '+(D.playLabel||'천천히 바꿔 보기')}}requestAnimationFrame(step)},true);
  if(D.random)action(hb,'↻ 다시 뽑기',function(){seed++;draw()});
  action(hb,'처음 값',function(){playing=false;D.params.forEach(function(q){ctl[q[0]].set(q[5])})});
  function draw(){var o=D.f(p,rng(seed*7919+13));K(o.k);dChart(c1,o.c[0],240);dChart(c2,o.c[1],240);I(o.note);c1._spec=o.c[0];c2._spec=o.c[1]}
  addMod(c1,function(dt){if(!dt&&c1._spec){dChart(c1,c1._spec,240);dChart(c2,c2._spec,240)}});draw();return {stop:function(){playing=false}}}
function initDash(){var el=$('.dash[data-dash]');if(el)Dash(el,el.dataset.dash);var tabs=$('.dtabs');if(tabs){var box=$('#dashbox'),cur=null;$$('button',tabs).forEach(function(b){b.addEventListener('click',function(){$$('button',tabs).forEach(function(x){x.setAttribute('aria-pressed','false')});b.setAttribute('aria-pressed','true');if(cur)cur.stop();cur=Dash(box,b.dataset.k);var a=$('#dashlink');if(a){a.href=b.dataset.f+'#dash';a.textContent=(+b.dataset.k)+'주차 해설 페이지에서 자세히 보기 →'}})});var f=$('button',tabs);if(f)f.click()}}

function rng0(){return 0}
function seqv(a,b,n){var o=[];for(var i=0;i<n;i++)o.push(a+(b-a)*i/(n-1));return o}
function logseq(a,b,n){var o=[];for(var i=0;i<n;i++)o.push(a*Math.pow(b/a,i/(n-1)));return o}
function lgam(x){var c=[76.18009172947146,-86.50532032941677,24.01409824083091,-1.231739572450155,.1208650973866179e-2,-.5395239384953e-5],y=x,t=x+5.5;t-=(x+.5)*Math.log(t);var s=1.000000000190015;for(var j=0;j<6;j++)s+=c[j]/++y;return -t+Math.log(2.5066282746310005*s/x)}
function betaPdf(x,a,b){if(x<=0||x>=1)return 0;return Math.exp((a-1)*Math.log(x)+(b-1)*Math.log(1-x)+lgam(a+b)-lgam(a)-lgam(b))}
function normCdf(z){var t=1/(1+.2316419*Math.abs(z)),d=.3989423*Math.exp(-z*z/2),p=d*t*(.3193815+t*(-.3565638+t*(1.781478+t*(-1.821256+t*1.330274))));return z>0?1-p:p}
function P1(v){return (v*100).toFixed(1)+'%'}function P0(v){return Math.round(v*100)+'%'}
function won(v){return Math.abs(v)>=1e8?(v/1e8).toFixed(1)+'억':Math.abs(v)>=1e4?nf(Math.round(v/1e4))+'만':nf(Math.round(v))}

/* 회계 대시보드 8개 — 모두 설명용 예시값 (단위는 그림 제목에 표시) */
function W_(v){return nf(Math.round(v))+'만'}function X1(v){return (+v).toFixed(1)}
DASHES['01']={tag:'1주차',title:'이익과 현금 대시보드',sub:'같은 한 달, 외상 비율만 바꿨을 때 이익과 통장이 어떻게 갈라지나 (카페 코이 예시)',play:'cr',playLabel:'외상 비율을 0%→100%로',
 params:[['s','이번 달 매출',0,2000,50,800,W_],['cr','외상(나중에 받는) 비율',0,100,5,40,function(v){return v+'%'}],['e','이번 달 현금 비용',0,1500,50,250,W_]],
 f:function(q){var pr=q.s-q.e,ar=q.s*q.cr/100,cash=q.s-ar-q.e,xs=seqv(0,100,21);
  return {k:[[W_(pr)+' 원','이익 (매출 − 비용)','g'],[W_(cash)+' 원','현금 증감','i'],[W_(ar)+' 원','매출채권 (받을 돈)','a'],[W_(pr-cash)+' 원','이익과 현금의 차이','r']],
   c:[{t:'bar',title:'이번 달 숫자 (만 원)',vals:[q.s,q.e,Math.max(0,pr),Math.max(0,cash)],labels:['매출','비용','이익','현금 증감'],cols:[COL.i,COL.a,COL.g,COL.s],fy:W_},
      {title:'외상 비율에 따른 이익과 현금 증감 (만 원)',xs:xs,ys:[{n:'이익',d:xs.map(function(){return pr}),c:COL.g},{n:'현금 증감',d:xs.map(function(x){return q.s*(1-x/100)-q.e}),c:COL.i}],fy:W_,fx:function(v){return v+'%'},mark:{x:q.cr,y:cash,l:'지금'},xl:'외상 비율'}],
   note:[['g','이익은 외상 비율과 상관없이 '+W_(pr)+' 원이에요. 팔린 시점에 매출을 적기 때문입니다(발생주의).'],[cash<0?'r':'a',cash<0?'현금은 '+W_(-cash)+' 원 줄었어요. 이익이 나도 통장이 마를 수 있습니다.':'현금은 '+W_(cash)+' 원 늘었어요. 이익과의 차이 '+W_(ar)+' 원은 매출채권으로 남아 있습니다.']]}}};
DASHES['02']={tag:'2주차',title:'매출·채권·원가 대시보드',sub:'매출 한 줄이 채권·현금·재고·원가로 갈라지는 모양 (카페 코이 4월 예시)',play:'col',playLabel:'회수율을 0%→100%로',
 params:[['s','카드·외상 매출',100,2000,50,800,W_],['col','이번 달 회수율',0,100,2.5,62.5,function(v){return v+'%'}],['cg','원가율 (매출원가 ÷ 매출)',10,70,1,30,function(v){return v+'%'}]],
 f:function(q){var got=q.s*q.col/100,ar=q.s-got,cogs=q.s*q.cg/100,gp=q.s-cogs,xs=seqv(10,70,25);
  return {k:[[W_(ar)+' 원','매출채권 잔액','a'],[W_(got)+' 원','회수한 현금','i'],[W_(gp)+' 원','매출총이익','g'],[X1(gp/q.s*100)+'%','매출총이익률','m']],
   c:[{t:'bar',title:'매출이 갈라지는 곳 (만 원)',vals:[q.s,got,ar,cogs,gp],labels:['매출','회수 현금','매출채권','매출원가','매출총이익'],cols:[COL.i,COL.s,COL.a,COL.r,COL.g],fy:W_},
      {title:'원가율과 매출총이익률',xs:xs,ys:[{n:'매출총이익률',d:xs.map(function(x){return 100-x}),c:COL.g}],fy:function(v){return Math.round(v)+'%'},fx:function(v){return v+'%'},mark:{x:q.cg,y:100-q.cg,l:'지금'},xl:'원가율'}],
   note:[['a','매출 '+W_(q.s)+' 원 중 '+W_(ar)+' 원은 아직 통장에 없어요. 재무상태표에 매출채권(자산)으로 적혀 있습니다.'],['g','매출총이익률 '+X1(gp/q.s*100)+'%는 매출 100원당 '+X1(gp/q.s*100)+'원이 남는다는 뜻이에요. 회수율과는 상관없습니다.']]}}};
DASHES['03']={tag:'3주차',title:'선급비용 대시보드',sub:'미리 낸 광고비가 달마다 자산에서 비용으로 옮겨 가는 모양',play:'t',playLabel:'시간을 0개월→끝까지',
 params:[['tot','미리 낸 금액',60,1200,60,300,W_],['m','나눠 쓸 기간',2,12,1,6,function(v){return v+'개월'}],['t','지난 개월 수',0,12,1,1,function(v){return v+'개월'}]],
 f:function(q){var t=Math.min(q.t,q.m),mon=q.tot/q.m,used=mon*t,left=q.tot-used,xs=seqv(0,q.m,q.m+1);
  return {k:[[W_(mon)+' 원','한 달 비용','i'],[W_(used)+' 원','지금까지 비용이 된 금액','r'],[W_(left)+' 원','남은 선급비용 (자산)','g'],[Math.round(t/q.m*100)+'%','진행률','a']],
   c:[{title:'남은 선급비용 (만 원)',xs:xs,ys:[{n:'선급비용 잔액',d:xs.map(function(x){return q.tot-mon*x}),c:COL.g,fill:true}],fy:W_,fx:function(v){return v+'개월'},ymin:0,mark:{x:t,y:left,l:'지금'},xl:'지난 개월 수'},
      {t:'bar',title:'지금의 나눔 (만 원)',vals:[used,left],labels:['비용 (손익계산서)','선급비용 (재무상태표)'],cols:[COL.r,COL.g],fy:W_,ymax:q.tot*1.18}],
   note:[['i','현금 '+W_(q.tot)+' 원은 처음에 한 번 나갔어요. 그 뒤로는 현금이 움직이지 않고, 달마다 '+W_(mon)+' 원씩 자산이 비용으로 옮겨집니다.'],[left===0?'g':'a',left===0?'기간이 끝나 선급비용이 0이 됐어요. 전액이 비용이 됐습니다.':'아직 '+W_(left)+' 원어치 광고를 받을 권리가 남아 있어요.']]}}};
DASHES['04']={tag:'4주차',title:'감가상각 대시보드',sub:'같은 오븐, 두 가지 나누는 법 — 정액법과 정률법',play:'t',playLabel:'1년차→마지막 해로',
 params:[['c','취득원가',500,5000,100,1500,W_],['n','쓰는 기간(내용연수)',3,10,1,5,function(v){return v+'년'}],['r','정률법 상각률',10,50,1,30,function(v){return v+'%'}],['t','몇 년차',1,10,1,1,function(v){return v+'년차'}]],
 f:function(q){var t=Math.min(q.t,q.n),sl=q.c/q.n,xs=seqv(1,q.n,q.n),r=q.r/100,db=xs.map(function(y){return q.c*Math.pow(1-r,y-1)*r}),bs=xs.map(function(y){return q.c-sl*y}),bd=xs.map(function(y){return q.c*Math.pow(1-r,y)});
  return {k:[[W_(sl)+' 원','정액법 '+t+'년차 상각비','i'],[W_(db[t-1])+' 원','정률법 '+t+'년차 상각비','m'],[W_(bs[t-1])+' 원','정액법 장부가액','g'],[W_(bd[t-1])+' 원','정률법 장부가액','a']],
   c:[{title:'해마다 비용으로 보내는 금액 (만 원)',xs:xs,ys:[{n:'정액법',d:xs.map(function(){return sl}),c:COL.i},{n:'정률법',d:db,c:COL.m}],fy:W_,fx:function(v){return v+'년'},ymin:0,mark:{x:t,l:t+'년차'}},
      {title:'남은 장부가액 (만 원)',xs:xs,ys:[{n:'정액법',d:bs,c:COL.i},{n:'정률법',d:bd,c:COL.m}],fy:W_,fx:function(v){return v+'년'},ymin:0,mark:{x:t,l:t+'년차'}}],
   note:[['i','정액법은 매년 '+W_(sl)+' 원으로 같아요. '+q.n+'년 뒤 장부가액은 0이 됩니다.'],[db[t-1]>sl?'m':'a',db[t-1]>sl?t+'년차에는 정률법 비용이 더 커요. 앞쪽 해의 이익이 더 작게 나옵니다.':t+'년차에는 정률법 비용이 더 작아요. 정률법은 '+q.n+'년 뒤에도 '+W_(bd[q.n-1])+' 원이 남습니다.']]}}};
DASHES['05']={tag:'5주차',title:'평균과 중앙값 대시보드',sub:'청구 8건 중 한 건이 유난히 클 때 — 평균만 보면 속는 이유',play:'x',playLabel:'큰 청구를 100만→3,000만 원으로',
 params:[['x','여덟 번째 청구 금액',100,3000,50,1200,W_]],
 f:function(q){var a=[120,150,90,200,130,160,110,q.x],s=a.reduce(function(p,v){return p+v},0),m=s/8,b=a.slice().sort(function(x,y){return x-y}),med=(b[3]+b[4])/2;
  return {k:[['8건','건수 — len','i'],[W_(s)+' 원','합계 — sum','g'],[W_(m)+' 원','평균 — mean','r'],[W_(med)+' 원','중앙값 — median','a']],
   c:[{t:'bar',title:'청구 8건 (만 원)',vals:a,labels:['1','2','3','4','5','6','7','8'],cols:a.map(function(v,i){return i===7?COL.r:COL.s}),fy:W_},
      {t:'bar',title:'대표값 두 가지 (만 원)',vals:[m,med],labels:['평균','중앙값'],cols:[COL.r,COL.a],fy:W_}],
   note:[['r','평균 '+W_(m)+' 원은 큰 청구 한 건에 끌려가요. 나머지 7건은 모두 200만 원 이하입니다.'],['a','중앙값 '+W_(med)+' 원은 거의 움직이지 않아요. 그래서 표를 받으면 평균 하나가 아니라 분포 요약을 함께 봅니다.']]}}};
DASHES['08']={tag:'8주차',title:'재고 평가 대시보드',sub:'같은 재고, 같은 판매 — 물가가 오를 때 방법에 따라 이익이 얼마나 달라지나',play:'d',playLabel:'매입 단가 변화를 −10원→+20원으로',
 params:[['d','매입할 때마다 단가 변화',-10,20,1,10,function(v){return (v>0?'+':'')+v+'원'}]],
 f:function(q){function g(d){var tot=16000+150*d,fi=8000+10*(80+d),li=50*(80+2*d)+50*(80+d)+800,av=tot/200*110;return [21000-fi,21000-av,21000-li,fi,av,li,tot]}var o=g(q.d),xs=seqv(-10,20,31);
  return {k:[[nf(o[3])+'원','선입선출법 매출원가','i'],[nf(Math.round(o[4]))+'원','총평균법 매출원가','g'],[nf(o[5])+'원','후입선출법 매출원가','m'],[nf(o[0]-o[2])+'원','선입선출 − 후입선출 이익 차이','r']],
   c:[{t:'bar',title:'방법별 매출총이익 (원)',vals:[o[0],o[1],o[2]],labels:['선입선출','총평균','후입선출'],cols:[COL.i,COL.g,COL.m],fy:function(v){return nf(Math.round(v))}},
      {title:'단가 변화에 따른 매출총이익 (원)',xs:xs,ys:[{n:'선입선출',d:xs.map(function(x){return g(x)[0]}),c:COL.i},{n:'총평균',d:xs.map(function(x){return g(x)[1]}),c:COL.g},{n:'후입선출',d:xs.map(function(x){return g(x)[2]}),c:COL.m}],fy:function(v){return nf(Math.round(v))},fx:function(v){return v+'원'},mark:{x:q.d,l:'지금'},xl:'매입 단가 변화'}],
   note:[[q.d>0?'i':q.d<0?'m':'g',q.d>0?'물가가 오를 때는 선입선출법의 이익이 가장 커요. 싼 옛 재고가 먼저 비용이 되기 때문입니다.':q.d<0?'물가가 내릴 때는 순서가 뒤집혀 후입선출법의 이익이 가장 커요.':'단가가 그대로면 세 방법의 결과가 같아요.'],['a','어느 방법이든 매출원가 + 기말재고 = '+nf(o[6])+'원(판매 가능한 재고 전체)으로 같습니다. 나누는 자리만 달라요.']]}}};
DASHES['09']={tag:'9주차',title:'매출채권 회전 대시보드',sub:'연 매출 1,200억 원 회사 — 회수기간이 바뀌면 묶이는 돈이 얼마나 달라지나',play:'w',playLabel:'회수기간을 1주→13주로',
 params:[['s','연간 매출액',400,3000,100,1200,function(v){return nf(v)+'억'}],['w','평균 회수기간',1,13,1,5,function(v){return v+'주'}]],
 f:function(q){var wk=q.s/52,ar=wk*q.w,to=q.s/ar,xs=seqv(1,13,13);
  return {k:[[X1(wk)+'억','1주 평균 매출','i'],[X1(ar)+'억','매출채권 잔액','a'],[X1(to)+'회','매출채권 회전율','g'],[(ar-wk*5>=0?'+':'')+X1(ar-wk*5)+'억','5주일 때보다 묶인 돈','r']],
   c:[{title:'회수기간과 매출채권 잔액 (억 원)',xs:xs,ys:[{n:'매출채권',d:xs.map(function(x){return wk*x}),c:COL.a,fill:true}],fy:X1,fx:function(v){return v+'주'},ymin:0,mark:{x:q.w,y:ar,l:'지금'},xl:'회수기간'},
      {title:'회수기간과 회전율 (회)',xs:xs,ys:[{n:'회전율',d:xs.map(function(x){return 52/x}),c:COL.g}],fy:X1,fx:function(v){return v+'주'},ymin:0,mark:{x:q.w,y:to,l:'지금'},xl:'회수기간'}],
   note:[['g','회전율 '+X1(to)+'회는 52주 ÷ '+q.w+'주와 같아요. 회전율과 회수기간은 같은 정보를 뒤집어 본 것입니다.'],['a','회수가 1주 늦어질 때마다 '+X1(wk)+'억 원이 더 묶여요. 매출은 그대로인데 현금만 늦게 들어옵니다.']]}}};
DASHES['10']={tag:'10주차',title:'간접법 대시보드',sub:'당기순이익 ₩170에서 출발해 영업활동 현금흐름까지 (교안의 서울(주) 예제)',play:'ar',playLabel:'매출채권 증가를 0→300으로',
 params:[['ar','매출채권 증가',0,300,10,100,function(v){return '₩'+v}],['dep','감가상각비',0,200,10,80,function(v){return '₩'+v}],['ap','매입채무·미지급급여 증가',0,200,10,90,function(v){return '₩'+v}]],
 f:function(q){function o(ar){return 170+q.dep-10-(ar+20)+60+q.ap}var v=o(q.ar),xs=seqv(0,300,31);
  return {k:[['₩170','당기순이익 (출발점)','i'],['₩'+nf(v),'영업활동 현금흐름','g'],[(v-170>=0?'+':'')+nf(v-170),'이익과 현금의 차이',v>=170?'a':'r'],[X1(v/170)+'배','영업현금흐름 ÷ 순이익','m']],
   c:[{t:'bar',title:'순이익에서 현금까지 더하고 뺀 것 (₩)',vals:[170,q.dep,60+q.ap,q.ar+20+10,Math.max(0,v)],labels:['순이익','+감가상각','+재고↓·부채↑','−채권↑·선급↑·처분이익','영업현금'],cols:[COL.i,COL.g,COL.g,COL.r,COL.s],fy:function(x){return nf(x)}},
      {title:'매출채권이 늘수록 줄어드는 영업현금흐름 (₩)',xs:xs,ys:[{n:'영업활동 현금흐름',d:xs.map(o),c:COL.g}],fy:function(x){return nf(x)},fx:function(x){return x},hline:170,hlabel:'당기순이익 170',mark:{x:q.ar,y:v,l:'지금'},xl:'매출채권 증가'}],
   note:[['g','감가상각비 ₩'+q.dep+'은 비용이지만 현금이 나가지 않아 다시 더해요.'],[v<170?'r':'a',v<170?'영업현금흐름이 순이익보다 작아요. 이익은 났지만 외상으로 깔린 돈이 많다는 신호입니다.':'영업현금흐름이 순이익보다 '+nf(v-170)+' 커요. 처음 값(100·80·90)에서는 교안과 같은 ₩270입니다.']]}}};
