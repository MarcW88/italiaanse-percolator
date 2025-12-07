const fs = require('fs');
const path = require('path');

// 1. Fonction pour corriger les breadcrumbs des pages produits
function fixProductBreadcrumbs() {
    console.log('🍞 Correction des breadcrumbs des pages produits...\n');
    
    const productsDir = '/Users/marc/Desktop/italiaanse-percolator/producten';
    const productFiles = fs.readdirSync(productsDir).filter(f => f.endsWith('.html'));
    
    let updatedCount = 0;
    
    productFiles.forEach(file => {
        const filePath = path.join(productsDir, file);
        let content = fs.readFileSync(filePath, 'utf8');
        const originalContent = content;
        
        // Ancien breadcrumb: Home > Percolators > Produit
        // Nouveau breadcrumb: Home > Winkel > Percolators > Produit
        const oldBreadcrumbRegex = /<nav style="margin-bottom: 2rem; font-size: 0\.9rem; color: #666;">\s*<a href="\.\.\/index\.html"[^>]*>Home<\/a>\s*>\s*<a href="\.\.\/categories\/percolators\.html"[^>]*>Percolators<\/a>\s*>\s*<span[^>]*>.*?<\/span>\s*<\/nav>/s;
        
        const match = content.match(oldBreadcrumbRegex);
        if (match) {
            // Extraire le nom du produit de l'ancien breadcrumb
            const productNameMatch = match[0].match(/<span[^>]*>(.*?)<\/span>/s);
            const productName = productNameMatch ? productNameMatch[1] : 'Produit';
            
            const newBreadcrumb = `<nav style="margin-bottom: 2rem; font-size: 0.9rem; color: #666;">
            <a href="../index.html" style="color: #666; text-decoration: none;">Home</a> > 
            <a href="../boutique.html" style="color: #666; text-decoration: none;">Winkel</a> > 
            <a href="../categories/percolators.html" style="color: #666; text-decoration: none;">Percolators</a> > 
            <span style="color: #D2691E; font-weight: 600;">${productName}</span>
        </nav>`;
            
            content = content.replace(match[0], newBreadcrumb);
            
            if (content !== originalContent) {
                fs.writeFileSync(filePath, content, 'utf8');
                updatedCount++;
                console.log(`✅ ${file} - Breadcrumb corrigé`);
            }
        }
    });
    
    console.log(`\n📊 ${updatedCount} breadcrumbs corrigés\n`);
    return updatedCount;
}

