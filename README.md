# StudyBot Evaluation

In diesem Projekt wird das Ergebnis meiner Studienarbeit an der DHBW Mosbach evaluiert. Für die Arbeit sollte ein Chatbot erstellt werden, der Fragen zu den Leitlinien beantworten kann.

## Aufbau

Das Django Projekt dient als Schicht zwischen dem User und dem Chatbot Framework PrivateGPT (https://github.com/zylon-ai/private-gpt).

Die Kommunikation mit dem Projekt ist über den API-Client Bruno (https://www.usebruno.com/) gedacht, für welchen hier auch ein Profil im Ordner "/bruno" vorhanden ist.

In der Evaluierung_StudyBot.xlsx sind die Ergebnisse der Untersuchung zusammengefasst.

## API

Es stehen 3 Endpunkte zur Verfügung, welche alle bereits im Bruno-Projekt eingerichtet sind. 

Diese Endpunkte unterscheiden sich dabei in der Sprache, in der sie den Prompt an das Sprachmodell weiterleiten, und in der Sprache des Dokuments, das als Wissensgrundlage des Sprachmodells dient.

## Setup

Für die Verwendung ist eine lokale PrivateGPT-Instanz notwendig. Das verwendete Sprachmodell für die Evaluierung ist Mistral 7B mit Ollama.