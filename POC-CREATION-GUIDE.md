# POC Creation Process

## Template Stack
**Always use the namespace-service template** (`~/microservices/namespace-service/`)

**Stack**: FastAPI + HTMX + Alpine.js + Tailwind CSS
**NOT Flask** - Flask is deprecated for new POCs

## Quick Start

```bash
# Create new POC
./create-poc.sh <poc-name> [microservices...]

# Example: Dashboard combining client and cost services  
./create-poc.sh client-dashboard client-service cost-calculator-service
```

## Manual Process

If you need to create a POC manually:

1. **Copy template**:
   ```bash
   cp -r ~/microservices/namespace-service ~/POCs/<poc-name>
   ```

2. **Update metadata**:
   - Edit `pyproject.toml` name and description
   - Update `README.md` with POC purpose

3. **Add microservices**:
   ```bash
   mkdir -p services
   cp -r ~/microservices/<service-name> services/
   ```

4. **Customize**:
   - `app/config.py` - Environment settings
   - `app/routes/` - API endpoints and UI routes
   - `frontend/templates/` - HTMX templates
   - `app/services/` - Business logic + service clients

## Common Mistakes to Avoid

- ❌ **DON'T use Flask** - Use FastAPI from template
- ❌ **DON'T create from scratch** - Always copy namespace-service
- ❌ **DON'T skip the script** - Use `create-poc.sh` for consistency
- ✅ **DO customize gradually** - Start with template, then modify
- ✅ **DO follow the stack** - FastAPI + HTMX + Alpine + Tailwind