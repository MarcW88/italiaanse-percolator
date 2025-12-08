const fs = require('fs');

function addAdvancedFilters() {
    console.log('🔍 Ajout des filtres avancés à la page percolators...\n');
    
    const filePath = '/Users/marc/Desktop/italiaanse-percolator/categories/percolators.html';
    
    if (!fs.existsSync(filePath)) {
        console.log('❌ Fichier percolators.html non trouvé');
        return false;
    }
    
    let content = fs.readFileSync(filePath, 'utf8');
    
    // Ajouter les styles CSS pour les filtres
    const filterStyles = `
    <style>
    .filters-container {
        display: grid;
        grid-template-columns: 280px 1fr;
        gap: 2rem;
        margin-top: 2rem;
    }
    
    .filters-sidebar {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        height: fit-content;
        position: sticky;
        top: 2rem;
    }
    
    .filter-section {
        margin-bottom: 2rem;
        padding-bottom: 1.5rem;
        border-bottom: 1px solid #eee;
    }
    
    .filter-section:last-child {
        border-bottom: none;
        margin-bottom: 0;
    }
    
    .filter-title {
        font-weight: 600;
        font-size: 1.1rem;
        margin-bottom: 1rem;
        color: #333;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .filter-option {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 0.75rem;
        cursor: pointer;
        padding: 0.5rem;
        border-radius: 6px;
        transition: background 0.2s;
    }
    
    .filter-option:hover {
        background: #f8f9fa;
    }
    
    .filter-checkbox {
        width: 18px;
        height: 18px;
        border: 2px solid #ddd;
        border-radius: 4px;
        position: relative;
        transition: all 0.2s;
    }
    
    .filter-checkbox.checked {
        background: #D2691E;
        border-color: #D2691E;
    }
    
    .filter-checkbox.checked::after {
        content: '✓';
        position: absolute;
        top: -2px;
        left: 2px;
        color: white;
        font-size: 12px;
        font-weight: bold;
    }
    
    .filter-label {
        font-size: 0.95rem;
        color: #555;
        flex: 1;
    }
    
    .filter-count {
        font-size: 0.85rem;
        color: #888;
        background: #f0f0f0;
        padding: 0.2rem 0.5rem;
        border-radius: 10px;
    }
    
    .price-slider {
        width: 100%;
        margin: 1rem 0;
    }
    
    .price-range {
        display: flex;
        justify-content: space-between;
        font-size: 0.9rem;
        color: #666;
        margin-top: 0.5rem;
    }
    
    .clear-filters {
        background: none;
        border: 1px solid #ddd;
        padding: 0.5rem 1rem;
        border-radius: 6px;
        cursor: pointer;
        font-size: 0.9rem;
        color: #666;
        width: 100%;
        margin-top: 1rem;
        transition: all 0.2s;
    }
    
    .clear-filters:hover {
        border-color: #D2691E;
        color: #D2691E;
    }
    
    .results-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1.5rem;
        padding: 1rem;
        background: #f8f9fa;
        border-radius: 8px;
    }
    
    .results-count {
        font-weight: 600;
        color: #333;
    }
    
    .color-options {
        display: flex;
        gap: 0.5rem;
        flex-wrap: wrap;
        margin-top: 0.5rem;
    }
    
    .color-option {
        width: 24px;
        height: 24px;
        border-radius: 50%;
        border: 2px solid #ddd;
        cursor: pointer;
        transition: all 0.2s;
        position: relative;
    }
    
    .color-option.selected {
        border-color: #D2691E;
        transform: scale(1.1);
    }
    
    .color-option.selected::after {
        content: '✓';
        position: absolute;
        top: 2px;
        left: 6px;
        color: white;
        font-size: 10px;
        font-weight: bold;
        text-shadow: 1px 1px 1px rgba(0,0,0,0.5);
    }
    
    @media (max-width: 768px) {
        .filters-container {
            grid-template-columns: 1fr;
        }
        
        .filters-sidebar {
            position: static;
            order: 2;
        }
        
        .products-grid {
            order: 1;
        }
    }
    </style>`;
    
    // Insérer les styles avant </head>
    content = content.replace('</head>', filterStyles + '\n</head>');
    
    // Créer la structure HTML des filtres
    const filtersHTML = `
        <div class="filters-container">
            <!-- Sidebar Filtres -->
            <div class="filters-sidebar">
                <h3 style="margin-bottom: 1.5rem; color: #333;">Filters</h3>
                
                <!-- Capacité -->
                <div class="filter-section">
                    <div class="filter-title">
                        ☕ Capaciteit
                    </div>
                    <div class="filter-option" onclick="toggleFilter('capacity', '1-2')">
                        <div class="filter-checkbox" id="capacity-1-2"></div>
                        <span class="filter-label">1-2 kopjes (solo)</span>
                        <span class="filter-count">8</span>
                    </div>
                    <div class="filter-option" onclick="toggleFilter('capacity', '3')">
                        <div class="filter-checkbox" id="capacity-3"></div>
                        <span class="filter-label">3 kopjes (1-2 pers)</span>
                        <span class="filter-count">15</span>
                    </div>
                    <div class="filter-option" onclick="toggleFilter('capacity', '4')">
                        <div class="filter-checkbox" id="capacity-4"></div>
                        <span class="filter-label">4 kopjes (2-3 pers)</span>
                        <span class="filter-count">12</span>
                    </div>
                    <div class="filter-option" onclick="toggleFilter('capacity', '6')">
                        <div class="filter-checkbox" id="capacity-6"></div>
                        <span class="filter-label">6 kopjes (3-4 pers)</span>
                        <span class="filter-count">18</span>
                    </div>
                    <div class="filter-option" onclick="toggleFilter('capacity', '9+')">
                        <div class="filter-checkbox" id="capacity-9+"></div>
                        <span class="filter-label">9+ kopjes (gezinnen)</span>
                        <span class="filter-count">3</span>
                    </div>
                </div>
                
                <!-- Matériau -->
                <div class="filter-section">
                    <div class="filter-title">
                        🔧 Materiaal
                    </div>
                    <div class="filter-option" onclick="toggleFilter('material', 'aluminium')">
                        <div class="filter-checkbox" id="material-aluminium"></div>
                        <span class="filter-label">Aluminium (klassiek)</span>
                        <span class="filter-count">42</span>
                    </div>
                    <div class="filter-option" onclick="toggleFilter('material', 'rvs')">
                        <div class="filter-checkbox" id="material-rvs"></div>
                        <span class="filter-label">RVS (inductie, modern)</span>
                        <span class="filter-count">14</span>
                    </div>
                </div>
                
                <!-- Compatibilité -->
                <div class="filter-section">
                    <div class="filter-title">
                        ⚡ Kookplaat
                    </div>
                    <div class="filter-option" onclick="toggleFilter('compatibility', 'all')">
                        <div class="filter-checkbox" id="compatibility-all"></div>
                        <span class="filter-label">Alle kookplaten</span>
                        <span class="filter-count">42</span>
                    </div>
                    <div class="filter-option" onclick="toggleFilter('compatibility', 'induction')">
                        <div class="filter-checkbox" id="compatibility-induction"></div>
                        <span class="filter-label">Speciaal voor inductie</span>
                        <span class="filter-count">14</span>
                    </div>
                </div>
                
                <!-- Gamme -->
                <div class="filter-section">
                    <div class="filter-title">
                        🏷️ Model type
                    </div>
                    <div class="filter-option" onclick="toggleFilter('model', 'moka-express')">
                        <div class="filter-checkbox" id="model-moka-express"></div>
                        <span class="filter-label">Moka Express (klassiek)</span>
                        <span class="filter-count">28</span>
                    </div>
                    <div class="filter-option" onclick="toggleFilter('model', 'venus')">
                        <div class="filter-checkbox" id="model-venus"></div>
                        <span class="filter-label">Venus (RVS/inductie)</span>
                        <span class="filter-count">12</span>
                    </div>
                    <div class="filter-option" onclick="toggleFilter('model', 'brikka')">
                        <div class="filter-checkbox" id="model-brikka"></div>
                        <span class="filter-label">Brikka (crema)</span>
                        <span class="filter-count">6</span>
                    </div>
                    <div class="filter-option" onclick="toggleFilter('model', 'mini-express')">
                        <div class="filter-checkbox" id="model-mini-express"></div>
                        <span class="filter-label">Mini Express (compact)</span>
                        <span class="filter-count">5</span>
                    </div>
                    <div class="filter-option" onclick="toggleFilter('model', 'rainbow')">
                        <div class="filter-checkbox" id="model-rainbow"></div>
                        <span class="filter-label">Rainbow (kleur)</span>
                        <span class="filter-count">5</span>
                    </div>
                </div>
                
                <!-- Prix -->
                <div class="filter-section">
                    <div class="filter-title">
                        💰 Prijsrange
                    </div>
                    <input type="range" class="price-slider" min="20" max="65" value="65" id="priceRange" oninput="updatePriceFilter(this.value)">
                    <div class="price-range">
                        <span>€20</span>
                        <span id="maxPrice">€65</span>
                    </div>
                </div>
                
                <!-- Couleurs -->
                <div class="filter-section">
                    <div class="filter-title">
                        🎨 Kleur
                    </div>
                    <div class="color-options">
                        <div class="color-option" style="background: #c41e3a;" onclick="toggleColorFilter('red')" id="color-red" title="Rood"></div>
                        <div class="color-option" style="background: #2c2c2c;" onclick="toggleColorFilter('black')" id="color-black" title="Zwart"></div>
                        <div class="color-option" style="background: #b87333;" onclick="toggleColorFilter('copper')" id="color-copper" title="Koper"></div>
                        <div class="color-option" style="background: #4169e1;" onclick="toggleColorFilter('blue')" id="color-blue" title="Blauw"></div>
                        <div class="color-option" style="background: #ffd700;" onclick="toggleColorFilter('yellow')" id="color-yellow" title="Geel"></div>
                        <div class="color-option" style="background: #228b22;" onclick="toggleColorFilter('green')" id="color-green" title="Groen"></div>
                        <div class="color-option" style="background: #f5f5dc;" onclick="toggleColorFilter('cream')" id="color-cream" title="Crème"></div>
                    </div>
                </div>
                
                <button class="clear-filters" onclick="clearAllFilters()">
                    Wis alle filters
                </button>
            </div>
            
            <!-- Zone produits -->
            <div class="products-grid">
                <div class="results-header">
                    <div class="results-count" id="resultsCount">56 producten</div>
                    <select id="sortSelect" onchange="sortProducts()" style="padding: 0.5rem; border: 1px solid #ddd; border-radius: 6px;">
                        <option value="popular">Meest populair</option>
                        <option value="price-low">Prijs: laag naar hoog</option>
                        <option value="price-high">Prijs: hoog naar laag</option>
                        <option value="rating">Beste beoordelingen</option>
                        <option value="name">Naam A-Z</option>
                    </select>
                </div>
                
                <div id="productsContainer">
                    <!-- Les produits seront chargés ici -->
                </div>
            </div>
        </div>`;
    
    // Remplacer le contenu après le header
    const headerEnd = content.indexOf('</header>');
    if (headerEnd !== -1) {
        const beforeHeader = content.substring(0, headerEnd + 9);
        const afterContent = content.substring(content.indexOf('</main>'));
        
        content = beforeHeader + '\n' + filtersHTML + '\n    ' + afterContent;
        
        fs.writeFileSync(filePath, content, 'utf8');
        console.log('✅ Structure des filtres avancés ajoutée');
        return true;
    }
    
    return false;
}

if (require.main === module) {
    addAdvancedFilters();
}

module.exports = { addAdvancedFilters };
