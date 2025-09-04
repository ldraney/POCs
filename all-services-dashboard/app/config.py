import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "All Services Dashboard")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./data/dashboard.db")
    
    # Server
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "9000"))
    RELOAD: bool = os.getenv("RELOAD", "False").lower() == "true"
    
    # Paths
    BASE_DIR = Path(__file__).resolve().parent.parent
    TEMPLATES_DIR = BASE_DIR / "frontend" / "templates"
    STATIC_DIR = BASE_DIR / "frontend" / "static"
    
    # All Microservices
    CLIENT_SERVICE_URL: str = os.getenv("CLIENT_SERVICE_URL", "http://localhost:7012")
    COST_CALCULATOR_SERVICE_URL: str = os.getenv("COST_CALCULATOR_SERVICE_URL", "http://localhost:7013") 
    EMAIL_SERVICE_URL: str = os.getenv("EMAIL_SERVICE_URL", "http://localhost:7014")
    FORMULA_SERVICE_URL: str = os.getenv("FORMULA_SERVICE_URL", "http://localhost:7015")
    PRICING_SERVICE_URL: str = os.getenv("PRICING_SERVICE_URL", "http://localhost:7016")
    PURCHASE_ORDER_SERVICE_URL: str = os.getenv("PURCHASE_ORDER_SERVICE_URL", "http://localhost:7017")
    WHITELABEL_SERVICE_URL: str = os.getenv("WHITELABEL_SERVICE_URL", "http://localhost:7018")
    
    # Feature Flags
    ENABLE_ALL_INTEGRATIONS: bool = os.getenv("ENABLE_ALL_INTEGRATIONS", "True").lower() == "true"

settings = Settings()