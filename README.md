# Glow - Beauty Blog

Glow is a beauty blog website designed to share beauty tips, skincare routines, makeup tutorials, and more. The site will soon feature an e-commerce platform for small beauty businesses to sell their products.

## Features
- **Beauty Blog**: A place to read and explore content about beauty, skincare, and makeup.
- **Future E-Commerce**: A planned feature where small beauty businesses can sell their products.

## Tech Stack
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap for responsive design
- **Deployment**: Vercel for hosting and deployment

## Future Features
- E-commerce integration for small beauty businesses to list and sell their products.
- User registration and authentication for commenting on posts.
- More interactive blog features such as reviews and ratings for beauty products.

## Live Link
You can check out the live website here: [glow-livid.vercel.app](https://glow-livid.vercel.app/)

## Setup Instructions

### Requirements:
- Python 3.x
- Django
- Bootstrap for frontend styling

### Installation:

1. Clone this repository:

   ```bash
   git clone https://github.com/aria-vero-s/glow.git
   ```

2. Navigate to the project folder:

   ```bash
   cd myproject
   ```

3. Set up a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the Django development server:

   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to `http://127.0.0.1:8000/` to see the website in action.

### Deployment

To deploy this project to Vercel, follow these steps:

1. Create a new Vercel app from the [Vercel dashboard](https://vercel.com/dashboard).
2. Link your GitHub repository to the Vercel app during the setup process.
3. Make sure to set the `DEBUG` setting to `False` in your Django `settings.py` file.
4. Run the following Django commands to prepare the static files for deployment:

   ```bash
   python manage.py collectstatic
   ```

5. Commit your changes and push to GitHub:

   ```bash
   git add .
   git commit -m "Prepare for deployment"
   git push
   ```

6. Once you push the changes to GitHub, Vercel will automatically deploy your app. You can check the status of your deployment on the Vercel dashboard.

## Contributing
Feel free to fork the repository and submit pull requests. Contributions are always welcome!
