const fs = require('fs');
const path = require('path');

// Configuration
const IMAGES_DIR = '/Users/marc/Desktop/italiaanse-percolator/Images';
const PRODUCTS_JSON = '/Users/marc/Desktop/italiaanse-percolator/all_products.json';
const PRODUCTEN_DIR = '/Users/marc/Desktop/italiaanse-percolator/producten';

// Fonction pour normaliser les noms de fichiers
function normalizeFileName(name) {
    return name
        .toLowerCase()
        .replace(/[àáâãäå]/g, 'a')
        .replace(/[èéêë]/g, 'e')
        .replace(/[ìíîï]/g, 'i')
        .replace(/[òóôõö]/g, 'o')
        .replace(/[ùúûü]/g, 'u')
        .replace(/[ç]/g, 'c')
        .replace(/[ñ]/g, 'n')
        .replace(/[^a-z0-9]/g, '-')
        .replace(/-+/g, '-')
        .replace(/^-|-$/g, '');
}

// Fonction pour créer un mapping des images
function createImageMapping() {
    console.log('🖼️  Création du mapping des images...');
    
    const imageFiles = fs.readdirSync(IMAGES_DIR)
        .filter(file => file.match(/\.(jpg|jpeg|png|webp)$/i))
        .filter(file => !file.startsWith('.'));
    
    console.log(`📁 ${imageFiles.length} images trouvées dans le dossier Images`);
    
    // Créer un mapping basé sur les noms de fichiers
    const imageMapping = {};
    
    imageFiles.forEach(imageFile => {
        const baseName = path.basename(imageFile, path.extname(imageFile));
        const normalizedName = normalizeFileName(baseName);
        
        // Essayer différentes variations du nom
        const variations = [
            normalizedName,
            normalizedName.replace(/\s+/g, '-'),
            normalizedName.replace(/-+/g, '-'),
            baseName.toLowerCase().replace(/\s+/g, '-').replace(/[^a-z0-9-]/g, '-')
        ];
        
        variations.forEach(variation => {
            if (!imageMapping[variation]) {
                imageMapping[variation] = imageFile;
            }
        });
        
        console.log(`   • ${imageFile} → variations: ${variations.slice(0, 2).join(', ')}`);
    });
    
    return { imageMapping, imageFiles };
}

// Fonction pour mettre à jour le JSON des produits
function updateProductsJSON(imageMapping) {
    console.log('\n📝 Mise à jour du fichier products JSON...');
    
    if (!fs.existsSync(PRODUCTS_JSON)) {
        console.log('❌ Fichier all_products.json non trouvé');
        return [];
    }
    
    const products = JSON.parse(fs.readFileSync(PRODUCTS_JSON, 'utf8'));
    let updatedCount = 0;
    
    products.forEach(product => {
        const productSlug = product.slug;
        const productName = normalizeFileName(product.name);
        
        // Chercher une image correspondante
        let matchedImage = null;
        
        // Essayer différentes stratégies de matching
        const searchTerms = [
            productSlug,
            productName,
            productSlug.replace(/-/g, ''),
            productName.replace(/-/g, ''),
            // Extraire les mots clés principaux
            productSlug.split('-').slice(0, 4).join('-'),
            productName.split('-').slice(0, 4).join('-')
        ];
        
        for (const term of searchTerms) {
            if (imageMapping[term]) {
                matchedImage = imageMapping[term];
                break;
            }
            
            // Recherche partielle
            const partialMatch = Object.keys(imageMapping).find(key => 
                key.includes(term) || term.includes(key)
            );
            if (partialMatch && !matchedImage) {
                matchedImage = imageMapping[partialMatch];
            }
        }
        
        if (matchedImage) {
            const oldImage = product.image;
            product.image = `Images/${matchedImage}`;
            
            console.log(`   ✅ ${product.name}`);
            console.log(`      ${oldImage} → ${product.image}`);
            updatedCount++;
        } else {
            console.log(`   ❌ Aucune image trouvée pour: ${product.name}`);
        }
    });
    
    // Sauvegarder le JSON mis à jour
    fs.writeFileSync(PRODUCTS_JSON, JSON.stringify(products, null, 2), 'utf8');
    console.log(`\n✅ ${updatedCount} produits mis à jour dans all_products.json`);
    
    return products;
}

