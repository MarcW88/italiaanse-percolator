const fs = require('fs');

// Mapping manuel précis des images ajoutées
const manualImageMapping = {
    // Images avec noms exacts
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
    
    // Images existantes à utiliser pour d'autres produits
    "bialetti-moka-express-percolator-3-kops-aluminium": "bialetti-moka-express-1.jpg",
    "bialetti-moka-express-percolator-6-kops-aluminium": "bialetti-moka-express-2.jpg",
    "bialetti-moka-express-percolator-4-kops-aluminium": "bialetti-moka-express-3.jpg",
    "bialetti-moka-express-percolator-1-kops-aluminium": "bialetti-moka-express-4.jpg",
    "bialetti-moka-express-percolator-2-kops-aluminium": "bialetti-moka-express-5.jpg",
    
    // Venus series
    "bialetti-venus-copper-percolator-6-kops-roestvrijstaal-inductiegeschikt": "bialetti_venus.jpg",
    "bialetti-venus-copper-percolator-4-kops-roestvrijstaal-inductiegeschikt": "bialetti_venus_2.jpg",
    "bialetti-venus-copper-percolator-2-kops-roestvrijstaal": "bialetti_venus_3.jpg",
    "bialetti-percolator-venus-6-kops-roestvrijstaal-inductiegeschikt": "bialetti_venus.jpg",
    "bialetti-percolator-venus-2-kops-roestvrijstaal": "bialetti_venus_3.jpg",
    
    // Alpina series
    "bialetti-moka-alpina-limited-editions-3-kops-120ml": "Bialetti Moka Alpina Limited Editions 3 Kops 120Ml .jpg",
    
    // Autres modèles avec images existantes
    "bialetti-fiammetta": "bialetti_fiammetta.jpg",
    "alessi-pulcina": "alessi_pulcina.jpg"
};

function updateProductsWithManualMapping() {
    console.log('🎯 Mise à jour avec mapping manuel précis...\n');
    
    const PRODUCTS_JSON = '/Users/marc/Desktop/italiaanse-percolator/all_products.json';
    
    if (!fs.existsSync(PRODUCTS_JSON)) {
        console.log('❌ Fichier all_products.json non trouvé');
        return;
    }
    
    const products = JSON.parse(fs.readFileSync(PRODUCTS_JSON, 'utf8'));
    let updatedCount = 0;
    
    products.forEach(product => {
        const slug = product.slug;
        
        if (manualImageMapping[slug]) {
            const oldImage = product.image;
            product.image = `Images/${manualImageMapping[slug]}`;
            
            console.log(`✅ ${product.name}`);
            console.log(`   ${oldImage} → ${product.image}`);
            updatedCount++;
        }
    });
    
    // Sauvegarder
    fs.writeFileSync(PRODUCTS_JSON, JSON.stringify(products, null, 2), 'utf8');
    
    console.log(`\n🎉 ${updatedCount} produits mis à jour avec le mapping manuel`);
    console.log(`📊 ${Object.keys(manualImageMapping).length} mappings définis`);
    
    return products;
}

function updateProductPagesWithImages() {
    console.log('\n🔧 Mise à jour des pages produits HTML...');
    
    const PRODUCTEN_DIR = '/Users/marc/Desktop/italiaanse-percolator/producten';
    const products = JSON.parse(fs.readFileSync('/Users/marc/Desktop/italiaanse-percolator/all_products.json', 'utf8'));
    
    let updatedPages = 0;
    
    Object.keys(manualImageMapping).forEach(slug => {
        const htmlFile = `${slug}.html`;
        const filePath = `${PRODUCTEN_DIR}/${htmlFile}`;
        
        if (fs.existsSync(filePath)) {
            const product = products.find(p => p.slug === slug);
            if (!product) return;
            
            let content = fs.readFileSync(filePath, 'utf8');
            const newImagePath = `../Images/${manualImageMapping[slug]}`;
            
            // Remplacer toutes les images de produit
            const imageRegex = /<img[^>]+src=["']([^"']*Images\/[^"']*)[^>]*>/gi;
            let hasChanges = false;
            
            content = content.replace(imageRegex, (match, src) => {
                // Ne pas toucher aux icônes, logos, etc.
                if (src.includes('icon') || src.includes('logo') || src.includes('background')) {
                    return match;
                }
                
                if (src !== newImagePath) {
                    console.log(`   📝 ${htmlFile}: ${src} → ${newImagePath}`);
                    hasChanges = true;
                    return match.replace(src, newImagePath);
                }
                return match;
            });
            
            if (hasChanges) {
                fs.writeFileSync(filePath, content, 'utf8');
                console.log(`   ✅ ${htmlFile} mis à jour`);
                updatedPages++;
            }
        }
    });
    
    console.log(`\n✅ ${updatedPages} pages produits mises à jour`);
}

// Fonction pour vérifier les images manquantes
function checkMissingImages() {
    console.log('🔍 Vérification des images manquantes...\n');
    
    const IMAGES_DIR = '/Users/marc/Desktop/italiaanse-percolator/Images';
    const products = JSON.parse(fs.readFileSync('/Users/marc/Desktop/italiaanse-percolator/all_products.json', 'utf8'));
    
    let missingCount = 0;
    
    products.forEach(product => {
        if (product.image && product.image.startsWith('Images/')) {
            const imagePath = product.image.replace('Images/', '');
            const fullPath = `${IMAGES_DIR}/${imagePath}`;
            
            if (!fs.existsSync(fullPath)) {
                console.log(`❌ Image manquante: ${product.name}`);
                console.log(`   Chemin: ${product.image}`);
                missingCount++;
            }
        }
    });
    
    if (missingCount === 0) {
        console.log('✅ Toutes les images sont présentes!');
    } else {
        console.log(`\n⚠️  ${missingCount} images manquantes trouvées`);
    }
}

// Fonction principale
function main() {
    console.log('🚀 Mise à jour manuelle des images produits...\n');
    
    // 1. Mettre à jour le JSON avec le mapping manuel
    updateProductsWithManualMapping();
    
    // 2. Mettre à jour les pages HTML
    updateProductPagesWithImages();
    
    // 3. Vérifier les images manquantes
    checkMissingImages();
    
    console.log('\n🎉 Mise à jour terminée!');
    console.log('\n💡 Vérifiez maintenant:');
    console.log('   • La page boutique (nouvelles images)');
    console.log('   • Quelques pages produits individuelles');
    console.log('   • Que toutes les images s\'affichent correctement');
}

if (require.main === module) {
    main();
}

module.exports = { manualImageMapping, updateProductsWithManualMapping };
