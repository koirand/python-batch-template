# batch-template
Template for executing python batch process.

## Usage
```sh
# Execute python script
python src/{file-name}.py
# Execute sql of MySQL
python src/{program-name}.py
# For Docker
docker build -t batch:latest .
docker run \
    --rm \
    -e ENV=development \
    batch:latest \
    python src/{file-name}.py
```

### Requirement
- Python3