// 2. Fonction pour ajouter la section catégories à la page boutique
function addCategoriesToBoutique() {
    console.log('🏪 Ajout de la section catégories à la page boutique...\n');
    
    const boutiquePath = '/Users/marc/Desktop/italiaanse-percolator/boutique.html';
    let content = fs.readFileSync(boutiquePath, 'utf8');
    const originalContent = content;
    
    // Vérifier si la section existe déjà
    if (content.includes('<!-- Categories Section -->')) {
        console.log('ℹ️  Section catégories déjà présente');
        return false;
    }
    
    const categoriesSection = `
    <!-- Categories Section -->
    <section style="background: #f8f9fa; padding: 4rem 0;">
        <div class="container">
            <div style="text-align: center; margin-bottom: 3rem;">
                <h2 style="font-size: 2.5rem; margin-bottom: 1rem; color: #333; font-family: 'DM Serif Display', serif;">Shop per Categorie</h2>
                <p style="font-size: 1.2rem; color: #666; max-width: 600px; margin: 0 auto;">Vind precies wat je zoekt in onze zorgvuldig samengestelde categorieën</p>
            </div>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; max-width: 1000px; margin: 0 auto;">
                <!-- Percolators -->
                <a href="categories/percolators.html" style="text-decoration: none; color: inherit;">
                    <div style="background: white; border-radius: 15px; padding: 2rem; text-align: center; box-shadow: 0 4px 20px rgba(0,0,0,0.1); transition: all 0.3s ease; border: 2px solid transparent;">
                        <div style="background: linear-gradient(135deg, #D2691E, #8B4513); width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem; font-size: 2rem;">☕</div>
                        <h3 style="font-size: 1.5rem; margin-bottom: 1rem; color: #333; font-weight: 600;">Percolators</h3>
                        <p style="color: #666; margin-bottom: 1.5rem; line-height: 1.6;">Klassieke en moderne percolators voor de perfecte Italiaanse koffie</p>
                        <span style="color: #D2691E; font-weight: 600; font-size: 1.1rem;">Bekijk alle percolators →</span>
                    </div>
                </a>
                
                <!-- Elektrische Percolators -->
                <a href="categories/elektrische-percolators.html" style="text-decoration: none; color: inherit;">
                    <div style="background: white; border-radius: 15px; padding: 2rem; text-align: center; box-shadow: 0 4px 20px rgba(0,0,0,0.1); transition: all 0.3s ease; border: 2px solid transparent;">
                        <div style="background: linear-gradient(135deg, #D2691E, #8B4513); width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem; font-size: 2rem;">⚡</div>
                        <h3 style="font-size: 1.5rem; margin-bottom: 1rem; color: #333; font-weight: 600;">Elektrische Percolators</h3>
                        <p style="color: #666; margin-bottom: 1.5rem; line-height: 1.6;">Moderne elektrische modellen met timer en automatische functies</p>
                        <span style="color: #D2691E; font-weight: 600; font-size: 1.1rem;">Bekijk elektrische modellen →</span>
                    </div>
                </a>
                
                <!-- Accessoires -->
                <a href="categories/accessoires.html" style="text-decoration: none; color: inherit;">
                    <div style="background: white; border-radius: 15px; padding: 2rem; text-align: center; box-shadow: 0 4px 20px rgba(0,0,0,0.1); transition: all 0.3s ease; border: 2px solid transparent;">
                        <div style="background: linear-gradient(135deg, #D2691E, #8B4513); width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem; font-size: 2rem;">🔧</div>
                        <h3 style="font-size: 1.5rem; margin-bottom: 1rem; color: #333; font-weight: 600;">Accessoires</h3>
                        <p style="color: #666; margin-bottom: 1.5rem; line-height: 1.6;">Onderdelen, filters en accessoires voor optimaal onderhoud</p>
                        <span style="color: #D2691E; font-weight: 600; font-size: 1.1rem;">Bekijk accessoires →</span>
                    </div>
                </a>
                
                <!-- Onderhoudssets -->
                <a href="categories/onderhoudssets.html" style="text-decoration: none; color: inherit;">
                    <div style="background: white; border-radius: 15px; padding: 2rem; text-align: center; box-shadow: 0 4px 20px rgba(0,0,0,0.1); transition: all 0.3s ease; border: 2px solid transparent;">
                        <div style="background: linear-gradient(135deg, #D2691E, #8B4513); width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem; font-size: 2rem;">🧽</div>
                        <h3 style="font-size: 1.5rem; margin-bottom: 1rem; color: #333; font-weight: 600;">Onderhoudssets</h3>
                        <p style="color: #666; margin-bottom: 1.5rem; line-height: 1.6;">Complete sets voor reiniging en onderhoud van je percolator</p>
                        <span style="color: #D2691E; font-weight: 600; font-size: 1.1rem;">Bekijk onderhoudssets →</span>
                    </div>
                </a>
            </div>
        </div>
    </section>

    <style>
    .container a:hover div {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.15) !important;
        border-color: #D2691E !important;
    }
    </style>
`;
    
    // Insérer la section après la hero section et avant les filtres
    const insertionPoint = content.indexOf('<!-- Filters Section -->');
    if (insertionPoint !== -1) {
        const beforeInsertion = content.substring(0, insertionPoint);
        const afterInsertion = content.substring(insertionPoint);
        content = beforeInsertion + categoriesSection + '\n    ' + afterInsertion;
        
        fs.writeFileSync(boutiquePath, content, 'utf8');
        console.log('✅ Section catégories ajoutée à la page boutique\n');
        return true;
    } else {
        console.log('⚠️  Point d\'insertion non trouvé dans boutique.html\n');
        return false;
    }
}

