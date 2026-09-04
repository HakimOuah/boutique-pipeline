/* Lot B : une silhouette seulement, cotes connues et tableau comparatif.
 * Helpers vectoriels repris du P6, sans modifier les photographies sources. */
const fs=require('node:fs'),path=require('node:path'),sharp=require('sharp');
const base=path.resolve(__dirname,'..'),out=path.join(base,'livraisons-visuels-codex/couverture-2026-09-05');
const jobs=require('./lot4-schema-jobs.json'),ink='#24211B',bg='#F6F3EC';
const esc = s => String(s).replaceAll('&','&amp;').replaceAll('<','&lt;');
function text(x,y,s,size=40){return `<text x="${x}" y="${y}" text-anchor="middle" font-size="${size}" fill="${ink}">${esc(s)}</text>`;}
function line(x1,y1,x2,y2,more=''){return `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${ink}" stroke-width="2" ${more}/>`;}
function dim(cx,y,w,label){return line(cx-w/2,y,cx+w/2,y)+line(cx-w/2,y-12,cx-w/2,y+12)+line(cx+w/2,y-12,cx+w/2,y+12)+text(cx,y+65,label,43);}
function vdim(x,y,h,label){return line(x,y,x,y+h)+line(x-10,y,x+10,y)+line(x-10,y+h,x+10,y+h)+`<text x="${x+35}" y="${y+h/2}" transform="rotate(-90 ${x+35} ${y+h/2})" text-anchor="middle" font-size="29" fill="${ink}">${esc(label)}</text>`;}
function cable(cx,top,bottom){const mid=(top+bottom)/2;return line(cx,top,cx,mid-8)+line(cx,mid+8,cx,bottom)+line(cx-10,mid+1,cx+10,mid-12)+line(cx-10,mid+12,cx+10,mid-1);}
function body(type,cx,cy,w,h,id){
  const x=cx-w/2,y=cy-h/2;
  let shape='', details='';
  if(type==='disque') return `<circle cx="${cx}" cy="${cy}" r="${w/2}" fill="#E8DFCF" stroke="${ink}" stroke-width="2.4"/>`;
  if(type==='plisse'){
    shape=`<ellipse cx="${cx}" cy="${cy}" rx="${w/2}" ry="${h/2}"/>`;
    for(let i=-8;i<=8;i++) {const dx=i*w/18; details+=`<path d="M ${cx} ${y} C ${cx+dx*1.36} ${y+h*.12}, ${cx+dx*1.36} ${y+h*.88}, ${cx} ${y+h}" fill="none"/>`;}
  } else if(type==='petales30'){
    // Le SKU Ø30 est une cloche à bordures sombres, pas le pétale ouvert des grands diamètres.
    const p=(a,b)=>`${x+w*a} ${y+h*b}`;
    shape=`<path d="M ${p(.5,0)} C ${p(.25,.2)},${p(.12,.4)},${p(0,.84)} Q ${p(.06,1)},${p(.20,.85)} Q ${p(.32,1.08)},${p(.50,.91)} Q ${p(.68,1.08)},${p(.80,.85)} Q ${p(.94,1)},${p(1,.84)} C ${p(.88,.4)},${p(.75,.2)},${p(.5,0)} Z"/>`;
    for(const a of [.2,.5,.8]) details+=`<path d="M ${p(.5,0)} Q ${p(a,.4)},${p(a,.85)}" fill="none" stroke-width="5"/>`;
  } else if(type==='petales'){
    const p=(a,b)=>`${x+w*a} ${y+h*b}`;
    // Les pétales se recouvrent comme sur la source, sans changer leur nombre entre tailles.
    shape=`<path d="M ${p(.5,0)} C ${p(.24,-.02)},${p(.06,.25)},${p(0,.66)} C ${p(.02,.84)},${p(.18,.72)},${p(.29,.42)} C ${p(.15,.75)},${p(.19,1)},${p(.35,.93)} C ${p(.39,1.03)},${p(.57,1.02)},${p(.65,.93)} C ${p(.81,1)},${p(.85,.75)},${p(.71,.42)} C ${p(.82,.72)},${p(.98,.84)},${p(1,.66)} C ${p(.94,.25)},${p(.76,-.02)},${p(.5,0)} Z"/>`;
    for(const [a,b] of [[.26,.15],[.38,.34],[.5,.51],[.62,.68],[.74,.86]]) details+=`<path d="M ${p(.5,0)} C ${p(a,.18)},${p(a-.06,.66)},${p(b,.76)} C ${p(b+.08,.92)},${p(b+.16,.68)},${p(.5,0)}" fill="none"/>`;
  } else if(type==='double'){
    shape=`<rect x="${x+w*.17}" y="${y}" width="${w*.66}" height="${h}" rx="${w*.10}"/><rect x="${x}" y="${y+h*.22}" width="${w}" height="${h*.56}" rx="${w*.10}"/>`;
  } else if(type==='dome'){
    shape=`<path d="M ${x} ${y+h*.82} C ${x} ${y+h*.22},${x+w*.20} ${y},${cx} ${y} C ${x+w*.80} ${y},${x+w} ${y+h*.22},${x+w} ${y+h*.82} Q ${x+w} ${y+h},${x+w*.92} ${y+h} L ${x+w*.08} ${y+h} Q ${x} ${y+h},${x} ${y+h*.82} Z"/>`;
  }
  const fill=type==='plisse'?bg:`url(#weave)`;
  return `<g fill="${fill}" stroke="${ink}" stroke-width="2.4">${shape}<g stroke-width="1.4">${details}</g></g>`;
}
function bars(cx,cy,w){
  const left=cx-w/2,right=cx+w/2,p1=cx-90,p2=cx+90;
  return `<g fill="${bg}" stroke="${ink}" stroke-width="2.5"><rect x="${cx-112.5}" y="${cy-290}" width="225" height="31.5"/>`+
    cable(p1,cy-265,cy-100)+cable(p2,cy-265,cy-100)+
    `<rect x="${left+w*.38}" y="${cy-25}" width="${w*.62}" height="7"/><rect x="${left}" y="${cy+35}" width="${w*.62}" height="7"/><rect x="${p1-8}" y="${cy-100}" width="16" height="170"/><rect x="${p2-8}" y="${cy-100}" width="16" height="180"/></g>`;
}

