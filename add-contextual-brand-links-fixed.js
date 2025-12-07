const fs = require('fs');
const path = require('path');

// Configuration des marques et leurs liens
const brandConfig = {
    'Bialetti': {
        url: '../marques/bialetti/index.html',
        patterns: [
            /\bBialetti\b(?!\s*<\/a>)/g,  // Bialetti pas déjà dans un lien
            /\bbialetti\b(?!\s*<\/a>)/g   // bialetti minuscule
        ]
    },
    'Alessi': {
        url: '../marques/alessi/index.html',
        patterns: [
            /\bAlessi\b(?!\s*<\/a>)/g,
            /\balessi\b(?!\s*<\/a>)/g
        ]
    },
    'Grosche': {
        url: '../marques/grosche/index.html',
        patterns: [
            /\bGrosche\b(?!\s*<\/a>)/g,
            /\bgrosche\b(?!\s*<\/a>)/g
        ]
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
    
    // Pour chaque marque
    Object.entries(brandConfig).forEach(([brandName, config]) => {
        let hasAddedLink = false;
        
        // Vérifier si un lien vers cette marque existe déjà dans les descriptions
        const existingLinkRegex = new RegExp(`<a[^>]+href="[^"]*marques/${brandName.toLowerCase()}[^"]*"[^>]*>${brandName}`, 'i');
        if (existingLinkRegex.test(bodyContent)) {
            return; // Lien déjà présent pour cette marque
        }
        
        // Essayer chaque pattern pour cette marque
        config.patterns.forEach(pattern => {
            if (hasAddedLink) return;
            
            const matches = [...bodyContent.matchAll(pattern)];
            if (matches.length > 0) {
                // Prendre la première occurrence qui n'est pas déjà dans un lien
                for (const match of matches) {
                    const beforeMatch = bodyContent.substring(0, match.index);
                    const afterMatch = bodyContent.substring(match.index + match[0].length);
                    
                    // Vérifier qu'on n'est pas déjà dans un lien
                    const lastOpenTag = beforeMatch.lastIndexOf('<a ');
                    const lastCloseTag = beforeMatch.lastIndexOf('</a>');
                    
                    if (lastOpenTag > lastCloseTag) {
                        continue; // On est dans un lien, passer au suivant
                    }
                    
                    // Ajouter le lien
                    const linkedText = `<a href="${config.url}" style="color: #D2691E; text-decoration: none; font-weight: 600;">${match[0]}</a>`;
                    bodyContent = beforeMatch + linkedText + afterMatch;
                    
                    changes.push(`${match[0]} → lien vers ${brandName}`);
                    hasAddedLink = true;
                    break;
                }
            }
        });
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
    console.log('🔗 Ajout de liens marques contextuels dans toutes les pages produits...\n');
    
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
        console.log(`\n🎉 Liens marques contextuels ajoutés avec succès!`);
        console.log(`💡 Les mentions de marques dans les descriptions pointent maintenant vers les hubs correspondants.`);
    } else {
        console.log(`\n✅ Aucune modification nécessaire - les liens sont déjà en place.`);
    }
}

// Test sur un fichier spécifique pour debug
function testOnSpecificFile(filename) {
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
    
    // Montrer un extrait du contenu modifié
    if (fs.existsSync(filePath)) {
        const content = fs.readFileSync(filePath, 'utf8');
        const descriptionMatch = content.match(/<h3[^>]*>Productbeschrijving<\/h3>\s*<p[^>]*>(.*?)<\/p>/s);
        if (descriptionMatch) {
            console.log(`\n📝 Description après modification:`);
            console.log(`"${descriptionMatch[1].substring(0, 200)}..."`);
        }
    }
}

function main() {
    const args = process.argv.slice(2);
    
    if (args.includes('--test') && args[1]) {
        testOnSpecificFile(args[1]);
    } else {
        console.log('🚀 Ajout de liens marques contextuels - Version corrigée\n');
        processAllProductPages();
    }
}

if (require.main === module) {
    main();
}

module.exports = { addBrandLinksToProduct, processAllProductPages };
