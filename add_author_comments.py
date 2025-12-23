#!/usr/bin/env python3
"""
Script pour ajouter le bloc auteur et la section commentaires aux articles du koopgids
"""

import re

# Styles CSS à ajouter
css_styles = """
        .author-box {
            background: linear-gradient(135deg, #fff9f0 0%, #ffe9d0 100%);
            border-left: 4px solid #4caf50;
            border-radius: 8px;
            padding: 2rem;
            margin: 3rem 0;
            display: flex;
            gap: 1.5rem;
            align-items: flex-start;
        }
        
        .author-avatar {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid #D2691E;
            flex-shrink: 0;
        }
        
        .author-info h3 {
            color: #4caf50;
            font-size: 1.3rem;
            margin: 0 0 0.5rem 0;
        }
        
        .author-name {
            font-size: 1.1rem;
            font-weight: 600;
            color: #333;
            margin-bottom: 1rem;
        }
        
        .author-bio {
            color: #555;
            line-height: 1.7;
            margin: 0;
        }
        
        .comments-section {
            background: #f8f9fa;
            border-radius: 8px;
            padding: 2rem;
            margin: 3rem 0;
        }
        
        .comments-section h3 {
            color: #D2691E;
            font-size: 1.8rem;
            margin-bottom: 1.5rem;
        }
        
        .comment-form {
            background: white;
            padding: 1.5rem;
            border-radius: 8px;
            margin-bottom: 2rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        
        .comment-form h4 {
            color: #333;
            margin-top: 0;
            margin-bottom: 1rem;
        }
        
        .form-group {
            margin-bottom: 1rem;
        }
        
        .form-group label {
            display: block;
            font-weight: 600;
            margin-bottom: 0.5rem;
            color: #555;
        }
        
        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-family: inherit;
            font-size: 1rem;
        }
        
        .form-group textarea {
            min-height: 120px;
            resize: vertical;
        }
        
        .submit-btn {
            background: #D2691E;
            color: white;
            padding: 0.75rem 2rem;
            border: none;
            border-radius: 4px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.3s;
        }
        
        .submit-btn:hover {
            background: #8B4513;
        }
        
        .comments-list {
            margin-top: 2rem;
        }
        
        .comment {
            background: white;
            padding: 1.5rem;
            border-radius: 8px;
            margin-bottom: 1rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        
        .comment-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid #eee;
        }
        
        .comment-author {
            font-weight: 600;
            color: #D2691E;
        }
        
        .comment-date {
            color: #999;
            font-size: 0.9rem;
        }
        
        .comment-body {
            color: #555;
            line-height: 1.6;
        }
        
        .no-comments {
            text-align: center;
            padding: 2rem;
            color: #999;
            font-style: italic;
        }
"""

# HTML du bloc auteur
author_box_html = """
        <!-- Author Box -->
        <div class="author-box">
            <img src="../Images/author-marc.jpg" alt="Marc - Koffie Expert" class="author-avatar" onerror="this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%22100%22 height=%22100%22 viewBox=%220 0 100 100%22%3E%3Ccircle cx=%2250%22 cy=%2250%22 r=%2250%22 fill=%22%23D2691E%22/%3E%3Ctext x=%2250%22 y=%2255%22 font-size=%2240%22 text-anchor=%22middle%22 fill=%22white%22 font-family=%22Arial%22%3EM%3C/text%3E%3C/svg%3E'">
            <div class="author-info">
                <h3>✍️ Over de auteur</h3>
                <div class="author-name">Marc</div>
                <p class="author-bio">
                    Als koffieliefhebber en Italië-kenner ben ik gefascineerd door de kunst van traditionele Italiaanse koffie. Met meer dan 10 jaar ervaring in het testen van percolators en het perfectioneren van mokakoffie, deel ik graag mijn kennis en passie. Mijn doel is om je te helpen de perfecte koffie-ervaring thuis te creëren, met de juiste apparatuur en techniek.
                </p>
                <p class="author-bio">
                    Door mijn artikelen leer je niet alleen welke percolator het beste bij je past, maar ook hoe je elke ochtend authentieke Italiaanse koffie zet. Buon caffè!
                </p>
            </div>
        </div>

        <!-- Comments Section -->
        <div class="comments-section">
            <h3>💬 Reacties</h3>
            
            <!-- Comment Form -->
            <div class="comment-form">
                <h4>Laat een reactie achter</h4>
                <form id="commentForm" onsubmit="return handleCommentSubmit(event)">
                    <div class="form-group">
                        <label for="comment-name">Naam *</label>
                        <input type="text" id="comment-name" name="name" required placeholder="Je naam">
                    </div>
                    <div class="form-group">
                        <label for="comment-email">E-mail * (wordt niet gepubliceerd)</label>
                        <input type="email" id="comment-email" name="email" required placeholder="je@email.nl">
                    </div>
                    <div class="form-group">
                        <label for="comment-message">Reactie *</label>
                        <textarea id="comment-message" name="message" required placeholder="Deel je ervaring of stel een vraag..."></textarea>
                    </div>
                    <button type="submit" class="submit-btn">Reactie plaatsen</button>
                </form>
            </div>
            
            <!-- Comments List -->
            <div class="comments-list" id="commentsList">
                <div class="no-comments">Wees de eerste om een reactie achter te laten!</div>
            </div>
        </div>
"""

