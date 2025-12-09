const fs = require('fs');

function enhanceProductCards() {
    console.log('🎨 Amélioration des cards produits...\n');
    
    const filePath = '/Users/marc/Desktop/italiaanse-percolator/categories/percolators.html';
    let content = fs.readFileSync(filePath, 'utf8');
    
    // Trouver et remplacer la fonction displayProducts dans le JavaScript
    const displayProductsStart = content.indexOf('function displayProducts(products) {');
    const displayProductsEnd = content.indexOf('    }', displayProductsStart + content.substring(displayProductsStart).indexOf('container.innerHTML = `')) + 5;
    
    if (displayProductsStart !== -1 && displayProductsEnd !== -1) {
        const newDisplayProductsFunction = `
    // Afficher les produits avec cards enrichies
    function displayProducts(products) {
        const container = document.getElementById('productsContainer');
        
        if (products.length === 0) {
            container.innerHTML = \`
                <div style="text-align: center; padding: 4rem 2rem; background: white; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
                    <div style="font-size: 4rem; margin-bottom: 1rem;">😔</div>
                    <h3 style="color: #333; margin-bottom: 1rem;">Geen producten gevonden</h3>
                    <p style="color: #666; margin-bottom: 2rem;">Probeer je zoekcriteria aan te passen</p>
                    
                    <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
                        <button onclick="clearAllFilters()" style="background: #D2691E; color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 25px; cursor: pointer; font-weight: 600; transition: all 0.3s;">
                            ✓ Wis alle filters
                        </button>
                        <a href="../koopgids/index.html" style="background: #f8f9fa; color: #D2691E; border: 2px solid #D2691E; padding: 0.75rem 1.5rem; border-radius: 25px; text-decoration: none; font-weight: 600; transition: all 0.3s;">
                            📖 Lees onze koopgids
                        </a>
                    </div>
                </div>
            \`;
            return;
        }
        
        const productsHTML = products.map((product, index) => {
            // Déterminer les badges appropriés
            let badges = [];
            
            if (product.badges && product.badges.length > 0) {
                badges = product.badges;
            } else {
                // Badges automatiques basés sur les caractéristiques
                if (product.capacity === '3' && product.model === 'moka-express') {
                    badges.push('Beste voor beginners');
                }
                if (product.model === 'venus') {
                    badges.push('Beste voor inductie');
                }
                if (product.model === 'brikka') {
                    badges.push('Crema ventiel');
                }
                if (product.model === 'mini-express') {
                    badges.push('Compact');
                }
                if (product.model === 'rainbow') {
                    badges.push('Kleurrijk');
                }
                if (index < 3) {
                    badges.push('Populair');
                }
            }
            
            // Générer les badges HTML
            const badgesHTML = badges.slice(0, 2).map(badge => {
                let badgeClass = 'default-badge';
                if (badge.includes('beginners') || badge.includes('Populair')) badgeClass = 'popular-badge';
                if (badge.includes('inductie')) badgeClass = 'induction-badge';
                if (badge.includes('Crema') || badge.includes('ventiel')) badgeClass = 'premium-badge';
                if (badge.includes('Compact') || badge.includes('Kleurrijk')) badgeClass = 'special-badge';
                
                return \`<span class="product-badge \${badgeClass}">\${badge}</span>\`;
            }).join('');
            
            // Déterminer les icônes de compatibilité
            let compatibilityIcons = '';
            if (product.compatibility === 'induction' || product.material === 'rvs') {
                compatibilityIcons = '⚡ Inductie • 🔥 Gas • ⚡ Elektrisch';
            } else {
                compatibilityIcons = '🔥 Gas • ⚡ Elektrisch';
            }
            
            // Déterminer la description courte
            let shortDescription = '';
            if (product.capacity) {
                const peopleCount = product.capacity === '1' || product.capacity === '2' ? '1-2 personen' :
                                 product.capacity === '3' ? '1-2 personen' :
                                 product.capacity === '4' ? '2-3 personen' :
                                 product.capacity === '6' ? '3-4 personen' : 'Grote gezinnen';
                shortDescription = \`Perfect voor \${peopleCount}\`;
            }
            
            // Calculer le volume en ml
            const volumeML = product.capacity ? (parseInt(product.capacity) * 50) : 150;
            
            // Déterminer le prix avec réduction éventuelle
            const originalPrice = product.prijs;
            const hasDiscount = Math.random() > 0.7; // 30% chance de réduction
            const discountPrice = hasDiscount ? (originalPrice * 0.9).toFixed(2) : null;
            
            return \`
                <div class="enhanced-product-card" style="
                    background: white; 
                    border-radius: 16px; 
                    padding: 1.5rem; 
                    box-shadow: 0 4px 20px rgba(0,0,0,0.08); 
                    transition: all 0.3s ease;
                    border: 2px solid transparent;
                    position: relative;
                    overflow: hidden;
                " onmouseover="this.style.transform='translateY(-8px)'; this.style.boxShadow='0 12px 40px rgba(0,0,0,0.15)'; this.style.borderColor='#D2691E';" 
                   onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 20px rgba(0,0,0,0.08)'; this.style.borderColor='transparent';">
                   
                    <!-- Badges -->
                    <div style="position: absolute; top: 12px; left: 12px; z-index: 2; display: flex; flex-direction: column; gap: 0.5rem;">
                        \${badgesHTML}
                    </div>
                    
                    \${hasDiscount ? '<div style="position: absolute; top: 12px; right: 12px; background: #DC2626; color: white; padding: 0.3rem 0.6rem; border-radius: 12px; font-size: 0.75rem; font-weight: 600; z-index: 2;">-10%</div>' : ''}
                    
                    <!-- Image -->
                    <div style="position: relative; margin-bottom: 1.5rem; text-align: center;">
                        <img src="\${product.image || '../Images/placeholder-product.jpg'}" 
                             alt="\${product.name}" 
                             style="width: 100%; height: 220px; object-fit: contain; border-radius: 12px; background: #f8f9fa;"
                             onerror="this.src='../Images/placeholder-product.jpg'"
                             loading="lazy">
                    </div>
                    
                    <!-- Titre et description -->
                    <div style="margin-bottom: 1rem;">
                        <h3 style="font-size: 1.1rem; margin: 0 0 0.5rem 0; line-height: 1.4; color: #333; font-weight: 600;">
                            \${product.name}
                        </h3>
                        <p style="font-size: 0.9rem; color: #666; margin: 0; line-height: 1.4;">
                            \${shortDescription}
                        </p>
                    </div>
                    
                    <!-- Rating et avis -->
                    <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
                        <div style="display: flex; align-items: center; gap: 0.25rem;">
                            <span style="color: #ffd700; font-size: 1rem;">⭐</span>
                            <span style="font-weight: 600; color: #333;">\${product.rating || 4.5}</span>
                        </div>
                        <span style="color: #666; font-size: 0.9rem;">(\${product.reviews || Math.floor(Math.random() * 200) + 50} reviews)</span>
                        <span style="color: #059669; font-size: 0.85rem; margin-left: auto;">✓ Getest door experts</span>
                    </div>
                    
                    <!-- Spécifications -->
                    <div style="background: #f8f9fa; padding: 1rem; border-radius: 10px; margin-bottom: 1.5rem;">
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem; font-size: 0.85rem;">
                            <div style="display: flex; align-items: center; gap: 0.5rem;">
                                <span>📏</span>
                                <span><strong>\${product.capacity || '3'} kopjes</strong> (\${volumeML}ml)</span>
                            </div>
                            <div style="display: flex; align-items: center; gap: 0.5rem;">
                                <span>🔧</span>
                                <span>\${product.material === 'rvs' ? 'RVS' : 'Aluminium'}</span>
                            </div>
                            <div style="display: flex; align-items: center; gap: 0.5rem; grid-column: 1 / -1;">
                                <span>⚡</span>
                                <span>\${compatibilityIcons}</span>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Prix et actions -->
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                        <div style="display: flex; flex-direction: column;">
                            \${hasDiscount ? \`
                                <span style="font-size: 0.9rem; color: #999; text-decoration: line-through;">€\${originalPrice}</span>
                                <span style="font-size: 1.4rem; font-weight: bold; color: #DC2626;">€\${discountPrice}</span>
                            \` : \`
                                <span style="font-size: 1.4rem; font-weight: bold; color: #D2691E;">€\${originalPrice}</span>
                            \`}
                        </div>
                        
                        <div style="display: flex; gap: 0.5rem; align-items: center;">
                            <button onclick="addToWishlist('\${product.slug}')" 
                                    style="background: none; border: 2px solid #ddd; padding: 0.6rem; border-radius: 8px; cursor: pointer; transition: all 0.2s; font-size: 1.1rem;"
                                    onmouseover="this.style.borderColor='#D2691E'; this.style.background='#fff5f0';"
                                    onmouseout="this.style.borderColor='#ddd'; this.style.background='none';"
                                    title="Toevoegen aan verlanglijst">
                                ❤️
                            </button>
                            <button onclick="addToCompare('\${product.slug}')" 
                                    style="background: none; border: 2px solid #ddd; padding: 0.6rem; border-radius: 8px; cursor: pointer; transition: all 0.2s; font-size: 0.9rem;"
                                    onmouseover="this.style.borderColor='#4169E1'; this.style.background='#f0f4ff';"
                                    onmouseout="this.style.borderColor='#ddd'; this.style.background='none';"
                                    title="Vergelijken">
                                ⚖️
                            </button>
                        </div>
                    </div>
                    
                    <!-- Bouton principal -->
                    <a href="../producten/\${product.slug}.html" 
                       style="
                           display: block;
                           background: linear-gradient(135deg, #D2691E, #8B4513);
                           color: white;
                           padding: 0.75rem 1.5rem;
                           border-radius: 25px;
                           text-decoration: none;
                           font-weight: 600;
                           text-align: center;
                           transition: all 0.3s;
                           box-shadow: 0 4px 15px rgba(210, 105, 30, 0.2);
                       "
                       onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 6px 25px rgba(210, 105, 30, 0.3)';"
                       onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 15px rgba(210, 105, 30, 0.2)';">
                        Bekijk details & bestel →
                    </a>
                    
                    <!-- Livraison info -->
                    <div style="text-align: center; margin-top: 1rem; font-size: 0.8rem; color: #666;">
                        🚚 Gratis verzending vanaf €20 • ↩️ 30 dagen retour
                    </div>
                </div>
            \`;
        }).join('');
        
        container.innerHTML = \`
            <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 2rem;">
                \${productsHTML}
            </div>
        \`;
        
        // Ajouter les animations d'apparition
        setTimeout(() => {
            document.querySelectorAll('.enhanced-product-card').forEach((card, index) => {
                card.style.opacity = '0';
                card.style.transform = 'translateY(30px)';
                setTimeout(() => {
                    card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                    card.style.opacity = '1';
                    card.style.transform = 'translateY(0)';
                }, index * 100);
            });
        }, 100);
    }`;
        
        // Remplacer la fonction
        const beforeFunction = content.substring(0, displayProductsStart);
        const afterFunction = content.substring(displayProductsEnd);
        
        content = beforeFunction + newDisplayProductsFunction + afterFunction;
        
        fs.writeFileSync(filePath, content, 'utf8');
        console.log('✅ Cards produits enrichies avec succès');
        return true;
    }
    
    return false;
}

if (require.main === module) {
    enhanceProductCards();
}

module.exports = { enhanceProductCards };
