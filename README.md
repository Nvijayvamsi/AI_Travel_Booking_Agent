# Deploy to Streamlit Community Cloud

Steps to deploy this Streamlit app (`frontend.py`) to Streamlit Community Cloud:

1. Create a GitHub repository and push the project (include `frontend.py`, `main.py`, `tools/`, and `requirements.txt`).
2. In the repository root ensure `frontend.py` is the app entrypoint (Streamlit will run this file).
3. In Streamlit Cloud (https://share.streamlit.io) create a new app and connect your GitHub repo and branch.
4. Set the **Main file path** to `frontend.py`.
5. Add the following environment variables in the Streamlit app settings:
   - `DATABASE_URL` (Postgres connection string used by `main.py`)
   - `TAVILY_API_KEY` (Tavily search API key)
   - `AVIATIONSTACK_API_KEY` (AviationStack API key)
   - Any other keys used in your `.env`
6. Confirm `requirements.txt` is present so Streamlit Cloud installs dependencies automatically.
7. Deploy. Monitor logs for missing packages or runtime errors.

Notes and caveats:
- The app expects a Postgres instance reachable from Streamlit Cloud if you use `DATABASE_URL`. For simple demos you can skip DB usage and run without persistent checkpointer.
- Large LLM models (local LLaMA 70B, Groq endpoints) cannot run on Streamlit Cloud. Ensure `ChatGroq` is pointing to a hosted LLM endpoint or mock it for demo purposes.
- If some packages are not available on PyPI, vendor them or provide lightweight fallbacks.

If you'd like, I can:
- Generate a `.gitignore` and small `.streamlit/config.toml`.
- Create a simplified `requirements.txt` with pinned versions.
- Prepare a short example `.env.example` listing required env vars.

Demo mode
---------

If you want to deploy the app to Streamlit quickly without configuring a Postgres database or LLM endpoints, enable demo mode by setting the environment variable `DEMO_MODE=true`. In demo mode the frontend renders canned responses so you can verify UI and Streamlit logs without external services.

For local testing copy `.env.example` to `.env` and adjust values, or set environment variables in your Streamlit Cloud app settings.