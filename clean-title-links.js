const fs = require('fs');
const path = require('path');

function cleanTitleLinks() {
    console.log('🧹 Nettoyage des liens incorrects dans les titres...\n');
    
    const productsDir = '/Users/marc/Desktop/italiaanse-percolator/producten';
    const productFiles = fs.readdirSync(productsDir)
        .filter(file => file.endsWith('.html'))
        .sort();
    
    let cleanedCount = 0;
    
    productFiles.forEach(file => {
        const filePath = path.join(productsDir, file);
        let content = fs.readFileSync(filePath, 'utf8');
        const originalContent = content;
        
        // Nettoyer les liens dans les titres
        const titleLinkRegex = /<title>.*?<a href="[^"]*marques\/[^"]*"[^>]*>(.*?)<\/a>(.*?)<\/title>/gi;
        
        content = content.replace(titleLinkRegex, (match, linkText, restOfTitle) => {
            console.log(`   📝 ${file}: Nettoyage du titre`);
            return `<title>${linkText}${restOfTitle}</title>`;
        });
        
        // Nettoyer les liens dans les breadcrumbs si nécessaire
        const breadcrumbLinkRegex = /<span style="color: #D2691E; font-weight: 600;">.*?<a href="[^"]*marques\/[^"]*"[^>]*>(.*?)<\/a>(.*?)<\/span>/gi;
        
        content = content.replace(breadcrumbLinkRegex, (match, linkText, restOfText) => {
            console.log(`   📝 ${file}: Nettoyage du breadcrumb`);
            return `<span style="color: #D2691E; font-weight: 600;">${linkText}${restOfText}</span>`;
        });
        
        if (content !== originalContent) {
            fs.writeFileSync(filePath, content, 'utf8');
            cleanedCount++;
            console.log(`   ✅ ${file} nettoyé\n`);
        }
    });
    
    console.log(`📊 ${cleanedCount} fichiers nettoyés`);
}

if (require.main === module) {
    cleanTitleLinks();
}

module.exports = { cleanTitleLinks };
