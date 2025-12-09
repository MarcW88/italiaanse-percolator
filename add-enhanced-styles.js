const fs = require('fs');

function addEnhancedStyles() {
    console.log('🎨 Ajout des styles pour les cards enrichies...\n');
    
    const filePath = '/Users/marc/Desktop/italiaanse-percolator/categories/percolators.html';
    let content = fs.readFileSync(filePath, 'utf8');
    
    const enhancedStyles = `
    
    /* Styles pour les badges produits */
    .product-badge {
        padding: 0.3rem 0.7rem;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
        color: white;
        text-shadow: 0 1px 2px rgba(0,0,0,0.2);
        box-shadow: 0 2px 8px rgba(0,0,0,0.15);
    }
    
    .default-badge { background: linear-gradient(135deg, #6B7280, #4B5563); }
    .popular-badge { background: linear-gradient(135deg, #DC2626, #991B1B); }
    .induction-badge { background: linear-gradient(135deg, #4169E1, #1E3A8A); }
    .premium-badge { background: linear-gradient(135deg, #059669, #047857); }
    .special-badge { background: linear-gradient(135deg, #D97706, #92400E); }
    
    /* Animations pour les cards */
    .enhanced-product-card {
        animation: fadeInUp 0.6s ease forwards;
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Hover effects améliorés */
    .enhanced-product-card:hover .product-badge {
        transform: scale(1.05);
        transition: transform 0.2s ease;
    }
    
    /* Responsive pour les cards enrichies */
    @media (max-width: 768px) {
        .enhanced-product-card {
            margin-bottom: 1.5rem;
        }
        
        .enhanced-product-card img {
            height: 180px !important;
        }
        
        .product-badge {
            font-size: 0.7rem;
            padding: 0.25rem 0.5rem;
        }
    }
    
    /* Styles pour la comparaison */
    .compare-bar {
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        background: white;
        border-radius: 25px;
        padding: 1rem 2rem;
        box-shadow: 0 8px 30px rgba(0,0,0,0.15);
        border: 2px solid #D2691E;
        z-index: 1000;
        display: none;
        align-items: center;
        gap: 1rem;
    }
    
    .compare-bar.visible {
        display: flex;
        animation: slideUp 0.3s ease;
    }
    
    @keyframes slideUp {
        from {
            opacity: 0;
            transform: translateX(-50%) translateY(100%);
        }
        to {
            opacity: 1;
            transform: translateX(-50%) translateY(0);
        }
    }
    
    /* Styles pour les spécifications */
    .specs-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 0.75rem;
        font-size: 0.85rem;
    }
    
    .spec-item {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem;
        background: white;
        border-radius: 6px;
        border: 1px solid #f0f0f0;
    }
    
    /* Loading states */
    .product-loading {
        background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
        background-size: 200% 100%;
        animation: loading 1.5s infinite;
    }
    
    @keyframes loading {
        0% { background-position: 200% 0; }
        100% { background-position: -200% 0; }
    }`;
    
    // Insérer les styles avant la fermeture du style existant
    const styleEnd = content.lastIndexOf('</style>');
    if (styleEnd !== -1) {
        content = content.substring(0, styleEnd) + enhancedStyles + content.substring(styleEnd);
    }
    
    // Ajouter les fonctions JavaScript pour la comparaison
    const compareScript = `
    
    // Système de comparaison
    let compareList = [];
    
    function addToCompare(productSlug) {
        if (compareList.includes(productSlug)) {
            removeFromCompare(productSlug);
            return;
        }
        
        if (compareList.length >= 3) {
            alert('Vous pouvez comparer maximum 3 produits à la fois');
            return;
        }
        
        compareList.push(productSlug);
        updateCompareBar();
        
        // Feedback visuel
        const button = event.target;
        button.style.background = '#4169E1';
        button.style.borderColor = '#4169E1';
        button.innerHTML = '✓';
        
        setTimeout(() => {
            button.style.background = 'none';
            button.style.borderColor = '#ddd';
            button.innerHTML = '⚖️';
        }, 1000);
    }
    
    function removeFromCompare(productSlug) {
        compareList = compareList.filter(slug => slug !== productSlug);
        updateCompareBar();
    }
    
    function updateCompareBar() {
        let compareBar = document.getElementById('compareBar');
        
        if (!compareBar) {
            compareBar = document.createElement('div');
            compareBar.id = 'compareBar';
            compareBar.className = 'compare-bar';
            document.body.appendChild(compareBar);
        }
        
        if (compareList.length === 0) {
            compareBar.classList.remove('visible');
            return;
        }
        
        compareBar.innerHTML = \`
            <div style="display: flex; align-items: center; gap: 1rem;">
                <span style="font-weight: 600; color: #333;">
                    \${compareList.length} product\${compareList.length > 1 ? 'en' : ''} geselecteerd
                </span>
                <button onclick="openCompareModal()" style="background: #4169E1; color: white; border: none; padding: 0.5rem 1rem; border-radius: 15px; cursor: pointer; font-weight: 600;">
                    Vergelijk nu
                </button>
                <button onclick="clearCompare()" style="background: none; border: 1px solid #ddd; padding: 0.5rem; border-radius: 8px; cursor: pointer;">
                    ✕
                </button>
            </div>
        \`;
        
        compareBar.classList.add('visible');
    }
    
    function clearCompare() {
        compareList = [];
        updateCompareBar();
    }
    
    function openCompareModal() {
        // Pour l'instant, rediriger vers une page de comparaison
        const compareUrl = '../vergelijking/index.html?products=' + compareList.join(',');
        window.open(compareUrl, '_blank');
    }
    
    // Améliorer la fonction wishlist avec feedback
    function addToWishlist(productSlug) {
        let wishlist = JSON.parse(localStorage.getItem('wishlist') || '[]');
        
        if (!wishlist.includes(productSlug)) {
            wishlist.push(productSlug);
            localStorage.setItem('wishlist', JSON.stringify(wishlist));
            
            // Feedback visuel amélioré
            const button = event.target;
            const originalContent = button.innerHTML;
            button.style.background = '#DC2626';
            button.style.borderColor = '#DC2626';
            button.innerHTML = '💖';
            
            // Notification toast
            showToast('Toegevoegd aan verlanglijst! ❤️', 'success');
            
            setTimeout(() => {
                button.style.background = 'none';
                button.style.borderColor = '#ddd';
                button.innerHTML = originalContent;
            }, 1500);
        } else {
            showToast('Al in verlanglijst!', 'info');
        }
    }
    
    // Système de notifications toast
    function showToast(message, type = 'info') {
        const toast = document.createElement('div');
        toast.style.cssText = \`
            position: fixed;
            top: 20px;
            right: 20px;
            background: \${type === 'success' ? '#059669' : type === 'error' ? '#DC2626' : '#4169E1'};
            color: white;
            padding: 1rem 1.5rem;
            border-radius: 12px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            z-index: 10000;
            font-weight: 600;
            transform: translateX(100%);
            transition: transform 0.3s ease;
        \`;
        toast.textContent = message;
        
        document.body.appendChild(toast);
        
        setTimeout(() => {
            toast.style.transform = 'translateX(0)';
        }, 100);
        
        setTimeout(() => {
            toast.style.transform = 'translateX(100%)';
            setTimeout(() => {
                document.body.removeChild(toast);
            }, 300);
        }, 3000);
    }
    
    // Lazy loading amélioré pour les images
    function setupLazyLoading() {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src || img.src;
                    img.classList.remove('product-loading');
                    observer.unobserve(img);
                }
            });
        });
        
        document.querySelectorAll('img[loading="lazy"]').forEach(img => {
            img.classList.add('product-loading');
            imageObserver.observe(img);
        });
    }
    
    // Initialiser au chargement
    document.addEventListener('DOMContentLoaded', function() {
        setTimeout(setupLazyLoading, 1000);
    });`;
    
    // Insérer le script avant la fermeture du script existant
    const scriptEnd = content.lastIndexOf('</script>');
    if (scriptEnd !== -1) {
        content = content.substring(0, scriptEnd) + compareScript + content.substring(scriptEnd);
        
        fs.writeFileSync(filePath, content, 'utf8');
        console.log('✅ Styles et fonctions enrichies ajoutés');
        return true;
    }
    
    return false;
}

if (require.main === module) {
    addEnhancedStyles();
}

module.exports = { addEnhancedStyles };
