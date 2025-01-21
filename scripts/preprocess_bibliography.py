# preprocess_bibliography.py
import re
from pathlib import Path
from typing import Dict, Set, Optional, Tuple
from dataclasses import dataclass
from urllib.parse import urlparse
import arxiv

@dataclass
class Citation:
    authors: str
    year: str
    url: str
    title: str = ""
    key: str = ""
    bibtex: str = ""

class BibliographyProcessor:
    def __init__(self, debug: bool = True):
        self.citations: Dict[str, Citation] = {}
        self.keys: Set[str] = set()
        self.debug = debug
    
    def extract_arxiv_id(self, url: str) -> Optional[str]:
        """Extract arXiv ID from URL."""
        if 'arxiv.org' not in url:
            return None
        match = re.search(r'(?:abs|pdf)/(\d+\.\d+)', url)
        return match.group(1) if match else None

    def get_arxiv_info(self, arxiv_id: str) -> Optional[Dict]:
        """Get paper info from arXiv API."""
        try:
            search = arxiv.Search(id_list=[arxiv_id])
            paper = next(search.results())
            return {
                'title': paper.title,
                'authors': ', '.join(author.name for author in paper.authors),
                'year': paper.published.year,
                'url': paper.entry_id,
            }
        except Exception as e:
            if self.debug:
                print(f"Error fetching arXiv info for {arxiv_id}: {e}")
            return None

    def read_existing_bib(self, bib_file: Path) -> Dict[str, Citation]:
        """Read existing citations from .bib file."""
        if not bib_file.exists():
            return {}
            
        existing = {}
        content = bib_file.read_text(encoding='utf-8')
        
        # Extract URL from bibtex entries
        url_pattern = r'url\s*=\s*{([^}]+)}'
        key_pattern = r'@(?:article|misc){([^,]+),'
        
        entries = re.split(r'(?=@(?:article|misc){)', content)
        for entry in entries:
            if not entry.strip():
                continue
                
            url_match = re.search(url_pattern, entry)
            key_match = re.search(key_pattern, entry)
            
            if url_match and key_match:
                url = url_match.group(1)
                citation = Citation(
                    authors="", # We don't need to parse these since we're keeping
                    year="",    # the entire bibtex entry
                    url=url,
                    bibtex=entry.strip()
                )
                existing[url] = citation
                self.keys.add(key_match.group(1))
                
        return existing

    def extract_citation_info(self, text: str, url: str) -> Citation:
        """Extract citation info and try to get arXiv details if available."""
        if self.debug:
            print(f"\nProcessing citation: {url}")

        # Try to get arXiv info first
        arxiv_id = self.extract_arxiv_id(url)
        if arxiv_id:
            arxiv_info = self.get_arxiv_info(arxiv_id)
            if arxiv_info:
                if self.debug:
                    print(f"Found arXiv info: {arxiv_info}")
                return Citation(
                    authors=arxiv_info['authors'],
                    year=str(arxiv_info['year']),
                    url=url,
                    title=arxiv_info['title']
                )

        # Fall back to extracting from text
        patterns = [
            r'\(?\[([^,]+)(?:,\s*et al\.?)?,\s*(\d{4})\]',  # (Author et al., 2024)
            r'\(?\[([^,]+(?:\s*(?:&|and)\s*[^,]+)*),\s*(\d{4})\]',  # (Author & Author, 2024)
            r'\(?\[([^,]+),\s*(\d{4})\]'  # (Author, 2024)
        ]
        
        authors = "Unknown"
        year = "0000"
        
        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                authors = match.group(1).strip()
                year = match.group(2)
                if self.debug:
                    print(f"Extracted from text - authors: {authors}, year: {year}")
                break

        return Citation(authors=authors, year=year, url=url)

    def generate_key(self, citation: Citation) -> str:
        """Generate unique BibTeX key."""
        # Extract first author's lastname
        first_author = citation.authors.split(',')[0].split()[-1]
        first_author = first_author.lower()
        first_author = first_author.replace("et", "").replace("al", "").strip(". ")
        
        # Create base key
        base_key = f"{first_author}{citation.year}"
        key = base_key
        suffix = 'a'
        
        while key in self.keys:
            key = f"{base_key}{suffix}"
            suffix = chr(ord(suffix) + 1)
        
        self.keys.add(key)
        return key

    def generate_bibtex_entry(self, citation: Citation) -> str:
        """Generate BibTeX entry."""
        # Use @article for arXiv papers, @misc for others
        entry_type = "article" if "arxiv.org" in citation.url else "misc"
        
        entry = [
            f"@{entry_type}{{{citation.key},",
            f"    author = {{{citation.authors}}},",
            f"    year = {{{citation.year}}},"
        ]
        
        if citation.title:
            entry.append(f"    title = {{{citation.title}}},")
        
        entry.append(f"    url = {{{citation.url}}},")
        
        if "arxiv.org" in citation.url:
            arxiv_id = self.extract_arxiv_id(citation.url)
            if arxiv_id:
                entry.append(f"    journal = {{arXiv preprint arXiv:{arxiv_id}}},")
        
        entry.append("}")
        return '\n'.join(entry)

    def find_citations(self, content: str) -> Set[Tuple[str, str]]:
        """Find all citations in content without modifying it."""
        citations = set()
        citation_pattern = r'\(\[(.*?)\]\((https?://[^)]+)\)\)'
        
        for match in re.finditer(citation_pattern, content):
            text = match.group(1)
            url = match.group(2)
            
            # Only include if it looks like a citation (has a year)
            if re.search(r'\d{4}', text):
                citations.add((text, url))
                
        return citations

def process(content: str, output_dir: Optional[Path] = None) -> None:
    """Process citations and update bibliography file."""
    processor = BibliographyProcessor(debug=True)
    print("Finding citations ...")
    
    # Just use output_dir directly to place references.bib
    bib_file = output_dir / "references.bib" if output_dir else Path("references.bib")
    existing_citations = processor.read_existing_bib(bib_file)
    
    if processor.debug:
        print(f"Found {len(existing_citations)} existing citations")
    
    # Find all citations in content
    citations = processor.find_citations(content)
    
    # Process new citations
    for text, url in citations:
        if url not in existing_citations:
            if processor.debug:
                print(f"\nProcessing new citation: {url}")
            citation = processor.extract_citation_info(text, url)
            citation.key = processor.generate_key(citation)
            citation.bibtex = processor.generate_bibtex_entry(citation)
            existing_citations[url] = citation
        elif processor.debug:
            print(f"\nSkipping existing citation: {url}")
    
    # Write updated bibliography file
    bib_content = '\n\n'.join(c.bibtex for c in existing_citations.values())
    bib_file.write_text(bib_content, encoding='utf-8')
    
    if processor.debug:
        print(f"\nWrote {len(existing_citations)} citations to: {bib_file}")

def test_processor():
    """Test function with sample content."""
    test_content = """
Some work ([Smith et al., 2024](https://arxiv.org/abs/2401.12345)) shows...

As proven by ([Johnson & Lee, 2023](https://example.com/paper))...
"""
    
    test_dir = Path("ch5/latex_output")
    test_dir.mkdir(parents=True, exist_ok=True)
    process(test_content, test_dir)

if __name__ == "__main__":
    test_processor()
