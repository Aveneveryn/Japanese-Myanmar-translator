# Running Nihongo2Myanmar from an iPhone

This guide explains practical ways to run and develop the project when you only have an iPhone.

Recommended approach (easy): Replit — runs the Flask app in the cloud and gives you a public URL you can open from Safari.
Alternative approaches: Gitpod / Codespaces (cloud dev environments) or cloud deployment (Railway, Render) — more advanced.

Option A — Replit (recommended for iPhone-only)
1. On your iPhone, open Safari and go to https://replit.com
2. Sign up / Log in. (Create a free account.)
3. Tap the "+ Create" button and choose "Import from GitHub" (you may need to connect your GitHub account).
4. Enter the repo URL: https://github.com/Aveneveryn/Japanese-Myanmar-translator and import.
5. After import completes, open the shell/console inside Replit (Replit provides a web terminal).
6. Make sure the run command is set to: flask run --host=0.0.0.0 --port=5000
   - In Replit's GUI, find the run configuration and set it.
7. Add environment variables: TRANSLATOR=stub (or other); See Replit's Secrets/Environment settings.
8. Click Run. Replit will install dependencies (may need to run `pip install -r requirements.txt` in the shell) and start the Flask app.
9. Replit will give you a public URL — open it in Safari to use the web UI.

Notes for Replit:
- SQLite database will be in the project workspace. For persistence, Replit keeps files across runs for private/personal projects.
- If pip install fails because Replit's default Python doesn't match, change Replit project's language to Python 3.11.

Option B — Gitpod / Codespaces
- Gitpod (https://gitpod.io) can open a full dev environment from your repo in the browser. You can run the Flask app and get a preview URL. Gitpod has a free tier and is mobile-web friendly.
- Codespaces requires a paid plan for private repos; if available you can use it similarly.

Option C — Deploy to a cloud host (Railway / Render / Fly)
- Connect your GitHub repository to Railway or Render and let it build. These services will provide a public URL where your app runs.
- Useful if you want a persistent public demo accessible from iPhone without running a dev environment.

Editing code and creating PRs from iPhone
- Use the GitHub mobile app (iOS) or github.dev in Safari (open the repo and press "." to open the web editor) to edit files.
- To create a pull request from your branch (aven/jmfinal):
  1. Open the repo in the GitHub app or in Safari to the branch page.
  2. Tap "Compare & pull request" (or choose "New pull request" and select your branch aven/jmfinal as the head branch).
  3. Add title and description, mark it as a Draft if you want, and Create Pull Request.

Creating milestones and issues from iPhone
- In GitHub mobile or the Safari web UI:
  1. Open the repo -> Issues -> Milestones -> New milestone. Fill in title (e.g., "Project setup (MVP)") and due date/description.
  2. Create Issues and in each issue's sidebar assign the milestone you created.

Testing API endpoints from iPhone
- Use Safari or an HTTP client app (e.g., HTTPBot, RESTed) to send POST requests to /api/translate/text with JSON {"text":"..."}.
- Or use Replit preview and test the UI directly from Safari.

Troubleshooting tips
- If third-party libraries fail to install on Replit, you can temporarily comment them out from requirements.txt and run the app; add them back when you can use a more capable environment.
- For heavy NLP models or OCR, prefer deploying the app to a cloud host and keep the heavy processing server-side.

Security
- Never commit secrets (API keys) into the repo. Use Replit Secrets / GitHub Secrets for Codespaces/CICD.

If you want, I can prepare a Replit-specific run guide and a minimal Procfile / start script to make deployment to Replit or Railway smoother.
