from fastapi import APIRouter, HTTPException
from app.config import settings
from app.services.microservice_client import microservice_client

router = APIRouter()

@router.get("/status")
async def get_service_status():
    """Get service status and configuration"""
    return {
        "service": settings.APP_NAME,
        "status": "running",
        "integrations": {
            "all_services": settings.ENABLE_ALL_INTEGRATIONS,
        },
        "endpoints": {
            "client_service": settings.CLIENT_SERVICE_URL,
            "cost_calculator_service": settings.COST_CALCULATOR_SERVICE_URL,
            "email_service": settings.EMAIL_SERVICE_URL,
            "formula_service": settings.FORMULA_SERVICE_URL,
            "pricing_service": settings.PRICING_SERVICE_URL,
            "purchase_order_service": settings.PURCHASE_ORDER_SERVICE_URL,
            "whitelabel_service": settings.WHITELABEL_SERVICE_URL,
        }
    }

@router.get("/services/health")
async def get_all_services_health():
    """Check health of all microservices"""
    return await microservice_client.get_all_services_status()

@router.get("/clients")
async def get_clients():
    """Get all clients from client-service"""
    return await microservice_client.get_clients()

@router.get("/clients/stats")
async def get_client_stats():
    """Get client statistics from client-service"""
    return await microservice_client.get_client_stats()