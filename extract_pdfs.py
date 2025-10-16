#!/usr/bin/env python3
"""
Extract text from PDF files using PyMuPDF
"""
import pymupdf  # PyMuPDF
import os
import sys

def extract_text_from_pdf(pdf_path, output_path=None):
    """Extract text from PDF and save to file"""
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file not found: {pdf_path}")
        return None
    
    # Open PDF
    doc = pymupdf.open(pdf_path)
    
    # Extract text from all pages
    full_text = []
    for page_num, page in enumerate(doc, 1):
        text = page.get_text()
        full_text.append(f"=== Page {page_num} ===\n\n{text}\n")
    
    # Combine all text
    extracted_text = "\n".join(full_text)
    
    # Save to file if output path provided
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(extracted_text)
        print(f"✓ Extracted {len(doc)} pages from {os.path.basename(pdf_path)}")
        print(f"  Saved to: {output_path}")
        print(f"  Total characters: {len(extracted_text):,}")
    
    doc.close()
    return extracted_text

def main():
    docs_dir = "/Users/wesleybeckner/code/trm_model/docs"
    
    print("=" * 60)
    print("PDF Text Extraction")
    print("=" * 60)
    print()
    
    # Extract TRM paper
    trm_pdf = os.path.join(docs_dir, "less_is_more_jolicoeur_martineau.pdf")
    trm_txt = os.path.join(docs_dir, "less_is_more_extracted.txt")
    extract_text_from_pdf(trm_pdf, trm_txt)
    print()
    
    # Extract HRM paper
    hrm_pdf = os.path.join(docs_dir, "hierarchical_reasoning_model_wang.pdf")
    hrm_txt = os.path.join(docs_dir, "hierarchical_reasoning_model_extracted.txt")
    extract_text_from_pdf(hrm_pdf, hrm_txt)
    print()
    
    print("=" * 60)
    print("✅ Extraction complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()

