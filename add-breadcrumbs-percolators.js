const fs = require('fs');

function addBreadcrumbsToPercolators() {
    console.log('🍞 Ajout des breadcrumbs à la page percolators...\n');
    
    const filePath = '/Users/marc/Desktop/italiaanse-percolator/categories/percolators.html';
    let content = fs.readFileSync(filePath, 'utf8');
    
    const breadcrumbsHTML = `
        <!-- Breadcrumb -->
        <nav style="margin-bottom: 2rem; font-size: 0.9rem; color: #666;">
            <a href="../index.html" style="color: #666; text-decoration: none;">Home</a> > 
            <a href="../boutique.html" style="color: #666; text-decoration: none;">Winkel</a> > 
            <span style="color: #D2691E; font-weight: 600;">Percolators</span>
        </nav>`;
    
    // Insérer après <main> et avant <header>
    const mainStart = content.indexOf('<main class="container"');
    const headerStart = content.indexOf('<!-- Header catégorie -->');
    
    if (mainStart !== -1 && headerStart !== -1) {
        const beforeBreadcrumb = content.substring(0, headerStart);
        const afterBreadcrumb = content.substring(headerStart);
        
        content = beforeBreadcrumb + breadcrumbsHTML + '\n        ' + afterBreadcrumb;
        
        fs.writeFileSync(filePath, content, 'utf8');
        console.log('✅ Breadcrumbs ajoutés à la page percolators');
        return true;
    }
    
    return false;
}

if (require.main === module) {
    addBreadcrumbsToPercolators();
}

module.exports = { addBreadcrumbsToPercolators };
