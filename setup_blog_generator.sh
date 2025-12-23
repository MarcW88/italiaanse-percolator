#!/bin/bash

echo "╔═══════════════════════════════════════════════════════════╗"
echo "║                                                           ║"
echo "║   INSTALLATION - Générateur d'Articles de Blog           ║"
echo "║   Italiaanse-Percolator.nl                               ║"
echo "║                                                           ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

# Couleurs
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Vérifier Python
echo -e "${BLUE}🔍 Vérification de Python...${NC}"
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✅ Python trouvé: $PYTHON_VERSION${NC}"
else
    echo -e "${RED}❌ Python 3 n'est pas installé!${NC}"
    echo "📥 Installer Python: https://www.python.org/downloads/"
    exit 1
fi

# Vérifier pip
echo ""
echo -e "${BLUE}🔍 Vérification de pip...${NC}"
if command -v pip3 &> /dev/null; then
    echo -e "${GREEN}✅ pip3 trouvé${NC}"
else
    echo -e "${RED}❌ pip3 n'est pas installé!${NC}"
    exit 1
fi

# Installer les dépendances
echo ""
echo -e "${BLUE}📦 Installation des dépendances Python...${NC}"
pip3 install -r requirements_blog.txt

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Dépendances installées avec succès!${NC}"
else
    echo -e "${RED}❌ Erreur lors de l'installation${NC}"
    exit 1
fi

# Créer le dossier blog
echo ""
echo -e "${BLUE}📁 Création du dossier blog/...${NC}"
mkdir -p blog
echo -e "${GREEN}✅ Dossier créé${NC}"

# Rendre les scripts exécutables
echo ""
echo -e "${BLUE}🔧 Configuration des permissions...${NC}"
chmod +x blog_generator.py
chmod +x blog_generator_advanced.py
chmod +x test_blog_setup.py
echo -e "${GREEN}✅ Scripts exécutables${NC}"

# Créer .env si nécessaire
echo ""
if [ ! -f .env ]; then
    echo -e "${YELLOW}📝 Création du fichier .env...${NC}"
    cp .env.example .env
    echo -e "${GREEN}✅ Fichier .env créé${NC}"
    echo -e "${YELLOW}⚠️  N'oublie pas d'ajouter ta clé API dans .env${NC}"
else
    echo -e "${BLUE}ℹ️  Fichier .env existe déjà${NC}"
fi

# Tester l'installation
echo ""
echo "════════════════════════════════════════════════════════════"
echo -e "${GREEN}✅ INSTALLATION TERMINÉE!${NC}"
echo "════════════════════════════════════════════════════════════"
echo ""
echo -e "${BLUE}📋 Prochaines étapes:${NC}"
echo ""
echo "1. Obtenir une clé API OpenAI:"
echo "   → https://platform.openai.com/api-keys"
echo ""
echo "2. Tester la configuration:"
echo "   → python3 test_blog_setup.py"
echo ""
echo "3. Générer ton premier article:"
echo "   → python3 blog_generator.py"
echo "   ou"
echo "   → python3 blog_generator_advanced.py"
echo ""
echo "4. Lire la documentation:"
echo "   → README_BLOG_GENERATOR.md"
echo ""
echo -e "${GREEN}🚀 Bon blogging!${NC}"
echo ""
