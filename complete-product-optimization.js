const fs = require('fs');
const path = require('path');

// Banque de questions FAQ diversifiées
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

function extractProductName(filename) {
    // Extract and clean product name from filename
    let name = filename.replace('.html', '');
    
    // Replace hyphens with spaces
    name = name.replace(/-/g, ' ');
    
    // Capitalize first letters
    name = name.split(' ').map(word => 
        word.charAt(0).toUpperCase() + word.slice(1)
    ).join(' ');
    
    return name;
}

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
                question: randomQuestion.question.replace(/{productName}/g, productName),
                answer: randomQuestion.answer.replace(/{productName}/g, productName)
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
            question: randomQuestion.question.replace(/{productName}/g, productName),
            answer: randomQuestion.answer.replace(/{productName}/g, productName)
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

function generateEnhancedDescription(productName, originalDescription) {
    // If description is too short or generic, enhance it
    if (originalDescription.length < 50 || originalDescription.includes('Cafetière')) {
        // Create enhanced description based on product name
        const isInduction = productName.toLowerCase().includes('inductie') || productName.toLowerCase().includes('venus') || productName.toLowerCase().includes('musa');
        const capacity = productName.match(/(\d+)\s*kops?/i);
        const material = productName.toLowerCase().includes('aluminium') ? 'aluminium' : 'roestvrijstaal';
        
        let description = `De ${productName} is een`;
        
        if (productName.toLowerCase().includes('bialetti')) {
            description += ' authentieke Bialetti';
        }
        
        description += ` <a href="../index.html#italiaanse-percolator" style="color: #D2691E; text-decoration: none; font-weight: 600;">italiaanse percolator</a>`;
        
        if (capacity) {
            const cupCount = capacity[1];
            if (cupCount === '1') {
                description += ' perfect voor individueel gebruik';
            } else if (cupCount === '2') {
                description += ' ideaal voor koppels of kleine huishoudens';
            } else if (parseInt(cupCount) <= 4) {
                description += ' geschikt voor kleine tot middelgrote huishoudens';
            } else {
                description += ' perfect voor grote huishoudens of kantoren';
            }
        }
        
        description += `. Gemaakt van hoogwaardig ${material}`;
        
        if (isInduction) {
            description += ' en geschikt voor inductiekookplaten';
        }
        
        description += '. Ideaal voor het bereiden van authentieke Italiaanse koffie met de traditionele moka-methode.';
        
        return description;
    }
    
    // If description exists but doesn't have link, add it
    if (!originalDescription.includes('italiaanse-percolator')) {
        return originalDescription.replace(
            /italiaanse percolator/i,
            '<a href="../index.html#italiaanse-percolator" style="color: #D2691E; text-decoration: none; font-weight: 600;">italiaanse percolator</a>'
        );
    }
    
    return originalDescription;
}

// Export functions
module.exports = {
    extractProductName,
    generateFAQHTML,
    generateEnhancedDescription,
    generateRandomFAQ
};

console.log('✅ Optimization functions loaded successfully!');
