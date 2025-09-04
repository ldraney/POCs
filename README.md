# POCs - Proof of Concepts

This directory contains experimental combinations of namespace-service with various backend microservices.

## Example POCs

### client-dashboard/
Namespace service + client-service integration
- Frontend for client management
- Connects to client-service API

### pricing-demo/  
Namespace service + pricing-service integration
- UI for pricing calculations
- Connects to pricing-service API

### full-stack-test/
Namespace service + multiple backend services
- Complete application demo
- Tests service composition

## Workflow

1. **Copy namespace-service** as starting point
2. **Customize** frontend/business logic for specific use case
3. **Copy infra configs** from `~/infra/` as needed
4. **Configure** service URLs in config.py
5. **Test** POC functionality
6. **Deploy** if successful