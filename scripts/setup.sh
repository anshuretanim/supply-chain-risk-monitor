#!/bin/bash
# scripts/setup.sh
# Run once to set up the project

echo "Setting up Supply Chain Risk Monitor..."

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Copy .env template
cp .env.example .env
echo "✓ Created .env (fill in your Algorand credentials)"

echo "✓ Setup complete!"
echo "Next steps:"
echo "  1. source venv/bin/activate"
echo "  2. python scripts/seed_db.py"
echo "  3. uvicorn backend.app:app --reload"
