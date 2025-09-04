#!/bin/bash

# POC Creation Script
# Usage: ./create-poc.sh <poc-name> [microservices...]
# Example: ./create-poc.sh client-dashboard client-service cost-calculator-service

set -e

POC_NAME="$1"
if [ -z "$POC_NAME" ]; then
    echo "Error: POC name required"
    echo "Usage: ./create-poc.sh <poc-name> [microservices...]"
    exit 1
fi

POC_DIR="$HOME/POCs/$POC_NAME"
NAMESPACE_TEMPLATE="$HOME/microservices/namespace-service"
MICROSERVICES_DIR="$HOME/microservices"

if [ -d "$POC_DIR" ]; then
    echo "Error: POC directory '$POC_DIR' already exists"
    exit 1
fi

if [ ! -d "$NAMESPACE_TEMPLATE" ]; then
    echo "Error: Namespace template not found at '$NAMESPACE_TEMPLATE'"
    exit 1
fi

echo "Creating POC: $POC_NAME"

# Step 1: Copy namespace-service template
echo "📋 Copying namespace-service template..."
cp -r "$NAMESPACE_TEMPLATE" "$POC_DIR"

# Step 2: Update POC metadata
echo "🔧 Updating POC metadata..."
cd "$POC_DIR"

# Update pyproject.toml
sed -i '' "s/name = \"namespace-service\"/name = \"$POC_NAME\"/" pyproject.toml
sed -i '' "s/description = \"Template namespace service.*/description = \"POC: $POC_NAME\"/" pyproject.toml

# Update README
cat > README.md << EOF
# $POC_NAME

POC demonstrating microservice composition patterns.

## Services Included

- **Frontend**: FastAPI + HTMX + Alpine.js + Tailwind
$(for service in "${@:2}"; do
    echo "- **${service}**: Microservice backend"
done)

## Development

\`\`\`bash
poetry install
poetry run python run.py
\`\`\`

## Architecture

This POC combines the namespace-service template with:
$(for service in "${@:2}"; do
    echo "- $service (from ~/microservices/$service/)"
done)
EOF

# Step 3: Copy requested microservices
if [ $# -gt 1 ]; then
    echo "📦 Adding microservices..."
    mkdir -p services
    
    for service in "${@:2}"; do
        service_path="$MICROSERVICES_DIR/$service"
        if [ -d "$service_path" ]; then
            echo "  → Adding $service"
            cp -r "$service_path" "services/$service"
        else
            echo "  ⚠️  Warning: Service '$service' not found at '$service_path'"
        fi
    done
fi

echo "✅ POC '$POC_NAME' created successfully at '$POC_DIR'"
echo ""
echo "Next steps:"
echo "1. cd $POC_DIR"
echo "2. poetry install"
echo "3. Customize app/config.py, routes/, and templates/"
echo "4. poetry run python run.py"