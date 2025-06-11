<!-- File: textbook/README.md -->

This repository is archived. We have moved to a completely different framework. The new repo is at - https://github.com/markov-root/atlas

The website is hosted at - https://ai-safety-atlas.com/

# AI Safety Atlas

## File Structure

```
project_root/
├── docs/ (contains your source files (md, images, etc.))
├── site/ (contains the built HTML website)
├── scripts/ (contains supplementary scripts)
├── mkdocs.yml (configuration file for mkdocs)
└── README.md
```

```
project_root/
├── docs/
│   ├── chapters/ (contains individual chapter folders)
│   │   ├── 01-capabilities/ (contains individual chapter md sections and images)
│   │   │   └── images/
│   │   │   └── extra.css
│   │   ├── 02-risks-landscape/
│   │   └── ...
│   ├── includes/ (additional supplementary files (e.g. glossary))
│   │   ├── snippets/
│   │   └── abbreviations.md
│   ├── overrides/ (css,js,html overrides to mkdocs)
│   │   ├── extra.css
│   │   ├── mathjax.js
│   │   ├── ...
│   │   └── main.html
│   ├── .pages.yml
│   ├── courses.md
│   └── index.md
```

## Development Process

### Content Management
1. **Content Creation**: All content is created and edited in Google Docs.
2. **Content Synchronization**: Run `python scripts/convert_gdoc2md.py` to update the repository with the latest content from Google Docs.

### Local Development
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run the local development server:
   ```
   mkdocs serve
   ```
3. View the site at `http://localhost:8000`

### Building the Site
- Run `mkdocs build` to generate the static site in the `site` directory.

## Deployment
The site is automatically deployed to GitHub Pages when changes are pushed to the main branch.

## Dependencies
- Python 3.x
- MkDocs
- MkDocs Material theme
- MkDocs Awesome Pages plugin

For a complete list of dependencies, see `requirements.txt`.

## Contributing
1. **Content Changes**: Make all content changes in the Google Docs.
2. **Export**: Export changes using [Docs to Markodown Pro plugin](https://workspace.google.com/u/0/marketplace/app/docs_to_markdown_pro/483386994804)
3. **Sync Content**: After significant changes, run `python scripts/convert_gdoc2md.py`.
4. **Code Changes**: For changes to the site structure, styling, or functionality:
   - Make changes in the appropriate directories (`docs/overrides/`, `mkdocs.yml`, etc.)
   - Test locally using `mkdocs serve`
   - Commit changes and push to GitHub

## File Descriptions
- `mkdocs.yml`: Configuration file for MkDocs
- `docs/`: Contains all source content and assets
- `docs/assets/`: Static files like images
- `docs/chapters/`: Markdown files for each chapter
- `docs/includes/`: Reusable content snippets
- `docs/overrides/`: Custom CSS, JavaScript, and HTML templates
- `scripts/`: Utility scripts for content management
- `.gitignore`: Specifies intentionally untracked files to ignore

For more help, consult the [MkDocs documentation](https://www.mkdocs.org/) or the [Material for MkDocs documentation](https://squidfunk.github.io/mkdocs-material/).