// Fonction pour mettre à jour les pages produits HTML
function updateProductPages(products, imageMapping) {
    console.log('\n🔧 Mise à jour des pages produits HTML...');
    
    if (!fs.existsSync(PRODUCTEN_DIR)) {
        console.log('❌ Dossier producten non trouvé');
        return;
    }
    
    const htmlFiles = fs.readdirSync(PRODUCTEN_DIR)
        .filter(file => file.endsWith('.html'));
    
    console.log(`📄 ${htmlFiles.length} pages produits trouvées`);
    
    let updatedPages = 0;
    
    htmlFiles.forEach(htmlFile => {
        const filePath = path.join(PRODUCTEN_DIR, htmlFile);
        const slug = path.basename(htmlFile, '.html');
        
        // Trouver le produit correspondant
        const product = products.find(p => p.slug === slug);
        
        if (product && product.image && product.image.startsWith('Images/')) {
            let content = fs.readFileSync(filePath, 'utf8');
            
            // Chercher et remplacer les références d'images
            const imageRegex = /<img[^>]+src=["']([^"']*)[^>]*>/gi;
            let hasChanges = false;
            
            content = content.replace(imageRegex, (match, src) => {
                // Si c'est une image de produit (pas les icônes, etc.)
                if (src.includes('Images/') && !src.includes('icon') && !src.includes('logo')) {
                    const newSrc = `../${product.image}`;
                    if (src !== newSrc) {
                        console.log(`      ${src} → ${newSrc}`);
                        hasChanges = true;
                        return match.replace(src, newSrc);
                    }
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

// Fonction principale
function main() {
    console.log('🚀 Mise à jour des images produits...\n');
    
    try {
        // 1. Créer le mapping des images
        const { imageMapping, imageFiles } = createImageMapping();
        
        // 2. Mettre à jour le JSON des produits
        const products = updateProductsJSON(imageMapping);
        
        // 3. Mettre à jour les pages HTML des produits
        updateProductPages(products, imageMapping);
        
        // 4. Statistiques finales
        console.log('\n📊 Résumé:');
        console.log(`   • ${imageFiles.length} images disponibles`);
        console.log(`   • ${products.length} produits dans la base`);
        console.log(`   • Images mises à jour avec succès`);
        
        console.log('\n🎉 Mise à jour terminée avec succès!');
        console.log('\n💡 Prochaines étapes:');
        console.log('   1. Vérifiez la boutique: les nouvelles images apparaissent');
        console.log('   2. Vérifiez quelques pages produits individuelles');
        console.log('   3. Commitez les changements si tout est correct');
        
    } catch (error) {
        console.error('❌ Erreur lors de la mise à jour:', error);
        process.exit(1);
    }
}

// Fonction pour afficher les correspondances trouvées
function showImageMatches() {
    console.log('🔍 Analyse des correspondances possibles...\n');
    
    const { imageMapping } = createImageMapping();
    const products = JSON.parse(fs.readFileSync(PRODUCTS_JSON, 'utf8'));
    
    console.log('Correspondances trouvées:');
    products.forEach(product => {
        const productSlug = product.slug;
        const searchTerms = [productSlug, normalizeFileName(product.name)];
        
        const matches = searchTerms.map(term => {
            const exactMatch = imageMapping[term];
            if (exactMatch) return { term, image: exactMatch, type: 'exact' };
            
            const partialMatch = Object.keys(imageMapping).find(key => 
                key.includes(term.split('-')[0]) && key.includes(term.split('-')[1])
            );
            if (partialMatch) return { term, image: imageMapping[partialMatch], type: 'partial' };
            
            return null;
        }).filter(Boolean);
        
        if (matches.length > 0) {
            console.log(`✅ ${product.name}`);
            matches.forEach(match => {
                console.log(`   → ${match.image} (${match.type})`);
            });
        } else {
            console.log(`❌ ${product.name} (aucune correspondance)`);
        }
    });
}

// Exécuter selon l'argument
if (process.argv.includes('--analyze')) {
    showImageMatches();
} else {
    main();
}

module.exports = { main, createImageMapping, updateProductsJSON };
