const fs = require('fs');
const path = require('path');

function addBrandLinksToDescriptions() {
    console.log('🔗 Ajout de liens marques dans les descriptions produits uniquement...\n');
    
    const productsDir = '/Users/marc/Desktop/italiaanse-percolator/producten';
    const productFiles = fs.readdirSync(productsDir)
        .filter(file => file.endsWith('.html'))
        .sort();
    
    let processedCount = 0;
    let changedCount = 0;
    
    productFiles.forEach(file => {
        const filePath = path.join(productsDir, file);
        let content = fs.readFileSync(filePath, 'utf8');
        const originalContent = content;
        
        // Chercher la section description produit
        const descriptionRegex = /<div[^>]*>\s*<h3[^>]*>Productbeschrijving<\/h3>\s*<p[^>]*>(.*?)<\/p>\s*<\/div>/s;
        const match = content.match(descriptionRegex);
        
        if (match) {
            let description = match[1];
            let hasChanged = false;
            
            // Ajouter lien Bialetti si présent et pas déjà lié
            if (description.includes('Bialetti') && !description.includes('href="../marques/bialetti/index.html">Bialetti')) {
                description = description.replace(/\bBialetti\b(?![^<]*<\/a>)/, '<a href="../marques/bialetti/index.html" style="color: #D2691E; text-decoration: none; font-weight: 600;">Bialetti</a>');
                hasChanged = true;
            }
            
            // Ajouter lien Alessi si présent et pas déjà lié
            if (description.includes('Alessi') && !description.includes('href="../marques/alessi/index.html">Alessi')) {
                description = description.replace(/\bAlessi\b(?![^<]*<\/a>)/, '<a href="../marques/alessi/index.html" style="color: #D2691E; text-decoration: none; font-weight: 600;">Alessi</a>');
                hasChanged = true;
            }
            
            // Ajouter lien Grosche si présent et pas déjà lié
            if (description.includes('Grosche') && !description.includes('href="../marques/grosche/index.html">Grosche')) {
                description = description.replace(/\bGrosche\b(?![^<]*<\/a>)/, '<a href="../marques/grosche/index.html" style="color: #D2691E; text-decoration: none; font-weight: 600;">Grosche</a>');
                hasChanged = true;
            }
            
            if (hasChanged) {
                // Remplacer la description dans le contenu
                const newDescriptionSection = match[0].replace(match[1], description);
                content = content.replace(match[0], newDescriptionSection);
                
                fs.writeFileSync(filePath, content, 'utf8');
                changedCount++;
                console.log(`✅ ${file} - Lien marque ajouté dans la description`);
            }
        }
        
        processedCount++;
    });
    
    console.log(`\n📊 Résumé:`);
    console.log(`   • ${processedCount} pages produits traitées`);
    console.log(`   • ${changedCount} pages avec liens marques ajoutés dans les descriptions`);
    
    if (changedCount > 0) {
        console.log(`\n🎉 Liens marques contextuels ajoutés dans les descriptions!`);
    }
}

// Test sur un fichier spécifique
function testOnFile(filename) {
    console.log(`🧪 Test sur ${filename}...\n`);
    
    const filePath = `/Users/marc/Desktop/italiaanse-percolator/producten/${filename}`;
    let content = fs.readFileSync(filePath, 'utf8');
    
    console.log('AVANT:');
    const descriptionRegex = /<div[^>]*>\s*<h3[^>]*>Productbeschrijving<\/h3>\s*<p[^>]*>(.*?)<\/p>\s*<\/div>/s;
    const match = content.match(descriptionRegex);
    if (match) {
        console.log(match[1].trim());
    }
    
    // Appliquer les changements
    if (match) {
        let description = match[1];
        let hasChanged = false;
        
        if (description.includes('Bialetti') && !description.includes('href="../marques/bialetti/index.html">Bialetti')) {
            description = description.replace(/\bBialetti\b(?![^<]*<\/a>)/, '<a href="../marques/bialetti/index.html" style="color: #D2691E; text-decoration: none; font-weight: 600;">Bialetti</a>');
            hasChanged = true;
        }
        
        if (hasChanged) {
            const newDescriptionSection = match[0].replace(match[1], description);
            content = content.replace(match[0], newDescriptionSection);
            fs.writeFileSync(filePath, content, 'utf8');
            
            console.log('\nAPRÈS:');
            console.log(description.trim());
            console.log('\n✅ Lien ajouté!');
        } else {
            console.log('\nℹ️  Aucun changement nécessaire');
        }
    }
}

function main() {
    const args = process.argv.slice(2);
    
    if (args.includes('--test') && args[1]) {
        testOnFile(args[1]);
    } else {
        addBrandLinksToDescriptions();
    }
}

if (require.main === module) {
    main();
}

module.exports = { addBrandLinksToDescriptions };
