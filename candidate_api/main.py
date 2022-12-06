from fastapi import FastAPI

from candidate_api.routers import candidate

app = FastAPI(
    title="Bolster Candidates API",
    description="An api to allow the querying and updating of candidate profiles and "
    "experiences.",
    version="0.9.0",
    contact=dict(
        name="Jake Duncan",
        url="https://www.linkedin.com/in/jakeduncan392/",
        email="duncan.jacob.mk@gmail.com",
    ),
    license_info=dict(name="MIT", url="https://opensource.org/licenses/MIT"),
)


# Attach routers
for route in [candidate]:
    app.include_router(candidate.router)

# Add list candidates endpoint to a custom endpoint
app.add_api_route("/candidates", candidate.list_candidates, tags=["candidate"])