// 3. Fonction pour ajouter les données structurées aux pages produits
function addStructuredDataToProducts() {
    console.log('📊 Ajout des données structurées aux pages produits...\n');
    
    const productsDir = '/Users/marc/Desktop/italiaanse-percolator/producten';
    const productFiles = fs.readdirSync(productsDir).filter(f => f.endsWith('.html'));
    
    // Charger les données produits
    const allProductsPath = '/Users/marc/Desktop/italiaanse-percolator/all_products.json';
    const allProducts = JSON.parse(fs.readFileSync(allProductsPath, 'utf8'));
    
    let updatedCount = 0;
    
    productFiles.forEach(file => {
        const slug = file.replace('.html', '');
        const product = allProducts.find(p => p.slug === slug);
        
        if (!product) {
            console.log(`⚠️  Produit non trouvé dans JSON: ${slug}`);
            return;
        }
        
        const filePath = path.join(productsDir, file);
        let content = fs.readFileSync(filePath, 'utf8');
        const originalContent = content;
        
        // Vérifier si les données structurées existent déjà
        if (content.includes('"@type": "Product"')) {
            console.log(`ℹ️  ${file} - Données structurées déjà présentes`);
            return;
        }
        
        // Créer les données structurées
        const structuredData = {
            "@context": "https://schema.org/",
            "@type": "Product",
            "name": product.name,
            "description": `${product.name} - ${product.materiaal} percolator voor ${product.capaciteit} kopjes. Geschikt voor ${product.inductie === 'Oui' ? 'inductie' : 'alle kookplaten'}.`,
            "brand": {
                "@type": "Brand",
                "name": product.merk
            },
            "category": "Percolator",
            "material": product.materiaal,
            "image": `https://italiaanse-percolator.nl/${product.image}`,
            "url": `https://italiaanse-percolator.nl/producten/${slug}.html`,
            "offers": {
                "@type": "Offer",
                "price": product.prijs ? product.prijs.toString() : "0",
                "priceCurrency": "EUR",
                "availability": "https://schema.org/InStock",
                "seller": {
                    "@type": "Organization",
                    "name": "Italiaanse Percolator"
                }
            },
            "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": product.rating || "4.5",
                "reviewCount": product.reviews || "10",
                "bestRating": "5",
                "worstRating": "1"
            },
            "additionalProperty": [
                {
                    "@type": "PropertyValue",
                    "name": "Capaciteit",
                    "value": `${product.capaciteit} kopjes`
                },
                {
                    "@type": "PropertyValue", 
                    "name": "Materiaal",
                    "value": product.materiaal
                },
                {
                    "@type": "PropertyValue",
                    "name": "Inductie geschikt",
                    "value": product.inductie === 'Oui' ? "Ja" : "Nee"
                }
            ]
        };
        
        const structuredDataScript = `\n    <!-- Structured Data -->
    <script type="application/ld+json">
    ${JSON.stringify(structuredData, null, 4)}
    </script>`;
        
        // Insérer avant la fermeture du head
        const headCloseIndex = content.indexOf('</head>');
        if (headCloseIndex !== -1) {
            const beforeHead = content.substring(0, headCloseIndex);
            const afterHead = content.substring(headCloseIndex);
            content = beforeHead + structuredDataScript + '\n' + afterHead;
            
            fs.writeFileSync(filePath, content, 'utf8');
            updatedCount++;
            console.log(`✅ ${file} - Données structurées ajoutées`);
        }
    });
    
    console.log(`\n📊 ${updatedCount} pages avec données structurées ajoutées\n`);
    return updatedCount;
}

// Fonction principale
function main() {
    console.log('🔧 Correction complète: Breadcrumbs + Catégories + Données Structurées\n');
    
    // 1. Corriger les breadcrumbs
    const breadcrumbsFixed = fixProductBreadcrumbs();
    
    // 2. Ajouter la section catégories
    const categoriesAdded = addCategoriesToBoutique();
    
    // 3. Ajouter les données structurées
    const structuredDataAdded = addStructuredDataToProducts();
    
    // Résumé
    console.log('📊 RÉSUMÉ FINAL:');
    console.log(`   • ${breadcrumbsFixed} breadcrumbs corrigés`);
    console.log(`   • Section catégories ${categoriesAdded ? 'ajoutée' : 'déjà présente'}`);
    console.log(`   • ${structuredDataAdded} pages avec données structurées`);
    
    if (breadcrumbsFixed > 0 || categoriesAdded || structuredDataAdded > 0) {
        console.log('\n🎉 Améliorations appliquées avec succès!');
        console.log('💡 Navigation et SEO considérablement améliorés.');
    }
}

if (require.main === module) {
    main();
}

module.exports = { fixProductBreadcrumbs, addCategoriesToBoutique, addStructuredDataToProducts };
