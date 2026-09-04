/* Schémas originaux vectoriels : aucune retouche des photos fournisseur.
 * Exécution : NODE_PATH=<packages du runtime> node <ce fichier>
 * Les seules cotes numériques proviennent du brief JSON ou des sources citées.
 * L'échelle des diamètres/largeurs est calculée, les hauteurs inconnues ne sont pas cotées.
 */
const fs = require('node:fs');
const path = require('node:path');
const sharp = require('sharp');
const base = path.resolve(__dirname, '..');
const out = path.join(base, 'livraisons-visuels-codex/variantes-forme');
const ink = '#24211B', bg = '#F6F3EC';
const jobs = [
  {h:'applique-murale-pierre-588683', type:'disque', sizes:[20,25,30], source:'06.jpg', note:'Épaisseur : 4,5 cm', full:true},
  {h:'suspension-moderne-led-noir-330664', type:'barres', sizes:[100,120,150], source:'02.jpg', note:'Hauteurs, câbles et fixation : cotes non documentées'},
  {h:'lustre-salon-blanc-246282', type:'plisse', sizes:[30,40,50,60], source:'04.jpg', note:'Hauteurs, câble et rosace : cotes non documentées'},
  {h:'suspension-rotin-led-761433', type:'petales', sizes:[30,40,50,60], source:'06.jpg', top:'Câble réglable : 120 cm max.', note:'Hauteurs et rosace : cotes non documentées'},
  {h:'suspension-bambou-led-50cm-377816', type:'double', sizes:[30,40,50], source:'05.jpg', top:'Longueur de câble : 150 cm', note:'Hauteurs et rosace : cotes non documentées'},
  {h:'suspension-bambou-655008', type:'dome', sizes:[30,38,45], source:'02.jpg', top:'Câble : 120 cm   ·   Rosace : Ø 10 cm', note:'Hauteurs Ø 30 et Ø 45 cm : non documentées'},
];
const esc = s => String(s).replaceAll('&','&amp;').replaceAll('<','&lt;');
function text(x,y,s,size=40){return `<text x="${x}" y="${y}" text-anchor="middle" font-size="${size}" fill="${ink}">${esc(s)}</text>`;}
function line(x1,y1,x2,y2,more=''){return `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${ink}" stroke-width="2" ${more}/>`;}
function dim(cx,y,w,label){return line(cx-w/2,y,cx+w/2,y)+line(cx-w/2,y-12,cx-w/2,y+12)+line(cx+w/2,y-12,cx+w/2,y+12)+text(cx,y+65,label,43);}
function cable(cx,top,bottom){const mid=(top+bottom)/2;return line(cx,top,cx,mid-8)+line(cx,mid+8,cx,bottom)+line(cx-10,mid+1,cx+10,mid-12)+line(cx-10,mid+12,cx+10,mid-1);}
function body(type,cx,cy,w,h,id){
  const x=cx-w/2,y=cy-h/2;
  let shape='', details='';
  if(type==='disque') return `<circle cx="${cx}" cy="${cy}" r="${w/2}" fill="#E8DFCF" stroke="${ink}" stroke-width="2.4"/>`;
  if(type==='plisse'){
    shape=`<ellipse cx="${cx}" cy="${cy}" rx="${w/2}" ry="${h/2}"/>`;
    for(let i=-8;i<=8;i++) {const dx=i*w/18; details+=`<path d="M ${cx} ${y} C ${cx+dx*1.36} ${y+h*.12}, ${cx+dx*1.36} ${y+h*.88}, ${cx} ${y+h}" fill="none"/>`;}
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
  const left=cx-w/2,right=cx+w/2,p1=cx-w*.09,p2=cx+w*.09;
  return `<g fill="${bg}" stroke="${ink}" stroke-width="2.5"><rect x="${p1-25}" y="${cy-290}" width="${p2-p1+50}" height="25"/>`+
    cable(p1,cy-265,cy-100)+cable(p2,cy-265,cy-100)+
    `<rect x="${left+w*.38}" y="${cy-25}" width="${w*.62}" height="7"/><rect x="${left}" y="${cy+35}" width="${w*.62}" height="7"/><rect x="${p1-8}" y="${cy-100}" width="16" height="170"/><rect x="${p2-8}" y="${cy-100}" width="16" height="180"/></g>`;
}
function render(j){
  let s=`<svg xmlns="http://www.w3.org/2000/svg" width="2048" height="2048" viewBox="0 0 2048 2048"><defs><pattern id="weave" width="20" height="20" patternUnits="userSpaceOnUse"><rect width="20" height="20" fill="#EEE6D7"/><path d="M-10 0L20 30 M0-10L30 20 M-10 20L20-10 M0 30L30 0" stroke="#C0AC89" stroke-width="1"/></pattern></defs><rect width="2048" height="2048" fill="${bg}"/><g font-family="Arial, Helvetica, sans-serif">`;
  s+=text(1024,135,j.type==='barres'?'Comparaison des largeurs':'Comparaison des diamètres',49);
  if(j.top) s+=text(1024,220,j.top,36);
  const geoms=[];
  if(j.type==='barres'){
    for(let i=0;i<3;i++){const w=j.sizes[i]*9,cy=560+i*530;s+=bars(1024,cy,w)+dim(1024,cy+130,w,`${j.sizes[i]} cm`);geoms.push({cm:j.sizes[i],width_px:w,px_per_cm:9});}
  } else if(j.type==='disque'){
    const scale=18,centers=[390,970,1660];
    for(let i=0;i<3;i++){const w=j.sizes[i]*scale;s+=body(j.type,centers[i],940,w,w,i)+dim(centers[i],1340,w,`Ø ${j.sizes[i]} cm`);geoms.push({cm:j.sizes[i],width_px:w,px_per_cm:scale});}
  } else {
    const grid=j.sizes.length===4;
    const scale=grid?11:10;
    const centers=grid?[[540,630],[1480,630],[540,1380],[1480,1380]]:[[390,1050],[990,1050],[1640,1050]];
    for(let i=0;i<j.sizes.length;i++){
      const [cx,cy]=centers[i],d=j.sizes[i],w=d*scale;
      const h=j.type==='plisse'?w*.42:j.type==='double'?w*.92:j.type==='dome'?w*(20/38):w*.40;
      const top=cy-h/2;
      s+=cable(cx,grid?top-180:top-340,top)+body(j.type,cx,cy,w,h,i)+dim(cx,grid?(i<2?920:1710):1450,w,`Ø ${d} cm`);
      if(j.type==='dome'&&d===38){const dx=cx+w/2+37;s+=line(dx,top,dx,top+h)+line(dx-10,top,dx+10,top)+line(dx-10,top+h,dx+10,top+h)+text(dx+75,cy+12,'20 cm',31);}
      geoms.push({cm:d,width_px:w,px_per_cm:scale,height_cm_confirmed:j.type==='dome'&&d===38?20:null});
    }
  }
  s+=text(1024,1910,j.note,34);
  if(!j.full) s+=text(1024,1970,'Échelle comparative des largeurs uniquement',28);
  s+='</g></svg>';
  return {svg:s,geoms};
}
(async()=>{
  const report=[];
  for(const j of jobs){
    const dir=path.join(out,j.h);fs.mkdirSync(dir,{recursive:true});
    const {svg,geoms}=render(j);
    const jpeg=path.join(dir,`${j.h}-schema-g6.jpg`);
    // Ne pas écraser un livrable existant sans contrôle explicite.
    if(fs.existsSync(jpeg)) throw new Error(`Sortie déjà présente : ${jpeg}`);
    fs.writeFileSync(path.join(dir,`${j.h}-schema-g6.svg`),svg);
    await sharp(Buffer.from(svg)).flatten({background:bg}).jpeg({quality:96,chromaSubsampling:'4:4:4'}).toFile(jpeg);
    const ratios=geoms.map(g=>g.width_px/g.cm);
    if(ratios.some(r=>Math.abs(r-ratios[0])>1e-9)) throw new Error('Échelle incohérente');
    report.push({handle:j.h,source:`catalogues/lumierematiere/sources-par-handle/${j.h}/${j.source}`,fichier:jpeg,geometrie:geoms,statut:j.full?'COMPLET':'PARTIEL_COTES_MANQUANTES',echelle:'PASS exacte dans le SVG',note:j.note});
  }
  fs.writeFileSync(path.join(out,'qa-geometrie.json'),JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify(report,null,2));
})().catch(e=>{console.error(e);process.exit(1);});
