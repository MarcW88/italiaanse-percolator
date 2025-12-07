const fs = require('fs');
const path = require('path');

// Configuration des marques et leurs liens
const brandConfig = {
    'Bialetti': {
        url: '../marques/bialetti/index.html',
        anchors: ['bialetti percolator', 'bialetti percolatoren', 'bialetti', 'Bialetti percolator', 'Bialetti percolatoren', 'Bialetti']
    },
    'Alessi': {
        url: '../marques/alessi/index.html', 
        anchors: ['alessi percolator', 'alessi percolatoren', 'alessi', 'Alessi percolator', 'Alessi percolatoren', 'Alessi']
    },
    'Grosche': {
        url: '../marques/grosche/index.html',
        anchors: ['grosche percolator', 'grosche percolatoren', 'grosche', 'Grosche percolator', 'Grosche percolatoren', 'Grosche']
    }
};

function addBrandLinksToProduct(filePath) {
    if (!fs.existsSync(filePath)) {
        return { success: false, reason: 'File not found' };
    }
    
    let content = fs.readFileSync(filePath, 'utf8');
    const originalContent = content;
    let changes = [];
    
    // Séparer le head et le body pour ne traiter que le body
    const headEndIndex = content.indexOf('</head>');
    if (headEndIndex === -1) {
        return { success: false, reason: 'Invalid HTML structure' };
    }
    
    const headContent = content.substring(0, headEndIndex + 7);
    let bodyContent = content.substring(headEndIndex + 7);
    
    // Trouver la section de description du produit (généralement entre des balises spécifiques)
    const descriptionRegex = /<div[^>]*class="[^"]*description[^"]*"[^>]*>(.*?)<\/div>/gis;
    const productInfoRegex = /<div[^>]*style="[^"]*"[^>]*>\s*<p[^>]*>(.*?)<\/p>/gis;
    
    // Fonction pour traiter le texte et ajouter les liens de marque
    function processTextForBrandLinks(text, brandName) {
        const brand = brandConfig[brandName];
        if (!brand) return text;
        
        let processedText = text;
        let hasLink = false;
        
        // Vérifier si un lien vers cette marque existe déjà
        const existingLinkRegex = new RegExp(`<a[^>]+href="[^"]*marques/${brandName.toLowerCase()}[^"]*"`, 'i');
        if (existingLinkRegex.test(processedText)) {
            return processedText; // Lien déjà présent
        }
        
        // Chercher les ancres dans l'ordre de préférence
        for (const anchor of brand.anchors) {
            if (hasLink) break;
            
            // Regex pour trouver l'ancre qui n'est pas déjà dans un lien
            const anchorRegex = new RegExp(`(?<!<a[^>]*>[^<]*)\\b(${anchor.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})\\b(?![^<]*<\/a>)`, 'gi');
            
            const matches = [...processedText.matchAll(anchorRegex)];
            if (matches.length > 0) {
                // Remplacer seulement la première occurrence
                let replaced = false;
                processedText = processedText.replace(anchorRegex, (match, p1) => {
                    if (!replaced && !hasLink) {
                        replaced = true;
                        hasLink = true;
                        changes.push(`${p1} → lien vers ${brandName}`);
                        return `<a href="${brand.url}" style="color: #D2691E; text-decoration: none; font-weight: 600;">${p1}</a>`;
                    }
                    return match;
                });
                break;
            }
        }
        
        return processedText;
    }
    
    // Traiter toutes les marques sur le contenu du body seulement
    Object.keys(brandConfig).forEach(brandName => {
        bodyContent = processTextForBrandLinks(bodyContent, brandName);
    });
    
    // Reconstituer le contenu complet
    const newContent = headContent + bodyContent;
    
    if (newContent !== originalContent) {
        fs.writeFileSync(filePath, newContent, 'utf8');
        return { success: true, changes: changes };
    }
    
    return { success: false, reason: 'No changes needed' };
}

