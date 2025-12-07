// Script pour analyser et corriger toutes les pages produits
const fs = require('fs');
const path = require('path');

// Navigation de référence (correcte)
const correctNavigation = `                <ul class="nav-menu">
                    <li><a href="../index.html" class="nav-link">Home</a></li>
                    <li><a href="../beste-italiaanse-percolators.html" class="nav-link">Top 10</a></li>
                    <li><a href="../koopgids/index.html" class="nav-link">Koopgids</a></li>
                    <li><a href="../vergelijking/index.html" class="nav-link">Vergelijking</a></li>
                    <li><a href="../over-ons.html" class="nav-link">Over ons</a></li>
                    <li><a href="../boutique.html" class="nav-link" style="background: #D2691E; color: white; padding: 0.5rem 1rem; border-radius: 6px; font-weight: 600;">Winkel</a></li>
                </ul>`;

// Favicon à ajouter
const faviconCode = `    
    <!-- Favicon -->
    <link rel="icon" type="image/svg+xml" href="../favicon.svg">
    <link rel="icon" type="image/svg+xml" sizes="16x16" href="../favicon-simple.svg">
    <link rel="apple-touch-icon" sizes="180x180" href="../favicon.svg">
    <meta name="theme-color" content="#D2691E">`;

// Footer uniforme
const uniformFooter = `    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h4>Italiaanse Percolator</h4>
                    <p style="color: #D1D5DB; line-height: 1.6;">De beste Italiaanse percolators getest en vergeleken. Onafhankelijke reviews voor de perfecte koffie-ervaring.</p>
                </div>
                
                <div class="footer-section">
                    <h4>Reviews</h4>
                    <a href="../beste-italiaanse-percolators.html">Top 10 Percolators</a>
                    <a href="../bialetti-fiammetta-review.html">Bialetti Fiammetta</a>
                    <a href="../bialetti-venus-review.html">Bialetti Venus</a>
                    <a href="../alessi-pulcina-review.html">Alessi Pulcina</a>
                </div>
                
                <div class="footer-section">
                    <h4>Gidsen</h4>
                    <a href="../koopgids/hoe-kies-je-de-juiste-percolator.html">Hoe kies je een percolator?</a>
                    <a href="../koopgids/hoe-onderhoud-je-een-percolator.html">Onderhoud & reiniging</a>
                    <a href="../koopgids/percolator-vs-espressoapparaat.html">Percolator vs espresso</a>
                </div>
                
                <div class="footer-section">
                    <h4>Over ons</h4>
                    <a href="../over-ons.html">Over ons</a>
                    <a href="../contact.html">Contact</a>
                    <a href="../privacy.html">Privacy</a>
                    <a href="../disclaimer.html">Disclaimer</a>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; 2025 Italiaanse Percolator. Als partner van Bol.com en Amazon verdienen wij aan kwalificerende aankopen.</p>
            </div>
        </div>
    </footer>`;

// FAQ questions bank
const faqQuestions = [
    {
        id: 1,
        question: "Hoe gebruik ik de {productName}?",
        answer: "Vul het onderste reservoir met water tot de veiligheidsklep. Plaats gemalen koffie in het filter (niet aandrukken). Schroef de delen samen en zet op middelhoog vuur. Wanneer de koffie begint te borrelen, haal van het vuur.",
        category: "usage"
    },
    {
        id: 2,
        question: "Welke maling moet ik gebruiken voor de {productName}?",
        answer: "Gebruik een middelfijne maling, iets grover dan voor espresso maar fijner dan voor filterkoffie. De maling mag niet te fijn zijn anders verstopt het filter.",
        category: "coffee"
    },
    {
        id: 3,
        question: "Hoe onderhoud ik mijn {productName}?",
        answer: "Spoel na gebruik met warm water (geen zeep). Droog goed af. Vervang de rubber ring en filter jaarlijks. Bewaar met open deksel om vochtophoping te voorkomen.",
        category: "maintenance"
    },
    {
        id: 4,
        question: "Is de {productName} geschikt voor inductie?",
        answer: "Dit hangt af van het materiaal. RVS modellen zoals de Venus en Musa zijn inductiegeschikt. Aluminium modellen hebben een inductieplaatje nodig.",
        category: "compatibility"
    },
    {
        id: 5,
        question: "Hoeveel kopjes koffie maakt de {productName}?",
        answer: "De capaciteit staat aangegeven in het aantal kopjes. Let op: dit zijn Italiaanse espresso-kopjes (ongeveer 50ml), niet grote mokken.",
        category: "capacity"
    },
    {
        id: 6,
        question: "Hoe lang gaat de {productName} mee?",
        answer: "Bij goed onderhoud kan een percolator 10-20 jaar meegaan. De rubber ring moet jaarlijks vervangen worden, maar het hoofdapparaat is zeer duurzaam.",
        category: "durability"
    },
    {
        id: 7,
        question: "Kan ik de {productName} in de vaatwasser?",
        answer: "Aluminium percolators mogen niet in de vaatwasser. RVS modellen zijn soms vaatwasserbestendig, maar handwas wordt aanbevolen voor langere levensduur.",
        category: "maintenance"
    },
    {
        id: 8,
        question: "Waarom smaakt mijn koffie uit de {productName} bitter?",
        answer: "Bittere koffie komt vaak door te hoge temperatuur, te fijne maling, of te lang op het vuur laten staan. Gebruik middelhoog vuur en haal direct van het vuur wanneer de koffie klaar is.",
        category: "troubleshooting"
    },
    {
        id: 9,
        question: "Welke koffie past het beste bij de {productName}?",
        answer: "Gebruik een donkere tot medium-donkere branding voor de beste resultaten. Italiaanse melanges werken uitstekend. Vermijd te lichte brandingen.",
        category: "coffee"
    },
    {
        id: 10,
        question: "Hoe weet ik wanneer de koffie klaar is in de {productName}?",
        answer: "Je hoort het typische pruttel- en sisgeluid langzaam wegvallen. De koffiestroom stopt en er komt een kort, scherp geluid. Zet dan direct het vuur uit.",
        category: "usage"
    },
    {
        id: 11,
        question: "Is de {productName} een goede keuze voor beginners?",
        answer: "Ja, percolators zijn ideaal voor beginners. Ze zijn eenvoudig te gebruiken, betaalbaar en maken consistent goede koffie zonder complexe instellingen.",
        category: "beginner"
    },
    {
        id: 12,
        question: "Hoeveel koffie moet ik gebruiken in de {productName}?",
        answer: "Vul het filter tot net onder de rand, maar druk niet aan. Ongeveer 7-8 gram koffie per kopje is een goede richtlijn.",
        category: "usage"
    }
];

