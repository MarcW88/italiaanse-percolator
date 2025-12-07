const fs = require('fs');
const path = require('path');

// Mapping des images depuis notre script précédent
const manualImageMapping = {
    "bialetti-brikka-espressopot-aluminium-4-kops-zilver": "Bialetti Brikka Espressopot Aluminium 4 Kops Zilver .jpg",
    "bialetti-brikka-evolution-percolator-2-kops-zwart-aluminium": "Bialetti Brikka Evolution Percolator 2 Kops Zwart Aluminium .jpg",
    "bialetti-brikka-induction-percolator-4-kops-inductiegeschikt": "Bialetti Brikka Induction Percolator 4 Kops Inductiegeschikt .jpg",
    "bialetti-brikka-percolator-2-kops-aluminium": "Bialetti Brikka Percolator 2 Kops Aluminium .jpg",
    "bialetti-cafetiere-preziosa-350ml": "Bialetti Cafetiere Preziosa 350Ml .jpg",
    "bialetti-easy-timer-moka-espressomaker-percolator-6-kops-elektrisch-aluminium": "Bialetti Easy Timer Moka Espressomaker Percolator 6 Kops Elektrisch Aluminium .jpg",
    "bialetti-inductieplaatje-voor-inductiekooplaat-o13cm": "Bialetti Inductieplaatje Voor Inductiekooplaat O13Cm .jpg",
    "bialetti-mini-express-percolator-2-kops-inductiegeschikt-met-2-kopjes": "Bialetti Mini Express Percolator 2 Kops Inductiegeschikt Met 2 Kopjes .jpg",
    "bialetti-mini-express-zwart-2-kops": "Bialetti Mini Express Zwart 2 Kops .jpg",
    "bialetti-moka-inductie-rood-4-kops-150ml-bialetti-koffie-proefpakket-3-x-250gr": "Bialetti Moka Inductie Rood 4 Kops 150Ml Bialetti Koffie Proefpakket 3 X 250Gr .jpg",
    "bialetti-percolator-onderhoudsset-12-kops": "Bialetti Percolator Onderhoudsset 12 Kops .jpg",
    "bialetti-moka-express-percolator-3-kops-aluminium": "bialetti-moka-express-1.jpg",
    "bialetti-moka-express-percolator-6-kops-aluminium": "bialetti-moka-express-2.jpg",
    "bialetti-moka-express-percolator-4-kops-aluminium": "bialetti-moka-express-3.jpg",
    "bialetti-moka-express-percolator-1-kops-aluminium": "bialetti-moka-express-4.jpg",
    "bialetti-moka-express-percolator-2-kops-aluminium": "bialetti-moka-express-5.jpg",
    "bialetti-venus-copper-percolator-6-kops-roestvrijstaal-inductiegeschikt": "bialetti_venus.jpg",
    "bialetti-venus-copper-percolator-4-kops-roestvrijstaal-inductiegeschikt": "bialetti_venus_2.jpg",
    "bialetti-venus-copper-percolator-2-kops-roestvrijstaal": "bialetti_venus_3.jpg",
    "bialetti-percolator-venus-6-kops-roestvrijstaal-inductiegeschikt": "bialetti_venus.jpg",
    "bialetti-percolator-venus-2-kops-roestvrijstaal": "bialetti_venus_3.jpg",
    "bialetti-moka-alpina-limited-editions-3-kops-120ml": "Bialetti Moka Alpina Limited Editions 3 Kops 120Ml .jpg"
};

function fixMainImagePaths() {
    console.log('🔧 Correction des chemins d\'images principaux...\n');
    
    const PRODUCTEN_DIR = '/Users/marc/Desktop/italiaanse-percolator/producten';
    let fixedCount = 0;
    
    Object.keys(manualImageMapping).forEach(slug => {
        const htmlFile = `${slug}.html`;
        const filePath = `${PRODUCTEN_DIR}/${htmlFile}`;
        
        if (fs.existsSync(filePath)) {
            let content = fs.readFileSync(filePath, 'utf8');
            const correctImagePath = `../Images/${manualImageMapping[slug]}`;
            
            // Chercher et remplacer le src principal de l'image
            const mainImageRegex = /<img\s+src=["']\.\.\/images\/producten\/[^"']*["']/gi;
            
            const originalContent = content;
            content = content.replace(mainImageRegex, (match) => {
                console.log(`   📝 ${htmlFile}: ${match} → src="${correctImagePath}"`);
                return match.replace(/src=["'][^"']*["']/, `src="${correctImagePath}"`);
            });
            
            if (content !== originalContent) {
                fs.writeFileSync(filePath, content, 'utf8');
                console.log(`   ✅ ${htmlFile} corrigé`);
                fixedCount++;
            }
        }
    });
    
    console.log(`\n✅ ${fixedCount} pages corrigées`);
}

function main() {
    console.log('🚀 Correction des chemins d\'images principaux...\n');
    fixMainImagePaths();
    console.log('\n🎉 Correction terminée!');
}

if (require.main === module) {
    main();
}

module.exports = { fixMainImagePaths };