function processAllProductPages() {
    console.log('🔗 Ajout de liens marques dans toutes les pages produits...\n');
    
    const productsDir = '/Users/marc/Desktop/italiaanse-percolator/producten';
    
    if (!fs.existsSync(productsDir)) {
        console.log('❌ Dossier producten non trouvé');
        return;
    }
    
    const productFiles = fs.readdirSync(productsDir)
        .filter(file => file.endsWith('.html'))
        .sort();
    
    console.log(`📄 ${productFiles.length} pages produits trouvées\n`);
    
    let processedCount = 0;
    let changedCount = 0;
    let totalChanges = 0;
    
    productFiles.forEach(file => {
        const filePath = path.join(productsDir, file);
        const result = addBrandLinksToProduct(filePath);
        
        processedCount++;
        
        if (result.success) {
            changedCount++;
            totalChanges += result.changes.length;
            console.log(`✅ ${file}`);
            result.changes.forEach(change => {
                console.log(`   • ${change}`);
            });
            console.log('');
        } else if (result.reason !== 'No changes needed') {
            console.log(`❌ ${file}: ${result.reason}`);
        }
    });
    
    console.log(`\n📊 Résumé:`);
    console.log(`   • ${processedCount} pages produits traitées`);
    console.log(`   • ${changedCount} pages modifiées`);
    console.log(`   • ${totalChanges} liens marques ajoutés`);
    
    if (changedCount > 0) {
        console.log(`\n🎉 Liens marques ajoutés avec succès!`);
        console.log(`💡 Les mentions de marques dans les descriptions pointent maintenant vers les hubs correspondants.`);
    } else {
        console.log(`\n✅ Aucune modification nécessaire - les liens sont déjà en place.`);
    }
}

// Fonction pour créer un exemple de ce qui sera fait
function showExample() {
    console.log('📝 Exemple de transformation:\n');
    
    console.log('AVANT:');
    console.log('   "De Bialetti Moka Express is de klassieke percolator..."');
    console.log('   "Alessi staat bekend om zijn design percolatoren..."');
    console.log('   "Grosche biedt moderne alternatieven..."');
    
    console.log('\nAPRÈS:');
    console.log('   "De <a href="../marques/bialetti/index.html">Bialetti</a> Moka Express is de klassieke percolator..."');
    console.log('   "<a href="../marques/alessi/index.html">Alessi</a> staat bekend om zijn design percolatoren..."');
    console.log('   "<a href="../marques/grosche/index.html">Grosche</a> biedt moderne alternatieven..."');
    
    console.log('\n🎯 Règles appliquées:');
    console.log('   • Un seul lien par marque par page');
    console.log('   • Priorité aux ancres "bialetti percolator", "alessi percolator", etc.');
    console.log('   • Style cohérent: couleur #D2691E, pas de soulignement');
    console.log('   • Liens relatifs vers les hubs marques');
}

// Fonction pour tester sur un fichier spécifique
function testOnFile(filename) {
    console.log(`🧪 Test sur ${filename}...\n`);
    
    const filePath = `/Users/marc/Desktop/italiaanse-percolator/producten/${filename}`;
    const result = addBrandLinksToProduct(filePath);
    
    if (result.success) {
        console.log(`✅ Modifications appliquées:`);
        result.changes.forEach(change => {
            console.log(`   • ${change}`);
        });
    } else {
        console.log(`ℹ️  ${result.reason}`);
    }
}

function main() {
    const args = process.argv.slice(2);
    
    if (args.includes('--example')) {
        showExample();
    } else if (args.includes('--test') && args[1]) {
        testOnFile(args[1]);
    } else {
        console.log('🚀 Ajout automatique de liens marques dans les descriptions produits\n');
        processAllProductPages();
    }
}

if (require.main === module) {
    main();
}

module.exports = { addBrandLinksToProduct, processAllProductPages };
