import json
import markdown
import os

# Carrega os dados das postagens do arquivo JSON
with open('data/posts.json', 'r') as json_file:
    posts = json.load(json_file)

# Pasta de saída para as páginas HTML geradas
output_dir = 'blog_pages'
os.makedirs(output_dir, exist_ok=True)

# Loop através das postagens
for post in posts:
    title = post['titulo']

    # Lê o conteúdo do arquivo Markdown correspondente
    markdown_file_path = os.path.join('posts', f"{title}.md")
    with open(markdown_file_path, 'r') as md_file:
        markdown_content = md_file.read()

    # Converte o conteúdo Markdown em HTML
    html_content = markdown.markdown(markdown_content)

    # Carrega o template HTML
    with open('templates/template.html', 'r') as template_file:
        template = template_file.read()

    # Substitui as variáveis no template pelos dados da postagem
    template = template.replace('{{ titulo }}', title)
    template = template.replace('{{ autor }}', post['autor'])
    template = template.replace('{{ conteudo }}', html_content)

    # Salva a página HTML gerada
    output_filename = os.path.join(output_dir, f"{title}.html")
    with open(output_filename, 'w') as html_file:
        html_file.write(template)

print("Páginas HTML geradas com sucesso!")
