const fs = require('fs');

function addSubcategoriesToPercolators() {
    console.log('🏷️ Ajout des sous-catégories à la page percolators...\n');
    
    const filePath = '/Users/marc/Desktop/italiaanse-percolator/categories/percolators.html';
    let content = fs.readFileSync(filePath, 'utf8');
    
    // Styles CSS pour les sous-catégories
    const subcategoryStyles = `
    .subcategories-container {
        margin-bottom: 3rem;
    }
    
    .subcategory-section {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid #f0f0f0;
        transition: all 0.3s ease;
    }
    
    .subcategory-section:hover {
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
        transform: translateY(-2px);
    }
    
    .subcategory-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 2px solid #f8f9fa;
    }
    
    .subcategory-title {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .subcategory-icon {
        width: 60px;
        height: 60px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.8rem;
        color: white;
        font-weight: bold;
    }
    
    .moka-express-icon { background: linear-gradient(135deg, #D2691E, #8B4513); }
    .venus-icon { background: linear-gradient(135deg, #4169E1, #1E3A8A); }
    .brikka-icon { background: linear-gradient(135deg, #059669, #047857); }
    .mini-rainbow-icon { background: linear-gradient(135deg, #DC2626, #991B1B); }
    
    .subcategory-info h3 {
        font-size: 1.8rem;
        margin: 0 0 0.5rem 0;
        color: #333;
        font-weight: 700;
    }
    
    .subcategory-description {
        color: #666;
        font-size: 1rem;
        line-height: 1.5;
        margin: 0;
    }
    
    .subcategory-badge {
        background: linear-gradient(135deg, #D2691E, #8B4513);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
        white-space: nowrap;
    }
    
    .venus-badge { background: linear-gradient(135deg, #4169E1, #1E3A8A); }
    .brikka-badge { background: linear-gradient(135deg, #059669, #047857); }
    .mini-rainbow-badge { background: linear-gradient(135deg, #DC2626, #991B1B); }
    
    .subcategory-products {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
        gap: 1.5rem;
        margin-bottom: 1.5rem;
    }
    
    .subcategory-product {
        background: #f8f9fa;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.2s;
        border: 2px solid transparent;
        position: relative;
        overflow: hidden;
    }
    
    .subcategory-product:hover {
        background: white;
        border-color: #D2691E;
        transform: translateY(-3px);
        box-shadow: 0 6px 25px rgba(0,0,0,0.1);
    }
    
    .product-badge {
        position: absolute;
        top: 12px;
        right: 12px;
        background: #D2691E;
        color: white;
        padding: 0.3rem 0.6rem;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    
    .bestseller-badge { background: #059669; }
    .popular-badge { background: #DC2626; }
    .induction-badge { background: #4169E1; }
    
    .subcategory-product img {
        width: 100%;
        height: 140px;
        object-fit: contain;
        margin-bottom: 1rem;
        border-radius: 8px;
    }
    
    .subcategory-product h4 {
        font-size: 1rem;
        margin: 0 0 0.5rem 0;
        color: #333;
        line-height: 1.3;
    }
    
    .subcategory-product .specs {
        font-size: 0.85rem;
        color: #666;
        margin-bottom: 1rem;
    }
    
    .subcategory-product .price {
        font-size: 1.2rem;
        font-weight: bold;
        color: #D2691E;
        margin-bottom: 1rem;
    }
    
    .view-all-btn {
        background: linear-gradient(135deg, #D2691E, #8B4513);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s;
        font-size: 0.95rem;
    }
    
    .view-all-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(210, 105, 30, 0.3);
    }
    
    .subcategory-stats {
        display: flex;
        gap: 2rem;
        margin-top: 1rem;
        font-size: 0.9rem;
        color: #666;
    }
    
    .stat-item {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    @media (max-width: 768px) {
        .subcategory-header {
            flex-direction: column;
            align-items: flex-start;
            gap: 1rem;
        }
        
        .subcategory-products {
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 1rem;
        }
        
        .subcategory-stats {
            flex-direction: column;
            gap: 0.5rem;
        }
    }`;
    
    // Insérer les styles après les styles existants
    const existingStylesEnd = content.indexOf('</style>');
    if (existingStylesEnd !== -1) {
        content = content.substring(0, existingStylesEnd) + subcategoryStyles + content.substring(existingStylesEnd);
    }
    
    // Structure HTML des sous-catégories
    const subcategoriesHTML = `
        <!-- Sous-catégories -->
        <div class="subcategories-container">
            <!-- Section 1: Moka Express -->
            <div class="subcategory-section" id="moka-express-section">
                <div class="subcategory-header">
                    <div class="subcategory-title">
                        <div class="subcategory-icon moka-express-icon">☕</div>
                        <div class="subcategory-info">
                            <h3>Bialetti Moka Express - De Klassieker</h3>
                            <p class="subcategory-description">
                                De iconische aluminium percolator sinds 1933. Perfect voor authentieke Italiaanse koffie op alle kookplaten behalve inductie.
                            </p>
                        </div>
                    </div>
                    <div class="subcategory-badge">Meest verkocht</div>
                </div>
                
                <div class="subcategory-products">
                    <div class="subcategory-product">
                        <div class="product-badge bestseller-badge">Bestseller</div>
                        <img src="../Images/bialetti-moka-express-1.jpg" alt="Moka Express 3 Kops" onerror="this.src='../Images/placeholder-product.jpg'">
                        <h4>Moka Express 3 Kops</h4>
                        <div class="specs">Aluminium • 150ml • Gas/Elektrisch</div>
                        <div class="price">€28,99</div>
                    </div>
                    
                    <div class="subcategory-product">
                        <img src="../Images/bialetti-moka-express-6.jpg" alt="Moka Express 6 Kops" onerror="this.src='../Images/placeholder-product.jpg'">
                        <h4>Moka Express 6 Kops</h4>
                        <div class="specs">Aluminium • 300ml • Gas/Elektrisch</div>
                        <div class="price">€35,95</div>
                    </div>
                    
                    <div class="subcategory-product">
                        <div class="product-badge popular-badge">Populair</div>
                        <img src="../Images/bialetti-moka-express-rood.jpg" alt="Moka Express Rood" onerror="this.src='../Images/placeholder-product.jpg'">
                        <h4>Moka Express 3 Kops Rood</h4>
                        <div class="specs">Aluminium • 150ml • Limited Edition</div>
                        <div class="price">€32,99</div>
                    </div>
                </div>
                
                <div class="subcategory-stats">
                    <div class="stat-item">📊 28 modellen beschikbaar</div>
                    <div class="stat-item">⭐ 4.7/5 gemiddelde score</div>
                    <div class="stat-item">🚚 Gratis verzending vanaf €20</div>
                </div>
                
                <div style="text-align: center; margin-top: 1.5rem;">
                    <button class="view-all-btn" onclick="filterByModel('moka-express')">
                        Bekijk alle Moka Express modellen →
                    </button>
                </div>
            </div>
            
            <!-- Section 2: Venus -->
            <div class="subcategory-section" id="venus-section">
                <div class="subcategory-header">
                    <div class="subcategory-title">
                        <div class="subcategory-icon venus-icon">⚡</div>
                        <div class="subcategory-info">
                            <h3>Bialetti Venus - Voor Inductie</h3>
                            <p class="subcategory-description">
                                Moderne RVS percolators speciaal ontworpen voor inductiekookplaten. Elegant design met superieure warmtegeleiding.
                            </p>
                        </div>
                    </div>
                    <div class="subcategory-badge venus-badge">Beste voor inductie</div>
                </div>
                
                <div class="subcategory-products">
                    <div class="subcategory-product">
                        <div class="product-badge induction-badge">Inductie</div>
                        <img src="../Images/bialetti_venus.jpg" alt="Venus 6 Kops" onerror="this.src='../Images/placeholder-product.jpg'">
                        <h4>Venus 6 Kops RVS</h4>
                        <div class="specs">RVS • 300ml • Alle kookplaten</div>
                        <div class="price">€45,95</div>
                    </div>
                    
                    <div class="subcategory-product">
                        <img src="../Images/bialetti-venus-copper.jpg" alt="Venus Copper" onerror="this.src='../Images/placeholder-product.jpg'">
                        <h4>Venus Copper 4 Kops</h4>
                        <div class="specs">RVS/Koper • 200ml • Premium</div>
                        <div class="price">€52,95</div>
                    </div>
                    
                    <div class="subcategory-product">
                        <img src="../Images/bialetti-venus-blue.jpg" alt="Venus Blue" onerror="this.src='../Images/placeholder-product.jpg'">
                        <h4>Venus Blue Metallic</h4>
                        <div class="specs">RVS • 300ml • Limited Edition</div>
                        <div class="price">€49,95</div>
                    </div>
                </div>
                
                <div class="subcategory-stats">
                    <div class="stat-item">📊 12 modellen beschikbaar</div>
                    <div class="stat-item">⭐ 4.5/5 gemiddelde score</div>
                    <div class="stat-item">⚡ 100% inductie compatible</div>
                </div>
                
                <div style="text-align: center; margin-top: 1.5rem;">
                    <button class="view-all-btn" onclick="filterByModel('venus')">
                        Bekijk alle Venus modellen →
                    </button>
                </div>
            </div>
            
            <!-- Section 3: Brikka -->
            <div class="subcategory-section" id="brikka-section">
                <div class="subcategory-header">
                    <div class="subcategory-title">
                        <div class="subcategory-icon brikka-icon">🌟</div>
                        <div class="subcategory-info">
                            <h3>Bialetti Brikka - Met Crema</h3>
                            <p class="subcategory-description">
                                Unieke percolator met speciaal drukventiel voor echte crema. Voor koffieliefhebbers die het beste willen.
                            </p>
                        </div>
                    </div>
                    <div class="subcategory-badge brikka-badge">Speciaal drukventiel</div>
                </div>
                
                <div class="subcategory-products">
                    <div class="subcategory-product">
                        <div class="product-badge">Crema</div>
                        <img src="../Images/bialetti-brikka.jpg" alt="Brikka 4 Kops" onerror="this.src='../Images/placeholder-product.jpg'">
                        <h4>Brikka 4 Kops Aluminium</h4>
                        <div class="specs">Aluminium • 200ml • Crema ventiel</div>
                        <div class="price">€42,95</div>
                    </div>
                    
                    <div class="subcategory-product">
                        <div class="product-badge induction-badge">Inductie</div>
                        <img src="../Images/bialetti-brikka-induction.jpg" alt="Brikka Induction" onerror="this.src='../Images/placeholder-product.jpg'">
                        <h4>Brikka Induction 4 Kops</h4>
                        <div class="specs">RVS • 200ml • Inductie + Crema</div>
                        <div class="price">€59,95</div>
                    </div>
                    
                    <div class="subcategory-product">
                        <img src="../Images/bialetti-brikka-evolution.jpg" alt="Brikka Evolution" onerror="this.src='../Images/placeholder-product.jpg'">
                        <h4>Brikka Evolution 2 Kops</h4>
                        <div class="specs">Aluminium • 100ml • Compact</div>
                        <div class="price">€38,95</div>
                    </div>
                </div>
                
                <div class="subcategory-stats">
                    <div class="stat-item">📊 6 modellen beschikbaar</div>
                    <div class="stat-item">⭐ 4.6/5 gemiddelde score</div>
                    <div class="stat-item">🌟 Uniek crema systeem</div>
                </div>
                
                <div style="text-align: center; margin-top: 1.5rem;">
                    <button class="view-all-btn" onclick="filterByModel('brikka')">
                        Bekijk alle Brikka modellen →
                    </button>
                </div>
            </div>
            
            <!-- Section 4: Mini Express & Rainbow -->
            <div class="subcategory-section" id="mini-rainbow-section">
                <div class="subcategory-header">
                    <div class="subcategory-title">
                        <div class="subcategory-icon mini-rainbow-icon">🎨</div>
                        <div class="subcategory-info">
                            <h3>Mini Express & Rainbow - Compact & Kleurrijk</h3>
                            <p class="subcategory-description">
                                Compacte modellen en kleurrijke varianten. Perfect voor kleine huishoudens of als cadeau.
                            </p>
                        </div>
                    </div>
                    <div class="subcategory-badge mini-rainbow-badge">Compact design</div>
                </div>
                
                <div class="subcategory-products">
                    <div class="subcategory-product">
                        <div class="product-badge">Compact</div>
                        <img src="../Images/bialetti-mini-express.jpg" alt="Mini Express 2 Kops" onerror="this.src='../Images/placeholder-product.jpg'">
                        <h4>Mini Express 2 Kops</h4>
                        <div class="specs">Aluminium • 100ml • Ultra compact</div>
                        <div class="price">€24,95</div>
                    </div>
                    
                    <div class="subcategory-product">
                        <div class="product-badge popular-badge">Kleurrijk</div>
                        <img src="../Images/bialetti-rainbow-rood.jpg" alt="Rainbow Rood" onerror="this.src='../Images/placeholder-product.jpg'">
                        <h4>Rainbow 3 Kops Rood</h4>
                        <div class="specs">Aluminium • 150ml • Vrolijke kleur</div>
                        <div class="price">€31,95</div>
                    </div>
                    
                    <div class="subcategory-product">
                        <img src="../Images/bialetti-rainbow-blauw.jpg" alt="Rainbow Blauw" onerror="this.src='../Images/placeholder-product.jpg'">
                        <h4>Rainbow 6 Kops Azzurro</h4>
                        <div class="specs">Aluminium • 300ml • Limited Edition</div>
                        <div class="price">€36,95</div>
                    </div>
                </div>
                
                <div class="subcategory-stats">
                    <div class="stat-item">📊 10 modellen beschikbaar</div>
                    <div class="stat-item">⭐ 4.4/5 gemiddelde score</div>
                    <div class="stat-item">🎁 Perfect als cadeau</div>
                </div>
                
                <div style="text-align: center; margin-top: 1.5rem;">
                    <button class="view-all-btn" onclick="filterByModel('mini-rainbow')">
                        Bekijk alle Mini & Rainbow modellen →
                    </button>
                </div>
            </div>
        </div>`;
    
    // Insérer les sous-catégories avant les filtres
    const filtersStart = content.indexOf('<div class="filters-container">');
    if (filtersStart !== -1) {
        const beforeSubcategories = content.substring(0, filtersStart);
        const afterSubcategories = content.substring(filtersStart);
        
        content = beforeSubcategories + subcategoriesHTML + '\n        ' + afterSubcategories;
        
        fs.writeFileSync(filePath, content, 'utf8');
        console.log('✅ Sous-catégories ajoutées avec succès');
        return true;
    }
    
    return false;
}

if (require.main === module) {
    addSubcategoriesToPercolators();
}

module.exports = { addSubcategoriesToPercolators };
