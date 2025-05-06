github client : https://github.com/solena8/set_solver_client
le solveur en ligne :https://set-game-solver.web.app/

# Start server command

python -m uvicorn api:app --reload


# Valid
http://127.0.0.1:8000/cards/1ORH,2OVP,3OMV,1ORP

# Not valid
http://127.0.0.1:8000/cards/1ORH,2OVP,3OMH,1ORP

# pour déployer : 
gcloud functions deploy set_game_api   --runtime python312   --trigger-http   --allow-unauthenticated   --source .
