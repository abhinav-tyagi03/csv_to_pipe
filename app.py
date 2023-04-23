from fastapi import FastAPI, File, UploadFile
import csv

app = FastAPI()

@app.post("/csv-to-pipe")
async def csv_to_pipe(file: UploadFile = File(...)):
    pipe_file_path = f"{(file.filename)[:-3]}_pipe_converted.txt"
    with open(pipe_file_path, 'w') as pipe_file:
        csv_reader = csv.reader((await file.read()).decode('utf-8-sig').splitlines())
        for row in csv_reader:
            pipe_file.write('|'.join(row) + '\n')
    return {"status": "file conversion successfull"}
