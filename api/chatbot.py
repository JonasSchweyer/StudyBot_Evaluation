import json
import os
from typing import Any

import httpcore
setattr(httpcore, 'SyncHTTPTransport', Any)  # This is necessary for googletrans to work

import gradio_client
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from gradio_client import file
from googletrans import Translator

client = gradio_client.Client("http://localhost:8001/")
translator = Translator()


@csrf_exempt
def chat1_english(request):
    if request.method == "POST":
        data = json.loads(request.body)
        prompt_german = data["prompt"]

        prompt_translation = translator.translate(prompt_german, dest="en")

        doc_path = get_latest_document("documents/english")

        result = client.predict(
            prompt_translation.text,
            "Query Files",
            [file(doc_path)],
            "",
            api_name="/chat"
        )

        parts = result.split("Sources")
        cleaned_text = parts[0].strip()

        response_translation = translator.translate(cleaned_text, dest="de")

        client.close()
        return HttpResponse(response_translation.text)


@csrf_exempt
def chat2_german(request):
    if request.method == "POST":
        data = json.loads(request.body)
        prompt_german = data["prompt"]

        doc_path = get_latest_document("documents/german")

        result = client.predict(
            prompt_german,
            "Query Files",
            [file(doc_path)],
            "",
            api_name="/chat"
        )

        parts = result.split("Sources")
        cleaned_text = parts[0].strip()

        response_translation = translator.translate(cleaned_text, dest="de")

        client.close()
        return HttpResponse(response_translation.text)


@csrf_exempt
def chat3_mixed(request):
    if request.method == "POST":
        data = json.loads(request.body)
        prompt_german = data["prompt"]

        doc_path = get_latest_document("documents/german")

        prompt_translation = translator.translate(prompt_german, dest="en")

        result = client.predict(
            prompt_translation.text,
            "Query Files",
            [file(doc_path)],
            "",
            api_name="/chat"
        )

        parts = result.split("Sources")
        cleaned_text = parts[0].strip()

        response_translation = translator.translate(cleaned_text, dest="de")

        client.close()
        return HttpResponse(response_translation.text)


def get_latest_document(folder):
    # Gets the last file in the dir, which should be the newest one following the naming scheme
    document_name = os.listdir(folder)[-1]

    document_path = folder + "/" + document_name

    return document_path
