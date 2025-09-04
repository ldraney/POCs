import aiohttp
import asyncio
from typing import Dict, Any, Optional
from app.config import settings

class MicroserviceClient:
    """Client for communicating with all microservices"""
    
    def __init__(self):
        self.services = {
            "client": settings.CLIENT_SERVICE_URL,
            "cost_calculator": settings.COST_CALCULATOR_SERVICE_URL,
            "email": settings.EMAIL_SERVICE_URL,
            "formula": settings.FORMULA_SERVICE_URL,
            "pricing": settings.PRICING_SERVICE_URL,
            "purchase_order": settings.PURCHASE_ORDER_SERVICE_URL,
            "whitelabel": settings.WHITELABEL_SERVICE_URL,
        }
    
    async def get_service_status(self, service_name: str) -> Dict[str, Any]:
        """Get status from a specific service"""
        url = self.services.get(service_name)
        if not url:
            return {"error": f"Unknown service: {service_name}"}
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{url}/") as response:
                    if response.status == 200:
                        return await response.json()
                    return {"error": f"Service returned {response.status}"}
        except Exception as e:
            return {"error": f"Connection failed: {str(e)}"}
    
    async def get_all_services_status(self) -> Dict[str, Dict[str, Any]]:
        """Get status from all microservices concurrently"""
        tasks = []
        for service_name in self.services:
            tasks.append(self.get_service_status(service_name))
        
        results = await asyncio.gather(*tasks)
        return dict(zip(self.services.keys(), results))
    
    async def get_clients(self) -> Dict[str, Any]:
        """Get all clients from client-service"""
        return await self._get_endpoint("client", "/clients")
    
    async def get_client_stats(self) -> Dict[str, Any]:
        """Get client statistics from client-service"""
        return await self._get_endpoint("client", "/stats")
    
    async def _get_endpoint(self, service_name: str, endpoint: str) -> Dict[str, Any]:
        """Generic method to call service endpoints"""
        url = self.services.get(service_name)
        if not url:
            return {"error": f"Unknown service: {service_name}"}
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{url}{endpoint}") as response:
                    if response.status == 200:
                        return await response.json()
                    return {"error": f"Endpoint returned {response.status}"}
        except Exception as e:
            return {"error": f"Connection failed: {str(e)}"}

# Global instance
microservice_client = MicroserviceClient()