function generateRandomFAQ(productName, numQuestions = 3) {
    // Get different categories for diversity
    const categories = [...new Set(faqQuestions.map(q => q.category))];
    const shuffledCategories = categories.sort(() => 0.5 - Math.random());
    const selectedQuestions = [];
    
    for (let i = 0; i < numQuestions && i < shuffledCategories.length; i++) {
        const categoryQuestions = faqQuestions.filter(q => q.category === shuffledCategories[i]);
        if (categoryQuestions.length > 0) {
            const randomQuestion = categoryQuestions[Math.floor(Math.random() * categoryQuestions.length)];
            selectedQuestions.push({
                ...randomQuestion,
                question: randomQuestion.question.replace('{productName}', productName),
                answer: randomQuestion.answer.replace('{productName}', productName)
            });
        }
    }
    
    // Fill remaining slots if needed
    while (selectedQuestions.length < numQuestions) {
        const remainingQuestions = faqQuestions.filter(q => 
            !selectedQuestions.some(sq => sq.id === q.id)
        );
        if (remainingQuestions.length === 0) break;
        
        const randomQuestion = remainingQuestions[Math.floor(Math.random() * remainingQuestions.length)];
        selectedQuestions.push({
            ...randomQuestion,
            question: randomQuestion.question.replace('{productName}', productName),
            answer: randomQuestion.answer.replace('{productName}', productName)
        });
    }
    
    return selectedQuestions;
}

function generateFAQHTML(productName) {
    const questions = generateRandomFAQ(productName, 3);
    
    let html = `        <!-- FAQ Section -->
        <section style="margin-bottom: 3rem; display: block; clear: both; width: 100%;">
            <h2 style="font-size: 2rem; margin-bottom: 2rem;">Veelgestelde Vragen over de ${productName}</h2>
            
            <div style="max-width: 800px;">`;
    
    questions.forEach((question, index) => {
        const isLast = index === questions.length - 1;
        html += `
                <div style="border: 1px solid #ddd; border-radius: 8px;${isLast ? '' : ' margin-bottom: 1rem;'}">
                    <button onclick="toggleFaq(${index + 1})" style="width: 100%; padding: 1.5rem; background: white; border: none; text-align: left; font-size: 1.1rem; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center;">
                        ${question.question}
                        <span id="faq-icon-${index + 1}">+</span>
                    </button>
                    <div id="faq-content-${index + 1}" style="display: none; padding: 0 1.5rem 1.5rem; color: #666; line-height: 1.6;">
                        ${question.answer}
                    </div>
                </div>`;
    });
    
    html += `
            </div>
        </section>`;
    
    return html;
}

function extractProductName(filename) {
    // Extract product name from filename
    let name = filename.replace('.html', '').replace(/-/g, ' ');
    
    // Capitalize first letters
    name = name.split(' ').map(word => 
        word.charAt(0).toUpperCase() + word.slice(1)
    ).join(' ');
    
    return name;
}

function analyzeProductPage(filePath) {
    const content = fs.readFileSync(filePath, 'utf8');
    const filename = path.basename(filePath);
    const productName = extractProductName(filename);
    
    const issues = [];
    
    // Check navigation
    if (content.includes('italiaanse-percolator-kopen.html')) {
        issues.push('Navigation uses old link (italiaanse-percolator-kopen.html instead of boutique.html)');
    }
    
    // Check favicon
    if (!content.includes('favicon.svg')) {
        issues.push('Missing favicon');
    }
    
    // Check for homepage link
    if (!content.includes('index.html#italiaanse-percolator')) {
        issues.push('Missing link to homepage anchor');
    }
    
    // Check for personalized FAQ
    if (!content.includes(`Veelgestelde Vragen over de ${productName}`)) {
        issues.push('Missing personalized FAQ');
    }
    
    // Check for uniform footer
    if (!content.includes('footer class="footer"')) {
        issues.push('Footer not uniformized');
    }
    
    return {
        filename,
        productName,
        issues,
        needsUpdate: issues.length > 0
    };
}

// Export functions for manual use
module.exports = {
    analyzeProductPage,
    generateFAQHTML,
    extractProductName,
    correctNavigation,
    faviconCode,
    uniformFooter
};
