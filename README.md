# Project Name

A brief description of what this project does and who it's for.

## Description

This Django project includes a set of models representing a mapping system, with related models for specific characteristics. The project is structured using Django REST Framework to provide a browsable API and is equipped with viewsets for each model.

## Models

The project includes the following models:
- `MapModel`: A central model that links to all other models.
- `FartiModel`: Represents the area-related attributes.
- `FasiModel`: Represents price-related attributes.
- `StatusiModel`: Represents status-related attributes.
- `MdebareobaModel`: Represents location-related attributes.

Each model is interconnected via Django's ForeignKey and OneToOneField relationships, ensuring data integrity and efficient querying.

## Installation

Instructions on how to get your development environment running.

### Prerequisites

List all the software and tools needed to install and run this project.

1. Python
2. Django
3. Django REST Framework

### Clone the repository

```bash
git clone https://github.com/georgetoloraia/map_in_django
cd your-repository-directory
```

## Set up a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

## Install required packages
```
pip install -r requirements.txt
```

## Running the application
### Instructions on how to run the application.
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## API Endpoints
### The project provides the following API endpoints:

- `mapmodels/`: For operations related to `MapModel`.
- `fartimodels/`: For operations related to `FartiModel`.
- `fasimodels/`: For operations related to `FasiModel`.
- `statusimodels/`: For operations related to `StatusiModel`.
- `mdebareobamodels/`: For operations related to `MdebareobaModel`.

## Contributing
- If you wish to contribute to this project, please fork it and send your Pull Requests.

