const fs = require('fs');
const path = require('path');

// Import optimization functions
const { extractProductName, generateFAQHTML, generateEnhancedDescription } = require('./complete-product-optimization.js');

const PRODUCTEN_DIR = '/Users/marc/Desktop/italiaanse-percolator/producten';

// Pages déjà complètement traitées (à ignorer)
const COMPLETED_PAGES = [
    'bialetti-cafetiere-preziosa-350ml.html',
    'bialetti-moka-express-percolator-3-kops-aluminium.html',
    'bialetti-moka-express-percolator-6-kops-aluminium-rood.html'
];

function processProductPage(filePath) {
    const filename = path.basename(filePath);
    
    // Skip already completed pages
    if (COMPLETED_PAGES.includes(filename)) {
        console.log(`⏭️  Skipping already completed: ${filename}`);
        return { success: true, skipped: true };
    }
    
    try {
        let content = fs.readFileSync(filePath, 'utf8');
        const productName = extractProductName(filename);
        let modified = false;
        
        console.log(`📝 Processing: ${filename}`);
        console.log(`   Product name: ${productName}`);
        
        // 1. Enhance product description with internal link
        const descriptionRegex = /<div style="margin-bottom: 2rem;">\s*<h3[^>]*>Productbeschrijving<\/h3>\s*<p[^>]*>(.*?)<\/p>\s*<\/div>/s;
        const descriptionMatch = content.match(descriptionRegex);
        
        if (descriptionMatch) {
            const originalDescription = descriptionMatch[1].trim();
            
            // Check if description needs enhancement
            if (originalDescription.length < 50 || !originalDescription.includes('italiaanse-percolator')) {
                const enhancedDescription = generateEnhancedDescription(productName, originalDescription);
                
                const newDescriptionBlock = `<div style="margin-bottom: 2rem;">
                    <h3 style="font-size: 1.2rem; margin-bottom: 1rem;">Productbeschrijving</h3>
                    <p style="color: #666; line-height: 1.6; font-size: 1rem;">
                        ${enhancedDescription}
                    </p>
                </div>`;
                
                content = content.replace(descriptionRegex, newDescriptionBlock);
                modified = true;
                console.log(`   ✅ Description enhanced with internal link`);
            } else {
                console.log(`   ✅ Description already has internal link`);
            }
        } else {
            console.log(`   ⚠️  No description section found`);
        }
        
        // 2. Replace generic FAQ with personalized FAQ
        const faqRegex = /<!-- FAQ Section -->[\s\S]*?<\/section>/;
        const faqMatch = content.match(faqRegex);
        
        if (faqMatch) {
            // Check if FAQ is already personalized
            if (!faqMatch[0].includes(`Veelgestelde Vragen over de ${productName}`)) {
                const personalizedFAQ = generateFAQHTML(productName);
                content = content.replace(faqRegex, personalizedFAQ);
                modified = true;
                console.log(`   ✅ FAQ personalized for ${productName}`);
            } else {
                console.log(`   ✅ FAQ already personalized`);
            }
        } else {
            console.log(`   ⚠️  No FAQ section found`);
        }
        
        // 3. Save the file if modified
        if (modified) {
            fs.writeFileSync(filePath, content, 'utf8');
            console.log(`   💾 File saved with improvements`);
            return { success: true, modified: true };
        } else {
            console.log(`   ℹ️  No changes needed`);
            return { success: true, modified: false };
        }
        
    } catch (error) {
        console.error(`   ❌ Error processing ${filename}:`, error.message);
        return { success: false, error: error.message };
    }
}

function processAllProducts() {
    console.log('🚀 Starting complete product optimization...\n');
    
    const files = fs.readdirSync(PRODUCTEN_DIR).filter(file => file.endsWith('.html'));
    const stats = {
        total: files.length,
        processed: 0,
        modified: 0,
        skipped: 0,
        errors: 0
    };
    
    files.forEach((filename, index) => {
        const filePath = path.join(PRODUCTEN_DIR, filename);
        console.log(`\n[${index + 1}/${files.length}] Processing: ${filename}`);
        
        const result = processProductPage(filePath);
        
        if (result.success) {
            stats.processed++;
            if (result.skipped) {
                stats.skipped++;
            } else if (result.modified) {
                stats.modified++;
            }
        } else {
            stats.errors++;
        }
    });
    
    console.log('\n🎉 Complete optimization finished!');
    console.log('\n📊 Final Statistics:');
    console.log(`   Total files: ${stats.total}`);
    console.log(`   Processed: ${stats.processed}`);
    console.log(`   Modified: ${stats.modified}`);
    console.log(`   Skipped (already complete): ${stats.skipped}`);
    console.log(`   Errors: ${stats.errors}`);
    
    const completionRate = Math.round((stats.processed / stats.total) * 100);
    console.log(`\n✅ Success rate: ${completionRate}%`);
    
    if (stats.modified > 0) {
        console.log(`\n🎯 ${stats.modified} pages have been enhanced with:`);
        console.log('   • Personalized FAQ sections');
        console.log('   • Enhanced descriptions with internal links');
        console.log('   • Improved SEO and user experience');
    }
}

// Run the optimization
if (require.main === module) {
    processAllProducts();
}

module.exports = { processAllProducts, processProductPage };
