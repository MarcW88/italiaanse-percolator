// Banque de questions FAQ pour pages produits
// Chaque question utilise {productName} comme placeholder

const faqQuestionsBank = [
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
        question: "Kan ik de {productName} op elk type kookplaat gebruiken?",
        answer: "Gas, elektrisch en keramisch werken altijd. Voor inductie heb je een RVS model nodig of een inductieplaatje voor aluminium modellen.",
        category: "compatibility"
    },
    {
        id: 12,
        question: "Wat is het verschil tussen de {productName} en andere percolators?",
        answer: "Elk model heeft unieke eigenschappen qua materiaal, capaciteit, design en prijs. Bekijk onze vergelijking om de verschillen te zien.",
        category: "comparison"
    },
    {
        id: 13,
        question: "Hoe vervang ik de rubber ring van de {productName}?",
        answer: "Draai de percolator uit elkaar, verwijder de oude ring voorzichtig en plaats de nieuwe ring in dezelfde positie. Zorg dat hij goed vastzit.",
        category: "maintenance"
    },
    {
        id: 14,
        question: "Waarom komt er geen koffie uit mijn {productName}?",
        answer: "Controleer of er genoeg water is, of de maling niet te fijn is, en of alle onderdelen goed vastzitten. Een verstopt filter kan ook de oorzaak zijn.",
        category: "troubleshooting"
    },
    {
        id: 15,
        question: "Is de {productName} een goede keuze voor beginners?",
        answer: "Ja, percolators zijn ideaal voor beginners. Ze zijn eenvoudig te gebruiken, betaalbaar en maken consistent goede koffie zonder complexe instellingen.",
        category: "beginner"
    },
    {
        id: 16,
        question: "Hoeveel koffie moet ik gebruiken in de {productName}?",
        answer: "Vul het filter tot net onder de rand, maar druk niet aan. Ongeveer 7-8 gram koffie per kopje is een goede richtlijn.",
        category: "usage"
    },
    {
        id: 17,
        question: "Kan ik melk opschuimen met de {productName}?",
        answer: "Nee, percolators maken alleen koffie. Voor melkschuim heb je een aparte melkopschuimer of espressomachine met stoompijp nodig.",
        category: "functionality"
    },
    {
        id: 18,
        question: "Wat moet ik doen als de {productName} lekt?",
        answer: "Controleer of de rubber ring goed zit en niet beschadigd is. Zorg dat alle delen goed vastgedraaid zijn, maar niet te strak.",
        category: "troubleshooting"
    }
];

// Functie om willekeurige FAQ te genereren voor een product
function generateProductFAQ(productName, numQuestions = 3) {
    // Selecteer verschillende categorieën voor diversiteit
    const categories = [...new Set(faqQuestionsBank.map(q => q.category))];
    const selectedQuestions = [];
    
    // Probeer verschillende categorieën te kiezen
    const shuffledCategories = categories.sort(() => 0.5 - Math.random());
    
    for (let i = 0; i < numQuestions && i < shuffledCategories.length; i++) {
        const categoryQuestions = faqQuestionsBank.filter(q => q.category === shuffledCategories[i]);
        if (categoryQuestions.length > 0) {
            const randomQuestion = categoryQuestions[Math.floor(Math.random() * categoryQuestions.length)];
            selectedQuestions.push({
                ...randomQuestion,
                question: randomQuestion.question.replace('{productName}', productName),
                answer: randomQuestion.answer.replace('{productName}', productName)
            });
        }
    }
    
    // Si on n'a pas assez de questions, ajouter des questions aléatoires
    while (selectedQuestions.length < numQuestions) {
        const remainingQuestions = faqQuestionsBank.filter(q => 
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

// Export pour utilisation
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { faqQuestionsBank, generateProductFAQ };
}
