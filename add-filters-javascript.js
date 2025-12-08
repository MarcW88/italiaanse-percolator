const fs = require('fs');

function addFiltersJavaScript() {
    console.log('⚡ Ajout du JavaScript pour les filtres...\n');
    
    const filePath = '/Users/marc/Desktop/italiaanse-percolator/categories/percolators.html';
    let content = fs.readFileSync(filePath, 'utf8');
    
    const filterScript = `
    <script>
    // État des filtres
    let activeFilters = {
        capacity: [],
        material: [],
        compatibility: [],
        model: [],
        colors: [],
        maxPrice: 65
    };
    
    // Données produits (simulées pour l'exemple - à remplacer par vraies données)
    let allProducts = [];
    
    // Charger les produits depuis all_products.json
    async function loadProducts() {
        try {
            const response = await fetch('../all_products.json');
            const products = await response.json();
            
            // Filtrer seulement les percolators (pas les accessoires)
            allProducts = products.filter(product => 
                product.type && product.type.includes('percolateur') || 
                product.name.toLowerCase().includes('percolator') ||
                product.name.toLowerCase().includes('moka') ||
                product.name.toLowerCase().includes('venus') ||
                product.name.toLowerCase().includes('brikka')
            );
            
            displayProducts(allProducts);
            updateResultsCount(allProducts.length);
        } catch (error) {
            console.error('Erreur chargement produits:', error);
            // Fallback avec produits de démonstration
            loadDemoProducts();
        }
    }
    
    function loadDemoProducts() {
        // Produits de démonstration pour tester les filtres
        allProducts = [
            {
                name: "Bialetti Moka Express 3 Kops Aluminium",
                slug: "bialetti-moka-express-percolator-3-kops-aluminium",
                prijs: 28.99,
                image: "../Images/bialetti-moka-express-1.jpg",
                rating: 4.7,
                reviews: 147,
                capacity: "3",
                material: "aluminium",
                compatibility: "all",
                model: "moka-express",
                color: "silver",
                badges: ["Beste voor beginners", "Meest populair"]
            },
            {
                name: "Bialetti Venus 6 Kops RVS Inductie",
                slug: "bialetti-percolator-venus-6-kops-roestvrijstaal-inductiegeschikt",
                prijs: 45.95,
                image: "../Images/bialetti_venus.jpg",
                rating: 4.5,
                reviews: 89,
                capacity: "6",
                material: "rvs",
                compatibility: "induction",
                model: "venus",
                color: "silver",
                badges: ["Beste voor inductie"]
            }
            // Plus de produits seraient ajoutés ici...
        ];
        
        displayProducts(allProducts);
        updateResultsCount(allProducts.length);
    }
    
    // Fonction pour basculer un filtre
    function toggleFilter(category, value) {
        const checkbox = document.getElementById(category + '-' + value);
        
        if (activeFilters[category].includes(value)) {
            // Retirer le filtre
            activeFilters[category] = activeFilters[category].filter(item => item !== value);
            checkbox.classList.remove('checked');
        } else {
            // Ajouter le filtre
            activeFilters[category].push(value);
            checkbox.classList.add('checked');
        }
        
        applyFilters();
    }
    
    // Fonction pour les filtres couleur
    function toggleColorFilter(color) {
        const colorElement = document.getElementById('color-' + color);
        
        if (activeFilters.colors.includes(color)) {
            activeFilters.colors = activeFilters.colors.filter(c => c !== color);
            colorElement.classList.remove('selected');
        } else {
            activeFilters.colors.push(color);
            colorElement.classList.add('selected');
        }
        
        applyFilters();
    }
    
    // Fonction pour le filtre prix
    function updatePriceFilter(maxPrice) {
        activeFilters.maxPrice = parseInt(maxPrice);
        document.getElementById('maxPrice').textContent = '€' + maxPrice;
        applyFilters();
    }
    
    // Appliquer tous les filtres
    function applyFilters() {
        let filteredProducts = allProducts.filter(product => {
            // Filtre capacité
            if (activeFilters.capacity.length > 0) {
                let matchesCapacity = false;
                for (let cap of activeFilters.capacity) {
                    if (cap === '1-2' && (product.capacity === '1' || product.capacity === '2')) {
                        matchesCapacity = true;
                    } else if (cap === '9+' && parseInt(product.capacity) >= 9) {
                        matchesCapacity = true;
                    } else if (product.capacity === cap) {
                        matchesCapacity = true;
                    }
                }
                if (!matchesCapacity) return false;
            }
            
            // Filtre matériau
            if (activeFilters.material.length > 0) {
                if (!activeFilters.material.includes(product.material)) return false;
            }
            
            // Filtre compatibilité
            if (activeFilters.compatibility.length > 0) {
                if (!activeFilters.compatibility.includes(product.compatibility)) return false;
            }
            
            // Filtre modèle
            if (activeFilters.model.length > 0) {
                if (!activeFilters.model.includes(product.model)) return false;
            }
            
            // Filtre couleur
            if (activeFilters.colors.length > 0) {
                if (!activeFilters.colors.includes(product.color)) return false;
            }
            
            // Filtre prix
            if (product.prijs > activeFilters.maxPrice) return false;
            
            return true;
        });
        
        displayProducts(filteredProducts);
        updateResultsCount(filteredProducts.length);
    }
    
    // Afficher les produits
    function displayProducts(products) {
        const container = document.getElementById('productsContainer');
        
        if (products.length === 0) {
            container.innerHTML = \`
                <div style="text-align: center; padding: 3rem; color: #666;">
                    <h3>😔 Geen producten gevonden</h3>
                    <p>Probeer:</p>
                    <button onclick="clearAllFilters()" style="margin: 1rem; padding: 0.5rem 1rem; background: #D2691E; color: white; border: none; border-radius: 6px; cursor: pointer;">Wis alle filters</button>
                    <br>
                    <a href="../koopgids/index.html" style="color: #D2691E;">Lees onze koopgids</a>
                </div>
            \`;
            return;
        }
        
        const productsHTML = products.map(product => \`
            <div class="product-card" style="background: white; border-radius: 12px; padding: 1.5rem; box-shadow: 0 4px 20px rgba(0,0,0,0.1); transition: transform 0.2s; margin-bottom: 1.5rem;">
                <div style="position: relative; margin-bottom: 1rem;">
                    <img src="\${product.image}" alt="\${product.name}" 
                         style="width: 100%; height: 200px; object-fit: contain; border-radius: 8px;"
                         onerror="this.src='../Images/placeholder-product.jpg'">
                    \${product.badges ? product.badges.map(badge => \`
                        <span style="position: absolute; top: 8px; left: 8px; background: #D2691E; color: white; padding: 0.3rem 0.6rem; border-radius: 12px; font-size: 0.8rem; font-weight: 600;">
                            \${badge}
                        </span>
                    \`).join('') : ''}
                </div>
                
                <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem; line-height: 1.3;">\${product.name}</h3>
                
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
                    <span style="color: #ffd700;">⭐ \${product.rating}</span>
                    <span style="color: #666; font-size: 0.9rem;">(\${product.reviews} reviews)</span>
                </div>
                
                <div style="margin-bottom: 1rem; font-size: 0.9rem; color: #666;">
                    <div>📏 Capaciteit: \${product.capacity} kopjes</div>
                    <div>🔧 Materiaal: \${product.material === 'rvs' ? 'RVS' : 'Aluminium'}</div>
                    <div>⚡ Geschikt voor: \${product.compatibility === 'induction' ? 'Inductie' : 'Alle kookplaten'}</div>
                </div>
                
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-size: 1.3rem; font-weight: bold; color: #D2691E;">€\${product.prijs}</span>
                    <div style="display: flex; gap: 0.5rem;">
                        <button onclick="addToWishlist('\${product.slug}')" style="background: none; border: 1px solid #ddd; padding: 0.5rem; border-radius: 6px; cursor: pointer;">❤️</button>
                        <a href="../producten/\${product.slug}.html" style="background: #D2691E; color: white; padding: 0.5rem 1rem; border-radius: 6px; text-decoration: none; font-weight: 600;">Bekijk details</a>
                    </div>
                </div>
            </div>
        \`).join('');
        
        container.innerHTML = \`
            <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1.5rem;">
                \${productsHTML}
            </div>
        \`;
    }
    
    // Mettre à jour le compteur de résultats
    function updateResultsCount(count) {
        document.getElementById('resultsCount').textContent = count + ' producten';
    }
    
    // Effacer tous les filtres
    function clearAllFilters() {
        activeFilters = {
            capacity: [],
            material: [],
            compatibility: [],
            model: [],
            colors: [],
            maxPrice: 65
        };
        
        // Réinitialiser l'interface
        document.querySelectorAll('.filter-checkbox').forEach(cb => cb.classList.remove('checked'));
        document.querySelectorAll('.color-option').forEach(co => co.classList.remove('selected'));
        document.getElementById('priceRange').value = 65;
        document.getElementById('maxPrice').textContent = '€65';
        
        // Réappliquer (montrer tous les produits)
        applyFilters();
    }
    
    // Trier les produits
    function sortProducts() {
        const sortValue = document.getElementById('sortSelect').value;
        const container = document.getElementById('productsContainer');
        const currentProducts = getCurrentDisplayedProducts();
        
        let sortedProducts = [...currentProducts];
        
        switch(sortValue) {
            case 'price-low':
                sortedProducts.sort((a, b) => a.prijs - b.prijs);
                break;
            case 'price-high':
                sortedProducts.sort((a, b) => b.prijs - a.prijs);
                break;
            case 'rating':
                sortedProducts.sort((a, b) => b.rating - a.rating);
                break;
            case 'name':
                sortedProducts.sort((a, b) => a.name.localeCompare(b.name));
                break;
            default: // popular
                // Garder l'ordre par défaut
                break;
        }
        
        displayProducts(sortedProducts);
    }
    
    function getCurrentDisplayedProducts() {
        // Récupérer les produits actuellement affichés après filtrage
        return allProducts.filter(product => {
            // Même logique que applyFilters()
            if (activeFilters.capacity.length > 0) {
                let matchesCapacity = false;
                for (let cap of activeFilters.capacity) {
                    if (cap === '1-2' && (product.capacity === '1' || product.capacity === '2')) {
                        matchesCapacity = true;
                    } else if (cap === '9+' && parseInt(product.capacity) >= 9) {
                        matchesCapacity = true;
                    } else if (product.capacity === cap) {
                        matchesCapacity = true;
                    }
                }
                if (!matchesCapacity) return false;
            }
            
            if (activeFilters.material.length > 0) {
                if (!activeFilters.material.includes(product.material)) return false;
            }
            
            if (activeFilters.compatibility.length > 0) {
                if (!activeFilters.compatibility.includes(product.compatibility)) return false;
            }
            
            if (activeFilters.model.length > 0) {
                if (!activeFilters.model.includes(product.model)) return false;
            }
            
            if (activeFilters.colors.length > 0) {
                if (!activeFilters.colors.includes(product.color)) return false;
            }
            
            if (product.prijs > activeFilters.maxPrice) return false;
            
            return true;
        });
    }
    
    // Fonction wishlist (localStorage)
    function addToWishlist(productSlug) {
        let wishlist = JSON.parse(localStorage.getItem('wishlist') || '[]');
        
        if (!wishlist.includes(productSlug)) {
            wishlist.push(productSlug);
            localStorage.setItem('wishlist', JSON.stringify(wishlist));
            
            // Feedback visuel
            alert('Toegevoegd aan verlanglijst! ❤️');
        } else {
            alert('Al in verlanglijst!');
        }
    }
    
    // Initialiser au chargement de la page
    document.addEventListener('DOMContentLoaded', function() {
        loadProducts();
    });
    </script>`;
    
    // Insérer le script avant </body>
    content = content.replace('</body>', filterScript + '\n</body>');
    
    fs.writeFileSync(filePath, content, 'utf8');
    console.log('✅ JavaScript des filtres ajouté');
    
    return true;
}

if (require.main === module) {
    addFiltersJavaScript();
}

module.exports = { addFiltersJavaScript };
