from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi.responses import RedirectResponse
from config import settings


router = APIRouter(
    prefix='/auth',
    tags=['Пользователь']  
)

templates = Jinja2Templates(directory='templates')

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=settings.AUTHORIZE_URL,
    tokenUrl=settings.TOKEN_URL,
)

@router.get('/')
def index(request: Request):
    return templates.TemplateResponse(
        name='home.html',
        context={'request': request}
    )

@router.get("/yandex")
async def auth_yandex():
    return RedirectResponse(
        f"{settings.AUTHORIZE_URL}?response_type=code&client_id={settings.CLIENT_ID}&redirect_uri={settings.REDIRECT_URL}"
    )