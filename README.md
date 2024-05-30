# Recipe Application

## Overview
The Recipe Application is a web-based platform built using Django that allows users to create, manage, and view recipes. The application includes features for automatically calculating recipe difficulty, adding pictures, and displaying charts related to recipes.

## Features
- User Authentication: Secure user registration and login system.
- Recipe Management: Users can create recipes.
- Automatic Difficulty Calculation: The application calculates the difficulty of recipes based on specific criteria.
- Image Upload: Users can upload pictures for their recipes.
- Chart Visualization: Recipes data visualization on a separate page.

## Installation
1. Clone the repository:
    ```
    git clone <https://github.com/jimmy8000/recipe-app>
    cd recipe-app
    ```

2. Create and activate a virtual environment:
    ```
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Apply database migrations:
    ```
    python manage.py migrate
    ```

5. Run the development server:
    ```
    python manage.py runserver
    ```

## Usage
- Home Page: The home page displays a list of all recipes. Users can navigate to create a new recipe or view details of existing ones.
- Recipe Details: This page shows detailed information about a recipe, including ingredients, steps, difficulty, and pictures.
- AddRecipe: Form for adding recipes, including fields for the title, ingredients, steps, and pictures. Difficulty is automatically calculated.
- Charts Page: A separate page that provides visualizations related to recipes data.

## Contributing
1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push to the branch.
5. Create a new Pull Request.