function render(j){
 let s='<svg xmlns="http://www.w3.org/2000/svg" width="2048" height="2048"><defs><pattern id="weave" width="20" height="20" patternUnits="userSpaceOnUse"><rect width="20" height="20" fill="#EEE6D7"/><path d="M-10 0L20 30 M0-10L30 20 M-10 20L20-10 M0 30L30 0" stroke="#C0AC89" stroke-width="1"/></pattern></defs><rect width="2048" height="2048" fill="'+bg+'"/><g font-family="Arial, Helvetica, sans-serif">';
 s+=text(1024,130,'Dimensions disponibles',52)+text(1024,200,'Une silhouette de référence · Mesures en cm',30);
 const w=j.type==='goutte'?320:760,h=j.height?w*j.height/j.d:j.type==='plisse'?300:j.type==='double'?560:250,cx=900,cy=700,top=cy-h/2;
 if(j.type==='barres')s+=bars(cx,cy,w);
 else if(j.type==='plafonnier')s+='<rect x="'+(cx-w/2)+'" y="'+top+'" width="'+w+'" height="'+h+'" rx="12" fill="#EAE8E1" stroke="'+ink+'" stroke-width="3"/>';
 else if(j.type==='goutte'){
  s+=cable(cx,280,top-40)+'<rect x="'+(cx-24)+'" y="'+(top-40)+'" width="48" height="40" rx="8" fill="#BD9963"/><path d="M '+cx+' '+top+' C '+(cx-w*.55)+' '+(top+h*.2)+','+(cx-w*.75)+' '+(top+h*.85)+','+cx+' '+(top+h)+' C '+(cx+w*.75)+' '+(top+h*.85)+','+(cx+w*.55)+' '+(top+h*.2)+','+cx+' '+top+' Z" fill="url(#weave)" stroke="'+ink+'" stroke-width="3"/>';
 }else if(j.type==='feston'){
  s+=cable(cx,290,top-35)+'<rect x="'+(cx-25)+'" y="'+(top-35)+'" width="50" height="35" fill="#BCA169"/><path d="M '+cx+' '+top+' C '+(cx-w*.3)+' '+top+','+(cx-w*.5)+' '+(top+h*.4)+','+(cx-w*.5)+' '+(top+h*.85);
  for(let i=0;i<8;i++)s+=' Q '+(cx-w/2+w*(i+.5)/8)+' '+(top+h*1.10)+','+(cx-w/2+w*(i+1)/8)+' '+(top+h*.85);
  s+=' C '+(cx+w*.5)+' '+(top+h*.4)+','+(cx+w*.3)+' '+top+','+cx+' '+top+' Z" fill="#D6DFD2" stroke="'+ink+'" stroke-width="3"/>';
 }else{if(!['disque','montages'].includes(j.type))s+=cable(cx,Math.min(300,top-90),top);s+=body(j.type==='montages'?'dome':j.type,cx,cy,w,j.type==='disque'?w:h,0);}
 const lowest=j.type==='disque'?cy+w/2:cy+h/2;
 s+=dim(cx,Math.max(1060,lowest+40),w,(j.type==='barres'?'L ':'Ø ')+j.d+' cm');
 if(j.height)s+=vdim(cx+w/2+55,top,h,String(j.height).replace('.',',')+' cm');
 s+=text(1024,1240,'Variante / diamètre ou largeur',32)+text(1690,1240,'Hauteur',32);
 const scale=360/Math.max(...j.widths);
 j.rows.forEach((r,i)=>{const y=1345+i*125;s+=text(640,y,r[0],34)+text(1690,y,r[1],34)+line(1120,y-12,1120+j.widths[i]*scale,y-12,'style="stroke-width:10"');});
 s+=text(1024,1865,j.note,29)+text(1024,1920,'Traits comparatifs à la même échelle · Silhouette indicative',27)+text(1024,1970,'— : cote non documentée · Câble représenté raccourci si présent',25);
 return s+'</g></svg>';
}
(async()=>{for(const j of jobs){const dir=path.join(out,j.h);fs.mkdirSync(dir,{recursive:true});const stem=path.join(dir,j.h+'-schema-g6'),svg=render(j);fs.writeFileSync(stem+'.svg',svg);await sharp(Buffer.from(svg)).jpeg({quality:96,chromaSubsampling:'4:4:4'}).toFile(stem+'.jpg');console.log(j.h);}})().catch(e=>{console.error(e);process.exit(1)});
