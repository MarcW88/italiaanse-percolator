const fs = require('fs');
const path = require('path');

function checkAndFixCSSLinks() {
    console.log('🔧 Vérification et correction des liens CSS...\n');
    
    const baseDir = '/Users/marc/Desktop/italiaanse-percolator';
    let fixedCount = 0;
    let checkedCount = 0;
    
    // Fonction récursive pour parcourir tous les fichiers HTML
    function processDirectory(dir, relativePath = '') {
        const files = fs.readdirSync(dir);
        
        files.forEach(file => {
            const fullPath = path.join(dir, file);
            const stat = fs.statSync(fullPath);
            
            if (stat.isDirectory() && !file.startsWith('.') && file !== 'node_modules') {
                processDirectory(fullPath, path.join(relativePath, file));
            } else if (file.endsWith('.html')) {
                checkedCount++;
                
                let content = fs.readFileSync(fullPath, 'utf8');
                const originalContent = content;
                
                // Détecter les liens CSS incorrects
                const wrongCSSRegex = /<link[^>]+href=["']([^"']*styles\.css)["'][^>]*>/gi;
                const matches = content.match(wrongCSSRegex);
                
                if (matches) {
                    // Corriger les liens CSS
                    content = content.replace(wrongCSSRegex, (match, href) => {
                        const correctedHref = href.replace('styles.css', 'style.css');
                        const correctedMatch = match.replace(href, correctedHref);
                        
                        console.log(`   📝 ${path.join(relativePath, file)}`);
                        console.log(`      ${href} → ${correctedHref}`);
                        
                        return correctedMatch;
                    });
                    
                    if (content !== originalContent) {
                        fs.writeFileSync(fullPath, content, 'utf8');
                        fixedCount++;
                        console.log(`   ✅ Corrigé: ${path.join(relativePath, file)}\n`);
                    }
                } else {
                    // Vérifier que le lien CSS existe et est correct
                    const cssLinkRegex = /<link[^>]+href=["']([^"']*style\.css)["'][^>]*>/i;
                    const cssMatch = content.match(cssLinkRegex);
                    
                    if (cssMatch) {
                        console.log(`   ✅ CSS OK: ${path.join(relativePath, file)} (${cssMatch[1]})`);
                    } else {
                        console.log(`   ⚠️  Aucun lien CSS trouvé: ${path.join(relativePath, file)}`);
                    }
                }
            }
        });
    }
    
    processDirectory(baseDir);
    
    console.log(`\n📊 Résumé:`);
    console.log(`   • ${checkedCount} fichiers HTML vérifiés`);
    console.log(`   • ${fixedCount} fichiers corrigés`);
    
    if (fixedCount > 0) {
        console.log(`\n🎉 Correction terminée! Les pages marques utilisent maintenant le bon CSS.`);
    } else {
        console.log(`\n✅ Tous les liens CSS sont corrects!`);
    }
}

// Fonction pour vérifier l'existence du fichier CSS principal
function verifyCSSFile() {
    const cssPath = '/Users/marc/Desktop/italiaanse-percolator/style.css';
    
    if (fs.existsSync(cssPath)) {
        const stats = fs.statSync(cssPath);
        console.log(`✅ Fichier CSS principal trouvé: style.css (${Math.round(stats.size / 1024)}KB)`);
        return true;
    } else {
        console.log(`❌ Fichier CSS principal non trouvé: style.css`);
        return false;
    }
}

function main() {
    console.log('🎨 Vérification des liens CSS sur tout le site...\n');
    
    // 1. Vérifier l'existence du CSS principal
    if (!verifyCSSFile()) {
        console.log('⚠️  Impossible de continuer sans le fichier CSS principal.');
        return;
    }
    
    console.log('');
    
    // 2. Vérifier et corriger tous les liens CSS
    checkAndFixCSSLinks();
    
    console.log('\n💡 Les pages marques devraient maintenant avoir le même style que le reste du site!');
}

if (require.main === module) {
    main();
}

module.exports = { checkAndFixCSSLinks };
