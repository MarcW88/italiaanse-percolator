const fs = require('fs');
const path = require('path');

function addBrandLinksToProduct(filePath) {
    if (!fs.existsSync(filePath)) {
        return { success: false, reason: 'File not found' };
    }
    
    let content = fs.readFileSync(filePath, 'utf8');
    const originalContent = content;
    let changes = [];
    
    // Chercher et remplacer les mentions de marques dans les descriptions
    // Seulement si elles ne sont pas déjà dans un lien vers une page marque
    
    // Bialetti
    if (content.includes('Bialetti') && !content.includes('href="../marques/bialetti/index.html">Bialetti')) {
        // Remplacer la première occurrence de "Bialetti" qui n'est pas déjà dans un lien marque
        const bialettiRegex = /\bBialetti\b(?![^<]*<\/a>)(?![^<]*href="[^"]*marques\/bialetti)/;
        if (bialettiRegex.test(content)) {
            content = content.replace(bialettiRegex, '<a href="../marques/bialetti/index.html" style="color: #D2691E; text-decoration: none; font-weight: 600;">Bialetti</a>');
            changes.push('Bialetti → lien vers hub Bialetti');
        }
    }
    
    // Alessi
    if (content.includes('Alessi') && !content.includes('href="../marques/alessi/index.html">Alessi')) {
        const alessiRegex = /\bAlessi\b(?![^<]*<\/a>)(?![^<]*href="[^"]*marques\/alessi)/;
        if (alessiRegex.test(content)) {
            content = content.replace(alessiRegex, '<a href="../marques/alessi/index.html" style="color: #D2691E; text-decoration: none; font-weight: 600;">Alessi</a>');
            changes.push('Alessi → lien vers hub Alessi');
        }
    }
    
    // Grosche
    if (content.includes('Grosche') && !content.includes('href="../marques/grosche/index.html">Grosche')) {
        const groscheRegex = /\bGrosche\b(?![^<]*<\/a>)(?![^<]*href="[^"]*marques\/grosche)/;
        if (groscheRegex.test(content)) {
            content = content.replace(groscheRegex, '<a href="../marques/grosche/index.html" style="color: #D2691E; text-decoration: none; font-weight: 600;">Grosche</a>');
            changes.push('Grosche → lien vers hub Grosche');
        }
    }
    
    if (content !== originalContent) {
        fs.writeFileSync(filePath, content, 'utf8');
        return { success: true, changes: changes };
    }
    
    return { success: false, reason: 'No changes needed' };
}

function processAllProductPages() {
    console.log('🔗 Ajout de liens marques contextuels - Version simplifiée...\n');
    
    const productsDir = '/Users/marc/Desktop/italiaanse-percolator/producten';
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
        }
    });
    
    console.log(`📊 Résumé:`);
    console.log(`   • ${processedCount} pages produits traitées`);
    console.log(`   • ${changedCount} pages modifiées`);
    console.log(`   • ${totalChanges} liens marques ajoutés`);
    
    if (changedCount > 0) {
        console.log(`\n🎉 Liens marques contextuels ajoutés avec succès!`);
        console.log(`💡 Les mentions de marques pointent maintenant vers les hubs correspondants.`);
    }
}

// Test sur un fichier spécifique
function testOnFile(filename) {
    console.log(`🧪 Test sur ${filename}...\n`);
    
    const filePath = `/Users/marc/Desktop/italiaanse-percolator/producten/${filename}`;
    const result = addBrandLinksToProduct(filePath);
    
    if (result.success) {
        console.log(`✅ Modifications appliquées:`);
        result.changes.forEach(change => {
            console.log(`   • ${change}`);
        });
        
        // Montrer la description modifiée
        const content = fs.readFileSync(filePath, 'utf8');
        const descriptionMatch = content.match(/<h3[^>]*>Productbeschrijving<\/h3>\s*<p[^>]*>(.*?)<\/p>/s);
        if (descriptionMatch) {
            console.log(`\n📝 Description après modification:`);
            console.log(`"${descriptionMatch[1].trim()}"`);
        }
    } else {
        console.log(`ℹ️  ${result.reason}`);
    }
}

function main() {
    const args = process.argv.slice(2);
    
    if (args.includes('--test') && args[1]) {
        testOnFile(args[1]);
    } else {
        processAllProductPages();
    }
}

if (require.main === module) {
    main();
}

module.exports = { addBrandLinksToProduct, processAllProductPages };
