from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

# Construção do servidor
app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
    "http://127.0.0.1:5500/",
    "http://127.0.0.1:5500/index.html",
    "https://soloaas.netlify.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

solo_todo = [
    "Visitar uma exposição de um artista que você gosta.",
    "Tomar um café diferentão naquela cafeteria que você vem cobiçando.",
    "Pegar um cineminha",
    "Fazer um piquenique gourmet num parque bonito, com direito a champanhe",
    "Pegar uma piscina, dá pra ouvir sua playlist favorita na cadeira (só não esquece o protetor solar)",
    "Sair pra dançar (Não esquece de compartilhar a localização com um contato de confiança se for a noite)",
    "Fazer uma sessão de auto cuidado completa ao som da melhor playlist",
    "Tá sem grana? Bora pesquisar o que tem de gratuito na cidade essa semana. O rolê vai ser cultural!",
    "Se arrumar toda e ir a um restaurante chique e pedir o melhor vinho. Vale comprar uma rosa pra você mesma.",
    "Ir a um Karaokê e cantar com o coração sem medo de ser feliz!",
    "Aprender algo novo, vale qualquer coisa!",
    "Pedir sua comida favorita e comer enquanto assiste sua série, ou filme de conforto.",
    "Afastar os móveis e aprender a coreografia da sua música favorita",
    "Cohecer aquele lugar que você sempre quis, mas nunca foi por 'falta de companhia'. Agora você tem a sua!"
]

class ProgramResponse(BaseModel):
    program: str

@app.get("/")
async def get_home():
    return 'Boas vindas à API Solo as a Service!'

@app.get("/solo_todo", response_model=ProgramResponse, summary="Obtenha um programa solo aleatório")
async def get_solotodo():
    program = random.choice(solo_todo)
    return {"program": program}