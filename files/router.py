from fastapi import APIRouter, File, HTTPException, UploadFile


router_file = APIRouter(
    prefix='/files',
    tags=['Файлы'] 
)

@router_file.post('/')
async def upload_file(name_file: str, uploaded_file: UploadFile = File(...)):
    file = uploaded_file.file
    filename = uploaded_file.filename

    if not filename.endswith('.mp3'):
        raise HTTPException(status_code=400, detail='Неверный формат файла, передайте, пожалуйста, аудио формат - .mp3') 

    with open(f"name_file", 'wb') as f:
        f.write(file.read())
        return {'message': 'Данные успешно сохранились'}