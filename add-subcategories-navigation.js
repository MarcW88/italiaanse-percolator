const fs = require('fs');

function addSubcategoriesNavigation() {
    console.log('🧭 Ajout de la navigation entre sous-catégories...\n');
    
    const filePath = '/Users/marc/Desktop/italiaanse-percolator/categories/percolators.html';
    let content = fs.readFileSync(filePath, 'utf8');
    
    const navigationScript = `
    
    // Navigation entre sous-catégories
    function filterByModel(modelType) {
        // Réinitialiser tous les filtres
        clearAllFilters();
        
        // Appliquer le filtre modèle spécifique
        activeFilters.model = [modelType === 'mini-rainbow' ? 'mini-express' : modelType];
        
        // Mettre à jour l'interface
        const checkbox = document.getElementById('model-' + (modelType === 'mini-rainbow' ? 'mini-express' : modelType));
        if (checkbox) {
            checkbox.classList.add('checked');
        }
        
        // Si mini-rainbow, ajouter aussi rainbow
        if (modelType === 'mini-rainbow') {
            activeFilters.model.push('rainbow');
            const rainbowCheckbox = document.getElementById('model-rainbow');
            if (rainbowCheckbox) {
                rainbowCheckbox.classList.add('checked');
            }
        }
        
        // Appliquer les filtres
        applyFilters();
        
        // Scroll vers la zone des résultats
        document.querySelector('.results-header').scrollIntoView({ 
            behavior: 'smooth',
            block: 'start'
        });
        
        // Highlight temporaire de la section
        highlightSection(modelType + '-section');
    }
    
    // Fonction pour highlight une section
    function highlightSection(sectionId) {
        const section = document.getElementById(sectionId);
        if (section) {
            section.style.background = 'linear-gradient(135deg, #fff5f0, #ffffff)';
            section.style.borderColor = '#D2691E';
            
            setTimeout(() => {
                section.style.background = 'white';
                section.style.borderColor = '#f0f0f0';
            }, 2000);
        }
    }
    
    // Fonction pour naviguer vers une section spécifique
    function scrollToSection(sectionId) {
        document.getElementById(sectionId).scrollIntoView({ 
            behavior: 'smooth',
            block: 'start'
        });
    }
    
    // Ajouter navigation rapide en haut
    function addQuickNavigation() {
        const header = document.querySelector('header');
        if (header) {
            const quickNav = document.createElement('div');
            quickNav.innerHTML = \`
                <div style="background: #f8f9fa; padding: 1rem; border-radius: 12px; margin-top: 1.5rem; text-align: center;">
                    <div style="margin-bottom: 0.5rem; font-weight: 600; color: #333;">Ga direct naar:</div>
                    <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
                        <button onclick="scrollToSection('moka-express-section')" style="background: #D2691E; color: white; border: none; padding: 0.5rem 1rem; border-radius: 20px; cursor: pointer; font-size: 0.9rem;">☕ Moka Express</button>
                        <button onclick="scrollToSection('venus-section')" style="background: #4169E1; color: white; border: none; padding: 0.5rem 1rem; border-radius: 20px; cursor: pointer; font-size: 0.9rem;">⚡ Venus</button>
                        <button onclick="scrollToSection('brikka-section')" style="background: #059669; color: white; border: none; padding: 0.5rem 1rem; border-radius: 20px; cursor: pointer; font-size: 0.9rem;">🌟 Brikka</button>
                        <button onclick="scrollToSection('mini-rainbow-section')" style="background: #DC2626; color: white; border: none; padding: 0.5rem 1rem; border-radius: 20px; cursor: pointer; font-size: 0.9rem;">🎨 Mini & Rainbow</button>
                    </div>
                </div>
            \`;
            header.appendChild(quickNav);
        }
    }
    
    // Améliorer la fonction de chargement des produits pour inclure les métadonnées
    function enhanceProductData() {
        // Enrichir les données produits avec les informations de catégorisation
        allProducts = allProducts.map(product => {
            // Déterminer le modèle basé sur le nom
            if (product.name.toLowerCase().includes('moka express') || 
                product.name.toLowerCase().includes('moka italia')) {
                product.model = 'moka-express';
                product.badges = product.badges || [];
                if (product.name.includes('3 kops') || product.name.includes('3 Kops')) {
                    product.badges.push('Beste voor beginners');
                }
            } else if (product.name.toLowerCase().includes('venus')) {
                product.model = 'venus';
                product.badges = product.badges || ['Beste voor inductie'];
                product.compatibility = 'induction';
                product.material = 'rvs';
            } else if (product.name.toLowerCase().includes('brikka')) {
                product.model = 'brikka';
                product.badges = product.badges || ['Crema ventiel'];
            } else if (product.name.toLowerCase().includes('mini express')) {
                product.model = 'mini-express';
                product.badges = product.badges || ['Compact'];
            } else if (product.name.toLowerCase().includes('rainbow')) {
                product.model = 'rainbow';
                product.badges = product.badges || ['Kleurrijk'];
            }
            
            // Déterminer la capacité
            if (product.name.includes('1 kop') || product.name.includes('1 Kop')) {
                product.capacity = '1';
            } else if (product.name.includes('2 kop') || product.name.includes('2 Kop')) {
                product.capacity = '2';
            } else if (product.name.includes('3 kop') || product.name.includes('3 Kop')) {
                product.capacity = '3';
            } else if (product.name.includes('4 kop') || product.name.includes('4 Kop')) {
                product.capacity = '4';
            } else if (product.name.includes('6 kop') || product.name.includes('6 Kop')) {
                product.capacity = '6';
            } else if (product.name.includes('9 kop') || product.name.includes('9 Kop')) {
                product.capacity = '9';
            } else if (product.name.includes('12 kop') || product.name.includes('12 Kop')) {
                product.capacity = '12';
            }
            
            // Déterminer le matériau
            if (product.name.toLowerCase().includes('roestvrijstaal') || 
                product.name.toLowerCase().includes('rvs') ||
                product.name.toLowerCase().includes('venus')) {
                product.material = 'rvs';
                product.compatibility = 'induction';
            } else {
                product.material = 'aluminium';
                product.compatibility = 'all';
            }
            
            // Déterminer la couleur
            if (product.name.toLowerCase().includes('rood') || product.name.toLowerCase().includes('red')) {
                product.color = 'red';
            } else if (product.name.toLowerCase().includes('zwart') || product.name.toLowerCase().includes('black')) {
                product.color = 'black';
            } else if (product.name.toLowerCase().includes('copper') || product.name.toLowerCase().includes('koper')) {
                product.color = 'copper';
            } else if (product.name.toLowerCase().includes('blue') || product.name.toLowerCase().includes('blauw')) {
                product.color = 'blue';
            } else if (product.name.toLowerCase().includes('geel') || product.name.toLowerCase().includes('yellow')) {
                product.color = 'yellow';
            } else if (product.name.toLowerCase().includes('groen') || product.name.toLowerCase().includes('green')) {
                product.color = 'green';
            } else if (product.name.toLowerCase().includes('creme') || product.name.toLowerCase().includes('cream')) {
                product.color = 'cream';
            } else {
                product.color = 'silver';
            }
            
            return product;
        });
    }
    
    // Mettre à jour la fonction de chargement
    const originalLoadProducts = loadProducts;
    loadProducts = async function() {
        await originalLoadProducts();
        enhanceProductData();
        addQuickNavigation();
    };
    
    // Ajouter des animations au scroll
    function addScrollAnimations() {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, { threshold: 0.1 });
        
        document.querySelectorAll('.subcategory-section').forEach(section => {
            section.style.opacity = '0';
            section.style.transform = 'translateY(20px)';
            section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(section);
        });
    }
    
    // Initialiser les animations au chargement
    document.addEventListener('DOMContentLoaded', function() {
        setTimeout(addScrollAnimations, 500);
    });`;
    
    // Insérer le script avant la fermeture du script existant
    const scriptEnd = content.lastIndexOf('</script>');
    if (scriptEnd !== -1) {
        content = content.substring(0, scriptEnd) + navigationScript + content.substring(scriptEnd);
        
        fs.writeFileSync(filePath, content, 'utf8');
        console.log('✅ Navigation entre sous-catégories ajoutée');
        return true;
    }
    
    return false;
}

if (require.main === module) {
    addSubcategoriesNavigation();
}

module.exports = { addSubcategoriesNavigation };
