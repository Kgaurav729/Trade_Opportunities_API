from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import Response
from utils.auth import verify_token
from services.rate_limiter import rate_limiter
from services.fetch_data import get_market_data
from services.analyze_data import analyze_sector_news
from utils.markdown_generator import generate_markdown_report

router = APIRouter()

@router.get("/{sector}", response_class=Response)
async def analyze_sector(sector: str, token: str = Depends(verify_token)):
    rate_limiter(token)
    
    allowed_sectors = ["pharmaceuticals", "technology", "agriculture"]
    if sector.lower() not in allowed_sectors:
        raise HTTPException(status_code=400, detail="Invalid sector provided.")
    
    news_data = get_market_data(sector)
    analysis = analyze_sector_news(sector, news_data)
    markdown = generate_markdown_report(sector, analysis)

    return Response(content=markdown, media_type="text/markdown")