# JavaScript pour les commentaires (template)
comments_js_template = """
    <script>
        // Comment submission handler
        function handleCommentSubmit(event) {
            event.preventDefault();
            
            const form = event.target;
            const name = form.name.value;
            const email = form.email.value;
            const message = form.message.value;
            
            // Get existing comments from localStorage
            const articleId = '{article_id}';
            let comments = JSON.parse(localStorage.getItem('comments_' + articleId) || '[]');
            
            // Add new comment
            const newComment = {
                id: Date.now(),
                name: name,
                email: email,
                message: message,
                date: new Date().toISOString()
            };
            
            comments.unshift(newComment);
            localStorage.setItem('comments_' + articleId, JSON.stringify(comments));
            
            // Clear form
            form.reset();
            
            // Reload comments
            loadComments();
            
            // Show success message
            alert('Bedankt voor je reactie! Je bericht is geplaatst.');
            
            return false;
        }
        
        // Load and display comments
        function loadComments() {
            const articleId = '{article_id}';
            const comments = JSON.parse(localStorage.getItem('comments_' + articleId) || '[]');
            const commentsList = document.getElementById('commentsList');
            
            if (comments.length === 0) {
                commentsList.innerHTML = '<div class="no-comments">Wees de eerste om een reactie achter te laten!</div>';
                return;
            }
            
            let html = '';
            comments.forEach(comment => {
                const date = new Date(comment.date);
                const dateStr = date.toLocaleDateString('nl-NL', { 
                    year: 'numeric', 
                    month: 'long', 
                    day: 'numeric' 
                });
                
                html += `
                    <div class="comment">
                        <div class="comment-header">
                            <span class="comment-author">${escapeHtml(comment.name)}</span>
                            <span class="comment-date">${dateStr}</span>
                        </div>
                        <div class="comment-body">
                            ${escapeHtml(comment.message).replace(/\\n/g, '<br>')}
                        </div>
                    </div>
                `;
            });
            
            commentsList.innerHTML = html;
        }
        
        // Escape HTML to prevent XSS
        function escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }
        
        // Load comments on page load
        document.addEventListener('DOMContentLoaded', loadComments);
    </script>
"""

# Configuration des articles
articles = [
    {
        'file': '/Users/marc/Desktop/italiaanse-percolator/koopgids/italiaanse-percolator-gebruiken-handleiding.html',
        'article_id': 'percolator-gebruiken'
    },
    {
        'file': '/Users/marc/Desktop/italiaanse-percolator/koopgids/beste-koffiebonen-italiaanse-percolator.html',
        'article_id': 'beste-koffiebonen'
    }
]

def process_article(filepath, article_id):
    """Ajoute le bloc auteur et commentaires à un article"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Ajouter les styles CSS avant @media
    if '.author-box' not in content:
        content = re.sub(
            r'(\s+@media \(max-width: 768px\))',
            css_styles + r'\1',
            content,
            count=1
        )
        print(f"✓ Styles CSS ajoutés à {filepath}")
    
    # 2. Ajouter le bloc auteur et commentaires avant </article>
    if '<!-- Author Box -->' not in content:
        content = re.sub(
            r'(\s+)</article>',
            author_box_html + r'\1</article>',
            content,
            count=1
        )
        print(f"✓ Bloc auteur et commentaires ajoutés à {filepath}")
    
    # 3. Ajouter le JavaScript avant </body>
    if 'handleCommentSubmit' not in content:
        js_code = comments_js_template.format(article_id=article_id)
        content = re.sub(
            r'(\s+)</body>',
            js_code + r'\1</body>',
            content,
            count=1
        )
        print(f"✓ JavaScript commentaires ajouté à {filepath}")
    
    # 4. Ajouter la responsive pour author-box dans @media si pas déjà présent
    if 'author-box' in content and '.author-box {' in content:
        # Vérifier si le responsive est déjà là
        if '@media (max-width: 768px)' in content and '.author-box {' not in content[content.find('@media (max-width: 768px)'):]:
            # Trouver la fermeture de @media et ajouter avant
            media_section = content[content.find('@media (max-width: 768px)'):]
            closing_brace_pos = content.find('        }', content.find('@media (max-width: 768px)'))
            
            responsive_author = """
            .author-box {
                flex-direction: column;
                text-align: center;
                align-items: center;
            }
            """
            
            content = content[:closing_brace_pos] + responsive_author + content[closing_brace_pos:]
            print(f"✓ Styles responsive ajoutés à {filepath}")
    
    # Sauvegarder
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {filepath} mis à jour avec succès!\n")

def main():
    print("🚀 Ajout du bloc auteur et commentaires aux articles...\n")
    
    for article in articles:
        try:
            process_article(article['file'], article['article_id'])
        except Exception as e:
            print(f"❌ Erreur pour {article['file']}: {e}\n")
    
    print("✅ Tous les articles ont été traités!")

if __name__ == '__main__':
    main()
