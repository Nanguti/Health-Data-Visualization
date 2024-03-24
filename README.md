# Health Data Visualization with Django REST API, Vue.js, and Chart.js

This project demonstrates a comprehensive health data visualization system, combining a Django REST API for data management and a Vue.js frontend with Chart.js for interactive data exploration.

## Project Overview

This project offers a solution to visualize health data for informed decision-making. It provides an API endpoint to access health data and a user interface to explore the data through charts.

## Technologies Used

**Backend:**

- Python
- Django REST Framework

**Frontend:**

- Vue.js
- Chart.js

## Getting Started

### Prerequisites:

- Python 3.x and pip installed
- Node.js and npm (or yarn) installed
- Basic understanding of Django REST Framework, Vue.js, and Chart.js

### 1. Backend (Django REST API):

1. Clone this repository or download the project files.
2. Install required dependencies:

   ```bash
   cd backend  # Navigate to the backend directory
   pip install -r requirements.txt
   ```

3. Configure your database settings in `backend/settings.py`.
4. Run database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

This will run the API server at [http://localhost:8000/](http://localhost:8000/) by default.

### 2. Frontend (Vue.js):

1. Navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run serve
   ```

This will open the frontend application in your default browser at [http://localhost:8080/](http://localhost:8080/) by default.

### API Configuration:

Update the `baseUrl` in `frontend/src/api/healthData.js` to point to the running Django REST API endpoint URL (e.g., [http://localhost:8000/api/v1/datapoints/](http://localhost:8000/api/v1/datapoints/)).

## Functionality

**Backend (Django REST API):**

- Provides an API endpoint to retrieve health data.
- Optionally supports filtering data by variables (e.g., "Blood Pressure") via query parameters.
- Manages data models for locations, datasets, variables, data points, and their relationships.

**Frontend (Vue.js):**

- Fetches data from the Django REST API for the desired variable (e.g., "Blood Pressure").
- Processes and parses the API response.
- Uses Chart.js to create a visual representation of the data (e.g., bar chart).
- Currently, the frontend demonstrates a bar chart comparing blood pressure values across different locations.

## Customization and Future Improvements

- You can modify the chart type, colors, or other options within the `createChart()` method in `frontend/src/components/BloodPressureChart.vue` to customize the visualization.
- Consider adding functionalities to filter data by different variables or explore trends over time based on your API capabilities.
- Implement user authentication and authorization if your data requires restricted access.

## Contributing

Feel free to fork this repository and contribute improvements or additional functionalities.
