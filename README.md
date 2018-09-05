# batch-template
Template for executing python batch process.

## Usage
```sh
# Install modules
pip install configparser mysql-connector-python-rf

# Execute python script
export ENV=development
python src/{file-name}.py
# Execute sql of MySQL
python src/exec-sql.py --options {sql-name}.sql

# For Docker
docker build -t batch:latest .
docker run \
    --rm \
    -e ENV=development \
    batch:latest \
    python src/{file-name}.py
```

## Requirement
- Python3
