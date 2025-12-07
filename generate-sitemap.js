const fs = require('fs');
const path = require('path');

// Configuration
const BASE_URL = 'https://italiaanse-percolator.nl';
const TODAY = new Date().toISOString().split('T')[0]; // Format YYYY-MM-DD

// Structure des URLs avec priorités et fréquences de changement
const urlStructure = {
    // Pages principales (priorité élevée)
    main: {
        priority: 0.9,
        changefreq: 'weekly',
        urls: [
            '/',
            '/beste-italiaanse-percolators.html',
            '/boutique.html'
        ]
    },
    
    // Pages de contenu important
    content: {
        priority: 0.8,
        changefreq: 'monthly',
        urls: [
            '/over-ons.html',
            '/vergelijking/index.html',
            '/koopgids/index.html'
        ]
    },
    
    // Guides et comparaisons
    guides: {
        priority: 0.7,
        changefreq: 'monthly',
        urls: [
            '/koopgids/hoe-kies-je-de-juiste-percolator.html',
            '/koopgids/hoe-onderhoud-je-een-percolator.html',
            '/koopgids/percolator-vs-espressoapparaat.html'
        ]
    },
    
    // Pages catégories webshop
    categories: {
        priority: 0.6,
        changefreq: 'weekly',
        urls: [
            '/categories/percolators.html',
            '/categories/accessoires.html',
            '/categories/elektrische-percolators.html',
            '/categories/inductie-adapters.html',
            '/categories/onderhoudssets.html'
        ]
    },
    
    // Reviews produits
    reviews: {
        priority: 0.8,
        changefreq: 'monthly',
        urls: [
            '/bialetti-fiammetta-review.html',
            '/bialetti-venus-review.html',
            '/bialetti-moka-review.html',
            '/bialetti-musa-review.html',
            '/bialetti-dama-review.html',
            '/bialetti-alpina-review.html',
            '/bialetti-brikka-review.html',
            '/bialetti-mini-express-review.html',
            '/alessi-pulcina-review.html',
            '/grosche-milano-review.html'
        ]
    },
    
    // Pages marques (hubs)
    brands: {
        priority: 0.8,
        changefreq: 'monthly',
        urls: [
            '/marques/index.html',
            '/marques/bialetti/index.html',
            '/marques/alessi/index.html',
            '/marques/grosche/index.html'
        ]
    },
    
    // Pages produits marques
    brandProducts: {
        priority: 0.6,
        changefreq: 'monthly',
        urls: [
            '/marques/bialetti/fiammetta.html',
            '/marques/bialetti/venus.html',
            '/marques/bialetti/moka-express.html',
            '/marques/alessi/pulcina.html',
            '/marques/grosche/milano.html'
        ]
    },

    // Pages légales
    legal: {
        priority: 0.3,
        changefreq: 'yearly',
        urls: [
            '/privacy.html',
            '/disclaimer.html',
            '/contact.html'
        ]
    }
};

function generateSitemap() {
    console.log('🗺️  Génération de la sitemap complète...');
    
    let sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">`;

    let totalUrls = 0;

    // Ajouter les URLs définies dans la structure
    for (const [category, config] of Object.entries(urlStructure)) {
        sitemap += `\n  <!-- ${category.charAt(0).toUpperCase() + category.slice(1)} Pages -->`;
        
        for (const url of config.urls) {
            sitemap += `
  <url>
    <loc>${BASE_URL}${url}</loc>
    <lastmod>${TODAY}</lastmod>
    <changefreq>${config.changefreq}</changefreq>
    <priority>${config.priority}</priority>
  </url>`;
            totalUrls++;
        }
        sitemap += '\n';
    }

    // Ajouter toutes les pages produits automatiquement
    sitemap += `\n  <!-- Product Pages -->`;
    const productenDir = '/Users/marc/Desktop/italiaanse-percolator/producten';
    
    if (fs.existsSync(productenDir)) {
        const productFiles = fs.readdirSync(productenDir)
            .filter(file => file.endsWith('.html'))
            .sort();
        
        for (const file of productFiles) {
            sitemap += `
  <url>
    <loc>${BASE_URL}/producten/${file}</loc>
    <lastmod>${TODAY}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>`;
            totalUrls++;
        }
        
        console.log(`📦 ${productFiles.length} pages produits ajoutées`);
    }

    sitemap += `
</urlset>
`;

    // Écrire la sitemap
    const sitemapPath = '/Users/marc/Desktop/italiaanse-percolator/sitemap.xml';
    fs.writeFileSync(sitemapPath, sitemap, 'utf8');
    
    console.log(`✅ Sitemap générée avec succès !`);
    console.log(`📊 Total URLs: ${totalUrls}`);
    console.log(`📅 Date de mise à jour: ${TODAY}`);
    console.log(`📁 Fichier: ${sitemapPath}`);
    
    // Statistiques par catégorie
    console.log('\n📈 Répartition par catégorie:');
    for (const [category, config] of Object.entries(urlStructure)) {
        console.log(`   • ${category}: ${config.urls.length} URLs (priorité ${config.priority})`);
    }
    
    const productCount = fs.existsSync(productenDir) ? 
        fs.readdirSync(productenDir).filter(file => file.endsWith('.html')).length : 0;
    console.log(`   • produits: ${productCount} URLs (priorité 0.5)`);
    
    return {
        totalUrls,
        categories: Object.keys(urlStructure).length + 1, // +1 pour produits
        lastmod: TODAY
    };
}

// Fonction pour valider la sitemap
function validateSitemap() {
    const sitemapPath = '/Users/marc/Desktop/italiaanse-percolator/sitemap.xml';
    
    if (!fs.existsSync(sitemapPath)) {
        console.log('❌ Sitemap non trouvée');
        return false;
    }
    
    const content = fs.readFileSync(sitemapPath, 'utf8');
    const urlCount = (content.match(/<url>/g) || []).length;
    const locCount = (content.match(/<loc>/g) || []).length;
    
    console.log(`\n🔍 Validation de la sitemap:`);
    console.log(`   • URLs trouvées: ${urlCount}`);
    console.log(`   • Balises <loc>: ${locCount}`);
    console.log(`   • Cohérence: ${urlCount === locCount ? '✅' : '❌'}`);
    
    return urlCount === locCount;
}

// Exécuter la génération
if (require.main === module) {
    const stats = generateSitemap();
    const isValid = validateSitemap();
    
    console.log(`\n🎉 Sitemap ${isValid ? 'générée et validée' : 'générée avec erreurs'} !`);
    console.log(`🌐 Prête pour soumission aux moteurs de recherche`);
}

module.exports = { generateSitemap, validateSitemap };
