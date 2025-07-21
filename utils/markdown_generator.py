from datetime import datetime

def generate_markdown_report(sector: str, content: str) -> str:
    date_str = datetime.now().strftime("%Y-%m-%d")
    header = f"# Market Analysis Report: {sector.capitalize()} Sector\n\n"
    meta = f"**Date**: {date_str}\n\n---\n\n"
    
    return header + meta + content.strip()