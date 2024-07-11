## Flask Application Design

### HTML Files

- `index.html`:
  - Serves as the main page of the application.
  - Displays a welcome message or a form for the user to input their health and fitness data.
- `dashboard.html`:
  - Shows the user's progress towards their goals.
  - Presents insights and correlations based on the user's data.

### Routes

- `/`:
  - Directs to the index page.
- `/submit`:
  - Processes the user's input data and stores it in a database.
  - Redirects to the dashboard page.
- `/dashboard`:
  - Displays the user's dashboard, showcasing their progress and insights.
- `/insights`:
  - Provides detailed information about the user's data, highlighting anomalies and correlations.
- `/goals`:
  - Allows the user to set and modify their health and fitness goals.